# -*- coding: utf-8 -*-
"""
Render src/content.py thanh file PDF dep, co tieng Viet day du.

Chay:  python3 src/build_outline.py
Phu thuoc: reportlab (pip install reportlab), PyMuPDF (tuy chon, de QA).
Font: assets/fonts/BeVietnamPro-*.ttf (SIL OFL 1.1) + DejaVu Sans (ky hieu).
"""

import os
import re
import sys
import html
from xml.sax.saxutils import escape as xml_escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                Flowable)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_DIR = os.path.join(ROOT, 'assets', 'fonts')
OUT = os.path.join(ROOT, 'DeCuong_OnTap_GK1_LichSu10_KNTT.pdf')

sys.path.insert(0, HERE)
from content import DOC  # noqa: E402

# ---------------------------------------------------------------- palettes
NAVY = colors.HexColor('#123049')
NAVY_D = colors.HexColor('#0C2237')
TEAL = colors.HexColor('#0E7C7B')
TEAL_D = colors.HexColor('#0A5F5E')
AMBER = colors.HexColor('#C0700F')
AMBER_L = colors.HexColor('#F0B44B')
GREEN = colors.HexColor('#2E7D52')
RED = colors.HexColor('#B5443A')
PURPLE = colors.HexColor('#5B4B9E')
GRAY = colors.HexColor('#4A5A69')
GRAY_L = colors.HexColor('#7D8B98')
WHITE = colors.white
DARK = colors.HexColor('#1E2E3C')

BLUE_BG = colors.HexColor('#EEF5FA')
TEAL_BG = colors.HexColor('#E6F4F2')
GREEN_BG = colors.HexColor('#EAF5EC')
AMBER_BG = colors.HexColor('#FFF3DE')
RED_BG = colors.HexColor('#FDEDEA')
PURPLE_BG = colors.HexColor('#F0EDFA')
GRAY_BG = colors.HexColor('#F3F6F9')
BORDER = colors.HexColor('#D5E1EB')

W, H = A4                      # 595.28 x 841.89
ML = MR = 46
MT = 54
MB = 48
CW = W - ML - MR              # ~503 pt

# ---------------------------------------------------------------- fonts
FONTS = {
    'BV': 'BeVietnamPro-Regular.ttf',
    'BV-B': 'BeVietnamPro-Bold.ttf',
    'BV-I': 'BeVietnamPro-Italic.ttf',
    'BV-BI': 'BeVietnamPro-BoldItalic.ttf',
    'BV-SB': 'BeVietnamPro-SemiBold.ttf',
}
for name, fn in FONTS.items():
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))
pdfmetrics.registerFontFamily('BV', normal='BV', bold='BV-B', italic='BV-I',
                              boldItalic='BV-BI')
