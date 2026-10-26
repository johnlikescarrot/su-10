# -*- coding: utf-8 -*-
"""Khung trình bày (style + page template + component) cho đề cương PDF."""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph as _Paragraph,
                                Spacer, Table, TableStyle, KeepTogether,
                                PageBreak, NextPageTemplate, Flowable)
from reportlab.platypus.tableofcontents import TableOfContents

# --------------------------------------------------------------------------
# Font
# --------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
F = {
    "serif": os.path.join(FONT_DIR, "DejaVuSerif.ttf"),
    "serif-b": os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf"),
    "sans": os.path.join(FONT_DIR, "DejaVuSans.ttf"),
    "sans-b": os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"),
    "mono": os.path.join(FONT_DIR, "DejaVuSansMono.ttf"),
}
REGISTERED = False


def register_fonts():
    global REGISTERED
    if REGISTERED:
        return
    pdfmetrics.registerFont(TTFont("Body", F["serif"]))
    pdfmetrics.registerFont(TTFont("Body-B", F["serif-b"]))
    pdfmetrics.registerFont(TTFont("Head", F["sans"]))
    pdfmetrics.registerFont(TTFont("Head-B", F["sans-b"]))
    pdfmetrics.registerFont(TTFont("Mono", F["mono"]))
    # Không có file italic -> ánh xạ về chính font thường để <i> không lỗi.
    addMapping("Body", 0, 0, "Body")
    addMapping("Body", 1, 0, "Body-B")
    addMapping("Body", 0, 1, "Body")
    addMapping("Body", 1, 1, "Body-B")
    addMapping("Head", 0, 0, "Head")
    addMapping("Head", 1, 0, "Head-B")
    addMapping("Head", 0, 1, "Head")
    addMapping("Head", 1, 1, "Head-B")
    REGISTERED = True


# --------------------------------------------------------------------------
# Bảng màu
# --------------------------------------------------------------------------
NAVY = colors.HexColor("#16325C")
BLUE = colors.HexColor("#2B5DA8")
BLUE_SOFT = colors.HexColor("#DCE8F7")
BLUE_PALE = colors.HexColor("#EEF4FC")
GOLD = colors.HexColor("#B07714")
GOLD_SOFT = colors.HexColor("#FDF3DE")
GOLD_LINE = colors.HexColor("#E0B45C")
RED = colors.HexColor("#A61B1B")
RED_SOFT = colors.HexColor("#FCEDEC")
GREEN = colors.HexColor("#186B47")
GREEN_SOFT = colors.HexColor("#E9F6EF")
PURPLE = colors.HexColor("#5B3A8E")
PURPLE_SOFT = colors.HexColor("#F1ECFA")
GRAY = colors.HexColor("#4A4A4A")
GRAY_LIGHT = colors.HexColor("#F4F5F7")
BORDER = colors.HexColor("#C4D3E8")
WHITE = colors.white

# --------------------------------------------------------------------------
# Bảo vệ hiển thị: một số ký hiệu không có trong DejaVu Serif -> chuyển sang Sans
# --------------------------------------------------------------------------
SERIF_MISSING = "☐✓✔✗★☆☞⚠✎"


def fix(text):
    """Chuyển các ký hiệu thiếu glyph sang font Sans để không bị ô vuông trống."""
    if not isinstance(text, str):
        return text
    for ch in SERIF_MISSING:
        if ch in text:
            text = text.replace(ch, '<font name="Head">%s</font>' % ch)
    return text


class _P(_Paragraph):
    """Paragraph tự động vá glyph."""

    def __init__(self, text, style=None, **kw):
        _Paragraph.__init__(self, fix(text), style, **kw)


Paragraph = _P

PAGE_W, PAGE_H = A4
M_LEFT, M_RIGHT, M_TOP, M_BOTTOM = 48, 42, 62, 52
CONTENT_W = PAGE_W - M_LEFT - M_RIGHT

