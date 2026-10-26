#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render the Grade 10 History midterm revision pack (Kết nối tri thức) to PDF.

Usage:  python3 tools/build_pdf.py [output.pdf]
Requires: reportlab (pip install reportlab) + DejaVu fonts (bundled with most Linux distros).
"""

import os
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame,
                                NextPageTemplate, PageBreak, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content  # noqa: E402

# ----------------------------------------------------------------------------- palette
NAVY = colors.HexColor("#15325B")
BLUE = colors.HexColor("#1F5FA9")
BLUE_L = colors.HexColor("#E8EFF9")
TEAL = colors.HexColor("#0E6E6B")
TEAL_L = colors.HexColor("#E2F1F0")
RED = colors.HexColor("#B0332B")
RED_L = colors.HexColor("#FBEAE8")
AMBER = colors.HexColor("#B57600")
AMBER_L = colors.HexColor("#FFF5DF")
GREEN = colors.HexColor("#2E6B3B")
GREEN_L = colors.HexColor("#EAF4EA")
GREY = colors.HexColor("#5A6675")
GRID = colors.HexColor("#B9C7D9")
ROW_ALT = colors.HexColor("#F4F7FC")

# ----------------------------------------------------------------------------- fonts
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DJV-B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DJVM", os.path.join(FONT_DIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily("DJV", normal="DJV", bold="DJV-B", italic="DJV", boldItalic="DJV-B")

BASE = dict(fontName="DJV", textColor=colors.HexColor("#1A1A1A"))

S = {}
S["body"] = ParagraphStyle("body", fontSize=10, leading=15, alignment=TA_JUSTIFY,
                           spaceAfter=4, **BASE)
S["body_c"] = ParagraphStyle("body_c", parent=S["body"], alignment=TA_CENTER)
S["lead"] = ParagraphStyle("lead", parent=S["body"], fontSize=10.5, leading=16,
                           textColor=colors.HexColor("#243447"))
S["h2"] = ParagraphStyle("h2", parent=S["body"], fontSize=12.6, leading=17,
                         fontName="DJV-B", textColor=BLUE, alignment=TA_LEFT,
                         spaceBefore=10, spaceAfter=5, leftIndent=0,
                         keepWithNext=1)
S["h3"] = ParagraphStyle("h3", parent=S["body"], fontSize=10.6, leading=15,
                         fontName="DJV-B", textColor=RED, spaceBefore=7, spaceAfter=3,
                         alignment=TA_LEFT, keepWithNext=1)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=13, bulletIndent=2,
                             spaceAfter=2.5, alignment=TA_LEFT)
S["bullet2"] = ParagraphStyle("bullet2", parent=S["bullet"], leftIndent=27, bulletIndent=15)
S["num"] = ParagraphStyle("num", parent=S["bullet"], leftIndent=18, bulletIndent=2)
S["cell"] = ParagraphStyle("cell", parent=S["body"], fontSize=8.8, leading=12.6,
                           alignment=TA_LEFT, spaceAfter=0)
S["cell_b"] = ParagraphStyle("cell_b", parent=S["cell"], fontName="DJV-B")
S["cell_c"] = ParagraphStyle("cell_c", parent=S["cell"], alignment=TA_CENTER)
S["th"] = ParagraphStyle("th", parent=S["cell"], fontName="DJV-B",
                         textColor=colors.white, alignment=TA_LEFT)
S["th_c"] = ParagraphStyle("th_c", parent=S["th"], alignment=TA_CENTER)
S["box_t"] = ParagraphStyle("box_t", parent=S["body"], fontName="DJV-B", fontSize=9.8,
                            leading=13.5, spaceAfter=2.5, alignment=TA_LEFT)
S["box"] = ParagraphStyle("box", parent=S["body"], fontSize=9.3, leading=13.4,
                          spaceAfter=1.5, alignment=TA_LEFT)
S["box_b"] = ParagraphStyle("box_b", parent=S["box"], leftIndent=11, bulletIndent=1)
S["q"] = ParagraphStyle("q", parent=S["body"], fontSize=9.8, leading=14.2,
                        spaceBefore=7, spaceAfter=2, alignment=TA_LEFT, leftIndent=0)
S["opt"] = ParagraphStyle("opt", parent=S["body"], fontSize=9.3, leading=13,
                          leftIndent=17, spaceAfter=1.2, alignment=TA_LEFT)
S["ans"] = ParagraphStyle("ans", parent=S["body"], fontSize=9.2, leading=13.2,
                          leftIndent=12, spaceAfter=2.5, alignment=TA_LEFT)
S["cover_sm"] = ParagraphStyle("cover_sm", parent=S["body"], fontSize=12, leading=18,
                              alignment=TA_CENTER, textColor=colors.white)
S["cover_big"] = ParagraphStyle("cover_big", parent=S["body"], fontSize=33, leading=42,
                               alignment=TA_CENTER, textColor=colors.white)
S["cover_mid"] = ParagraphStyle("cover_mid", parent=S["body"], fontSize=23, leading=32,
                               alignment=TA_CENTER, textColor=colors.white)
S["tree"] = ParagraphStyle("tree", parent=S["body"], fontSize=7.9, leading=11.6,
                           alignment=TA_LEFT, spaceAfter=0, textColor=colors.HexColor("#1D2B3A"),
                           leftIndent=2)
S["small"] = ParagraphStyle("small", parent=S["body"], fontSize=8.2, leading=11.5,
                            textColor=GREY, alignment=TA_LEFT)
S["cover_t1"] = ParagraphStyle("cover_t1", parent=S["body"], fontName="DJV-B", fontSize=12,
                               leading=18, textColor=colors.white, alignment=TA_CENTER)
S["cover_t2"] = ParagraphStyle("cover_t2", parent=S["body"], fontName="DJV-B", fontSize=30,
                               leading=36, textColor=colors.white, alignment=TA_CENTER)
S["cover_t3"] = ParagraphStyle("cover_t3", parent=S["body"], fontSize=12.5, leading=19,
                               textColor=colors.white, alignment=TA_CENTER, fontName="DJV-B")
S["cover_t4"] = ParagraphStyle("cover_t4", parent=S["body"], fontSize=10, leading=15,
                               textColor=colors.HexColor("#2A3B52"), alignment=TA_CENTER)


class Outline(Flowable):
    """Invisible flowable that bookmarks the current position for the PDF outline."""

    _n = 0

    def __init__(self, title, level=0):
        Flowable.__init__(self)
        Outline._n += 1
        self.key = "sec%d" % Outline._n
        self.title = title
        self.level = level
        self.width = self.height = 0

    def wrap(self, aW, aH):
        return (0, 0)

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, level=self.level, closed=False)


def P(txt, style="body"):
    return Paragraph(txt, S[style] if isinstance(style, str) else style)


# ----------------------------------------------------------------------------- flowables
class Banner(Table):
    """Full-width coloured section banner."""

    def __init__(self, label, title, width, color=NAVY):
        inner = [
            Paragraph('<font size="8.4" color="#AFC7E8">%s</font>' % label, S["body"]),
            Paragraph('<font size="14.5" color="#FFFFFF"><b>%s</b></font>' % title, S["body"]),
        ]
        super().__init__([[inner]], colWidths=[width])
        self.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), color),
            ("LEFTPADDING", (0, 0), (-1, -1), 11),
            ("RIGHTPADDING", (0, 0), (-1, -1), 11),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))


def callout(title, lines, kind="note", width=17.0 * cm):
    theme = {
        "note": (BLUE_L, BLUE, "■"),
        "mnemonic": (AMBER_L, AMBER, "★"),
        "warn": (RED_L, RED, "!"),
        "tip": (GREEN_L, GREEN, "✓"),
        "teal": (TEAL_L, TEAL, "◆"),
    }[kind]
    bg, line, glyph = theme
    flow = []
    if title:
        flow.append(Paragraph('<font color="%s">%s</font>&nbsp; %s' %
                              (line.hexval().replace("0x", "#"), glyph, title), S["box_t"]))
    for ln in lines:
        if ln.startswith("- "):
            flow.append(Paragraph(ln[2:], S["box_b"], bulletText="•"))
        else:
            flow.append(Paragraph(ln, S["box"]))
    t = Table([[flow]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.9, line),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, line),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def data_table(header, rows, widths, center_cols=(), header_bg=NAVY, font_size=8.8,
               row_h=None):
    def cell(txt, style):
        if isinstance(txt, Paragraph):
            return txt
        return Paragraph(str(txt), S[style])

    data = [[cell(h, "th_c" if i in center_cols else "th") for i, h in enumerate(header)]] if header else []
    for row in rows:
        data.append([cell(c, "cell_c" if i in center_cols else "cell") for i, c in enumerate(row)])
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT",
              rowHeights=row_h)
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), header_bg),
                 ("TOPPADDING", (0, 0), (-1, 0), 5.5),
                 ("BOTTOMPADDING", (0, 0), (-1, 0), 5.5)]
        start = 1
    else:
        start = 0
    for i in range(start, len(data)):
        if (i - start) % 2 == 1:
            cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(cmds))
    return t


def kv_table(rows, widths=(4.2 * cm, 12.8 * cm)):
    data = [[Paragraph(k, S["cell_b"]), Paragraph(v, S["cell"])] for k, v in rows]
    t = Table(data, colWidths=list(widths), hAlign="LEFT")
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("BACKGROUND", (0, 0), (0, -1), BLUE_L),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


# ----------------------------------------------------------------------------- render
WIDTH = A4[0] - 2 * 1.55 * cm


def render(block, story):
    kind = block[0]
    if kind in ("banner", "banner2", "banner3"):
        if kind in ("banner2", "banner3"):
            story.append(CondPageBreak(11 * cm))
        story.append(Outline(block[2].replace("&amp;", "&"), 0))
        color = {"banner": NAVY, "banner2": BLUE, "banner3": TEAL}[kind]
        story.append(Banner(block[1], block[2], WIDTH, color))
        story.append(Spacer(1, 7))
    elif kind == "h2":
        story.append(Outline(block[1].replace("&amp;", "&"), 1))
        story.append(Paragraph(block[1], S["h2"]))
    elif kind == "h3":
        if len(block) > 2:
            story.append(CondPageBreak(block[2] * cm))
        story.append(Paragraph(block[1], S["h3"]))
    elif kind == "p":
        story.append(Paragraph(block[1], S["body"]))
    elif kind == "lead":
        story.append(Paragraph(block[1], S["lead"]))
    elif kind == "small":
        story.append(Paragraph(block[1], S["small"]))
    elif kind == "q":
        story.append(Paragraph(block[1], S["q"]))
    elif kind == "opt":
        for item in block[1]:
            story.append(Paragraph(item, S["opt"]))
    elif kind == "ans":
        story.append(Paragraph(block[1], S["ans"]))
    elif kind == "trees":
        boxes = []
        for title, lines in block[1]:
            inner = [Paragraph('<font color="#0E6E6B"><b>%s</b></font>' % title, S["box_t"])]
            inner += [Paragraph(l.replace(" ", "&nbsp;"), S["tree"]) for l in lines]
            boxes.append(inner)
        story.append(Table([boxes], colWidths=[WIDTH / float(len(boxes))] * len(boxes),
                           style=TableStyle([
                               ("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("BACKGROUND", (0, 0), (-1, -1), TEAL_L),
                               ("BOX", (0, 0), (-1, -1), 0.9, TEAL),
                               ("INNERGRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#9CC7C5")),
                               ("LEFTPADDING", (0, 0), (-1, -1), 7),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                               ("TOPPADDING", (0, 0), (-1, -1), 7),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                           ])))
        story.append(Spacer(1, 8))
    elif kind == "bullets":
        for item in block[1]:
            story.append(Paragraph(item, S["bullet"], bulletText="•"))
        story.append(Spacer(1, 2))
    elif kind == "sub":
        for item in block[1]:
            story.append(Paragraph(item, S["bullet2"], bulletText="–"))
        story.append(Spacer(1, 2))
    elif kind == "nums":
        for i, item in enumerate(block[1], 1):
            story.append(Paragraph(item, S["num"], bulletText="%d." % i))
        story.append(Spacer(1, 2))
    elif kind == "box":
        spec = block[1]
        story.append(callout(spec.get("title", ""), spec["lines"],
                             spec.get("kind", "note"), WIDTH))
        story.append(Spacer(1, 7))
    elif kind == "table":
        spec = block[1]
        story.append(data_table(spec["header"], spec["rows"], spec["widths"],
                                spec.get("center", ()), header_bg=spec.get("bg", NAVY),
                                row_h=spec.get("row_h")))
        story.append(Spacer(1, 8))
    elif kind == "kv":
        story.append(kv_table(block[1]))
        story.append(Spacer(1, 8))
    elif kind == "space":
        story.append(Spacer(1, block[1]))
    elif kind == "rule":
        story.append(Table([[""]], colWidths=[WIDTH], rowHeights=[1],
                           style=TableStyle([("LINEABOVE", (0, 0), (-1, -1), 1, BLUE)])))
        story.append(Spacer(1, 6))
    elif kind == "pagebreak":
        min_h = block[1] if len(block) > 1 else 12
        story.append(CondPageBreak(min_h * cm))
    else:
        raise ValueError("unknown block %r" % (kind,))


def cover(story):
    hero_row = [
        Paragraph('<font color="#9DBBE4" size="10">TRƯỜNG THPT &nbsp;•&nbsp; TỔ LỊCH SỬ &nbsp;•&nbsp; '
                  'NĂM HỌC 2026 – 2027</font>', S["body_c"]),
        Spacer(1, 26),
        Paragraph('<font color="#E9B44C" size="12"><b>ĐỀ CƯƠNG ÔN TẬP</b></font>', S["cover_sm"]),
        Spacer(1, 12),
        Paragraph('<font color="#FFFFFF" size="33"><b>GIỮA HỌC KÌ I</b></font>', S["cover_big"]),
        Spacer(1, 8),
        Paragraph('<font color="#FFFFFF" size="23"><b>MÔN LỊCH SỬ – LỚP 10</b></font>', S["cover_mid"]),
        Spacer(1, 18),
        Paragraph('<font color="#C8D8EE" size="10.5">Chủ đề 1: Lịch sử và Sử học (Bài 1, 2) &nbsp;|&nbsp; '
                  'Chủ đề 2: Vai trò của Sử học (Bài 3)</font>', S["body_c"]),
        Spacer(1, 20),
        Paragraph('<font color="#FFFFFF" size="11.5"><b>BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG</b></font>',
                  S["body_c"]),
        Spacer(1, 16),
    ]
    hero = Table([[hero_row]], colWidths=[WIDTH])
    hero.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 18),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 30),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 30),
    ]))
    story.append(hero)
    story.append(Spacer(1, 0.28 * cm))
    story.append(Table([[""]], colWidths=[WIDTH], rowHeights=[4],
                       style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), AMBER)])))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph('<font color="#15325B" size="11"><b>TRỌN BỘ TÀI LIỆU GỒM</b></font>', S["body"]))
    story.append(Spacer(1, 0.2 * cm))
    items = [
        "① <b>Tóm tắt kiến thức trọng tâm 3 bài</b> – trình bày bằng bảng, sơ đồ, cặp đối lập để dễ nhớ.",
        "② <b>Bảng phân biệt &amp; mẹo ghi nhớ (mnemonic)</b> cho từng nội dung, kèm 12 cặp từ khoá dễ nhầm.",
        "③ <b>Đề kiểm tra minh hoạ đúng ma trận:</b> 20 câu trắc nghiệm + 2 câu đúng/sai (8 ý) + 1 câu tự luận.",
        "④ <b>Đáp án chi tiết:</b> giải thích vì sao đúng – vì sao sai, đáp án đúng/sai, dàn ý và biểu điểm tự luận.",
        "⑤ <b>Chiến thuật phòng thi</b> và checklist 10 giây trước giờ làm bài.",
    ]
    box = Table([[[Paragraph(x, S["box"]) for x in items]]], colWidths=[WIDTH])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_L),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#B9CFEA")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(box)
    story.append(Spacer(1, 0.55 * cm))
    info = Table([[Paragraph('<b>Thời gian làm bài:</b> 45 phút', S["cell"]),
                   Paragraph('<b>Hình thức:</b> TN nhiều lựa chọn + Đúng/Sai + Tự luận', S["cell"]),
                   Paragraph('<b>Phạm vi:</b> Bài 1, 2, 3', S["cell"])]],
                 colWidths=[WIDTH / 3.0] * 3)
    info.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, GRID),
        ("INNERGRID", (0, 0), (-1, -1), 0.8, GRID),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FAFBFD")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(info)
    story.append(Spacer(1, 0.9 * cm))
    story.append(Paragraph('<font color="#7A8797" size="8.5">Tài liệu lưu hành nội bộ – dùng cho ôn tập cá nhân. '
                           'Nội dung biên soạn theo ma trận và bản đặc tả đề kiểm tra giữa học kì I của tổ bộ môn.</font>',
                           S["body_c"]))
    story.append(PageBreak())


def decorate(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#8FA3BD"))
    canvas.setFont("DJV", 7.4)
    canvas.drawString(1.55 * cm, A4[1] - 1.05 * cm,
                      "ÔN TẬP GIỮA HỌC KÌ I – LỊCH SỬ 10 (KẾT NỐI TRI THỨC)")
    canvas.drawRightString(A4[0] - 1.55 * cm, A4[1] - 1.05 * cm,
                           "Chủ đề 1 & 2 – Bài 1, 2, 3")
    canvas.setStrokeColor(colors.HexColor("#CFDAE8"))
    canvas.setLineWidth(0.7)
    canvas.line(1.55 * cm, A4[1] - 1.22 * cm, A4[0] - 1.55 * cm, A4[1] - 1.22 * cm)
    canvas.drawCentredString(A4[0] / 2.0, 0.85 * cm, "— %d —" % doc.page)
    canvas.restoreState()


def decorate_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 0.55 * cm, A4[0], 0.55 * cm, stroke=0, fill=1)
    canvas.rect(0, 0, A4[0], 0.55 * cm, stroke=0, fill=1)
    canvas.restoreState()


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "ON_TAP_LS10_GK1_KNTT.pdf"
    doc = BaseDocTemplate(out, pagesize=A4,
                          leftMargin=1.55 * cm, rightMargin=1.55 * cm,
                          topMargin=1.55 * cm, bottomMargin=1.35 * cm,
                          title="Ôn tập Giữa học kì I – Lịch sử 10 (Kết nối tri thức)",
                          author="Tổ Lịch sử",
                          subject="Đề cương ôn tập + đề minh họa + đáp án")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[frame], onPage=decorate_cover),
        PageTemplate(id="main", frames=[frame], onPage=decorate),
    ])

    story = [NextPageTemplate("main")]
    cover(story)
    for block in content.BLOCKS:
        render(block, story)
    doc.build(story)
    print("wrote", out)


if __name__ == "__main__":
    main()