pdfmetrics.registerFont(TTFont('DV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

try:
    from fontTools.ttLib import TTFont as _FT
    _BV_CMAP = set(_FT(os.path.join(FONT_DIR, FONTS['BV'])).getBestCmap().keys())
    _DV_CMAP = set(_FT('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf').getBestCmap().keys())
except Exception:
    _BV_CMAP, _DV_CMAP = set(), set()

MISSING_BOTH = []
TOTAL_PAGES = [0]

# Cac ki tu chi co o font du phong: khong dung trong TOC/outline (vi TOC
# duoc ve bang font chinh), nen thay bang ky tu an toan.
_SAFE_MAP = {
    '\u2192': '–', '\u2194': '–', '\u21c4': '–', '\u2190': '–',
    '\u2605': '*', '\u25a1': '-', '\u25cf': '*', '\u2713': 'v',
    '\u2013': '–', '\u2014': '—',
}


def safe_label(text):
    for k, v in _SAFE_MAP.items():
        text = text.replace(k, v)
    return text


def _fallback_glyphs(s):
    """Boc cac ki tu khong co trong Be Vietnam Pro bang font DejaVu."""
    parts = re.split(r'(<[^>]*>)', s)
    out = []
    for seg in parts:
        if seg.startswith('<') and seg.endswith('>'):
            out.append(seg)
            continue
        buf = []
        for ch in seg:
            cp = ord(ch)
            if cp in _BV_CMAP or ch in '\n\r\t':
                buf.append(ch)
            else:
                if buf:
                    out.append(''.join(buf))
                    buf = []
                if cp in _DV_CMAP:
                    out.append('<font name="DV">%s</font>' % xml_escape(ch))
                else:
                    MISSING_BOTH.append(ch)
                    out.append('?')
        if buf:
            out.append(''.join(buf))
    return ''.join(out)


def rich(text):
    """Chuyen markup thanh the Paragraph cua reportlab."""
    if text is None:
        return ''
    s = xml_escape(str(text))
    s = s.replace('\n', '<br/>')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'//(.+?)//', r'<i>\1</i>', s)
    s = re.sub(r'__(.+?)__', r'<u>\1</u>', s)
    s = re.sub(r'\{\{(.+?)\}\}', r'<font color="#0A5F5E"><b>\1</b></font>', s)
    return _fallback_glyphs(s)


def P(text, style):
    return Paragraph(rich(text), style)


# ---------------------------------------------------------------- styles
def st(name, **kw):
    base = dict(fontName='BV', fontSize=9.2, leading=13.6, textColor=DARK,
                spaceAfter=0, alignment=TA_JUSTIFY)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    'body': st('body', spaceAfter=5, leading=13.8),
    'body_tight': st('body_tight', spaceAfter=2, leading=13.0),
    'small': st('small', fontSize=8.2, leading=11.8, spaceAfter=3),
    'caption': st('caption', fontName='BV-B', fontSize=8.4, leading=12,
                  textColor=TEAL_D, spaceBefore=7, spaceAfter=4, alignment=TA_LEFT,
                  keepWithNext=1),
    'h1n': st('h1n', fontName='BV-B', fontSize=9.5, leading=12, textColor=AMBER_L,
              alignment=TA_LEFT),
    'h1t': st('h1t', fontName='BV-B', fontSize=16.5, leading=20, textColor=WHITE,
              alignment=TA_LEFT),
    'h1s': st('h1s', fontName='BV-I', fontSize=9.2, leading=12.5,
              textColor=colors.HexColor('#CFE3EA'), alignment=TA_LEFT),
    'h2': st('h2', fontName='BV-B', fontSize=11.6, leading=15.5, textColor=NAVY,
             spaceBefore=11, spaceAfter=6, alignment=TA_LEFT, keepWithNext=1),
    'h3': st('h3', fontName='BV-SB', fontSize=10, leading=14, textColor=TEAL_D,
             spaceBefore=9, spaceAfter=5, alignment=TA_LEFT, keepWithNext=1),
    'box_title': st('box_title', fontName='BV-B', fontSize=9.4, leading=13,
                    textColor=NAVY, alignment=TA_LEFT, spaceAfter=4),
    'box_item': st('box_item', fontSize=9, leading=13.2, spaceAfter=4),
    'th': st('th', fontName='BV-B', fontSize=8.1, leading=11, textColor=WHITE,
             alignment=TA_LEFT),
    'td': st('td', fontSize=8.2, leading=11.6, alignment=TA_LEFT),
    'tdc': st('tdc', fontSize=8.2, leading=11.6, alignment=TA_CENTER),
    'qhead': st('qhead', fontName='BV-B', fontSize=8, leading=11, textColor=TEAL_D,
                alignment=TA_LEFT),
    'qstem': st('qstem', fontName='BV-SB', fontSize=9.2, leading=13.6,
                alignment=TA_JUSTIFY, spaceAfter=3),
    'qopt': st('qopt', fontSize=8.9, leading=12.8, alignment=TA_LEFT),
    'why': st('why', fontSize=8.6, leading=12.4, alignment=TA_JUSTIFY),
    'ansbig': st('ansbig', fontName='BV-B', fontSize=9.5, leading=12,
                 textColor=WHITE, alignment=TA_CENTER),
    'kq': st('kq', fontName='BV-B', fontSize=8.9, leading=12, textColor=TEAL_D),
    'kv': st('kv', fontSize=8.8, leading=12.6, alignment=TA_JUSTIFY),
    'cardq': st('cardq', fontName='BV-SB', fontSize=8.6, leading=11.8,
                textColor=NAVY, alignment=TA_LEFT),
    'carda': st('carda', fontSize=8.2, leading=11.4, textColor=GRAY,
                alignment=TA_LEFT),
    'bullet': st('bullet', fontSize=9, leading=13.4, alignment=TA_JUSTIFY),
    'numtxt': st('numtxt', fontSize=9, leading=13.4, alignment=TA_JUSTIFY),
    'toc0': st('toc0', fontName='BV-B', fontSize=10, leading=16, textColor=NAVY,
               spaceBefore=6, alignment=TA_LEFT),
    'toc1': st('toc1', fontSize=8.9, leading=13.5, textColor=DARK,
               leftIndent=15, alignment=TA_LEFT),
    'toc2': st('toc2', fontSize=8, leading=11.8, textColor=GRAY,
               leftIndent=30, alignment=TA_LEFT),
    'cover_note': st('cover_note', fontSize=8.6, leading=12.6, textColor=GRAY,
                     alignment=TA_LEFT),
}