# --------------------------------------------------------------------------
# Paragraph styles
# --------------------------------------------------------------------------
S = {}


def _mk():
    S["toctitle"] = ParagraphStyle("toctitle", fontName="Head-B", fontSize=17, leading=21,
                                   textColor=NAVY, alignment=TA_LEFT)
    S["body"] = ParagraphStyle(
        "body", fontName="Body", fontSize=9.5, leading=14.2,
        alignment=TA_JUSTIFY, textColor=colors.HexColor("#1A1A1A"),
        spaceBefore=1.5, spaceAfter=3.5)
    S["bodyc"] = ParagraphStyle("bodyc", parent=S["body"], alignment=TA_CENTER)
    S["small"] = ParagraphStyle("small", parent=S["body"], fontSize=8.2, leading=11.6,
                                textColor=GRAY)
    S["cell"] = ParagraphStyle("cell", fontName="Body", fontSize=8.4, leading=11.6,
                               textColor=colors.HexColor("#1A1A1A"))
    S["cellc"] = ParagraphStyle("cellc", parent=S["cell"], alignment=TA_CENTER)
    S["cellb"] = ParagraphStyle("cellb", parent=S["cell"], fontName="Body-B")
    S["th"] = ParagraphStyle("th", fontName="Head-B", fontSize=8.6, leading=11.4,
                             textColor=WHITE, alignment=TA_CENTER)
    S["thl"] = ParagraphStyle("thl", parent=S["th"], alignment=TA_LEFT)
    S["h1"] = ParagraphStyle("h1", fontName="Head-B", fontSize=15.5, leading=19,
                             textColor=WHITE)
    S["h2"] = ParagraphStyle("h2", fontName="Head-B", fontSize=11.6, leading=15,
                             textColor=NAVY)
    S["h3"] = ParagraphStyle("h3", fontName="Head-B", fontSize=10.2, leading=13.5,
                             textColor=colors.HexColor("#22303F"))
    S["h3g"] = ParagraphStyle("h3g", fontName="Head-B", fontSize=9.6, leading=13,
                              textColor=GOLD)
    S["bul"] = ParagraphStyle("bul", parent=S["body"], leftIndent=13,
                              bulletIndent=3, spaceAfter=2.2)
    S["bul2"] = ParagraphStyle("bul2", parent=S["body"], leftIndent=27,
                               bulletIndent=16, spaceAfter=2.0)
    S["num"] = ParagraphStyle("num", parent=S["body"], fontSize=9.4, leading=13.8)
    S["boxt"] = ParagraphStyle("boxt", fontName="Head-B", fontSize=9.3, leading=12.4)
    S["boxb"] = ParagraphStyle("boxb", fontName="Body", fontSize=9.1, leading=13.4,
                               alignment=TA_JUSTIFY, textColor=colors.HexColor("#1A1A1A"))
    S["quote"] = ParagraphStyle("quote", fontName="Body", fontSize=9.2, leading=13.6,
                                alignment=TA_JUSTIFY, leftIndent=10, rightIndent=6,
                                textColor=colors.HexColor("#2B2B2B"))
    S["toc1"] = ParagraphStyle("toc1", fontName="Head-B", fontSize=9.8, leading=16,
                               textColor=NAVY)
    S["toc2"] = ParagraphStyle("toc2", fontName="Body", fontSize=9.0, leading=13.4,
                               leftIndent=16, textColor=colors.HexColor("#333333"))
    S["toc3"] = ParagraphStyle("toc3", fontName="Body", fontSize=8.6, leading=12.4,
                               leftIndent=32, textColor=GRAY)


_mk()


def P(text, style="body"):
    return Paragraph(text, S[style])


