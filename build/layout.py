# -*- coding: utf-8 -*-
"""
layout.py — Bộ khung trình bày cho đề cương (ReportLab platypus).
Tác giả: Arena Agent. Giấy phép nội dung: xem OFL.txt của Be Vietnam Pro.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Flowable, KeepTogether,
                                NextPageTemplate, PageBreak, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(os.path.dirname(HERE), "assets", "fonts")

# ---------------------------------------------------------------- palette
NAVY = colors.HexColor("#16325C")
NAVY_D = colors.HexColor("#0E2140")
GOLD = colors.HexColor("#C08B2C")
GOLD_L = colors.HexColor("#F6EEDA")
RED = colors.HexColor("#A63A2E")
RED_L = colors.HexColor("#FBEDEA")
TEAL = colors.HexColor("#0F6B62")
TEAL_L = colors.HexColor("#E8F4F1")
INK = colors.HexColor("#1D2433")
MUTED = colors.HexColor("#5C6675")
GREY_L = colors.HexColor("#F3F5F9")
GREY_M = colors.HexColor("#DDE2EA")
WHITE = colors.white

# ---------------------------------------------------------------- fonts
def register_fonts():
    files = {
        "BVP": "BeVietnamPro-Regular.ttf",
        "BVPM": "BeVietnamPro-Medium.ttf",
        "BVPSB": "BeVietnamPro-SemiBold.ttf",
        "BVPB": "BeVietnamPro-Bold.ttf",
        "BVPXB": "BeVietnamPro-ExtraBold.ttf",
        "BVPI": "BeVietnamPro-Italic.ttf",
        "DJ": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "DJF": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    }
    for name, fn in files.items():
        path = fn if fn.startswith("/") else os.path.join(FONT_DIR, fn)
        pdfmetrics.registerFont(TTFont(name, path))
    pdfmetrics.registerFontFamily("BVP", normal="BVP", bold="BVPB",
                                  italic="BVPI", boldItalic="BVPB")

register_fonts()

# ký hiệu không có trong Be Vietnam Pro -> lấy từ DejaVu
def sym(ch):
    return '<font name="DJ">%s</font>' % ch

CHECK = sym("\u2713")      # ✓
CROSS = sym("\u2717")      # ✗
ARROW = sym("\u2192")      # →
DOT = sym("\u25CF")        # ●
TRI = sym("\u25B2")        # ▲
STAR = sym("\u2605")       # ★
WARN = sym("\u26A0")       # ⚠

# ---------------------------------------------------------------- styles
S = {}
S["body"] = ParagraphStyle("body", fontName="BVP", fontSize=9.7, leading=15.4,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=4.5)
S["body_l"] = ParagraphStyle("body_l", parent=S["body"], alignment=TA_LEFT)
S["small"] = ParagraphStyle("small", parent=S["body"], fontSize=8.7, leading=13.2)
S["small_l"] = ParagraphStyle("small_l", parent=S["small"], alignment=TA_LEFT)
S["tiny"] = ParagraphStyle("tiny", parent=S["small"], fontSize=7.8, leading=11.4)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=13, bulletIndent=3,
                             spaceAfter=3.0, alignment=TA_LEFT)
S["bullet_s"] = ParagraphStyle("bullet_s", parent=S["small"], leftIndent=12,
                               bulletIndent=2.5, spaceAfter=2.4, alignment=TA_LEFT)
S["num"] = ParagraphStyle("num", parent=S["body"], leftIndent=16, bulletIndent=0,
                          spaceAfter=3.0, alignment=TA_LEFT)
S["h2"] = ParagraphStyle("h2", fontName="BVPSB", fontSize=13.2, leading=17.5,
                         textColor=NAVY, spaceBefore=11, spaceAfter=5, alignment=TA_LEFT,
                         keepWithNext=1)
S["h3"] = ParagraphStyle("h3", fontName="BVPB", fontSize=10.4, leading=14.6,
                         textColor=TEAL, spaceBefore=7, spaceAfter=3, alignment=TA_LEFT,
                         keepWithNext=1)
S["h4"] = ParagraphStyle("h4", fontName="BVPSB", fontSize=9.6, leading=13.5,
                         textColor=NAVY, spaceBefore=5, spaceAfter=2, alignment=TA_LEFT,
                         keepWithNext=1)
S["quote"] = ParagraphStyle("quote", fontName="BVPI", fontSize=9.2, leading=14,
                            textColor=MUTED, leftIndent=10, rightIndent=8,
                            spaceBefore=3, spaceAfter=5, alignment=TA_JUSTIFY)
S["center"] = ParagraphStyle("center", parent=S["body"], alignment=TA_CENTER)
S["tbl"] = ParagraphStyle("tbl", fontName="BVP", fontSize=8.6, leading=12.6,
                          textColor=INK, alignment=TA_LEFT)
S["tbl_c"] = ParagraphStyle("tbl_c", parent=S["tbl"], alignment=TA_CENTER)
S["tbl_h"] = ParagraphStyle("tbl_h", fontName="BVPSB", fontSize=8.6, leading=12.4,
                            textColor=WHITE, alignment=TA_LEFT)
S["tbl_hc"] = ParagraphStyle("tbl_hc", parent=S["tbl_h"], alignment=TA_CENTER)
S["card_t"] = ParagraphStyle("card_t", fontName="BVPB", fontSize=8.9, leading=12.4,
                             spaceAfter=2.5, alignment=TA_LEFT)
S["opt"] = ParagraphStyle("opt", fontName="BVP", fontSize=9.3, leading=13.2,
                          textColor=INK, alignment=TA_LEFT, spaceAfter=0.8)
S["toc0"] = ParagraphStyle("toc0", fontName="BVPSB", fontSize=10.2, leading=20,
                           textColor=NAVY, spaceBefore=6)
S["toc1"] = ParagraphStyle("toc1", fontName="BVP", fontSize=9.2, leading=16,
                           textColor=INK, leftIndent=16)

CW = A4[0] - 36 * mm   # bề rộng vùng nội dung


# ---------------------------------------------------------------- primitives
class SectionBand(Flowable):
    """Dải tiêu đề phần lớn, có đánh số — đồng thời là mốc mục lục."""
    _seq = 0

    def __init__(self, number, title, kicker="", level=0, key=None):
        Flowable.__init__(self)
        self.number, self.title, self.kicker = number, title, kicker
        self.level = level
        self.key = key or title
        self.height = 21 * mm if kicker else 16 * mm
        self.text = ("%s. %s" % (number, title)) if number else title
        self.bkey = None
        self.width = CW

    def wrap(self, aw, ah):
        self.width = aw
        return (aw, self.height)

    def draw(self):
        c = self.canv
        h = self.height
        c.setFillColor(NAVY)
        c.rect(0, 0, self.width, h, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(0, 0, 3.2, h, stroke=0, fill=1)
        # số thứ tự
        if self.number:
            c.setFillColor(GOLD)
            c.circle(15.5 * mm, h / 2, 6.4 * mm, stroke=0, fill=1)
            c.setFillColor(NAVY_D)
            c.setFont("BVPXB", 13)
            c.drawCentredString(15.5 * mm, h / 2 - 4.6, str(self.number))
            x = 26 * mm
        else:
            x = 7 * mm
        avail = self.width - x - 4 * mm
        if self.kicker:
            c.setFillColor(colors.HexColor("#9DB4D4"))
            ks = 7.6
            while ks > 5.6 and c.stringWidth(self.kicker.upper(), "BVPM", ks) > avail:
                ks -= 0.3
            c.setFont("BVPM", ks)
            c.drawString(x, h - 6.2 * mm, self.kicker.upper())
            c.setFillColor(WHITE)
            fs = 15.6
            while fs > 9.6 and c.stringWidth(self.title, "BVPXB", fs) > avail:
                fs -= 0.4
            c.setFont("BVPXB", fs)
            if c.stringWidth(self.title, "BVPXB", fs) > avail:
                # xuống dòng theo từ
                words, line1, line2 = self.title.split(" "), "", ""
                for w in words:
                    cand = (line1 + " " + w).strip()
                    if c.stringWidth(cand, "BVPXB", fs) <= avail:
                        line1 = cand
                    else:
                        line2 = (line2 + " " + w).strip()
                c.drawString(x, h - 12.4 * mm, line1)
                fs2 = fs
                while fs2 > 8.6 and c.stringWidth(line2, "BVPXB", fs2) > avail:
                    fs2 -= 0.3
                c.setFont("BVPXB", fs2)
                c.drawString(x, h - 17.2 * mm, line2)
            else:
                c.drawString(x, h - 14.2 * mm, self.title)
        else:
            c.setFillColor(WHITE)
            fs = 14.6
            while fs > 9.6 and c.stringWidth(self.title, "BVPXB", fs) > avail:
                fs -= 0.4
            c.setFont("BVPXB", fs)
            c.drawString(x, h / 2 - 5.2, self.title)
        # bookmark + outline để mục lục liên kết được
        SectionBand._seq += 1
        self.bkey = "sec%04d" % SectionBand._seq
        try:
            c.bookmarkPage(self.bkey)
            c.addOutlineEntry(self.text[:70], self.bkey, level=min(self.level, 2), closed=False)
        except Exception:
            self.bkey = None


def band(number, title, kicker="", level=0, page_break=True, space_before=0):
    out = []
    if page_break:
        out.append(PageBreak())
    if space_before:
        out.append(Spacer(1, space_before))
    out.append(SectionBand(number, title, kicker, level))
    out.append(Spacer(1, 5))
    return out


def h1(title, kicker=""):
    """Tiêu đề cấp 1 trong nội dung (không phải dải phần)."""
    return SectionBand("", title, kicker, level=1)


def h2(text, color=None, rule=True):
    """Tiêu đề mục: chữ đậm màu navy + gạch chân mảnh."""
    style = ParagraphStyle("h2x", parent=S["h2"], textColor=color or NAVY)
    p = Paragraph(text, style)
    if not rule:
        return p
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW", (0, 0), (-1, -1), 0.7, GREY_M),
    ]))
    t._is_heading = True
    return t


def h3(text):
    return Paragraph(text, S["h3"])


def h4(text):
    return Paragraph(text, S["h4"])


def p(text, style="body"):
    st = S[style] if isinstance(style, str) else style
    return Paragraph(text, st)


def bullets(items, style="bullet", mark=None):
    out = []
    for it in items:
        m = mark if mark is not None else "•"
        out.append(Paragraph(it, S[style], bulletText=m))
    return out


def numbered(items, start=1):
    return [Paragraph(it, S["num"], bulletText="%d." % (start + i))
            for i, it in enumerate(items)]


def quote(text):
    t = Table([[Paragraph(text, S["quote"])]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREY_L),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


CARD_KINDS = {
    "meo": ("MẸO NHỚ", GOLD, GOLD_L, colors.HexColor("#7A5310")),
    "bay": ("BẪY ĐỀ", RED, RED_L, RED),
    "vd": ("VÍ DỤ", TEAL, TEAL_L, TEAL),
    "chot": ("CHỐT KIẾN THỨC", NAVY, colors.HexColor("#EDF1F8"), NAVY),
    "thi": ("MẸO LÀM BÀI THI", GOLD, GOLD_L, colors.HexColor("#7A5310")),
    "mau": ("BÀI LÀM THAM KHẢO", NAVY, colors.HexColor("#F7F9FC"), NAVY),
}


def card(kind, body, title=None, keep=True):
    label, accent, bg, tcol = CARD_KINDS[kind]
    head = title if title else label
    inner = [Paragraph(
        '<font name="BVPSB" color="%s">%s</font>' % (accent.hexval().replace("0x", "#"), head.upper()),
        ParagraphStyle("ct", fontName="BVPSB", fontSize=8.2, leading=11.6, spaceAfter=3.5))]
    if isinstance(body, str):
        body = [Paragraph(body, S["small"])]
    inner += body
    t = Table([[inner]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 8.5),
    ]))
    out = [Spacer(1, 3), t, Spacer(1, 6)]
    return KeepTogether(out) if keep else out


def data_table(rows, widths, header=True, zebra=True, align_center=None,
               font_h=None, valign="TOP", bg=WHITE, box=True):
    """rows: list of list (str hoặc list-flowable)."""
    align_center = align_center or []
    hs = font_h or S["tbl_h"]
    conv = []
    for r, row in enumerate(rows):
        line = []
        for c, cell in enumerate(row):
            if isinstance(cell, str):
                if r == 0 and header:
                    st = S["tbl_hc"] if c in align_center else hs
                else:
                    st = S["tbl_c"] if c in align_center else S["tbl"]
                line.append(Paragraph(cell, st))
            elif isinstance(cell, list):
                line.append(cell)
            else:
                line.append(cell)
        conv.append(line)
    t = Table(conv, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 6.5), ("RIGHTPADDING", (0, 0), (-1, -1), 6.5),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
        ("BACKGROUND", (0, 0), (-1, -1), bg),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    if zebra:
        for r in range(1 if header else 0, len(conv)):
            if (r % 2 == 0):
                style.append(("BACKGROUND", (0, r), (-1, r), GREY_L))
    if box:
        style.append(("BOX", (0, 0), (-1, -1), 0.6, GREY_M))
        style.append(("LINEBELOW", (0, 0), (-1, -1), 0.4, GREY_M))
    t.setStyle(TableStyle(style))
    return t


def keep_headings(story, min_space=44, probe=170):
    """Giữ tiêu đề mục không bị lẻ cuối trang.

    - Mỗi tiêu đề được chèn trước một CondPageBreak nhỏ (đề phòng).
    - Nếu tiêu đề + phần thân kế tiếp vừa một "khối" hợp lí, gói chúng vào
      KeepTogether để tránh trường hợp tiêu đề + 2 dòng nằm cuối trang.
    """
    out, i = [], 0
    n = len(story)
    while i < n:
        f = story[i]
        if getattr(f, "_is_heading", False):
            out.append(CondPageBreak(min_space * mm))
            if i + 1 < n:
                nxt = story[i + 1]
                if not isinstance(nxt, (SectionBand, PageBreak)):
                    try:
                        h = f.wrap(CW, 700)[1] + nxt.wrap(CW, 700)[1]
                    except Exception:
                        h = 10 ** 6
                    if h <= probe * mm:
                        out.append(KeepTogether([f, nxt]))
                        i += 2
                        continue
            out.append(f)
            i += 1
            continue
        out.append(f)
        i += 1
    return out


# ---------------------------------------------------------------- mục lục
class MyDoc(BaseDocTemplate):
    def __init__(self, filename, chapter_source=None, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        self.cur_chapter = ""
        self.chapter_source = chapter_source or (lambda: "")

    def afterFlowable(self, flowable):
        if isinstance(flowable, SectionBand):
            if flowable.level == 0:
                self.cur_chapter = flowable.text
            if getattr(flowable, "bkey", None):
                self.notify("TOCEntry", (flowable.level, flowable.text, self.page, flowable.bkey))
            else:
                self.notify("TOCEntry", (flowable.level, flowable.text, self.page))


def build_toc():
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"]]
    toc.dotsMinLevel = 0
    return toc