BOX_STYLE = {
    'note':   (BLUE_BG, NAVY, NAVY),
    'key':    (TEAL_BG, TEAL, TEAL_D),
    'tip':    (GREEN_BG, GREEN, GREEN),
    'warn':   (AMBER_BG, AMBER, AMBER),
    'exam':   (PURPLE_BG, PURPLE, PURPLE),
    'sample': (GRAY_BG, GRAY_L, NAVY),
    'question': (BLUE_BG, NAVY, NAVY),
}


# ---------------------------------------------------------------- helpers
def scale_cols(cols):
    total = float(sum(cols))
    return [c * CW / total for c in cols]


def grid_style(nrows, ncols, fontsize=8.2, header=True, zebra=True,
               align_center_cols=()):
    cmds = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('LINEBELOW', (0, 0), (-1, 0), 0.8, NAVY),
    ]
    if header:
        cmds.append(('BACKGROUND', (0, 0), (-1, 0), NAVY))
    if zebra:
        for r in range(1 if header else 0, nrows):
            if r % 2 == (1 if header else 0):
                cmds.append(('BACKGROUND', (0, r), (-1, r), GRAY_BG))
    for c in align_center_cols:
        cmds.append(('ALIGN', (c, 0), (c, -1), 'CENTER'))
    return TableStyle(cmds)


def add_caption(story, caption):
    if caption:
        story.append(P(caption, S['caption']))


def make_box(kind, title, items, story):
    bg, bar, title_color = BOX_STYLE.get(kind, BOX_STYLE['note'])
    # Chia nho cac hop qua dai de khong bi "Flowable too large".
    chunks, cur, size = [], [], 0
    for it in items:
        L = len(str(it))
        if cur and size + L > 950:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(it)
        size += L
    if cur:
        chunks.append(cur)

    for ci, chunk in enumerate(chunks):
        inner = []
        if ci == 0 and title:
            ts = ParagraphStyle('bt', parent=S['box_title'], textColor=title_color)
            inner.append(Paragraph(rich(title), ts))
        elif ci > 0 and title:
            ts = ParagraphStyle('bt2', parent=S['box_title'], textColor=title_color,
                                fontSize=8.4)
            inner.append(Paragraph(rich(title + ' (tiếp theo)'), ts))
        for it in chunk:
            inner.append(P(it, S['box_item']))
        t = Table([[inner]], colWidths=[CW])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), bg),
            ('LINEBEFORE', (0, 0), (0, -1), 3.2, bar),
            ('BOX', (0, 0), (-1, -1), 0.4, BORDER),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(t)
        story.append(Spacer(1, 8))


def make_table(block, story):
    cols = scale_cols(block['cols'])
    fs = block.get('fontsize', 8.2)
    th = ParagraphStyle('thx', parent=S['th'], fontSize=fs)
    td = ParagraphStyle('tdx', parent=S['td'], fontSize=fs)
    head = block.get('head')
    rows = []
    if head:
        rows.append([Paragraph(rich(h), th) for h in head])
    for r in block['rows']:
        rows.append([Paragraph(rich(c), td) for c in r])
    t = Table(rows, colWidths=cols, repeatRows=1 if head else 0, hAlign='LEFT')
    t.setStyle(grid_style(len(rows), len(cols), fontsize=fs, header=bool(head)))
    add_caption(story, block.get('caption'))
    story.append(t)
    story.append(Spacer(1, 8))


def make_kv(block, story):
    rows = []
    for k, v in block['items']:
        ks = ParagraphStyle('kk', parent=S['kv'], fontName='BV-B', textColor=TEAL_D,
                            alignment=TA_LEFT)
        rows.append([Paragraph(rich(k), ks), Paragraph(rich(v), S['kv'])])
    t = Table(rows, colWidths=[CW * 0.27, CW * 0.73], hAlign='LEFT')
    cmds = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('LINEBEFORE', (0, 0), (0, -1), 2.4, TEAL),
    ]
    for i in range(len(rows)):
        if i % 2 == 0:
            cmds.append(('BACKGROUND', (0, i), (-1, i), TEAL_BG))
    t.setStyle(TableStyle(cmds))
    story.append(t)
    story.append(Spacer(1, 8))


