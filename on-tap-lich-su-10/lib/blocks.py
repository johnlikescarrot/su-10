# -*- coding: utf-8 -*-
"""Các khối trình bày dùng lại: tiêu đề phần, hộp ghi nhớ, bảng biểu, DSL nội dung."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    CondPageBreak,
    HRFlowable,
    KeepTogether,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from .theme import (
    CONTENT_W,
    CREAM,
    GOLD,
    GOLD_LT,
    GREEN,
    GREEN_LT,
    INK,
    MUTED,
    PAPER,
    PRIMARY,
    PRIMARY_DK,
    PRIMARY_LT,
    RED,
    RED_LT,
    RULE,
    RULE_LT,
    STYLES,
    WHITE,
)

BOX_KINDS = {
    "def": (PRIMARY_LT, PRIMARY, PRIMARY_DK),
    "memo": (GOLD_LT, GOLD, colors.HexColor("#7A5312")),
    "trap": (RED_LT, RED, colors.HexColor("#7A2A20")),
    "tip": (GREEN_LT, GREEN, colors.HexColor("#245038")),
    "example": (PAPER, colors.HexColor("#A79C86"), colors.HexColor("#5C5245")),
}


# --------------------------------------------------------------------- khối lẻ
def banner(kicker: str, title: str) -> Paragraph:
    """Dải tiêu đề phần: nền xanh đậm, vạch vàng bên trái.

    Trả về một Paragraph (không phải Table) để afterFlowable của khuôn trang có thể
    bắt được tiêu đề và đưa vào mục lục/dấu trang PDF.
    """
    text = (
        f'<font name="Sans-Bold" size="7.4" color="#D9BE84">{kicker.upper()}</font>'
        f'<br/><font name="Sans-Bold" color="#C9A227">▌</font> '
        f'<font name="Sans-Bold" size="13.8" color="#FFFFFF">{title}</font>'
    )
    return Paragraph(text, STYLES["PartHeading"])


def rule(color=RULE, thickness=0.6, space_before=2, space_after=6, width="100%"):
    return HRFlowable(
        width=width, thickness=thickness, color=color,
        spaceBefore=space_before, spaceAfter=space_after, lineCap="butt",
    )


def callout(kind: str, title: str, items) -> Table:
    """Hộp ghi nhớ / định nghĩa / bẫy / ví dụ."""
    bg, line, title_color = BOX_KINDS[kind]
    flow = []
    if title:
        st = ParagraphStyle(
            f"boxtitle-{kind}", fontName="Sans-Bold", fontSize=8.7, leading=11.6,
            textColor=title_color, spaceAfter=2.4,
        )
        flow.append(Paragraph(title.upper(), st))
    flow.extend(_render(items, box=True))
    t = Table([[flow]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, 0), 3, line),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    # Hộp ngắn thì giữ nguyên khối để không bị cắt đôi giữa hai trang.
    try:
        if t.wrap(CONTENT_W, 10000)[1] <= 150 * mm:
            return KeepTogether([t])
    except Exception:
        pass
    return t


def _cell(content, style_name="cell", center=False):
    if isinstance(content, Paragraph):
        return content
    text = str(content).replace("\n", "<br/>")
    return Paragraph(text, STYLES[style_name])


def data_table(header, rows, widths_mm, *, zebra=True, header_bg=PRIMARY,
               font_size=8.5, align_center_cols=(), first_col_bold=False,
               caption=None, keep=True):
    """Bảng dữ liệu có tiêu đề, kẻ mảnh, sọc xen kẽ."""
    style_cell = ParagraphStyle(
        "tc", fontName="Body", fontSize=font_size, leading=font_size * 1.36,
        textColor=INK, alignment=TA_LEFT,
    )
    style_cell_c = ParagraphStyle("tcc", parent=style_cell, alignment=TA_CENTER)
    style_cell_b = ParagraphStyle("tcb", parent=style_cell, fontName="Body-Bold")
    style_head = ParagraphStyle(
        "th", fontName="Sans-Bold", fontSize=font_size - 0.1, leading=(font_size - 0.1) * 1.33,
        textColor=WHITE, alignment=TA_LEFT,
    )
    style_head_c = ParagraphStyle("thc", parent=style_head, alignment=TA_CENTER)

    head_cells = []
    for j, h in enumerate(header):
        st = style_head_c if j in align_center_cols else style_head
        head_cells.append(Paragraph(str(h), st))
    data = [head_cells]
    for r in rows:
        line = []
        for j, c in enumerate(r):
            if isinstance(c, Paragraph):
                line.append(c)
                continue
            if j in align_center_cols:
                st = style_cell_c
            elif first_col_bold and j == 0:
                st = style_cell_b
            else:
                st = style_cell
            line.append(Paragraph(str(c).replace("\n", "<br/>"), st))
        data.append(line)

    widths = [w * mm for w in widths_mm]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE_LT),
        ("BOX", (0, 0), (-1, -1), 0.5, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, PRIMARY_DK),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F8F5EE")))
    t.setStyle(TableStyle(cmds))
    out = []
    if keep:
        out.append(KeepTogether([t]) if len(data) <= 6 else t)
    else:
        out.append(t)
    if caption:
        out.append(Paragraph(caption, STYLES["caption"]))
    else:
        out.append(Spacer(1, 5))
    return out


def exam_head(title, subtitle, meta_rows, note=None):
    """Khối tiêu đề của đề kiểm tra."""
    box = []
    tstyle = ParagraphStyle(
        "eht", fontName="Sans-Bold", fontSize=12.4, leading=16,
        textColor=PRIMARY_DK, alignment=TA_CENTER, spaceAfter=1.6,
    )
    sstyle = ParagraphStyle(
        "ehs", fontName="Body-Italic", fontSize=9.2, leading=12.6,
        textColor=MUTED, alignment=TA_CENTER, spaceAfter=6,
    )
    box.append(Paragraph(title, tstyle))
    box.append(Paragraph(subtitle, sstyle))
    if meta_rows:
        rows = [[Paragraph(k, ParagraphStyle("ehk", fontName="Sans-Bold", fontSize=8.2,
                                             leading=11, textColor=PRIMARY)),
                 Paragraph(v, ParagraphStyle("ehv", fontName="Body", fontSize=8.4,
                                             leading=11.4, textColor=INK))]
                for k, v in meta_rows]
        mt = Table(rows, colWidths=[30 * mm, CONTENT_W - 44 * mm])
        mt.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2.2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
            ("LINEBELOW", (0, 0), (-1, -2), 0.3, RULE_LT),
        ]))
        box.append(mt)
    if note:
        box.append(Spacer(1, 4))
        box.append(Paragraph(note, ParagraphStyle(
            "ehn", fontName="Body-Italic", fontSize=8.4, leading=11.8, textColor=MUTED)))
    t = Table([[box]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6F2E8")),
        ("BOX", (0, 0), (-1, -1), 0.9, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t


# ------------------------------------------------------------------------ DSL
def _render(items, box=False):
    """Chuyển danh sách mô tả nội dung thành flowable.

    Tiêu đề (h2/h3/h4) được gom với khối nội dung ngay sau nó để không bị lạc
    ở cuối trang — ReportLab không tự gom tiêu đề với bảng đã nằm trong
    KeepTogether, nên việc gom được làm ngay ở đây.
    """
    out = []
    pending = []

    def _height(flowable, limit_mm=196):
        """Chiều cao ước tính (pt) của một flowable, kể cả KeepTogether."""
        if isinstance(flowable, KeepTogether):
            return sum(_height(f) for f in flowable._content)
        try:
            return flowable.wrap(CONTENT_W, limit_mm * mm)[1]
        except Exception:
            return limit_mm * mm + 1

    def too_tall(flowable, limit_mm=196):
        return _height(flowable, limit_mm) > limit_mm * mm

    def emit(flowable):
        if isinstance(flowable, list):
            for f in flowable:
                emit(f)
            return
        if pending:
            heads = list(pending)
            pending.clear()
            if isinstance(flowable, KeepTogether) and not too_tall(flowable):
                out.append(KeepTogether(heads + list(flowable._content)))
                return
            if isinstance(flowable, Paragraph) or isinstance(flowable, Table):
                if not too_tall(flowable):
                    out.append(KeepTogether(heads + [flowable]))
                    return
            out.extend(heads)
        out.append(flowable)

    for it in items:
        kind = it[0]
        if kind == "p":
            emit(Paragraph(it[1], STYLES["box_body"] if box else STYLES["body"]))
        elif kind == "lead":
            emit(Paragraph(it[1], STYLES["lead"]))
        elif kind == "h2":
            para = Paragraph(it[1], STYLES["h2"])
            if len(it) > 2:
                para._toc_key = it[2]
            pending.append(para)
        elif kind == "h3":
            pending.append(Paragraph(it[1], STYLES["h3"]))
        elif kind == "h4":
            pending.append(Paragraph(it[1], STYLES["h4"]))
        elif kind == "bul":
            st = "box_bullet" if box else "bullet"
            for line in it[1]:
                emit(Paragraph(line, STYLES[st], bulletText="•"))
        elif kind == "num":
            for i, line in enumerate(it[1], 1):
                emit(Paragraph(line, STYLES["num"], bulletText=f"{i}."))
        elif kind == "dash":
            for line in it[1]:
                emit(Paragraph(line, STYLES["box_bullet" if box else "bullet"], bulletText="–"))
        elif kind == "box":
            emit(callout(it[1], it[2], it[3]))
            out.append(Spacer(1, 6))
        elif kind == "tbl":
            opts = it[3] if len(it) > 3 and it[3] else {}
            for f in data_table(*it[1], **opts):
                emit(f)
        elif kind == "small":
            emit(Paragraph(it[1], STYLES["small"]))
        elif kind == "note":
            emit(Paragraph(it[1], STYLES["note"]))
        elif kind == "sp":
            out.append(Spacer(1, it[1]))
        elif kind == "rule":
            out.append(rule())
        elif kind == "pb":
            from reportlab.platypus import PageBreak
            out.append(PageBreak())
        elif kind == "keep":
            emit(KeepTogether(_render(it[1], box=box)))
        elif kind == "cond":
            emit(CondPageBreak(it[1] * mm))
        elif kind == "raw":
            emit(it[1])
        elif kind == "q":
            emit(Paragraph(it[1], STYLES["q"]))
        elif kind == "opts":
            for letter, text in zip("ABCD", it[1]):
                emit(Paragraph(f"<b>{letter}.</b>&nbsp;{text}", STYLES["opt"]))
            out.append(Spacer(1, 2.2))
        elif kind == "stmt":
            for letter, text in it[1]:
                emit(Paragraph(f"<b>{letter})</b>&nbsp;{text}", STYLES["opt"]))
            out.append(Spacer(1, 2.2))
        elif kind == "examhead":
            emit(exam_head(*it[1]))
        elif kind == "qgroup":
            emit(Paragraph(it[1], STYLES["qgroup"]))
        elif kind == "banner":
            para = banner(it[1], it[2])
            if len(it) > 3:
                para._toc_key = it[3]
            emit(para)
            out.append(Spacer(1, 7))
        else:  # pragma: no cover
            raise ValueError(f"Kiểu khối không hợp lệ: {kind}")

    out.extend(pending)
    return out


def render(items, box=False):
    return _render(items, box=box)


def cover_flow():
    """Nội dung chữ của trang bìa (nền do canvas vẽ)."""
    from .theme import STYLES as S

    flow = [Spacer(1, 9 * mm)]
    flow.append(Paragraph("TÀI LIỆU ÔN TẬP NỘI BỘ · LỚP 10", S["cover_kicker"]))
    flow.append(Spacer(1, 4 * mm))
    flow.append(HRFlowable(width=36 * mm, thickness=1.1, color=GOLD,
                           spaceBefore=0, spaceAfter=0, hAlign="CENTER"))
    flow.append(Spacer(1, 7 * mm))
    flow.append(Paragraph("ĐỀ CƯƠNG ÔN TẬP", S["cover_title"]))
    flow.append(Spacer(1, 1 * mm))
    flow.append(Paragraph("GIỮA HỌC KÌ I", S["cover_title"]))
    flow.append(Spacer(1, 3 * mm))
    flow.append(Paragraph("LỊCH SỬ 10", S["cover_title2"]))
    flow.append(Spacer(1, 4 * mm))
    flow.append(Paragraph("Bộ sách Kết nối tri thức với cuộc sống", S["cover_sub"]))
    flow.append(Spacer(1, 7 * mm))

    info = [
        ["Năm học", "2026 – 2027"],
        ["Phạm vi", "Chủ đề 1 (Bài 1, Bài 2) và Chủ đề 2 (Bài 3)"],
        ["Hình thức", "20 câu trắc nghiệm nhiều lựa chọn + 2 câu trắc nghiệm đúng/sai (4 ý/câu) + 1 câu tự luận"],
        ["Thời gian", "45 phút · Thang điểm 10"],
        ["Căn cứ biên soạn", "Ma trận kiểm tra định kì và Bảng đặc tả ma trận đề trong tệp\nLS10- MTGK1-26-27-HHT.docx"],
    ]
    rows = [[Paragraph(k, S["cover_meta_b"]), Paragraph(v, S["cover_meta"])] for k, v in info]
    t = Table(rows, colWidths=[38 * mm, CONTENT_W - 58 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE_LT),
        ("LINEABOVE", (0, 0), (-1, 0), 0.9, GOLD),
    ]))
    holder = Table([["", t]], colWidths=[14 * mm, CONTENT_W - 14 * mm])
    holder.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    flow.append(holder)
    flow.append(Spacer(1, 8 * mm))

    inner_title = ParagraphStyle(
        "coverinner", fontName="Sans-Bold", fontSize=8.2, leading=11,
        textColor=GOLD, spaceAfter=3.2,
    )
    inner_item = ParagraphStyle(
        "coveritem", fontName="Body", fontSize=8.9, leading=13.2,
        textColor=INK, leftIndent=10, bulletIndent=0, spaceAfter=1.6,
    )
    flow.append(Paragraph("NỘI DUNG CHÍNH", inner_title))
    for line in [
        "Hệ thống kiến thức ba bài, biên soạn theo yêu cầu cần đạt của bản đặc tả.",
        "Bảng tổng hợp ghi nhớ nhanh, mẹo nhớ và các bẫy thường gặp.",
        "Kĩ năng làm bài và chiến lược phân bổ 45 phút.",
        "Đề kiểm tra tham khảo đủ 20 câu + 2 câu đúng/sai + 1 tự luận, kèm đáp án, giải thích và biểu điểm.",
        "30 câu tự kiểm tra, kế hoạch ôn tập 7 ngày và checklist trước khi thi.",
    ]:
        flow.append(Paragraph(line, inner_item, bulletText="▪"))
    flow.append(Spacer(1, 7 * mm))

    quick_title = ParagraphStyle(
        "coverquick", fontName="Sans-Bold", fontSize=8.2, leading=11,
        textColor=PRIMARY, spaceAfter=3,
    )
    quick_body = ParagraphStyle(
        "coverqb", fontName="Body", fontSize=8.6, leading=12.6,
        textColor=INK, leftIndent=10, bulletIndent=0, spaceAfter=1.4,
    )
    flow.append(Paragraph("DÙNG NHANH", quick_title))
    for line in [
        "<b>Muốn biết đề hỏi gì:</b> đọc Phần I (ma trận, trọng số) rồi Phần V (bảng tra nhanh).",
        "<b>Muốn học bài:</b> đọc Phần II, III, IV; mỗi mục có hộp định nghĩa, bảng so sánh và mẹo nhớ.",
        "<b>Muốn luyện:</b> làm Phần VII trong 45 phút, chấm bằng Phần VIII, ôn lại theo Phần IX và X.",
    ]:
        flow.append(Paragraph(line, quick_body, bulletText="▪"))

    flow.append(Spacer(1, 16 * mm))
    return flow