# --------------------------------------------------------------------------
# Heading có đánh số + mục lục + bookmark
# --------------------------------------------------------------------------
class Anchor(Flowable):
    """Flowable rỗng đặt ngay trước tiêu đề để ghi mục lục + bookmark ở đúng trang."""

    def __init__(self, level, text, key):
        Flowable.__init__(self)
        self.toc_level = level
        self.toc_text = text
        self.toc_key = key

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        pass


# --------------------------------------------------------------------------
# Doc template
# --------------------------------------------------------------------------
class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=M_LEFT, rightMargin=M_RIGHT,
                                 topMargin=M_TOP, bottomMargin=M_BOTTOM,
                                 title="Đề cương ôn tập Giữa học kì 1 – Lịch sử 10 (Kết nối tri thức)",
                                 author="Tài liệu ôn thi Lịch sử 10",
                                 subject="Đề cương ôn tập giữa học kì 1 môn Lịch sử lớp 10 – bộ Kết nối tri thức với cuộc sống",
                                 **kw)
        frame_cover = Frame(0, 0, PAGE_W, PAGE_H, id="cover",
                            leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        frame_body = Frame(M_LEFT, M_BOTTOM, CONTENT_W, PAGE_H - M_TOP - M_BOTTOM,
                           id="body", leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_cover], onPage=self._draw_cover),
            PageTemplate(id="body", frames=[frame_body], onPage=self._draw_body),
        ])

    # -- trang bìa -------------------------------------------------------
    def _draw_cover(self, canv, doc):
        canv.saveState()
        # nền trên
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - 300, PAGE_W, 300, stroke=0, fill=1)
        canv.setFillColor(GOLD_LINE)
        canv.rect(0, PAGE_H - 306, PAGE_W, 6, stroke=0, fill=1)
        # hoa văn nhẹ
        canv.setStrokeColor(colors.Color(1, 1, 1, alpha=0.10))
        canv.setLineWidth(1)
        for i in range(0, int(PAGE_W) + 60, 26):
            canv.line(i, PAGE_H - 300, i + 60, PAGE_H)
        # dòng trên
        canv.setFillColor(GOLD_LINE)
        canv.setFont("Head-B", 11)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 92,
                               "TÀI LIỆU ÔN THI TRỌNG TÂM  •  BÁM SÁT MA TRẬN ĐỀ")
        canv.setFillColor(WHITE)
        canv.setFont("Head-B", 45)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 158, "ĐỀ CƯƠNG")
        canv.setFont("Head-B", 25)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 196, "ÔN TẬP GIỮA HỌC KÌ 1")
        canv.setFillColor(GOLD_LINE)
        canv.setFont("Head-B", 13.5)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 232, "NĂM HỌC 2026 – 2027")

        # khối tên môn
        canv.setFillColor(NAVY)
        canv.setFont("Head-B", 62)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 400, "LỊCH SỬ 10")
        canv.setFillColor(colors.HexColor("#5C6B80"))
        canv.setFont("Head-B", 12)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 432,
                               "BỘ SÁCH: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
        canv.setStrokeColor(GOLD)
        canv.setLineWidth(2)
        canv.line(PAGE_W / 2 - 60, PAGE_H - 447, PAGE_W / 2 + 60, PAGE_H - 447)

        # thẻ thông tin
        x0, x1 = 66, PAGE_W - 66
        y_top = PAGE_H - 480
        h = 150
        canv.setFillColor(BLUE_PALE)
        canv.setStrokeColor(BORDER)
        canv.setLineWidth(1)
        canv.roundRect(x0, y_top - h, x1 - x0, h, 9, stroke=1, fill=1)
        canv.setFillColor(GOLD)
        canv.rect(x0, y_top - h, 5, h, stroke=0, fill=1)

        canv.setFillColor(NAVY)
        canv.setFont("Head-B", 9.6)
        canv.drawString(x0 + 20, y_top - 24, "PHẠM VI ÔN TẬP")
        canv.setFont("Body", 9.2)
        canv.setFillColor(colors.HexColor("#22303F"))
        y = y_top - 43
        for line in [
            "Chủ đề 1. Lịch sử và Sử học  →  Bài 1, Bài 2",
            "Chủ đề 2. Vai trò của Sử học  →  Bài 3",
        ]:
            canv.drawString(x0 + 20, y, line)
            y -= 16
        canv.setFont("Head-B", 9.6)
        canv.setFillColor(NAVY)
        canv.drawString(x0 + 20, y - 6, "HÌNH THỨC KIỂM TRA")
        canv.setFont("Body", 9.2)
        canv.setFillColor(colors.HexColor("#22303F"))
        canv.drawString(x0 + 20, y - 24,
                        "Thời gian 45 phút  •  20 câu TN + 2 câu Đúng/Sai + 1 câu Tự luận")
        canv.drawString(x0 + 20, y - 40,
                        "Thang điểm 10  •  28 lệnh hỏi trắc nghiệm + 01 câu tự luận")

        # dải nội dung
        canv.setFillColor(GRAY_LIGHT)
        canv.roundRect(x0, 150, x1 - x0, 52, 6, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#3D4A5C"))
        canv.setFont("Head-B", 8.2)
        canv.drawCentredString(PAGE_W / 2, 184, "NỘI DUNG TÀI LIỆU")
        canv.setFont("Body", 8.2)
        canv.drawCentredString(PAGE_W / 2, 167,
                               "Kiến thức trọng tâm  •  Sơ đồ tư duy  •  Bảng so sánh  •  Mẹo nhớ")
        canv.drawCentredString(PAGE_W / 2, 152,
                               "64 câu hỏi có đáp án  •  Đề mẫu 23 câu  •  Thang điểm chi tiết  •  Checklist tự kiểm tra")

        # chân trang
        canv.setFillColor(NAVY)
        canv.rect(0, 0, PAGE_W, 42, stroke=0, fill=1)
        canv.setFillColor(colors.Color(1, 1, 1, alpha=0.75))
        canv.setFont("Head", 8)
        canv.drawCentredString(PAGE_W / 2, 17,
                               "Tài liệu học tập dành cho học sinh lớp 10 – Lưu hành nội bộ")
        canv.restoreState()

    # -- trang nội dung --------------------------------------------------
    def _draw_body(self, canv, doc):
        canv.saveState()
        # header
        canv.setStrokeColor(BORDER)
        canv.setLineWidth(0.7)
        canv.line(M_LEFT, PAGE_H - 42, PAGE_W - M_RIGHT, PAGE_H - 42)
        canv.setFillColor(NAVY)
        canv.setFont("Head-B", 7.4)
        canv.drawString(M_LEFT, PAGE_H - 37,
                        "LỊCH SỬ 10  •  KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
        canv.setFillColor(colors.HexColor("#7A879A"))
        canv.setFont("Head", 7.4)
        canv.drawRightString(PAGE_W - M_RIGHT, PAGE_H - 37,
                             "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ 1")
        # footer
        canv.setStrokeColor(BORDER)
        canv.setLineWidth(0.7)
        canv.line(M_LEFT, 38, PAGE_W - M_RIGHT, 38)
        canv.setFillColor(GOLD)
        canv.rect(PAGE_W / 2 - 17, 27, 34, 13, stroke=0, fill=1)
        canv.setFillColor(WHITE)
        canv.setFont("Head-B", 7.6)
        canv.drawCentredString(PAGE_W / 2, 30.4, "%d" % doc.page)
        canv.setFillColor(colors.HexColor("#8A96A8"))
        canv.setFont("Head", 6.8)
        canv.drawString(M_LEFT, 30, "Đề cương Giữa HK1 – Lịch sử 10")
        canv.drawRightString(PAGE_W - M_RIGHT, 30, "Năm học 2026 – 2027")
        canv.restoreState()

    # -- mục lục ---------------------------------------------------------
    def afterFlowable(self, flowable):
        if isinstance(flowable, Anchor):
            lvl = flowable.toc_level
            self.notify("TOCEntry", (lvl, flowable.toc_text, self.page))
            key = "sec_%s" % flowable.toc_key
            try:
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(flowable.toc_text, key,
                                          level=min(lvl, 2), closed=(lvl > 0))
            except Exception:
                pass


# --------------------------------------------------------------------------
# Component
# --------------------------------------------------------------------------
def h1(num, title, key):
    """Tiêu đề cấp 1: thanh màu navy, số thứ tự trong ô vàng."""
    data = [[Paragraph(num, ParagraphStyle("n", fontName="Head-B", fontSize=15,
                                           leading=18, textColor=GOLD,
                                           alignment=TA_CENTER)),
             Paragraph(title, S["h1"])]]
    t = Table(data, colWidths=[46, CONTENT_W - 46], rowHeights=None)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#0E2142")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEAFTER", (0, 0), (0, 0), 1, GOLD),
    ]))
    return [Anchor(0, "%s. %s" % (num, title), key), Spacer(1, 6), t, Spacer(1, 9)]