def make_cards(block, story):
    rows = []
    items = block['items']
    for i in range(0, len(items), 2):
        row = []
        for q, a in items[i:i + 2]:
            cell = [Paragraph(rich('CÂU: ' + q), S['cardq']),
                    Spacer(1, 2),
                    Paragraph(rich('→ ' + a), S['carda'])]
            row.append(cell)
        while len(row) < 2:
            row.append('')
        rows.append(row)
    t = Table(rows, colWidths=[CW / 2, CW / 2], hAlign='LEFT')
    cmds = [('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
            ('LEFTPADDING', (0, 0), (-1, -1), 7),
            ('RIGHTPADDING', (0, 0), (-1, -1), 7),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]
    for i in range(len(rows)):
        for j in range(2):
            cmds.append(('BACKGROUND', (j, i), (j, i),
                         TEAL_BG if (i + j) % 2 == 0 else GRAY_BG))
    t.setStyle(TableStyle(cmds))
    story.append(t)
    story.append(Spacer(1, 8))


def make_list(block, story, numbered=False):
    rows = []
    for idx, it in enumerate(block['items'], 1):
        label = ('%d.' % idx) if numbered else '•'
        ls = ParagraphStyle('lbl', parent=S['body_tight'], fontName='BV-B',
                            textColor=TEAL if numbered else NAVY,
                            alignment=TA_CENTER, fontSize=9)
        rows.append([Paragraph(rich(label), ls), P(it, S['numtxt'])])
    t = Table(rows, colWidths=[24, CW - 24], hAlign='LEFT')
    cmds = [('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    t.setStyle(TableStyle(cmds))
    story.append(t)
    story.append(Spacer(1, 7))


def make_checklist(block, story):
    rows = []
    for it in block['items']:
        rows.append([Paragraph('<font name="DV">\u25a1</font>',
                               ParagraphStyle('chk', fontName='BV', fontSize=12,
                                              leading=14, textColor=TEAL)),
                     P(it, S['numtxt'])])
    t = Table(rows, colWidths=[24, CW - 24], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))


def section_header(block, story, key):
    inner = [
        Paragraph(rich(block['n']), S['h1n']),
        Spacer(1, 2),
        Paragraph(rich(block['title']), S['h1t']),
        Spacer(1, 3),
        Paragraph(rich(block.get('sub', '')), S['h1s']),
    ]
    t = Table([[inner]], colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('LINEBEFORE', (0, 0), (0, -1), 5, AMBER_L),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 11),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    t._toc = (0, safe_label('%s · %s' % (block['n'], block['title'])), key)
    story.append(t)
    story.append(Spacer(1, 12))


def heading(text, level, story, key):
    style = S['h2'] if level == 1 else S['h3']
    p = Paragraph(rich(text), style)
    p._toc = (level, safe_label(text), key)
    story.append(p)


QW = CW - 22   # be trong cua hop cau hoi (da tru padding trai/phai)


def question_card(code, meta, inner_flowables, story, accent=TEAL, bg=GRAY_BG):
    head = Table([[Paragraph(rich('CÂU ' + code), S['qhead']),
                   Paragraph(rich(meta), ParagraphStyle('qm', parent=S['small'],
                                                        textColor=GRAY,
                                                        alignment=2))]],
                 colWidths=[QW * 0.35, QW * 0.65])
    head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER),
    ]))
    content = [head, Spacer(1, 5)] + inner_flowables
    t = Table([[content]], colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LINEBEFORE', (0, 0), (0, -1), 2.6, accent),
        ('BOX', (0, 0), (-1, -1), 0.4, BORDER),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(KeepTogether(t))
    story.append(Spacer(1, 8))


def make_mcq(block, story, QA):
    inner = [P(block['q'], S['qstem']), Spacer(1, 3)]
    for o in block['opts']:
        inner.append(P(o, S['qopt']))
    if block.get('extra'):
        inner.append(Spacer(1, 4))
        inner.append(P('**Đáp án: ' + block['ans'] + '.** ' + block['why'], S['why']))
    else:
        QA['mcq'].append(block)
    question_card(block['code'], block['meta'], inner, story, accent=TEAL, bg=GRAY_BG)


def make_tf(block, story, QA):
    inner = [P(block['q'], S['qstem']), Spacer(1, 5)]
    for letter, statement, ans, why in block['items']:
        line = Table([[Paragraph(rich('**' + letter + '.** ' + statement), S['qopt']),
                       Paragraph('<font name="DV">\u25a1</font> Đ   '
                                 '<font name="DV">\u25a1</font> S',
                                 ParagraphStyle('ds', parent=S['small'],
                                                alignment=2, textColor=GRAY))]],
                     colWidths=[QW - 90, 90])
        line.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ]))
        inner.append(line)
    QA['tf'].append(block)
    question_card(block['code'], block['meta'], inner, story, accent=PURPLE, bg=PURPLE_BG)


