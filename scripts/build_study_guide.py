"""Build the Vietnamese study PDF from the reviewable Markdown source.
Run: .venv/bin/python scripts/build_study_guide.py
"""
from pathlib import Path
import os
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path(os.environ.get('DEJAVU_FONT_DIR', '/usr/share/fonts/truetype/dejavu'))
for name, file in [('DV', 'DejaVuSans.ttf'), ('DV-Bold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-Bold', italic='DV', boldItalic='DV-Bold')
OUT = ROOT / 'study-guides/LS10-de-cuong-on-tap-giua-ki-1-2026-2027.pdf'
styles = {
    'body': ParagraphStyle('body', fontName='DV', fontSize=10.2, leading=15, spaceAfter=6, textColor=colors.HexColor('#253249')),
    'h1': ParagraphStyle('h1', fontName='DV-Bold', fontSize=23, leading=31, spaceAfter=18, textColor=colors.HexColor('#153f5e')),
    'h2': ParagraphStyle('h2', fontName='DV-Bold', fontSize=15, leading=22, spaceBefore=8, spaceAfter=14, keepWithNext=True, textColor=colors.HexColor('#153f5e')),
    'h3': ParagraphStyle('h3', fontName='DV-Bold', fontSize=11.5, leading=17, spaceBefore=11, spaceAfter=8, keepWithNext=True, textColor=colors.HexColor('#14736f')),
    'option': ParagraphStyle('option', fontName='DV', fontSize=10.2, leading=15, leftIndent=13, spaceAfter=3),
}

def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(colors.HexColor('#c4d6df'))
    canvas.line(45, 39, w - 45, 39)
    canvas.setFont('DV', 8)
    canvas.setFillColor(colors.HexColor('#526779'))
    canvas.drawString(45, 26, 'LỊCH SỬ 10 • GIỮA KÌ I • TÀI LIỆU ÔN TẬP / ĐỀ LUYỆN')
    canvas.drawRightString(w - 45, 26, str(doc.page))
    canvas.restoreState()


def build():
    lines = (ROOT / 'study-guides/de-cuong-lich-su-10.md').read_text(encoding='utf-8').splitlines()
    story = []
    i = 0
    question_count = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        if line == '---':
            story.append(PageBreak())
            continue
        # Keep each MCQ stem and its four options together.
        if re.match(r'^I\.\d+\. ', line):
            block = [Paragraph(escape(line), styles['body'])]
            while i < len(lines) and re.match(r'^[A-D]\. ', lines[i]):
                block.append(Paragraph(escape(lines[i]), styles['option']))
                i += 1
            if len(block) != 5:
                raise ValueError(f'Expected four choices: {line}')
            question_count += 1
            block.append(Spacer(1, 9))
            story.append(KeepTogether(block))
            continue
        if line.startswith('### 8.3.'):
            block = [Paragraph(escape(line[4:]), styles['h3'])]
            while i < len(lines):
                if lines[i].strip():
                    block.append(Paragraph(escape(lines[i]), styles['body']))
                i += 1
            story.append(KeepTogether(block))
            continue
        if line.startswith('### '):
            style, line = 'h3', line[4:]
        elif line.startswith('## '):
            style, line = 'h2', line[3:]
        elif line.startswith('# '):
            style, line = 'h1', line[2:]
        else:
            style = 'body'
        story.append(Paragraph(escape(line), styles[style]))
    assert question_count == 20
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=45, leftMargin=45,
                            topMargin=43, bottomMargin=53, title='Đề cương Lịch sử 10 — Giữa học kì I 2026–2027',
                            author='Tài liệu ôn tập — biên soạn theo ma trận được cung cấp')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)

if __name__ == '__main__':
    build()