def h2(title, key):
    p = Paragraph(title, S["h2"])
    t = Table([[p]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_PALE),
        ("LINEBEFORE", (0, 0), (0, 0), 3.2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [Anchor(1, title, key), Spacer(1, 9), t, Spacer(1, 6)]


def h3(title, key=None):
    if key:
        return [Anchor(2, title, key), Spacer(1, 4), Paragraph(title, S["h3"]),
                Spacer(1, 2.5)]
    return [Spacer(1, 4), Paragraph(title, S["h3"]), Spacer(1, 2.5)]


def h4(title):
    return [Spacer(1, 2), Paragraph(title, S["h3g"]), Spacer(1, 1.5)]


def sp(h=4):
    return Spacer(1, h)


def bullets(items, style="bul", sym="▪"):
    out = []
    for it in items:
        out.append(Paragraph(it, S[style], bulletText=sym))
    return out


def dash(items):
    return bullets(items, sym="–")


def numlist(items, start=1):
    out = []
    for i, it in enumerate(items, start):
        out.append(Paragraph(it, S["bul"], bulletText="%d." % i))
    return out


def box(title, flows, kind="note", icon=None):
    """Ô ghi chú màu. flows: list flowable hoặc list string."""
    palette = {
        "note": (BLUE, BLUE_PALE),
        "tip": (GOLD, GOLD_SOFT),
        "warn": (RED, RED_SOFT),
        "ok": (GREEN, GREEN_SOFT),
        "purple": (PURPLE, PURPLE_SOFT),
    }[kind]
    accent, bg = palette
    inner = []
    if title:
        tp = ParagraphStyle("bt", parent=S["boxt"], textColor=accent)
        inner.append(Paragraph(title, tp))
        inner.append(Spacer(1, 2.5))
    for f in flows:
        if isinstance(f, str):
            inner.append(Paragraph(f, S["boxb"]))
        else:
            inner.append(f)
    t = Table([[inner]], colWidths=[CONTENT_W - 8])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, 0), 3.2, accent),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.Color(accent.red, accent.green, accent.blue, 0.25)),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 6)]