def make_essay(block, story):
    inner = [P(block['q'], S['qstem']), Spacer(1, 5)]
    for g in block['guide']:
        inner.append(P(g, S['small']))
        inner.append(Spacer(1, 1))
    question_card(block['code'], block['meta'], inner, story, accent=AMBER, bg=AMBER_BG)


# ---------------------------------------------------------------- answers
def make_answers(story, QA, add_heading):
    mcqs = QA['mcq']
    tfs = QA['tf']

    # ---- 4.2 bang dap an nhanh phan I
    add_heading('4.2. Bảng đáp án nhanh — Phần I (20 câu TN)', 1, story)
    for start in (0, 10):
        group = mcqs[start:start + 10]
        head = ['Câu'] + [m['code'] for m in group]
        row1 = ['Mã'] + [m['code'].replace('I.', '') for m in group]
        row2 = ['Đáp án'] + [m['ans'] for m in group]
        fs = 8.4
        ths = ParagraphStyle('ths', parent=S['th'], fontSize=fs, alignment=TA_CENTER)
        tds = ParagraphStyle('tds', parent=S['tdc'], fontSize=fs)
        bold = ParagraphStyle('bld', parent=tds, fontName='BV-B', textColor=TEAL_D)
        rows = [[Paragraph(rich(h), ths) for h in head],
                [Paragraph(rich(row1[0]), bold)] + [Paragraph(rich(x), tds) for x in row1[1:]],
                [Paragraph(rich(row2[0]), bold)] + [Paragraph(rich(x), bold) for x in row2[1:]]]
        cw = [CW * 0.14] + [CW * 0.86 / 10] * 10
        t = Table(rows, colWidths=cw, hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), NAVY),
            ('BACKGROUND', (0, 2), (-1, 2), TEAL_BG),
            ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ]))
        story.append(t)
        story.append(Spacer(1, 7))
    story.append(P('**Tự chấm:** mỗi câu đúng 0,25 điểm → tối đa **5,0 điểm**. '
                   'Tổng 20 câu này chiếm đúng một nửa điểm bài kiểm tra.', S['body']))

    # ---- 4.3 bang dap an nhanh phan II
    add_heading('4.3. Bảng đáp án nhanh — Phần II (2 câu Đúng/Sai)', 1, story)
    rows = [['Câu', 'ý a', 'ý b', 'ý c', 'ý d', 'Điểm']]
    for tf in tfs:
        rows.append([tf['code']] + [it[2] for it in tf['items']] + ['1,0'])
    fs = 8.8
    ths = ParagraphStyle('ths2', parent=S['th'], fontSize=fs, alignment=TA_CENTER)
    tds = ParagraphStyle('tds2', parent=S['tdc'], fontSize=fs)
    rr = [[Paragraph(rich(c), ths if i == 0 else tds) for c in row]
          for i, row in enumerate(rows)]
    t = Table(rr, colWidths=[CW * 0.16] + [CW * 0.168] * 4 + [CW * 0.168],
              hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 1), (-1, -1), GRAY_BG),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))
    story.append(P('**Tự chấm:** mỗi ý đúng 0,25 điểm → 8 ý = **2,0 điểm**. '
                   'Ghi nhớ: một ý chỉ Đúng khi **mọi vế** trong ý đều đúng.', S['body']))

    # ---- 4.4 giai thich chi tiet phan I
    add_heading('4.4. Giải thích chi tiết 20 câu trắc nghiệm (I.1 – I.20)', 1, story)
    code_badge = ParagraphStyle('codebadge', parent=S['ansbig'], fontSize=8.2,
                                leading=10.5)
    for m in mcqs:
        badge = Table([[Paragraph(rich(m['code']), code_badge)],
                       [Paragraph(rich(m['ans']), S['ansbig'])]],
                      colWidths=[34])
        badge.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), NAVY),
            ('BACKGROUND', (0, 1), (-1, 1), TEAL),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        txt = [Paragraph(rich('**' + m['code'] + ' · ' + m['meta'] + '**'), S['kq']),
               Spacer(1, 2),
               P(m['q'], S['why']), Spacer(1, 2),
               P('**Đáp án ' + m['ans'] + '.** ' + m['why'], S['why'])]
        cell = Table([[badge, txt]], colWidths=[38, CW - 38])
        cell.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (0, 0), 0),
            ('RIGHTPADDING', (0, 0), (0, 0), 6),
            ('LEFTPADDING', (1, 0), (1, 0), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LINEBELOW', (0, 0), (-1, -1), 0.4, BORDER),
        ]))
        story.append(KeepTogether(cell))
        story.append(Spacer(1, 3))

    # ---- 4.5 giai thich chi tiet phan II
    add_heading('4.5. Giải thích chi tiết 8 ý Đúng/Sai (II.1, II.2)', 1, story)
    for tf in tfs:
        story.append(P('**' + tf['code'] + '** — ' + tf['meta'], S['kq']))
        story.append(Spacer(1, 3))
        rows = []
        for letter, statement, ans, why in tf['items']:
            acol = TEAL if ans == 'Đ' else RED
            ast = ParagraphStyle('ast', parent=S['tdc'], fontName='BV-B',
                                 textColor=WHITE, fontSize=9)
            badge = Table([[Paragraph(ans, ast)]], colWidths=[20])
            badge.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), acol),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            rows.append([Paragraph(rich('**' + letter + '.**'), S['td']),
                         badge,
                         Paragraph(rich(statement), S['td']),
                         Paragraph(rich(why), S['why'])])
        t = Table([[Paragraph(rich('Ý'), S['th']), Paragraph(rich('Đ/S'), S['th']),
                    Paragraph(rich('Nội dung ý'), S['th']),
                    Paragraph(rich('Giải thích'), S['th'])]] + rows,
                  colWidths=[22, 24, CW * 0.36, CW * 0.64 - 46], hAlign='LEFT')
        t.setStyle(grid_style(len(rows) + 1, 4, fontsize=8, header=True))
        story.append(t)
        story.append(Spacer(1, 10))


