"""Build the Vietnamese study guide. Run: python scripts/build_pdf.py."""
from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER

ROOT = Path(__file__).resolve().parents[1]
FONT = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('DV', str(FONT / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DV-Bold', str(FONT / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-Bold', italic='DV', boldItalic='DV-Bold')
navy = colors.HexColor('#16324f')
styles = {
    'body': ParagraphStyle('body', fontName='DV', fontSize=10, leading=15.5, spaceAfter=7, textColor=colors.HexColor('#202a35')),
    'title': ParagraphStyle('title', fontName='DV-Bold', fontSize=23, leading=31, spaceAfter=18, textColor=navy),
    'h2': ParagraphStyle('h2', fontName='DV-Bold', fontSize=15, leading=22, spaceBefore=12, spaceAfter=12, textColor=navy, keepWithNext=True),
    'h3': ParagraphStyle('h3', fontName='DV-Bold', fontSize=11.5, leading=17, spaceBefore=9, spaceAfter=8, textColor=navy, keepWithNext=True),
}
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.states = []
    def showPage(self):
        self.states.append(dict(self.__dict__))
        self._startPage()
    def save(self):
        count = len(self.states)
        for state in self.states:
            self.__dict__.update(state)
            self.setStrokeColor(colors.HexColor('#d6e0e8'))
            self.line(45, 43, 550, 43)
            self.setFont('DV', 8)
            self.setFillColor(navy)
            self.drawString(45, 29, 'LỊCH SỬ 10 • ÔN GIỮA KÌ I • BÀI 1–3')
            self.drawRightString(550, 29, f'{self._pageNumber} / {count}')
            super().showPage()
        super().save()

source = ROOT / 'docs/de-cuong-lich-su-10.md'
output = ROOT / 'docs/de-cuong-lich-su-10-giua-ki-1.pdf'
story = []
block = []
def flush():
    if block:
        # Keep each question and its four options together.
        story.append(KeepTogether([Paragraph(escape(x), styles['body']) for x in block]))
        block.clear()
for raw in source.read_text().splitlines():
    line = raw.strip()
    if not line:
        flush()
        continue
    if line.startswith('# '):
        flush(); story.append(Spacer(1, 40)); story.append(Paragraph(escape(line[2:]), styles['title']))
    elif line.startswith('## '):
        flush()
        text = line[3:]
        if len(text) > 2 and text[1:3] == '. ':
            story.append(PageBreak())
        story.append(Paragraph(escape(text), styles['h2']))
    elif line.startswith('### '):
        flush(); story.append(Paragraph(escape(line[4:]), styles['h3']))
    elif line.startswith('Câu ') or (len(line)>2 and line[0] in 'ABCD' and line[1:3] == '. ' and block):
        block.append(line)
    else:
        flush(); story.append(Paragraph(escape(line), styles['body']))
flush()
doc = SimpleDocTemplate(str(output), pagesize=(595.28, 841.89), rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=59, title='Đề cương ôn tập giữa học kì I – Lịch sử 10', author='Tài liệu ôn tập theo ma trận được cung cấp')
doc.build(story, canvasmaker=NumberedCanvas)
print(output)
