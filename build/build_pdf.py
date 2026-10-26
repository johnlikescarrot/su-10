# -*- coding: utf-8 -*-
"""
build_pdf.py — Dựng đề cương ôn tập giữa học kì I môn Lịch sử 10 (KNTT) thành PDF.

Chạy:  python build/build_pdf.py
Kết quả: De-cuong-on-tap-Giua-ky-1-Lich-su-10-KNTT.pdf (ở thư mục gốc repo)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, NextPageTemplate, PageBreak, Table, TableStyle)
from layout import (MyDoc, build_toc, S, CW, NAVY, NAVY_D, GOLD, INK, MUTED, GREY_M,
                    WHITE, SectionBand, band, h2, p)
from layout import keep_headings
import c_intro, c_l1, c_l2, c_l3, c_questions, c_review

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "De-cuong-on-tap-Giua-ky-1-Lich-su-10-KNTT.pdf")

PW, PH = A4
LM, RM, TM, BM = 18 * mm, 18 * mm, 24 * mm, 20 * mm
GOLD_L = colors.HexColor("#F6EEDA")
SOFT = colors.HexColor("#9DB4D4")


# ------------------------------------------------------------------ helpers
def tracked(c, x, y, text, font, size, color, track=1.6, center_width=None):
    """Vẽ chữ có giãn chữ (letter-spacing)."""
    c.setFont(font, size)
    c.setFillColor(color)
    widths = [c.stringWidth(ch, font, size) for ch in text]
    total = sum(widths) + track * (len(text) - 1)
    xx = x
    if center_width is not None:
        xx = x + (center_width - total) / 2.0
    for ch, w in zip(text, widths):
        c.drawString(xx, y, ch)
        xx += w + track


def tracked_width(c, text, font, size, track=1.6):
    return sum(c.stringWidth(ch, font, size) for ch in text) + track * (len(text) - 1)


# ------------------------------------------------------------------ cover
def draw_cover(canv, doc):
    c = canv
    SectionBand._seq = 0   # đặt lại bộ đếm bookmark ở mỗi lượt dựng
    c.saveState()
    # nền
    c.setFillColor(NAVY_D)
    c.rect(0, 0, PW, PH, stroke=0, fill=1)

    # vòng trang trí
    c.setFillColor(colors.HexColor("#17325C"))
    c.circle(PW + 40, PH - 120, 210, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#132C50"))
    c.circle(PW - 90, 70, 150, stroke=0, fill=1)

    # khung mảnh
    c.setStrokeColor(colors.HexColor("#3B5680"))
    c.setLineWidth(0.6)
    c.rect(12 * mm, 12 * mm, PW - 24 * mm, PH - 24 * mm, stroke=1, fill=0)

    x = LM
    # kicker
    tracked(c, x, PH - 62 * mm, "ĐỀ CƯƠNG ÔN TẬP", "BVPB", 10, GOLD, track=3.2)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(x, PH - 66 * mm, x + 34 * mm, PH - 66 * mm)

    # tiêu đề
    c.setFillColor(WHITE)
    c.setFont("BVPXB", 33)
    c.drawString(x, PH - 84 * mm, "GIỮA HỌC KÌ I")
    c.setFillColor(GOLD)
    c.setFont("BVPXB", 46)
    c.drawString(x, PH - 102 * mm, "LỊCH SỬ 10")

    c.setFillColor(colors.HexColor("#C9D6E8"))
    c.setFont("BVPM", 11.5)
    c.drawString(x, PH - 114 * mm, "Bám sát SGK Kết nối tri thức với cuộc sống")
    c.setFont("BVP", 10.5)
    c.setFillColor(SOFT)
    c.drawString(x, PH - 120 * mm, "Chủ đề 1: Lịch sử và Sử học  ·  Chủ đề 2: Vai trò của Sử học")

    # thẻ nội dung
    top = PH - 132 * mm
    h = 96 * mm
    c.setFillColor(WHITE)
    c.roundRect(x, top - h, PW - 2 * LM, h, 3 * mm, stroke=0, fill=1)

    tracked(c, x + 9 * mm, top - 12 * mm, "TRONG TÀI LIỆU NÀY", "BVPB", 8, GOLD, track=2.4)

    items = [
        ("01", "Bản đồ ôn tập", "Phân tích ma trận – bảng đặc tả của đề, chiến lược phân bổ thời gian"),
        ("02", "Kiến thức cốt lõi 3 bài", "Sơ đồ, bảng so sánh, mẹo nhớ và bẫy đề của Bài 1 – 2 – 3"),
        ("03", "28 lệnh hỏi + 1 tự luận", "Đầy đủ câu hỏi, đáp án, giải thích và bài làm tham khảo"),
        ("04", "Ôn nhanh & chiến lược", "36 flashcard, kế hoạch 5 ngày, checklist, 10 lỗi mất điểm"),
    ]
    yy = top - 24 * mm
    for num, title, sub in items:
        c.setFillColor(NAVY)
        c.setFont("BVPXB", 13)
        c.drawString(x + 9 * mm, yy - 1 * mm, num)
        c.setFillColor(colors.HexColor("#C08B2C"))
        c.rect(x + 9 * mm, yy - 4.4 * mm, 9 * mm, 0.8, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont("BVPSB", 10.2)
        c.drawString(x + 24 * mm, yy, title)
        c.setFillColor(MUTED)
        c.setFont("BVP", 8.4)
        c.drawString(x + 24 * mm, yy - 5.2 * mm, sub)
        yy -= 17 * mm

    # chân trang bìa
    c.setStrokeColor(colors.HexColor("#3B5680"))
    c.setLineWidth(0.6)
    c.line(x, 44 * mm, PW - LM, 44 * mm)
    c.setFillColor(WHITE)
    c.setFont("BVPSB", 9.6)
    c.drawString(x, 37 * mm, "Năm học 2026 – 2027")
    c.setFillColor(SOFT)
    c.setFont("BVP", 8.6)
    c.drawString(x, 31.5 * mm, "Thời gian làm bài: 45 phút  ·  20 câu TN + 2 câu Đ/S + 1 câu tự luận  ·  10 điểm")

    c.setFillColor(GOLD)
    c.setFont("BVPB", 8.6)
    c.drawRightString(PW - LM, 37 * mm, "LỊCH SỬ 10")
    c.setFillColor(SOFT)
    c.setFont("BVP", 8.6)
    c.drawRightString(PW - LM, 31.5 * mm, "Tài liệu ôn tập có hệ thống")
    c.restoreState()


# ------------------------------------------------------------------ body page
def draw_body(canv, doc):
    c = canv
    c.saveState()
    # header
    c.setStrokeColor(GREY_M)
    c.setLineWidth(0.5)
    c.line(LM, PH - 15 * mm, PW - RM, PH - 15 * mm)
    c.setFillColor(MUTED)
    c.setFont("BVP", 7)
    c.drawString(LM, PH - 12.6 * mm, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  LỊCH SỬ 10  ·  KNTT")
    chap = (doc.cur_chapter or "").upper()
    if chap:
        c.setFillColor(NAVY)
        c.setFont("BVPSB", 7)
        c.drawRightString(PW - RM, PH - 12.6 * mm, chap[:64])

    # footer
    c.setStrokeColor(GREY_M)
    c.setLineWidth(0.5)
    c.line(LM, 15 * mm, PW - RM, 15 * mm)
    c.setFillColor(MUTED)
    c.setFont("BVP", 7)
    c.drawString(LM, 11.2 * mm, "Bám sát SGK Lịch sử 10 – Kết nối tri thức với cuộc sống")
    c.setFillColor(NAVY)
    c.setFont("BVPB", 8.4)
    c.drawRightString(PW - RM, 11 * mm, "Trang %d" % doc.page)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.4)
    c.line(PW - RM - 13 * mm, 15 * mm, PW - RM, 15 * mm)
    c.restoreState()


# ------------------------------------------------------------------ build
def main():
    doc = MyDoc(
        OUT, pagesize=A4,
        leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
        title="Đề cương ôn tập giữa học kì I – Lịch sử 10 (KNTT)",
        author="Arena Agent",
        subject="Ôn tập giữa kì 1 Lịch sử 10 – Kết nối tri thức với cuộc sống",
        keywords="lịch sử 10, KNTT, đề cương, giữa học kì 1, sử học, di sản",
    )

    cover_frame = Frame(0, 0, PW, PH, id="cover",
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    body_frame = Frame(LM, BM, CW, PH - TM - BM, id="body",
                       leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
        PageTemplate(id="body", frames=[body_frame], onPageEnd=draw_body),
    ])

    story = []
    # trang bìa (do canvas vẽ)
    story += [Spacer(1, 1), NextPageTemplate("body"), PageBreak()]

    # mục lục
    story.append(Paragraph("MỤC LỤC", ParagraphStyle(
        "mt", fontName="BVPXB", fontSize=21, leading=26, textColor=NAVY, spaceAfter=4)))
    story.append(Paragraph("Bấm vào tên mục để nhảy tới trang tương ứng (bản PDF có mục lục liên kết).",
                           ParagraphStyle("mt2", fontName="BVPI", fontSize=8.6, leading=12,
                                          textColor=MUTED, spaceAfter=14)))
    toc = build_toc()
    story.append(toc)
    story.append(Spacer(1, 14))
    story.append(Paragraph(
        "<b>Cấu trúc tài liệu:</b> Phần 0 – phân tích đề và cách học; Phần 1, 2, 3 – kiến thức cốt lõi "
        "của ba bài; Phần 4 – toàn bộ câu hỏi kèm đáp án, giải thích và bài tự luận mẫu; "
        "Phần 5 – ôn nhanh, kế hoạch 5 ngày, checklist và các lỗi thường gặp.",
        ParagraphStyle("mt3", fontName="BVP", fontSize=8.8, leading=13.4, textColor=INK)))

    for mod in (c_intro, c_l1, c_l2, c_l3, c_questions, c_review):
        story += mod.story()

    # ---------------------------------------------------------- phụ lục
    story += band("", "PHỤ LỤC · VỀ TÀI LIỆU NÀY", "Nguồn, phương pháp biên soạn và ghi chú sử dụng")
    story.append(Spacer(1, 4))
    story.append(h2("1. Cơ sở biên soạn"))
    for t in [
        "<b>Ma trận đề và bảng đặc tả</b> đi kèm đề kiểm tra định kì giữa học kì I môn Lịch sử 10, "
        "năm học 2026–2027 (tệp <i>LS10- MTGK1-26-27-HHT.docx</i>) — quyết định cấu trúc, số lượng, "
        "dạng câu, mức độ tư duy và phạm vi kiến thức của toàn bộ đề cương.",
        "<b>Chương trình GDPT 2018 môn Lịch sử 10</b> và sách <i>Lịch sử 10 – Kết nối tri thức với cuộc sống</i>: "
        "Bài 1, Bài 2 (Chủ đề 1) và Bài 3 (Chủ đề 2).",
        "<b>Luật Di sản văn hoá</b> và danh mục di sản được UNESCO ghi danh của Việt Nam (dùng cho Phần 3).",
    ]:
        story.append(Paragraph(t, S["bullet"], bulletText="•"))

    story.append(h2("2. Nguyên tắc biên soạn"))
    for t in [
        "<b>Bám đặc tả:</b> mỗi dòng của bảng đặc tả được “dịch” thành câu hỏi và phần kiến thức tương ứng, "
        "không thêm nội dung ngoài phạm vi ba bài.",
        "<b>Ưu tiên trí nhớ dài hạn:</b> dùng sơ đồ, bảng so sánh, cụm từ khoá, mẹo nhớ, phản ví dụ và "
        "hệ thống câu hỏi tự kiểm tra theo nguyên tắc <i>truy hồi chủ động</i> (active recall) và "
        "<i>ôn cách quãng</i> (spaced repetition).",
        "<b>Đáp án có lí giải:</b> mỗi câu đều có mục “Vì sao” để học sinh hiểu bản chất và nhận ra bẫy, "
        "thay vì học vẹt đáp án.",
    ]:
        story.append(Paragraph(t, S["bullet"], bulletText="•"))

    story.append(h2("3. Ghi chú về dữ liệu đầu vào"))
    story.append(Paragraph(
        "Tệp đề gốc cung cấp ma trận và bảng đặc tả nhưng không chứa nội dung chữ của câu hỏi. "
        "Bộ câu hỏi ở Phần 4 vì vậy được biên soạn bám sát từng dòng đặc tả (số câu, đơn vị kiến thức, "
        "mức độ tư duy), kèm đáp án và giải thích. Khi có tệp đề chính thức, chỉ cần thay nội dung câu hỏi "
        "— phần kiến thức của đề cương vẫn dùng được nguyên vẹn.", S["small"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Phông chữ: Be Vietnam Pro (Google Fonts, giấy phép SIL Open Font License 1.1). "
        "Tài liệu được tạo tự động bằng ReportLab từ mã nguồn trong thư mục <i>build/</i>; "
        "chạy <i>python build/build_pdf.py</i> để dựng lại bản PDF này.", S["small"]))

    story = keep_headings(story)
    doc.multiBuild(story)
    print("OK ->", OUT)
    print("pages:", doc.page)


if __name__ == "__main__":
    main()
