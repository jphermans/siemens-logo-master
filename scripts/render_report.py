#!/usr/bin/env python3
"""Create original, illustrative A4 landscape FBD report from JSON (not native Siemens export)."""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Table, TableStyle
from reportlab.graphics.shapes import Drawing, Rect, String, Line

BLUE=colors.HexColor('#08759b')
INK=colors.HexColor('#263744')
LIGHT=colors.HexColor('#edf4f7')
def safe(v): return escape(str(v))

def main(source, destination):
    data=json.loads(Path(source).read_text(encoding='utf-8'))
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TechTitle',parent=styles['Title'],fontSize=19,textColor=BLUE,spaceAfter=12))
    styles.add(ParagraphStyle(name='TechHead',parent=styles['Heading2'],fontSize=12,textColor=BLUE,spaceBefore=12,spaceAfter=7))
    styles.add(ParagraphStyle(name='TechBody',parent=styles['BodyText'],fontSize=9,leading=13,spaceAfter=6))
    styles.add(ParagraphStyle(name='TechCell',parent=styles['BodyText'],fontSize=8,leading=11))
    page=landscape(A4)
    doc=SimpleDocTemplate(destination,pagesize=page,leftMargin=34,rightMargin=34,topMargin=43,bottomMargin=40)
    story=[]
    def p(v):return Paragraph(safe(v),styles['TechBody'])
    def heading(v):story.append(Paragraph(safe(v),styles['TechHead']))
    def table(headers,rows):
        cells=[[Paragraph(safe(x),styles['TechCell']) for x in headers]]
        cells.extend([[Paragraph(safe(x),styles['TechCell']) for x in row] for row in rows])
        tab=Table(cells,repeatRows=1,hAlign='LEFT',colWidths=[(page[0]-68)/len(headers)]*len(headers))
        tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#a7b7c1')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
        story.append(tab)
    story.append(Paragraph(safe(data.get('project','LOGO! FBD')),styles['TechTitle']))
    for key,label in [('version','Versie'),('date','Datum'),('hardware','Hardware'),('software','Software'),('verification','Verificatie')]:
        story.append(p(f"{label}: {data.get(key,'Onbekend')}"))
    heading('Functionele beschrijving')
    story.append(p(data.get('description','Geen beschrijving')))
    heading('Ingangen')
    table(['ID','Naam','Actief','Omschrijving'],[[v.get('id',''),v.get('name',''),v.get('active',''),v.get('description','')] for v in data.get('inputs',[])])
    heading('Uitgangen')
    table(['ID','Naam','Omschrijving'],[[v.get('id',''),v.get('name',''),v.get('description','')] for v in data.get('outputs',[])])
    story.append(PageBreak())
    heading('FBD schema - illustratie (geen native export)')
    drawing=Drawing(755,310)
    drawing.add(Rect(0,0,755,310,strokeColor=LIGHT,fillColor=colors.white))
    positions={}
    for item in data.get('nodes',[]):
        x=float(item.get('x',0))*1.25+25
        y=float(item.get('y',0))*1.65+25
        positions[item['id']]=(x+26,y+11)
        drawing.add(Rect(x,y,52,24,fillColor=LIGHT,strokeColor=BLUE))
        drawing.add(String(x+26,y+8,str(item.get('label',item['id'])),textAnchor='middle',fontSize=10,fillColor=INK))
    for item in data.get('blocks',[]):
        x=float(item.get('x',0))*1.25+25
        y=float(item.get('y',0))*1.65+25
        positions[item['id']]=(x+39,y+21)
        drawing.add(Rect(x,y,78,43,fillColor=colors.white,strokeColor=INK))
        drawing.add(String(x+39,y+27,item['id'],textAnchor='middle',fontSize=9,fillColor=BLUE))
        drawing.add(String(x+39,y+12,str(item.get('name',''))[:17],textAnchor='middle',fontSize=8,fillColor=INK))
    for connection in data.get('connections',[]):
        a=connection['from'].split('.')[0]
        b=connection['to'].split('.')[0]
        if a in positions and b in positions:
            x1,y1=positions[a]
            x2,y2=positions[b]
            drawing.add(Line(x1+20,y1,x2-20,y2,strokeColor=BLUE,strokeWidth=1))
    story.append(drawing)
    story.append(p('Lijnen zijn slechts illustratief. Gebruik de exacte terminalverbindingen hieronder en controleer ze in Soft Comfort.'))
    heading('Netlist')
    table(['Van','Naar'],[[c.get('from',''),c.get('to','')] for c in data.get('connections',[])])
    story.append(PageBreak())
    heading('Blokken en parameters')
    table(['ID','Bloknaam','Pinnen','Parameters','Werking'],[[b.get(k,'') for k in ('id','name','pins','params','description')] for b in data.get('blocks',[])])
    heading('Stap-voor-stap opbouw')
    for i,step in enumerate(data.get('steps',[]),1):story.append(p(f'{i}. {step}'))
    heading('Tests en verwachte resultaten')
    table(['Scenario','Verwacht','Status'],[[v.get('scenario',''),v.get('expected',''),v.get('status','')] for v in data.get('tests',[])])
    heading('Veiligheid en beperkingen')
    for warning in data.get('warnings',[]):story.append(p('- '+warning))
    heading('Bronnen')
    for source in data.get('sources',[]):story.append(p(source))
    heading('Revisiehistoriek')
    table(['Versie','Datum','Wijziging'],[[r.get('version',''),r.get('date',''),r.get('changes','')] for r in data.get('revisions',[])])
    def footer(canvas,document):
        canvas.saveState()
        width,height=page
        canvas.setStrokeColor(BLUE)
        canvas.line(34,height-32,width-34,height-32)
        canvas.setFont('Helvetica',8)
        canvas.setFillColor(INK)
        canvas.drawString(34,24,f"{data.get('project','LOGO!')} | v{data.get('version','?')} | {data.get('verification','Niet geverifieerd')}")
        canvas.drawRightString(width-34,24,f"Pagina {document.page} | {data.get('date','')}")
        canvas.restoreState()
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(destination)

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('Usage: render_report.py input.json output.pdf')
    main(sys.argv[1],sys.argv[2])