def mk_table(data, widths=None, header=True, align_center=None,
             font_size=8.4, zebra=True, header_bg=NAVY,
             first_col_bold=False, valign="MIDDLE"):
    """data: list of rows; ô có thể là str hoặc flowable."""
    if widths is None:
        widths = [CONTENT_W / len(data[0])] * len(data[0])
    total = sum(widths)
    widths = [w * CONTENT_W / total for w in widths]
    rows = []
    for ri, row in enumerate(data):
        r = []
        for ci, cell in enumerate(row):
            if isinstance(cell, (_Paragraph, Table, Flowable)):
                r.append(cell)
            else:
                txt = str(cell)
                if ri == 0 and header:
                    st = "thl" if ci == 0 and not (align_center and align_center[0]) else "th"
                    r.append(Paragraph(txt, S[st]))
                else:
                    stl = "cell"
                    if ci == 0 and first_col_bold:
                        stl = "cellb"
                    if align_center and ci in align_center:
                        stl = "cellc" if stl == "cell" else "cellc"
                    pst = ParagraphStyle("x%d_%d" % (ri, ci), parent=S[stl],
                                         fontSize=font_size, leading=font_size * 1.36)
                    r.append(Paragraph(txt, pst))
        rows.append(r)
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), header_bg),
                 ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD)]
        if zebra:
            for i in range(1, len(rows)):
                if i % 2 == 0:
                    cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F6F9FD")))
    t.setStyle(TableStyle(cmds))
    return t


