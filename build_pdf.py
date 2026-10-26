#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dựng PDF đề cương ôn tập từ các tệp Markdown nhẹ trong src/.
Yêu cầu: reportlab, font DejaVu (có sẵn trên Linux).
Chạy:  python3 build_pdf.py
"""
import os
import re
import glob
import html
import json

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                Flowable, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents

# ----------------------------------------------------------------------------
# Fonts
# ----------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DV-B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")

# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
NAVY = colors.HexColor("#1B2A4A")
INDIGO = colors.HexColor("#25406F")
TEAL = colors.HexColor("#0E6E63")
AMBER = colors.HexColor("#B45309")
RED = colors.HexColor("#A32B2B")
GREEN = colors.HexColor("#1E6B4F")
TEXT = colors.HexColor("#26313F")
MUTED = colors.HexColor("#5C6A7C")
GRID = colors.HexColor("#CBD5E1")
BG_BLUE = colors.HexColor("#EEF3FA")
BG_GREEN = colors.HexColor("#ECF6F1")
BG_AMBER = colors.HexColor("#FDF4E8")
BG_KEY = colors.HexColor("#EDF1F8")
ZEBRA = colors.HexColor("#F7F9FC")
WHITE = colors.white

PAGE_W, PAGE_H = A4
LM = RM = 17 * mm
TM = 21 * mm
BM = 17 * mm
CONTENT_W = PAGE_W - LM - RM

# ----------------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------------
def S(name, **kw):
    base = dict(fontName="DV", fontSize=9.6, leading=14.0, textColor=TEXT,
                alignment=TA_JUSTIFY, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)

st_body = S("body")
st_bullet = S("bullet", leftIndent=13, bulletIndent=2, spaceAfter=2.4, bulletFontName="DV")
st_sub = S("sub", leftIndent=27, bulletIndent=16, spaceAfter=1.8, fontSize=9.2, leading=13.2)
st_num = S("num", leftIndent=17, firstLineIndent=-17, spaceAfter=2.4)
st_h1 = S("h1", fontName="DV-B", fontSize=15.5, leading=19, textColor=WHITE,
          alignment=TA_LEFT, spaceAfter=0)
st_h2 = S("h2", fontName="DV-B", fontSize=12.4, leading=16, textColor=INDIGO,
          alignment=TA_LEFT, spaceBefore=10, spaceAfter=4)
st_h3 = S("h3", fontName="DV-B", fontSize=10.4, leading=14, textColor=TEAL,
          alignment=TA_LEFT, spaceBefore=7, spaceAfter=2.5)
st_h4 = S("h4", fontName="DV-B", fontSize=9.6, leading=13, textColor=NAVY,
          alignment=TA_LEFT, spaceBefore=5, spaceAfter=2)
st_cell = S("cell", fontSize=8.5, leading=11.6, alignment=TA_LEFT, spaceAfter=0)
st_cellc = S("cellc", fontSize=8.5, leading=11.6, alignment=TA_CENTER, spaceAfter=0)
st_th = S("th", fontName="DV-B", fontSize=8.6, leading=11.4, textColor=WHITE,
          alignment=TA_LEFT, spaceAfter=0)
st_thc = S("thc", fontName="DV-B", fontSize=8.6, leading=11.4, textColor=WHITE,
           alignment=TA_CENTER, spaceAfter=0)
st_opt = S("opt", leftIndent=16, firstLineIndent=-16, spaceAfter=1.2, fontSize=9.4, leading=13.2)
st_qlabel = S("qlabel", fontName="DV-B", fontSize=9.5, leading=13.4, textColor=NAVY,
              alignment=TA_LEFT, spaceAfter=2)
st_boxlabel = S("boxlabel", fontName="DV-B", fontSize=7.8, leading=10, textColor=AMBER,
                alignment=TA_LEFT, spaceAfter=2)
st_boxbody = S("boxbody", fontSize=9.2, leading=13.4, alignment=TA_JUSTIFY, spaceAfter=2.5)
st_boxbullet = S("boxbullet", fontSize=9.2, leading=13.4, leftIndent=11, bulletIndent=1, spaceAfter=1.6)
st_toc0 = S("toc0", fontName="DV-B", fontSize=9.2, leading=12.4, spaceBefore=2.6, textColor=NAVY, alignment=TA_LEFT)
st_toc1 = S("toc1", fontSize=8.3, leading=9.7, leftIndent=13, textColor=TEXT, alignment=TA_LEFT)

# ----------------------------------------------------------------------------
# Inline markup
# ----------------------------------------------------------------------------
def inline(text):
    t = html.escape(text.strip(), quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t

# ----------------------------------------------------------------------------
# Custom flowables
# ----------------------------------------------------------------------------
class Rule(Flowable):
    """Đường kẻ mảnh."""
    def __init__(self, width, thickness=0.5, color=GRID, space_before=4, space_after=4):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.color = color
        self.spaceBefore = space_before
        self.spaceAfter = space_after
        self.height = thickness

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


def h1_block(title):
    """Banner chương: nền navy, viền trái hổ phách."""
    p = Paragraph(inline(title), st_h1)
    t = Table([[p]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LINEBEFORE", (0, 0), (0, -1), 4.5, colors.HexColor("#E0912F")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    t.spaceBefore = 0
    t.spaceAfter = 8
    return t


def h2_block(title):
    p = Paragraph(inline(title), st_h2)
    t = Table([[p]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, colors.HexColor("#D9A441")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    t.spaceBefore = 11
    t.spaceAfter = 5
    return t


# ----------------------------------------------------------------------------
# Table builder
# ----------------------------------------------------------------------------
def col_widths(rows, avail, forced=None):
    if forced:
        total = float(sum(forced))
        return [avail * w / total for w in forced]
    ncols = max(len(r) for r in rows)
    weights = []
    for c in range(ncols):
        mx = 4
        for r in rows:
            if c < len(r):
                mx = max(mx, len(re.sub(r"\*\*", "", r[c])))
        weights.append(max(9, min(mx, 46)))
    total = float(sum(weights))
    return [avail * w / total for w in weights]


def make_table(rows, avail, forced=None):
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    data = []
    for i, r in enumerate(rows):
        line = []
        for c, cell in enumerate(r):
            sty = st_th if i == 0 else st_cell
            if i == 0 and c == 0:
                sty = st_th
            line.append(Paragraph(inline(cell), sty))
        data.append(line)
    widths = col_widths(rows, avail, forced)
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), INDIGO),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    t.spaceBefore = 3
    t.spaceAfter = 8
    return t


# ----------------------------------------------------------------------------
# Boxes
# ----------------------------------------------------------------------------
BOX_STYLE = {
    "note": dict(label="GHI CHÚ", color=INDIGO, bg=BG_BLUE),
    "tip": dict(label="MẸO GHI NHỚ", color=GREEN, bg=BG_GREEN),
    "warn": dict(label="CẢNH BÁO", color=AMBER, bg=BG_AMBER),
    "key": dict(label="ĐIỀU CẦN KHẮC SÂU", color=NAVY, bg=BG_KEY),
    "a": dict(label="TRẢ LỜI", color=GREEN, bg=colors.HexColor("#F4FAF7")),
    "q": dict(label=None, color=INDIGO, bg=colors.HexColor("#F5F8FD")),
}


def make_box(kind, arg, inner_flowables, avail):
    cfg = BOX_STYLE.get(kind, BOX_STYLE["note"])
    content = []
    if kind == "q":
        content.append(Paragraph(inline(arg), st_qlabel))
    else:
        label = arg.strip() if arg.strip() and kind in ("tip", "warn", "key", "note") else cfg["label"]
        if label:
            content.append(Paragraph(label.upper(), ParagraphStyle(
                "lbl_" + kind, parent=st_boxlabel, textColor=cfg["color"])))
    content.extend(inner_flowables)
    t = Table([[content]], colWidths=[avail])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), cfg["bg"]),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, cfg["color"]),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#DDE5EF")),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    t.spaceBefore = 4
    t.spaceAfter = 8
    return t


# ----------------------------------------------------------------------------
# Markdown-light parser
# ----------------------------------------------------------------------------
def fix_orphans(flow, avail):
    """Giữ (các) tiêu đề đi liền với khối nội dung kế tiếp nếu tổng chiều cao còn vừa một trang."""
    res = []
    i = 0
    n = len(flow)
    while i < n:
        f = flow[i]
        if getattr(f, "_is_heading", False):
            group = [f]
            j = i + 1
            while j < n and getattr(flow[j], "_is_heading", False) and len(group) < 3:
                group.append(flow[j])
                j += 1
            if j < n and not isinstance(flow[j], PageBreak):
                group.append(flow[j])
                try:
                    h = sum(g.wrap(avail, PAGE_H)[1] for g in group) + 10 * len(group)
                except Exception:
                    h = 9999
                if h <= 165 * mm:
                    res.append(KeepTogether(group))
                    i = j + 1
                    continue
        res.append(f)
        i += 1
    return res


def parse_blocks(lines, avail, in_box=False):
    out = []
    i = 0
    forced_cols = None
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip("\n")
        s = line.strip()

        if not s:
            i += 1
            continue

        if s.startswith("::cols "):
            forced_cols = [float(x) for x in s[7:].split(",")]
            i += 1
            continue

        if s.startswith("::"):
            head = s[2:].strip()
            parts = head.split(" ", 1)
            kind = parts[0].strip()
            arg = parts[1].strip() if len(parts) > 1 else ""
            j = i + 1
            while j < len(lines) and lines[j].strip() != "::end":
                j += 1
            inner_lines = lines[i + 1:j]
            inner = parse_blocks(inner_lines, avail - 22, in_box=True)
            out.append(make_box(kind, arg, inner, avail))
            i = j + 1
            continue

        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            out.append(make_table(rows, avail, forced_cols))
            forced_cols = None
            continue

        if s.startswith("- "):
            indent = len(raw) - len(raw.lstrip(" "))
            sty = st_sub if indent >= 2 else st_bullet
            txt = s[2:].strip()
            out.append(Paragraph(inline(txt), sty, bulletText="–" if indent >= 2 else "•"))
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            out.append(Paragraph(f"<b>{m.group(1)}.</b> " + inline(m.group(2)), st_num))
            i += 1
            continue

        m = re.match(r"^([A-D])\.\s+(.*)$", s)
        if m:
            out.append(Paragraph(f"<b>{m.group(1)}.</b> " + inline(m.group(2)), st_opt))
            i += 1
            continue

        m = re.match(r"^([a-d])\)\s+(.*)$", s)
        if m:
            out.append(Paragraph(f"<b>{m.group(1)})</b> " + inline(m.group(2)), st_opt))
            i += 1
            continue

        if s.startswith("#### "):
            out.append(Paragraph(inline(s[5:]), st_h4))
            i += 1
            continue
        if s.startswith("### "):
            f = Paragraph(inline(s[4:]), st_h3)
            f._is_heading = True
            out.append(f)
            i += 1
            continue
        if s.startswith("## "):
            block = h2_block(s[3:])
            block._toc = (1, s[3:].strip(), "h2-%d" % len(out))
            block._is_heading = True
            out.append(block)
            i += 1
            continue
        if s.startswith("# "):
            block = h1_block(s[2:])
            block._toc = (0, s[2:].strip(), "h1-%d" % len(out))
            block._is_heading = True
            out.append(block)
            i += 1
            continue

        out.append(Paragraph(inline(s), st_boxbody if in_box else st_body))
        i += 1

    return out


# ----------------------------------------------------------------------------
# Doc template with TOC + header/footer
# ----------------------------------------------------------------------------
TOC_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".toc_cache.json")


class DeCuongDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập giữa học kì I – Lịch sử 10 (KNTT)",
                                 author="Tài liệu ôn tập",
                                 subject="Lịch sử 10 – Kết nối tri thức với cuộc sống",
                                 **kw)
        self.toc_entries = []
        frame = Frame(LM, BM, CONTENT_W, PAGE_H - TM - BM, id="normal",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="first", frames=[frame], onPage=self.draw_cover),
            PageTemplate(id="later", frames=[frame], onPage=self.draw_body),
        ])

    # ---------------- cover ----------------
    def draw_cover(self, canv, doc):
        canv.saveState()
        # nền
        canv.setFillColor(colors.HexColor("#FBFAF7"))
        canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        # dải trên
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - 118 * mm, PAGE_W, 118 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#E0912F"))
        canv.rect(0, PAGE_H - 119.4 * mm, PAGE_W, 1.4 * mm, stroke=0, fill=1)

        # nhãn nhỏ
        canv.setFillColor(colors.HexColor("#9FB4D4"))
        canv.setFont("DV-B", 8)
        canv.drawString(LM, PAGE_H - 28 * mm, "TÀI LIỆU ÔN TẬP  ·  NĂM HỌC 2026 – 2027")
        canv.setStrokeColor(colors.HexColor("#3D5480"))
        canv.setLineWidth(0.7)
        canv.line(LM, PAGE_H - 32 * mm, LM + 62 * mm, PAGE_H - 32 * mm)

        # tiêu đề
        canv.setFillColor(WHITE)
        canv.setFont("DV-B", 33)
        canv.drawString(LM, PAGE_H - 55 * mm, "ĐỀ CƯƠNG ÔN TẬP")
        canv.setFont("DV-B", 19)
        canv.setFillColor(colors.HexColor("#E6ECF6"))
        canv.drawString(LM, PAGE_H - 70 * mm, "GIỮA HỌC KÌ I  ·  MÔN LỊCH SỬ")

        # khối lớp
        canv.setFillColor(colors.HexColor("#E0912F"))
        canv.setFont("DV-B", 46)
        canv.drawString(LM, PAGE_H - 98 * mm, "LỚP 10")
        canv.setFillColor(WHITE)
        canv.setFont("DV", 10.5)
        canv.drawString(LM + 78 * mm, PAGE_H - 87 * mm, "Bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
        canv.setFillColor(colors.HexColor("#9FB4D4"))
        canv.setFont("DV", 9)
        canv.drawString(LM + 78 * mm, PAGE_H - 93.5 * mm, "Chủ đề 1: Lịch sử và sử học  ·  Chủ đề 2: Vai trò của sử học")

        # ba thẻ thông tin
        cards = [
            ("PHẠM VI", "Bài 1 – Bài 2 – Bài 3", "Chủ đề 1 và Chủ đề 2"),
            ("CẤU TRÚC ĐỀ", "20 TN + 2 Đ/S + 1 TL", "28 lệnh hỏi + 1 tự luận"),
            ("THỜI GIAN", "45 phút", "Thang điểm 10"),
        ]
        y = PAGE_H - 148 * mm
        w = (CONTENT_W - 12 * mm) / 3
        for idx, (lab, val, sub) in enumerate(cards):
            x = LM + idx * (w + 6 * mm)
            canv.setFillColor(WHITE)
            canv.setStrokeColor(colors.HexColor("#E2DED4"))
            canv.setLineWidth(0.6)
            canv.roundRect(x, y, w, 27 * mm, 2.5 * mm, stroke=1, fill=1)
            canv.setFillColor(colors.HexColor("#E0912F"))
            canv.rect(x, y + 27 * mm - 1.2 * mm, w, 1.2 * mm, stroke=0, fill=1)
            canv.setFillColor(MUTED)
            canv.setFont("DV-B", 7.2)
            canv.drawString(x + 5 * mm, y + 20.5 * mm, lab)
            canv.setFillColor(NAVY)
            canv.setFont("DV-B", 11.5)
            canv.drawString(x + 5 * mm, y + 13.5 * mm, val)
            canv.setFillColor(colors.HexColor("#7A8798"))
            canv.setFont("DV", 7.8)
            canv.drawString(x + 5 * mm, y + 7.5 * mm, sub)

        # nội dung chính
        canv.setFillColor(NAVY)
        canv.setFont("DV-B", 10)
        canv.drawString(LM, PAGE_H - 168 * mm, "NỘI DUNG CHÍNH")
        canv.setFillColor(colors.HexColor("#D9A441"))
        canv.setLineWidth(1.6)
        canv.line(LM, PAGE_H - 170.5 * mm, LM + 30 * mm, PAGE_H - 170.5 * mm)

        items = [
            ("PHẦN 0", "Phân tích ma trận – đặc tả đề và chiến lược ôn tập"),
            ("PHẦN 1 – 3", "Hệ thống kiến thức Bài 1, Bài 2, Bài 3 (bảng so sánh, sơ đồ, mẹo nhớ)"),
            ("PHẦN 4", "10 cặp khái niệm dễ nhầm – 20 thẻ ghi nhớ nhanh"),
            ("PHẦN 5 – 6", "Đề luyện tập mô phỏng 100% cấu trúc + đáp án, giải thích, thang điểm"),
            ("PHẦN 7", "Chiến lược làm bài 45 phút và lộ trình ôn 5 ngày"),
        ]
        yy = PAGE_H - 178 * mm
        for tag, text in items:
            canv.setFillColor(colors.HexColor("#E0912F"))
            canv.setFont("DV-B", 8.2)
            canv.drawString(LM, yy, tag)
            canv.setFillColor(TEXT)
            canv.setFont("DV", 9)
            canv.drawString(LM + 26 * mm, yy, text)
            yy -= 7.2 * mm

        # ghi chú nguồn
        canv.setFillColor(colors.HexColor("#F1EEE6"))
        canv.setStrokeColor(colors.HexColor("#E2DED4"))
        canv.setLineWidth(0.6)
        canv.roundRect(LM, 26 * mm, CONTENT_W, 20 * mm, 2 * mm, stroke=1, fill=1)
        canv.setFillColor(MUTED)
        canv.setFont("DV", 7.9)
        canv.drawString(LM + 5 * mm, 39.5 * mm,
                        "Biên soạn trên cơ sở MA TRẬN và BẢNG ĐẶC TẢ đề kiểm tra định kì giữa học kì I – Lịch sử 10")
        canv.drawString(LM + 5 * mm, 35 * mm,
                        "Tệp gốc: “LS10- MTGK1-26-27-HHT.docx” (20 câu TN + 2 câu Đ/S + 1 câu TL, thời gian 45 phút)")
        canv.drawString(LM + 5 * mm, 30.5 * mm,
                        "Đề cương gồm: hệ thống kiến thức trọng tâm · câu hỏi – đáp án · đề luyện tập · chiến lược phòng thi")

        canv.setFillColor(colors.HexColor("#8A8577"))
        canv.setFont("DV", 8)
        canv.drawRightString(PAGE_W - LM, 14 * mm, "Tháng 10 năm 2026")
        canv.restoreState()

    # ---------------- header / footer ----------------
    def draw_body(self, canv, doc):
        canv.saveState()
        # header
        canv.setFont("DV", 7.2)
        canv.setFillColor(colors.HexColor("#8A93A0"))
        canv.drawString(LM, PAGE_H - 14 * mm, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I")
        canv.drawRightString(PAGE_W - RM, PAGE_H - 14 * mm, "LỊCH SỬ 10  ·  KẾT NỐI TRI THỨC")
        canv.setStrokeColor(colors.HexColor("#DCE3EC"))
        canv.setLineWidth(0.6)
        canv.line(LM, PAGE_H - 16 * mm, PAGE_W - RM, PAGE_H - 16 * mm)

        # footer
        canv.setStrokeColor(colors.HexColor("#E6EAF0"))
        canv.setLineWidth(0.5)
        canv.line(LM, BM - 4 * mm, PAGE_W - RM, BM - 4 * mm)
        canv.setFont("DV", 7.6)
        canv.setFillColor(colors.HexColor("#8A93A0"))
        canv.drawString(LM, BM - 8.4 * mm, "Tài liệu ôn tập cá nhân – lưu hành nội bộ")
        canv.setFillColor(INDIGO)
        canv.setFont("DV-B", 8)
        canv.drawCentredString(PAGE_W / 2, BM - 8.6 * mm, "%d" % doc.page)
        canv.restoreState()

    # ---------------- TOC hook ----------------
    def afterFlowable(self, flowable):
        if hasattr(flowable, "_toc"):
            level, text, key = flowable._toc
            self.toc_entries.append([level, text, self.page, key])
            self.notify("TOCEntry", (level, text, self.page, key))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level, closed=False)


# ----------------------------------------------------------------------------
# Build
# ----------------------------------------------------------------------------
def load_content():
    files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "src", "*.md")))
    lines = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            lines.extend(fh.read().splitlines())
        lines.append("")
    return lines


def build():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "De-cuong-on-tap-Giua-ki-1-Lich-su-10-KNTT.pdf")
    lines = load_content()
    story = []

    # trang bìa (vẽ bằng canvas) -> đẩy nội dung sang trang 2
    story.append(NextPageTemplate("later"))
    story.append(PageBreak())

    # mục lục
    story.append(Paragraph("MỤC LỤC", ParagraphStyle(
        "toch", parent=st_h2, fontSize=16, leading=20, spaceBefore=0, spaceAfter=2)))
    story.append(Paragraph("Nhấn vào tiêu đề để nhảy tới phần tương ứng (bản PDF có mục lục tương tác).",
                           ParagraphStyle("tocsub", parent=st_body, fontSize=8.6, textColor=MUTED,
                                          spaceAfter=10)))
    toc = TableOfContents()
    toc.levelStyles = [st_toc0, st_toc1]
    toc.dotsMinLevel = 0
    if os.path.exists(TOC_CACHE):
        try:
            with open(TOC_CACHE, encoding="utf-8") as fh:
                for lvl, text, page, key in json.load(fh):
                    toc.notify("TOCEntry", (lvl, text, page, key))
        except Exception:
            pass
    toc.tableStyle = TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.6),
    ])
    story.append(toc)

    story.append(PageBreak())
    story.extend(fix_orphans(parse_blocks(lines, CONTENT_W), CONTENT_W))

    doc = DeCuongDoc(out)
    # trang 1 = bìa, trang 2+ = nội dung
    doc.build(story)
    with open(TOC_CACHE, "w", encoding="utf-8") as fh:
        json.dump(doc.toc_entries, fh, ensure_ascii=False)
    print("Đã tạo:", out, "| số mục lục:", len(doc.toc_entries))


if __name__ == "__main__":
    build()
