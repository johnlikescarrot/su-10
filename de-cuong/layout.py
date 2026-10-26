"""Các hàm dựng bố cục PDF (reportlab) cho đề cương ôn tập.

Dùng font Be Vietnam Pro (SIL OFL 1.1) để hiển thị đầy đủ tiếng Việt.
"""
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    CondPageBreak,
    KeepTogether,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus import Paragraph as _RLParagraph

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

# ---------------------------------------------------------------- fonts
_FONTS = {
    "BVP": "BeVietnamPro_400Regular.ttf",
    "BVP-I": "BeVietnamPro_400Regular_Italic.ttf",
    "BVP-B": "BeVietnamPro_600SemiBold.ttf",
    "BVP-BI": "BeVietnamPro_600SemiBold_Italic.ttf",
    "BVP-H": "BeVietnamPro_700Bold.ttf",
    "BVP-X": "BeVietnamPro_800ExtraBold.ttf",
}
for _name, _file in _FONTS.items():
    pdfmetrics.registerFont(TTFont(_name, os.path.join(FONT_DIR, _file)))
pdfmetrics.registerFontFamily(
    "BVP", normal="BVP", bold="BVP-B", italic="BVP-I", boldItalic="BVP-BI"
)
# Font dự phòng cho kí hiệu (★ ☐ ① → ⊕ …) mà Be Vietnam Pro không có.
pdfmetrics.registerFont(TTFont("DJV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DJV-B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DJV", normal="DJV", bold="DJV-B", italic="DJV", boldItalic="DJV-B")

_BVP_CMAP = set(pdfmetrics.getFont("BVP").face.charToGlyph.keys())


def sym(text):
    """Bọc các kí tự không có trong Be Vietnam Pro bằng font DejaVu Sans."""
    out = []
    for ch in text:
        if ord(ch) > 127 and ord(ch) not in _BVP_CMAP:
            out.append(f'<font name="DJV">{ch}</font>')
        else:
            out.append(ch)
    return "".join(out)


class Paragraph(_RLParagraph):
    def __init__(self, text, style=None, *args, **kw):
        super().__init__(sym(text), style, *args, **kw)

# ---------------------------------------------------------------- colours
NAVY = colors.HexColor("#14365d")
BLUE = colors.HexColor("#1f5fa8")
SKY = colors.HexColor("#e8f1fb")
RED = colors.HexColor("#b3261e")
ROSE = colors.HexColor("#fdecea")
GREEN = colors.HexColor("#1e7b45")
MINT = colors.HexColor("#e7f6ec")
AMBER = colors.HexColor("#a35c00")
CREAM = colors.HexColor("#fff6e0")
PURPLE = colors.HexColor("#5b3a99")
LILAC = colors.HexColor("#f1ecfa")
GREY = colors.HexColor("#5f6b7a")
LINE = colors.HexColor("#c9d3df")
ZEBRA = colors.HexColor("#f5f8fc")

PAGE_W, PAGE_H = A4
MARGIN_X = 1.7 * cm
CONTENT_W = PAGE_W - 2 * MARGIN_X

# ---------------------------------------------------------------- styles
BASE = 10.2
S = {
    "body": ParagraphStyle(
        "body", fontName="BVP", fontSize=BASE, leading=BASE * 1.45,
        alignment=TA_JUSTIFY, spaceAfter=3,
    ),
    "small": ParagraphStyle(
        "small", fontName="BVP", fontSize=8.6, leading=11.5, alignment=TA_LEFT,
    ),
    "cell": ParagraphStyle(
        "cell", fontName="BVP", fontSize=9.2, leading=12.6, alignment=TA_LEFT,
    ),
    "cellc": ParagraphStyle(
        "cellc", fontName="BVP", fontSize=9.2, leading=12.6, alignment=TA_CENTER,
    ),
    "cellh": ParagraphStyle(
        "cellh", fontName="BVP-H", fontSize=9.2, leading=12.4,
        alignment=TA_CENTER, textColor=colors.white,
    ),
    "bullet": ParagraphStyle(
        "bullet", fontName="BVP", fontSize=BASE, leading=BASE * 1.42,
        leftIndent=13, bulletIndent=2, alignment=TA_JUSTIFY, spaceAfter=1.5,
    ),
    "bullet2": ParagraphStyle(
        "bullet2", fontName="BVP", fontSize=BASE - 0.4, leading=(BASE - 0.4) * 1.42,
        leftIndent=27, bulletIndent=15, alignment=TA_JUSTIFY, spaceAfter=1,
    ),
    "h1": ParagraphStyle(
        "h1", fontName="BVP-X", fontSize=14.5, leading=19, textColor=colors.white,
    ),
    "h2": ParagraphStyle(
        "h2", fontName="BVP-H", fontSize=12.6, leading=16.5, textColor=NAVY,
        spaceBefore=8, spaceAfter=3,
    ),
    "h3": ParagraphStyle(
        "h3", fontName="BVP-H", fontSize=10.8, leading=14.5, textColor=BLUE,
        spaceBefore=6, spaceAfter=2,
    ),
    "boxtitle": ParagraphStyle(
        "boxtitle", fontName="BVP-H", fontSize=10.2, leading=13.5,
    ),
    "q": ParagraphStyle(
        "q", fontName="BVP", fontSize=BASE, leading=BASE * 1.42,
        alignment=TA_JUSTIFY, spaceAfter=1,
    ),
    "opt": ParagraphStyle(
        "opt", fontName="BVP", fontSize=BASE - 0.2, leading=(BASE - 0.2) * 1.38,
        leftIndent=0,
    ),
    "ans": ParagraphStyle(
        "ans", fontName="BVP", fontSize=9.5, leading=13.4, alignment=TA_JUSTIFY,
        spaceAfter=2.5,
    ),
}


# ---------------------------------------------------------------- helpers
def P(text, style="body", **kw):
    st = S[style]
    if kw:
        st = ParagraphStyle(style + "x", parent=st, **kw)
    return Paragraph(text, st)


def bullets(items, style="bullet", sym="•", color="#1f5fa8"):
    """items: list of str or (str, [sub-items])."""
    out = []
    for it in items:
        if isinstance(it, tuple):
            head, subs = it
            out.append(Paragraph(head, S[style], bulletText=sym))
            for s in subs:
                out.append(Paragraph(s, S["bullet2"], bulletText="–"))
        else:
            out.append(Paragraph(it, S[style], bulletText=sym))
    return out


def numbered(items):
    out = []
    for i, it in enumerate(items, 1):
        out.append(Paragraph(it, S["bullet"], bulletText=f"{i}."))
    return out


def H1(text, color=NAVY, sub=None):
    content = [Paragraph(text, S["h1"])]
    if sub:
        content.append(
            Paragraph(sub, ParagraphStyle("h1s", parent=S["small"], textColor=colors.white,
                                          fontSize=9.2, leading=12))
        )
    t = Table([[content]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [5, 5, 5, 5]),
    ]))
    return [CondPageBreak(5 * cm), t, Spacer(1, 6)]