def tb(data, **kw):
    """Bảng kèm khoảng đệm, dùng trực tiếp trong story."""
    sp_after = kw.pop("sp_after", 7)
    return [Spacer(1, 2), mk_table(data, **kw), Spacer(1, sp_after)]


def caption(text):
    return Paragraph(text, ParagraphStyle("cap", fontName="Head-B", fontSize=8.2,
                                          leading=11, textColor=GOLD,
                                          alignment=TA_LEFT, spaceBefore=2,
                                          spaceAfter=3))


def rule(color=GOLD, w=1.2, space=6):
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[0.1])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), w, color),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [Spacer(1, space), t, Spacer(1, space)]


# --------------------------------------------------------------------------
# Thành phần dạng đề thi
# --------------------------------------------------------------------------
def mcq(num, stem, opts, tag=None):
    """Câu trắc nghiệm: số thứ tự trong ô + đề + 4 phương án dạng lưới 2x2."""
    badge = Paragraph("<b>%s</b>" % num,
                      ParagraphStyle("qb", fontName="Head-B", fontSize=8.6,
                                     leading=11, textColor=WHITE,
                                     alignment=TA_CENTER))
    bcell = Table([[badge]], colWidths=[22], rowHeights=[15])
    bcell.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY),
                               ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 2),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    stem_p = Paragraph(stem, ParagraphStyle("qs", parent=S["body"], fontSize=9.2,
                                            leading=13.4, spaceAfter=2))
    head = Table([[bcell, stem_p]], colWidths=[26, CONTENT_W - 26])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 2),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                              ("TOPPADDING", (0, 0), (-1, -1), 2),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    labels = "ABCD"
    cells = []
    for i, o in enumerate(opts[:4]):
        cells.append(Paragraph("<b>%s.</b> %s" % (labels[i], o),
                               ParagraphStyle("op", parent=S["cell"], fontSize=8.6,
                                              leading=11.4, leftIndent=13,
                                              bulletIndent=0)))
    rows = [[cells[0], cells[1]], [cells[2], cells[3]]]
    ot = Table(rows, colWidths=[(CONTENT_W - 26) / 2] * 2)
    ot.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 4),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 1.2),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2)]))
    wrap = Table([[head], [ot]], colWidths=[CONTENT_W])
    wrap.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                              ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#E3EAF4"))]))
    return wrap


