# -*- coding: utf-8 -*-
"""Bảng màu, phông chữ và kiểu đoạn cho đề cương PDF."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"

# ---------------------------------------------------------------- kích thước
PAGE_W, PAGE_H = 210 * mm, 297 * mm
MARGIN_L = MARGIN_R = 17 * mm
MARGIN_T = 22 * mm
MARGIN_B = 18 * mm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R  # 176 mm

# -------------------------------------------------------------------- màu sắc
INK = colors.HexColor("#1B2430")
MUTED = colors.HexColor("#5C6673")
PRIMARY = colors.HexColor("#22405C")
PRIMARY_DK = colors.HexColor("#16293B")
PRIMARY_LT = colors.HexColor("#E9EFF6")
GOLD = colors.HexColor("#A8792B")
GOLD_LT = colors.HexColor("#FBF3E2")
GREEN = colors.HexColor("#2F6B4F")
GREEN_LT = colors.HexColor("#ECF4EF")
RED = colors.HexColor("#9B3B2F")
RED_LT = colors.HexColor("#FBEDEA")
CREAM = colors.HexColor("#FCFAF4")
PAPER = colors.HexColor("#F7F4EC")
RULE = colors.HexColor("#D9D2C3")
RULE_LT = colors.HexColor("#E9E3D6")
WHITE = colors.white


def register_fonts() -> None:
    """Đăng ký bộ phông DejaVu (đủ dấu tiếng Việt) cho ReportLab."""
    faces = {
        "Body": "DejaVuSerif.ttf",
        "Body-Bold": "DejaVuSerif-Bold.ttf",
        "Body-Italic": "DejaVuSerif-Italic.ttf",
        "Body-BoldItalic": "DejaVuSerif-BoldItalic.ttf",
        "Sans": "DejaVuSans.ttf",
        "Sans-Bold": "DejaVuSans-Bold.ttf",
    }
    for name, filename in faces.items():
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
    pdfmetrics.registerFontFamily(
        "Body",
        normal="Body",
        bold="Body-Bold",
        italic="Body-Italic",
        boldItalic="Body-BoldItalic",
    )
    pdfmetrics.registerFontFamily(
        "Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold"
    )


# ------------------------------------------------------------------- kiểu chữ
STYLES = {}


def _s(name, **kwargs):
    parent = kwargs.pop("parent", None)
    STYLES[name] = ParagraphStyle(name, parent=parent, **kwargs)
    return STYLES[name]


_s(
    "body",
    fontName="Body",
    fontSize=9.7,
    leading=14.4,
    textColor=INK,
    alignment=TA_JUSTIFY,
    spaceAfter=3.2,
)
_s("body_c", parent=STYLES["body"], alignment=TA_CENTER)
_s("lead", parent=STYLES["body"], fontSize=10.4, leading=15.4, textColor=PRIMARY_DK, spaceAfter=5)
_s("H2Numbered", fontName="Sans-Bold", fontSize=11.6, leading=15, textColor=PRIMARY,
   spaceBefore=11, spaceAfter=5, backColor=PRIMARY_LT, borderPadding=4,
   leftIndent=0, keepWithNext=1)
STYLES["h2"] = STYLES["H2Numbered"]

_s("PartKicker", fontName="Sans-Bold", fontSize=7.6, leading=10,
   textColor=colors.HexColor("#D9BE84"), alignment=TA_LEFT)
_s("PartHeading", fontName="Sans-Bold", fontSize=14.2, leading=21,
   textColor=WHITE, alignment=TA_LEFT, backColor=PRIMARY, borderPadding=6.5,
   spaceBefore=4, spaceAfter=4)
_s("h3", fontName="Sans-Bold", fontSize=10.2, leading=14, textColor=PRIMARY_DK,
   spaceBefore=8, spaceAfter=3.5, keepWithNext=1)
_s("h4", fontName="Sans-Bold", fontSize=9.4, leading=13, textColor=GOLD,
   spaceBefore=6, spaceAfter=2.5, keepWithNext=1)
_s("bullet", parent=STYLES["body"], leftIndent=13, bulletIndent=3.5, spaceAfter=2.4)
_s("bullet2", parent=STYLES["body"], leftIndent=25, bulletIndent=15, spaceAfter=2.0, fontSize=9.4)
_s("num", parent=STYLES["body"], leftIndent=15, bulletIndent=3.5, spaceAfter=2.6)
_s("small", fontName="Body", fontSize=8.3, leading=11.6, textColor=MUTED, alignment=TA_LEFT)
_s("note", parent=STYLES["small"], fontName="Body-Italic", spaceAfter=4)
_s("caption", fontName="Sans", fontSize=8, leading=10.5, textColor=MUTED, alignment=TA_LEFT,
   spaceBefore=2, spaceAfter=6)

# Ô trong bảng
_s("cell", fontName="Body", fontSize=8.5, leading=11.6, textColor=INK, alignment=TA_LEFT)
_s("cell_c", parent=STYLES["cell"], alignment=TA_CENTER)
_s("cell_b", parent=STYLES["cell"], fontName="Body-Bold")
_s("cell_head", fontName="Sans-Bold", fontSize=8.4, leading=11,
   textColor=WHITE, alignment=TA_LEFT)
_s("cell_head_c", parent=STYLES["cell_head"], alignment=TA_CENTER)

# Hộp gọi chú ý
_s("box_title", fontName="Sans-Bold", fontSize=8.8, leading=11.6, spaceAfter=2.4)
_s("box_body", parent=STYLES["body"], fontSize=9.2, leading=13.4, spaceAfter=2)
_s("box_bullet", parent=STYLES["box_body"], leftIndent=11, bulletIndent=2, spaceAfter=1.8)

# Trang bìa
_s("cover_kicker", fontName="Sans-Bold", fontSize=9.2, leading=12, textColor=GOLD_LT,
   alignment=TA_CENTER)
_s("cover_title", fontName="Sans-Bold", fontSize=30, leading=36, textColor=WHITE,
   alignment=TA_CENTER)
_s("cover_title2", fontName="Sans-Bold", fontSize=40, leading=46, textColor=colors.HexColor("#E7C072"),
   alignment=TA_CENTER)
_s("cover_sub", fontName="Body-Italic", fontSize=12.5, leading=18, textColor=colors.HexColor("#E8EEF5"),
   alignment=TA_CENTER)
_s("cover_meta", fontName="Body", fontSize=9.4, leading=14, textColor=INK, alignment=TA_LEFT)
_s("cover_meta_b", fontName="Sans-Bold", fontSize=8.6, leading=13, textColor=PRIMARY, alignment=TA_LEFT)

# Đề kiểm tra
_s("q", fontName="Body", fontSize=9.6, leading=14, textColor=INK, alignment=TA_JUSTIFY,
   spaceBefore=5, spaceAfter=1.5, keepWithNext=1)
_s("opt", fontName="Body", fontSize=9.4, leading=13.2, textColor=INK, alignment=TA_LEFT,
   leftIndent=17, firstLineIndent=-9, spaceAfter=0.8)
_s("ans_title", fontName="Sans-Bold", fontSize=9.6, leading=13, textColor=PRIMARY_DK,
   spaceBefore=6, spaceAfter=2, keepWithNext=1)
_s("ans", fontName="Body", fontSize=9.1, leading=12.8, textColor=INK, alignment=TA_JUSTIFY,
   leftIndent=15, firstLineIndent=-15, spaceAfter=3.4)

_s("qgroup", fontName="Sans-Bold", fontSize=9.8, leading=13.2, textColor=WHITE,
   backColor=PRIMARY_DK, borderPadding=3.4, spaceBefore=12, spaceAfter=7, keepWithNext=1)

# Mục lục
_s("toc_title", fontName="Sans-Bold", fontSize=22, leading=26, textColor=PRIMARY,
   alignment=TA_LEFT, spaceBefore=0, spaceAfter=4)

_s("toc0", fontName="Sans-Bold", fontSize=10, leading=18, textColor=PRIMARY,
   spaceBefore=6, leftIndent=0, firstLineIndent=0)
_s("toc1", fontName="Body", fontSize=9.4, leading=15.2, textColor=INK,
   leftIndent=14, firstLineIndent=0)
_s("toc2", fontName="Body", fontSize=8.8, leading=13, textColor=MUTED,
   leftIndent=28, firstLineIndent=0)
