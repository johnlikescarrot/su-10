# -*- coding: utf-8 -*-
"""Khuôn trang A4, đầu trang – chân trang, dấu trang PDF và mục lục hai lượt."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle

from .theme import (
    CONTENT_W,
    CREAM,
    GOLD,
    INK,
    MARGIN_B,
    MARGIN_L,
    MARGIN_R,
    MARGIN_T,
    MUTED,
    PAGE_H,
    PAGE_W,
    PRIMARY,
    PRIMARY_DK,
    RULE,
    STYLES,
)

# Số trang của từng tiêu đề, ghi trong lượt dựng thứ nhất.
PAGES: dict[str, int] = {}


def reset_pages() -> None:
    PAGES.clear()


class GuideDoc(BaseDocTemplate):
    """DocTemplate có đầu trang, chân trang, dấu trang PDF và ghi nhận số trang tiêu đề."""

    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(
            self,
            filename,
            pagesize=(PAGE_W, PAGE_H),
            leftMargin=MARGIN_L,
            rightMargin=MARGIN_R,
            topMargin=MARGIN_T,
            bottomMargin=MARGIN_B,
            title="Đề cương ôn tập Giữa học kì I – Lịch sử 10 (Kết nối tri thức)",
            author="Tài liệu ôn tập Lịch sử 10",
            subject="Ôn tập giữa học kì I môn Lịch sử lớp 10 – Chủ đề 1 và Chủ đề 2",
            keywords="Lịch sử 10, Kết nối tri thức, giữa học kì I, đề cương, ôn tập",
            **kwargs,
        )
        frame = Frame(
            MARGIN_L,
            MARGIN_B,
            CONTENT_W,
            PAGE_H - MARGIN_T - MARGIN_B,
            id="body",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        cover_frame = Frame(
            MARGIN_L,
            14 * mm,
            CONTENT_W,
            PAGE_H - 28 * mm,
            id="cover",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._cover_bg),
            PageTemplate(id="body", frames=[frame], onPage=self._body_decor),
        ])
        self._bookmark_seq = 0

    # ------------------------------------------------------------------ trang
    def _cover_bg(self, canv, doc):
        canv.saveState()
        canv.setFillColor(CREAM)
        canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

        band_h = 97 * mm
        canv.setFillColor(PRIMARY)
        canv.rect(0, PAGE_H - band_h, PAGE_W, band_h, stroke=0, fill=1)
        canv.setFillColor(PRIMARY_DK)
        canv.rect(0, PAGE_H - 24 * mm, PAGE_W, 24 * mm, stroke=0, fill=1)
        canv.setFillColor(GOLD)
        canv.rect(0, PAGE_H - band_h - 1.4 * mm, PAGE_W, 1.4 * mm, stroke=0, fill=1)

        # hoa văn chấm mờ trong dải xanh
        canv.setFillColor(colors.Color(1, 1, 1, alpha=0.05))
        step = 7 * mm
        y = PAGE_H - band_h + 6 * mm
        row = 0
        while y < PAGE_H - 30 * mm:
            x = 8 * mm + (step / 2 if row % 2 else 0)
            while x < PAGE_W - 6 * mm:
                canv.circle(x, y, 0.55 * mm, stroke=0, fill=1)
                x += step
            y += step * 0.86
            row += 1

        # khối "cấu trúc đề" neo ở đáy trang
        canv.setFont("Sans-Bold", 7.6)
        canv.setFillColor(GOLD)
        canv.drawString(MARGIN_L, 55 * mm, "CẤU TRÚC ĐỀ KIỂM TRA")
        chips = [
            ("20 câu", "5,0 điểm", "Trắc nghiệm nhiều lựa chọn", 56 * mm),
            ("2 câu", "2,0 điểm", "Trắc nghiệm đúng/sai, 4 ý/câu", 56 * mm),
            ("1 câu", "3,0 điểm", "Tự luận, hai phần a) và b)", 56 * mm),
        ]
        x = MARGIN_L
        for big, score, label, width in chips:
            y0, h = 26 * mm, 21 * mm
            canv.setFillColor(colors.HexColor("#FFFFFF"))
            canv.setStrokeColor(colors.Color(0.85, 0.80, 0.68))
            canv.setLineWidth(0.6)
            canv.roundRect(x, y0, width, h, 2.2 * mm, stroke=1, fill=1)
            canv.setFillColor(PRIMARY)
            canv.setFont("Sans-Bold", 13)
            canv.drawString(x + 4 * mm, y0 + h - 8 * mm, big)
            canv.setFillColor(GOLD)
            canv.setFont("Sans-Bold", 8.4)
            canv.drawString(x + 4 * mm + canv.stringWidth(big, "Sans-Bold", 13) + 2.4 * mm,
                            y0 + h - 8 * mm, score)
            canv.setFillColor(MUTED)
            canv.setFont("Sans", 7.4)
            canv.drawString(x + 4 * mm, y0 + 4.4 * mm, label)
            x += width + 4 * mm

        canv.setStrokeColor(GOLD)
        canv.setLineWidth(0.8)
        canv.rect(10 * mm, 10 * mm, PAGE_W - 20 * mm, PAGE_H - 20 * mm, stroke=1, fill=0)
        canv.setStrokeColor(colors.Color(0.66, 0.47, 0.17, alpha=0.45))
        canv.setLineWidth(0.4)
        canv.rect(11.6 * mm, 11.6 * mm, PAGE_W - 23.2 * mm, PAGE_H - 23.2 * mm, stroke=1, fill=0)
        canv.restoreState()

    def _body_decor(self, canv, doc):
        canv.saveState()
        top = PAGE_H - MARGIN_T + 9 * mm
        canv.setFont("Sans", 7.2)
        canv.setFillColor(MUTED)
        canv.drawString(MARGIN_L, top, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  LỊCH SỬ 10")
        canv.drawRightString(PAGE_W - MARGIN_R, top, "KẾT NỐI TRI THỨC")
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.4)
        canv.line(MARGIN_L, top - 2.6 * mm, PAGE_W - MARGIN_R, top - 2.6 * mm)

        base = 12.4 * mm
        canv.line(MARGIN_L, base, PAGE_W - MARGIN_R, base)
        canv.setFont("Sans", 7.4)
        canv.setFillColor(MUTED)
        canv.drawString(MARGIN_L, base - 4.4 * mm, "Năm học 2026 – 2027")
        canv.setFillColor(PRIMARY)
        canv.setFont("Sans-Bold", 8)
        canv.drawRightString(PAGE_W - MARGIN_R, base - 4.4 * mm, f"Trang {doc.page}")
        canv.restoreState()

    # --------------------------------------------------------------- tiêu đề
    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style = flowable.style.name
        if style not in ("PartHeading", "H2Numbered", "toc_title"):
            return
        key = getattr(flowable, "_toc_key", None)
        if key is None and style == "PartHeading":
            key = flowable.getPlainText().replace("▌", "").strip()
        self._bookmark_seq += 1
        anchor = f"bm{self._bookmark_seq}"
        self.canv.bookmarkPage(anchor)
        if style == "PartHeading":
            label = " ".join(flowable.getPlainText().replace("▌ ", "· ").replace("▌", " · ").split())
        else:
            label = " ".join(flowable.getPlainText().split())
        if style != "toc_title":
            self.canv.addOutlineEntry(label, anchor,
                                      level=0 if style == "PartHeading" else 1,
                                      closed=True)
        if key:
            PAGES.setdefault(key, self.page)


# ------------------------------------------------------------------- mục lục
def _dot_leader(width_pt: float, size: float = 8.4) -> str:
    dot = stringWidth(".", "Body", size) + stringWidth(" ", "Body", size)
    count = max(0, int(width_pt // dot))
    return " ".join("." * count) if count else ""


def toc_flowables(entries, pages) -> list:
    """Mục lục một trang: mỗi phần một dòng có dòng chấm và số trang,
    dưới đó là danh sách các mục con (không kèm số trang) để thấy cấu trúc."""
    out = []
    page_style = ParagraphStyle(
        "tocpage", fontName="Sans-Bold", fontSize=8.8, leading=13,
        textColor=PRIMARY_DK, alignment=TA_RIGHT,
    )
    title_style = ParagraphStyle(
        "toct0", fontName="Sans-Bold", fontSize=9.3, leading=12.6, textColor=PRIMARY,
    )
    desc_style = ParagraphStyle(
        "tocdesc", fontName="Sans", fontSize=7.5, leading=10.4, textColor=MUTED,
        spaceBefore=1.2, spaceAfter=4.5,
    )

    page_w = 9 * mm
    i = 0
    while i < len(entries):
        level, title, key = entries[i]
        if level != 0:
            i += 1
            continue
        gap = 3 * mm
        # dòng chấm dài cố định cho mọi phần -> các số trang thẳng hàng
        mid_w = 22 * mm
        title_w = CONTENT_W - mid_w - page_w - gap
        dots = _dot_leader(mid_w - 1.4 * mm, 9.3)
        number = pages.get(key)
        row = [
            Paragraph(title, title_style),
            Paragraph(dots, ParagraphStyle(
                "tocdots", fontName="Body", fontSize=8.6, leading=11,
                textColor=MUTED, alignment=TA_RIGHT)),
            Paragraph(str(number) if number else "", page_style),
        ]
        t = Table([row], colWidths=[title_w, mid_w + gap / 2, page_w])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (1, 0), 1.5),
            ("TOPPADDING", (0, 0), (-1, -1), 7 if out else 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        out.append(t)

        # các mục con của phần này
        j = i + 1
        subs = []
        while j < len(entries) and entries[j][0] == 1:
            subs.append(entries[j][1])
            j += 1
        if subs:
            out.append(Paragraph(" · ".join(subs), desc_style))
        i = j
    return out