def tf_item(num, context, statements):
    """Câu Đúng/Sai: bối cảnh + 4 ý a-d (chỉ in đề, không in đáp án)."""
    rows = []
    badge = Paragraph("<b>II.%s</b>" % num,
                      ParagraphStyle("tb", fontName="Head-B", fontSize=8.6,
                                     leading=11, textColor=WHITE,
                                     alignment=TA_CENTER))
    bcell = Table([[badge]], colWidths=[34], rowHeights=[15])
    bcell.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD),
                               ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    ctx = Paragraph(context, ParagraphStyle("tc", parent=S["body"], fontSize=9.0,
                                            leading=13.0))
    head = Table([[bcell, ctx]], colWidths=[40, CONTENT_W - 40])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 2),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                              ("TOPPADDING", (0, 0), (-1, -1), 2),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    st_rows = []
    for i, st in enumerate(statements):
        st_rows.append([Paragraph("<b>%s)</b>" % "abcd"[i],
                                  ParagraphStyle("tfl", parent=S["cell"], fontSize=8.7,
                                                 leading=11.6, alignment=TA_CENTER)),
                        Paragraph(st, ParagraphStyle("tfs", parent=S["cell"],
                                                     fontSize=8.7, leading=11.6)),
                        Paragraph("Đ  /  S", ParagraphStyle("tfa", parent=S["cellc"],
                                                            fontSize=8.2, textColor=GRAY))])
    st_t = Table(st_rows, colWidths=[24, CONTENT_W - 114, 52])
    st_t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("BOX", (0, 0), (-1, -1), 0.3, BORDER),
                              ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#DCE4EF")),
                              ("LEFTPADDING", (0, 0), (-1, -1), 4),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                              ("TOPPADDING", (0, 0), (-1, -1), 2.6),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
                              ("BACKGROUND", (2, 0), (2, -1), GRAY_LIGHT)]))
    wrap = Table([[head], [st_t]], colWidths=[CONTENT_W])
    wrap.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 4),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                              ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#E3EAF4"))]))
    return wrap


def answer_grid(pairs, per_row=10):
    """pairs = [(số câu, đáp án), ...] -> bảng đáp án gọn."""
    rows, cur = [], []
    for i, (q, a) in enumerate(pairs):
        cur.append(Paragraph("<b>%s</b>" % q, ParagraphStyle("ag", parent=S["cellc"],
                                                             fontSize=7.4, textColor=GRAY)))
        cur.append(Paragraph("<b>%s</b>" % a, ParagraphStyle("aa", parent=S["cellc"],
                                                             fontSize=9.2, textColor=RED)))
        if len(cur) == per_row * 2:
            rows.append(cur)
            cur = []
    if cur:
        while len(cur) < per_row * 2:
            cur += [Paragraph("", S["cell"]), Paragraph("", S["cell"])]
        rows.append(cur)
    unit = CONTENT_W / per_row
    widths = []
    for _ in range(per_row):
        widths += [unit * 0.5, unit * 0.5]
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.3, BORDER),
                           ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FBFCFE")),
                           ("LEFTPADDING", (0, 0), (-1, -1), 1),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 1),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
                           ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    return t


def essay(num, title, prompt, hints, sample=None):
    """Câu tự luận: đề + gợi ý dàn ý + (tuỳ chọn) bài mẫu."""
    s = []
    hd = Table([[Paragraph("<b>%s</b>" % num, ParagraphStyle("en", fontName="Head-B",
                                                             fontSize=9, leading=12,
                                                             textColor=WHITE,
                                                             alignment=TA_CENTER)),
                 Paragraph("<b>%s</b>" % title, ParagraphStyle("et", fontName="Head-B",
                                                               fontSize=9.4, leading=12.4,
                                                               textColor=NAVY))]],
               colWidths=[30, CONTENT_W - 30])
    hd.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), BLUE),
                            ("BACKGROUND", (1, 0), (1, 0), BLUE_PALE),
                            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 3),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    s += [Spacer(1, 5), hd, Spacer(1, 3)]
    s += [Paragraph("<b>Đề:</b> " + prompt, ParagraphStyle("ep", parent=S["body"],
                                                           fontSize=9.0, leading=13.2))]
    s += [Spacer(1, 2), Paragraph("Gợi ý dàn ý", ParagraphStyle("eh", fontName="Head-B",
                                                                fontSize=8.6,
                                                                textColor=GOLD, leading=11))]
    for it in hints:
        s += [Paragraph(it, ParagraphStyle("eh2", parent=S["cell"], fontSize=8.6,
                                           leading=11.6, leftIndent=10, bulletIndent=1),
                        bulletText="▸")]
    if sample:
        s += [Spacer(1, 3)]
        s += box("BÀI VIẾT THAM KHẢO", [Paragraph(sample, S["boxb"])], "note")
    return s