def H2(text):
    return [CondPageBreak(3.2 * cm), Paragraph(text, S["h2"]),
            HRule(NAVY, 1.1), Spacer(1, 3)]


def H3(text):
    return [CondPageBreak(2.4 * cm), Paragraph(text, S["h3"])]


class HRule(Table):
    def __init__(self, color=LINE, thickness=0.6, width=None):
        super().__init__([[""]], colWidths=[width or CONTENT_W], rowHeights=[2])
        self.setStyle(TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), thickness, color),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))


def box(title, flowables, color=BLUE, bg=SKY, icon="", keep=True):
    """Hộp ghi nhớ có viền trái đậm."""
    inner = []
    if title:
        inner.append(Paragraph(
            f"{icon + ' ' if icon else ''}{title}",
            ParagraphStyle("bt", parent=S["boxtitle"], textColor=color),
        ))
        inner.append(Spacer(1, 2))
    if isinstance(flowables, str):
        flowables = [P(flowables)]
    inner.extend(flowables)
    t = Table([[inner]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, color),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [t, Spacer(1, 6)] if not keep else [KeepTogether([t]), Spacer(1, 6)]


def table(rows, widths, header=True, head_bg=NAVY, zebra=True, center_cols=(),
          font_size=None, valign="MIDDLE", bold_first_col=False):
    """rows: list of lists of str (header row first if header=True)."""
    data = []
    for r_i, row in enumerate(rows):
        cells = []
        for c_i, cell in enumerate(row):
            if not isinstance(cell, str):
                cells.append(cell)
                continue
            if header and r_i == 0:
                st = S["cellh"]
            elif c_i in center_cols:
                st = S["cellc"]
            else:
                st = S["cell"]
            if font_size:
                st = ParagraphStyle("tmp", parent=st, fontSize=font_size,
                                    leading=font_size * 1.36)
            if bold_first_col and c_i == 0 and not (header and r_i == 0):
                cell = f"<b>{cell}</b>"
            cells.append(Paragraph(cell, st))
        data.append(cells)
    total = sum(widths)
    widths = [w * CONTENT_W / total for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), head_bg))
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                style.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    return [t, Spacer(1, 7)]