# ---------------------------------------------------------------- canvas
def draw_cover(c, doc):
    c.saveState()
    # Nen trang
    c.setFillColor(WHITE)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    # Bang tren
    c.setFillColor(NAVY)
    c.rect(0, 516, W, H - 516, stroke=0, fill=1)
    # Khoi cheo mau teal
    c.setFillColor(TEAL_D)
    p = c.beginPath()
    p.moveTo(452, H)
    p.lineTo(W, H)
    p.lineTo(W, H - 182)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(AMBER_L)
    c.rect(0, 516, W, 4, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(48, 470, 74, 3, stroke=0, fill=1)

    # Nhan nho
    c.setFont('BV-SB', 10)
    c.setFillColor(AMBER_L)
    c.drawString(48, 792, 'NĂM HỌC 2026 – 2027   ·   KIỂM TRA ĐỊNH KÌ GIỮA HỌC KÌ I')

    # Tieu de lon
    c.setFont('BV-B', 46)
    c.setFillColor(WHITE)
    c.drawString(46, 728, 'ĐỀ CƯƠNG')
    c.setFont('BV-B', 24)
    c.drawString(48, 692, 'ÔN TẬP KIỂM TRA')
    c.drawString(48, 660, 'GIỮA HỌC KÌ I')
    c.setFont('BV-B', 41)
    c.setFillColor(AMBER_L)
    c.drawString(46, 602, 'LỊCH SỬ 10')
    c.setFont('BV', 12)
    c.setFillColor(colors.HexColor('#DCEAF0'))
    c.drawString(48, 574, 'Bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG')
    c.setFont('BV-I', 9.5)
    c.drawString(48, 551, 'Biên soạn từ ma trận đề & bảng đặc tả LS10- MTGK1-26-27-HHT.docx')

    # Phan than trang
    c.setFillColor(NAVY)
    c.setFont('BV-B', 11)
    c.drawString(48, 478, 'BÁM SÁT 100% MA TRẬN ĐỀ   ·   TỐI ƯU CHO VIỆC GHI NHỚ')

    cards = [
        (48, 385, '45 PHÚT', 'Thời gian làm bài', NAVY),
        (307, 385, '10 ĐIỂM', 'Thang điểm tối đa', TEAL),
        (48, 283, '20 + 2 + 1', 'TN nhiều lựa chọn · TN Đ/S · Tự luận', PURPLE),
        (307, 283, '28 + 1', 'Lệnh hỏi TN + 1 câu TL', AMBER),
    ]
    for x, y, big, small, col in cards:
        c.setFillColor(GRAY_BG)
        c.roundRect(x, y, 240, 82, 7, stroke=0, fill=1)
        c.setFillColor(col)
        c.rect(x, y, 4, 82, stroke=0, fill=1)
        c.setFont('BV-B', 23)
        c.drawString(x + 16, y + 45, big)
        c.setFont('BV', 9)
        c.setFillColor(GRAY)
        c.drawString(x + 16, y + 24, small)

    # Hop noi bat
    c.setFillColor(TEAL_BG)
    c.roundRect(48, 192, 499, 68, 7, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(48, 192, 4, 68, stroke=0, fill=1)
    c.setFont('BV-B', 11)
    c.setFillColor(TEAL_D)
    c.drawString(65, 236, 'TOÀN BỘ 28 LỆNH HỎI TRẮC NGHIỆM + 1 CÂU TỰ LUẬN')
    c.setFont('BV', 9.4)
    c.setFillColor(DARK)
    c.drawString(65, 216, 'Tái tạo đúng mã câu I.1 – I.20 · II.1a – d · II.2a – d · TL,')
    c.drawString(65, 202, 'kèm đáp án, giải thích chi tiết, sơ đồ tư duy và lịch ôn 7 ngày.')

    # Thanh 3 bai
    c.setFont('BV-B', 9)
    c.setFillColor(NAVY)
    c.drawString(48, 160, 'PHÂN BỔ ĐIỂM THEO BÀI')
    seps = [(48, 'BÀI 1', '1,50 đ  ·  15%', 152),
            (215, 'BÀI 2', '2,75 đ  ·  27,5%', 152),
            (382, 'BÀI 3', '5,75 đ  ·  57,5%', 165)]
    for x, name, val, wd in seps:
        c.setFillColor(NAVY if name != 'BÀI 3' else TEAL)
        c.roundRect(x, 108, wd, 40, 5, stroke=0, fill=1)
        c.setFont('BV-B', 10)
        c.setFillColor(WHITE)
        c.drawString(x + 12, 131, name)
        c.setFont('BV', 9)
        c.drawString(x + 12, 116, val)

    c.setStrokeColor(BORDER)
    c.line(48, 78, W - 48, 78)
    c.setFont('BV', 8)
    c.setFillColor(GRAY_L)
    c.drawString(48, 62, 'Tài liệu học tập · Có mục lục tương tác, đánh dấu trang và đáp án tự chấm.')
    c.drawRightString(W - 48, 62, 'PDF · 2026')
    c.restoreState()


def draw_later(c, doc):
    c.saveState()
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.line(ML, H - 40, W - MR, H - 40)
    c.line(ML, 36, W - MR, 36)
    c.setFont('BV-SB', 7.6)
    c.setFillColor(NAVY)
    c.drawString(ML, H - 32, 'ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  LỊCH SỬ 10  ·  KẾT NỐI TRI THỨC')
    c.setFont('BV', 7.6)
    c.setFillColor(GRAY_L)
    c.drawRightString(W - MR, H - 32, 'Năm học 2026 – 2027')
    c.drawString(ML, 24, 'Lịch sử 10 · Kết nối tri thức với cuộc sống')
    total = TOTAL_PAGES[0]
    label = ('Trang %d / %d' % (doc.page, total)) if total else ('Trang %d' % doc.page)
    c.drawRightString(W - MR, 24, label)
    c.restoreState()


# ---------------------------------------------------------------- doc template
class OutlineDoc(BaseDocTemplate):
    def beforeDocument(self):
        self._seen_keys = set()

    def afterFlowable(self, flowable):
        if hasattr(flowable, '_toc'):
            level, text, key = flowable._toc
            if key in getattr(self, '_seen_keys', set()):
                return
            self._seen_keys.add(key)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=min(level, 2), closed=False)
            self.notify('TOCEntry', (level, text, self.page, key))


# ---------------------------------------------------------------- build
def build_story():
    story = []
    QA = {'mcq': [], 'tf': []}
    counter = [0]

    def key():
        counter[0] += 1
        return 'bm%04d' % counter[0]

    def add_heading(text, level, st_list):
        heading(text, level, st_list, key())

    for block in DOC:
        t = block['t']
        if t == 'toc':
            toc = TableOfContents()
            toc.levelStyles = [
                ParagraphStyle('t0', parent=S['toc0'], leftIndent=0, firstLineIndent=0),
                ParagraphStyle('t1', parent=S['toc1'], leftIndent=16, firstLineIndent=-8),
                ParagraphStyle('t2', parent=S['toc2'], leftIndent=32, firstLineIndent=-8),
            ]
            toc.dotsMinLevel = 0
            story.append(Paragraph('MỤC LỤC', ParagraphStyle(
                'tochead', fontName='BV-B', fontSize=18, leading=24,
                textColor=NAVY, spaceAfter=10)))
            story.append(Paragraph(
                'Nhấn vào một mục để chuyển tới trang tương ứng (PDF có đánh dấu trang).',
                S['small']))
            story.append(Spacer(1, 10))
            story.append(toc)
            story.append(PageBreak())
        elif t == 'h1':
            section_header(block, story, key())
        elif t == 'h2':
            heading(block['title'], 1, story, key())
        elif t == 'h3':
            heading(block['title'], 2, story, key())
        elif t == 'p':
            story.append(P(block['text'], S['body']))
        elif t == 'box':
            make_box(block.get('kind', 'note'), block.get('title'),
                     block['items'], story)
        elif t == 'table':
            make_table(block, story)
        elif t == 'kv':
            make_kv(block, story)
        elif t == 'cards':
            make_cards(block, story)
        elif t == 'bul':
            make_list(block, story, numbered=False)
        elif t == 'num':
            make_list(block, story, numbered=True)
        elif t == 'checklist':
            make_checklist(block, story)
        elif t == 'mcq':
            make_mcq(block, story, QA)
        elif t == 'tf':
            make_tf(block, story, QA)
        elif t == 'essay':
            make_essay(block, story)
        elif t == 'answers':
            make_answers(story, QA, add_heading)
        elif t == 'pb':
            story.append(PageBreak())
        elif t == 'spacer':
            story.append(Spacer(1, block.get('h', 6)))
        else:
            raise ValueError('Unknown block type: %r' % t)
    return story


def count_pages(path):
    data = open(path, 'rb').read()
    return len(re.findall(rb'/Type\s*/Page[^s]', data))


def make_doc():
    doc = OutlineDoc(OUT, pagesize=A4,
                     leftMargin=ML, rightMargin=MR,
                     topMargin=MT, bottomMargin=MB,
                     title='Đề cương ôn tập kiểm tra giữa học kì I - Lịch sử 10 (Kết nối tri thức)',
                     author='Biên soạn từ ma trận đề LS10- MTGK1-26-27-HHT.docx',
                     subject='Lịch sử 10 · Kết nối tri thức với cuộc sống · Năm học 2026-2027',
                     creator='Arena.ai Agent Mode · reportlab')
    frame = Frame(ML, MB, CW, H - MT - MB, id='body',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def on_page(c, d):
        if d.page == 1:
            draw_cover(c, d)
        else:
            draw_later(c, d)

    doc.addPageTemplates([PageTemplate(id='all', frames=[frame], onPage=on_page)])
    story = build_story()
    # Trang 1 = bia (chi co anh ve bang canvas), trang 2 tro di = noi dung.
    seq = [Spacer(1, 1), PageBreak()] + story
    return doc, seq


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    # Pass 1: xac dinh tong so trang (footer chua biet tong -> hien "Trang n").
    doc, seq = make_doc()
    doc.multiBuild(seq)
    TOTAL_PAGES[0] = count_pages(OUT)
    # Pass 2: ve lai voi footer "Trang n / N". Khong doi luong flowable nen
    # so trang va muc luc van giu nguyen.
    doc2, seq2 = make_doc()
    doc2.multiBuild(seq2)
    final_pages = count_pages(OUT)
    if final_pages != TOTAL_PAGES[0]:
        TOTAL_PAGES[0] = final_pages
        doc3, seq3 = make_doc()
        doc3.multiBuild(seq3)
        final_pages = count_pages(OUT)
    print('WROTE', OUT, os.path.getsize(OUT), 'bytes,', final_pages, 'pages')
    if MISSING_BOTH:
        print('WARNING: ki tu thieu trong ca 2 font:', sorted(set(MISSING_BOTH)))


if __name__ == '__main__':
    main()