def mindmap(title, branches, sub=None):
    """Sơ đồ khối: một nút trung tâm + các nhánh. branches = [(tên nhánh, [ý...]), ...]"""
    inner = [Paragraph("<b>%s</b>" % title,
                       ParagraphStyle("mm", fontName="Head-B", fontSize=10,
                                      leading=13, textColor=WHITE,
                                      alignment=TA_CENTER))]
    top = Table([[inner]], colWidths=[CONTENT_W - 8])
    top.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("BOX", (0, 0), (-1, -1), 0.4, NAVY),
    ]))
    if sub:
        tail = Paragraph(sub, ParagraphStyle("mms", fontName="Body", fontSize=8.2,
                                             leading=11, textColor=GRAY,
                                             alignment=TA_CENTER))
    n = len(branches)
    cells, widths = [], []
    for i, (name, items) in enumerate(branches):
        acc = [BLUE, GOLD, GREEN, PURPLE, RED][i % 5]
        soft = [BLUE_PALE, GOLD_SOFT, GREEN_SOFT, PURPLE_SOFT, RED_SOFT][i % 5]
        body = [Paragraph("<b>%s</b>" % name,
                          ParagraphStyle("bn", fontName="Head-B", fontSize=8.4,
                                         leading=11, textColor=WHITE,
                                         alignment=TA_CENTER))]
        box = Table([[body]], colWidths=[(CONTENT_W - 8) / n - 6])
        box.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), acc),
                                 ("TOPPADDING", (0, 0), (-1, -1), 4),
                                 ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 3),
                                 ("RIGHTPADDING", (0, 0), (-1, -1), 3)]))
        lst = [box, Spacer(1, 3)]
        for it in items:
            lst.append(Paragraph("• " + it,
                                 ParagraphStyle("bi", fontName="Body", fontSize=7.7,
                                                leading=10.3, leftIndent=5,
                                                bulletIndent=0,
                                                textColor=colors.HexColor("#1F1F1F"))))
            lst.append(Spacer(1, 1.2))
        cell = Table([[lst]], colWidths=[(CONTENT_W - 8) / n - 6])
        cell.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), soft),
                                  ("BOX", (0, 0), (-1, -1), 0.4, acc),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 4),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                                  ("TOPPADDING", (0, 0), (-1, -1), 4),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
        cells.append(cell)
        widths.append((CONTENT_W - 8) / n)
    grid = Table([cells], colWidths=widths)
    grid.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 2),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                              ("TOPPADDING", (0, 0), (-1, -1), 3),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    out = [Spacer(1, 4), top]
    if sub:
        out += [Spacer(1, 2), tail]
    out += [Spacer(1, 3), grid, Spacer(1, 7)]
    return out


def compare(left, right, rows, wl=1.05, wr=1.05, wc=1.9, head_bg=None):
    """Bảng so sánh 2 đối tượng. rows = [(tiêu chí, giá trị trái, giá trị phải), ...]"""
    data = [["Tiêu chí", left, right]] + [[r[0], r[1], r[2]] for r in rows]
    t = mk_table(data, widths=[wc, wl, wr], align_center=[],
                 first_col_bold=True, font_size=8.2)
    return [Spacer(1, 2), t, Spacer(1, 8)]


def toc_title(text="MỤC LỤC"):
    t = Table([[Paragraph(text, S["toctitle"]),
                Paragraph("Trang", ParagraphStyle("pt", fontName="Head", fontSize=8,
                                                  textColor=GRAY, alignment=TA_RIGHT))]],
              colWidths=[CONTENT_W - 46, 46])
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 2, NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def make_toc():
    toc = TableOfContents()
    toc.levelStyles = [S["toc1"], S["toc2"], S["toc3"]]
    toc.dotsMinLevel = 0
    return toc