def tag(text, color="#5f6b7a"):
    return f'<font name="BVP-I" size="8" color="{color}">[{text}]</font>'


LETTERS = "ABCD"


def arrange(options, key):
    """options[0] là đáp án đúng; chèn nó vào vị trí `key` (A–D)."""
    correct, *wrong = options
    idx = LETTERS.index(key)
    arranged = wrong[:]
    arranged.insert(idx, correct)
    return arranged


def mcq(num, stem, options, key, level=None):
    """Câu trắc nghiệm nhiều lựa chọn; options[0] là đáp án đúng."""
    opts = arrange(options, key)
    head = f'<font name="BVP-H" color="#14365d">Câu {num}.</font> {stem}'
    if level:
        head += " " + tag(level)
    parts = [Paragraph(head, S["q"])]
    longest = max(len(o) for o in opts)
    if longest <= 26:
        cols, w = 4, CONTENT_W / 4
    elif longest <= 82:
        cols, w = 2, CONTENT_W / 2
    else:
        cols, w = 1, CONTENT_W
    cells = [Paragraph(f'<font name="BVP-B" color="#1f5fa8">{LETTERS[i]}.</font> {o}', S["opt"])
             for i, o in enumerate(opts)]
    rows = [cells[i:i + cols] for i in range(0, 4, cols)]
    t = Table(rows, colWidths=[w] * cols)
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    parts.append(t)
    parts.append(Spacer(1, 5))
    return [KeepTogether(parts)], opts


def tf_question(num, intro, source, statements, level_tags=None):
    """Câu Đúng/Sai: statements = list of (text, bool)."""
    head = f'<font name="BVP-H" color="#14365d">Câu {num}.</font> {intro}'
    parts = [Paragraph(head, S["q"]), Spacer(1, 2)]
    src = Table([[Paragraph(source, ParagraphStyle(
        "src", parent=S["body"], fontName="BVP-I", fontSize=9.6, leading=13.6))]],
        colWidths=[CONTENT_W - 16])
    src.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#e2c27a")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    wrap = Table([[src]], colWidths=[CONTENT_W])
    wrap.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 8),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
    parts.append(wrap)
    parts.append(Spacer(1, 3))
    rows = []
    for i, (txt, _ok) in enumerate(statements):
        lv = (" " + tag(level_tags[i])) if level_tags else ""
        rows.append([
            Paragraph(f'<font name="BVP-B" color="#1f5fa8">{"abcd"[i]})</font> {txt}{lv}', S["opt"]),
            Paragraph("Đ ☐&nbsp;&nbsp;S ☐", S["cellc"]),
        ])
    t = Table(rows, colWidths=[CONTENT_W - 2.4 * cm, 2.4 * cm])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (0, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, LINE),
    ]))
    parts.append(t)
    parts.append(Spacer(1, 7))
    return [KeepTogether(parts)]


def key_grid(keys, start=1, per_row=10):
    """Bảng đáp án nhanh."""
    rows = []
    for i in range(0, len(keys), per_row):
        chunk = keys[i:i + per_row]
        rows.append([f"<b>{start + i + j}</b>" for j in range(len(chunk))])
        rows.append([f'<font name="BVP-H" color="#b3261e">{k}</font>' for k in chunk])
    data = [[Paragraph(c, S["cellc"]) for c in r] for r in rows]
    t = Table(data, colWidths=[CONTENT_W / per_row] * per_row)
    st = [("GRID", (0, 0), (-1, -1), 0.5, LINE),
          ("TOPPADDING", (0, 0), (-1, -1), 2.5),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for r in range(0, len(rows), 2):
        st.append(("BACKGROUND", (0, r), (-1, r), SKY))
    t.setStyle(TableStyle(st))
    return [t, Spacer(1, 7)]
