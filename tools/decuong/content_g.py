# -*- coding: utf-8 -*-
"""Phần G – Checklist tự kiểm tra."""
from style import *
from reportlab.platypus import PageBreak


def build():
    s = []
    s += h1("G", "CHECKLIST TỰ KIỂM TRA TRƯỚC KHI THI", "G")
    s += [P("Hãy đọc từng dòng và <b>tự đánh dấu</b> vào ô phù hợp. Nguyên tắc: chỉ đánh dấu “Hiểu & vận dụng” "
            "khi bạn có thể <b>nói lại bằng lời của mình</b> mà không nhìn tài liệu. "
            "Mọi dòng còn để trống hoặc mới ở mức “Nhớ máy móc” đều là <b>nội dung cần ôn lại</b>.")]

    s += h2("G1. Checklist kiến thức theo bài", "G1")

    rows = [["Bài", "Nội dung cần nắm", "Chưa nhớ", "Nhớ máy móc", "Hiểu & vận dụng"]]
    items = [
        ("Bài 1", [
            "Khái niệm lịch sử; hai nghĩa của lịch sử",
            "Khái niệm hiện thực lịch sử và 3 đặc điểm",
            "Khái niệm lịch sử được con người nhận thức và 4 đặc điểm",
            "Phân biệt hiện thực và nhận thức (7 tiêu chí)",
            "Vì sao cùng sự kiện có nhiều cách nhận thức",
            "Khái niệm Sử học; đối tượng nghiên cứu",
            "Hai chức năng của Sử học",
            "Ba nhiệm vụ của Sử học",
            "Bốn nguyên tắc cơ bản; nguyên tắc quan trọng nhất",
            "Ý nghĩa của việc nắm vững nguyên tắc",
        ]),
        ("Bài 2", [
            "Khái niệm tri thức lịch sử",
            "Vai trò, ý nghĩa của tri thức lịch sử",
            "Bốn lí do phải học tập lịch sử suốt đời",
            "Hai nhóm nhiệm vụ: sưu tầm – thu thập / xử lí",
            "Bốn bước của quy trình và thứ tự đúng",
            "Phân biệt sử liệu sơ cấp – thứ cấp",
            "Năm loại hình sử liệu",
            "Bản chất của việc kết nối tri thức vào cuộc sống",
            "Kĩ năng kiểm chứng thông tin trên internet",
        ]),
        ("Bài 3", [
            "Khái niệm di sản văn hoá, vật thể, phi vật thể, thiên nhiên",
            "Mối quan hệ Sử học – bảo tồn di sản",
            "Vai trò của bảo tồn với di sản vật thể",
            "Vai trò của bảo tồn với di sản phi vật thể",
            "Vai trò của bảo tồn với di sản thiên nhiên",
            "Vai trò của lịch sử – văn hoá với du lịch",
            "Vai trò của du lịch với bảo tồn",
            "Tác động tiêu cực của du lịch",
            "Năm nhóm biện pháp bảo tồn",
            "Kể tên 5 di sản vật thể, 5 phi vật thể, 3 thiên nhiên của Việt Nam",
            "Liên hệ di sản ở Nghệ An",
        ]),
    ]
    for bai, lst in items:
        for i, it in enumerate(lst):
            rows.append([Paragraph("<b>%s</b>" % bai, S["cellc"]) if i == 0 else "",
                         it, "☐", "☐", "☐"])
    t = mk_table(rows, widths=[0.62, 4.3, 0.75, 0.95, 1.0],
                 align_center=[0, 2, 3, 4], font_size=8.3)
    # gộp ô bài
    style = [("SPAN", (0, 1), (0, len(items[0][1])),),
             ("SPAN", (0, len(items[0][1]) + 1), (0, len(items[0][1]) + len(items[1][1]))),
             ("SPAN", (0, len(items[0][1]) + len(items[1][1]) + 1),
              (0, len(items[0][1]) + len(items[1][1]) + len(items[2][1]))),
             ("VALIGN", (0, 0), (0, -1), "MIDDLE"),
             ("BACKGROUND", (0, 1), (0, -1), BLUE_PALE)]
    t.setStyle(TableStyle(style))
    s += [caption("Bảng G.1 – Checklist kiến thức (đánh dấu ☐ vào cột tương ứng)"), t, Spacer(1, 8)]

    s += h2("G2. Lịch ôn tập 7 ngày", "G2")
    s += [P("Nếu bạn còn một tuần, hãy đi theo lịch dưới đây. Mỗi ngày chỉ cần <b>60 – 90 phút</b> "
            "nhưng phải <b>đều đặn</b> – hiệu quả của việc học cách quãng (spaced repetition) "
            "cao hơn nhiều so với học dồn một đêm.")]
    s += tb([
        ["Ngày", "Nội dung", "Thời lượng", "Sản phẩm cần có"],
        ["<b>Ngày 1</b>", "Đọc Phần A + mục B2 (Bài 1); học bảng so sánh và mẹo nhớ", "75 phút",
         "Tự vẽ lại sơ đồ B.1 bằng tay"],
        ["<b>Ngày 2</b>", "Làm 20 câu trắc nghiệm Bài 1 (Phần E1.1); chữa lỗi", "60 phút",
         "Danh sách các câu sai và lí do sai"],
        ["<b>Ngày 3</b>", "Học mục B3 (Bài 2); học thuộc 4 bước quy trình", "75 phút",
         "Viết lại 4 bước không nhìn tài liệu"],
        ["<b>Ngày 4</b>", "Học mục C1 – C2 (Bài 3); học bảng di sản Việt Nam", "90 phút",
         "Bảng 5 – 5 – 3 di sản tự ghi"],
        ["<b>Ngày 5</b>", "Làm đề mẫu Phần F trong 45 phút; tự chấm theo thang điểm", "90 phút",
         "Điểm số và danh sách lỗi"],
        ["<b>Ngày 6</b>", "Chữa đề; làm 8 câu Đúng/Sai; ôn bảng D.1, D.2", "75 phút",
         "Các cặp khái niệm đã phân biệt được"],
        ["<b>Ngày 7</b>", "Đọc lại Phần D + checklist G1; viết 1 bài tự luận hoàn chỉnh", "60 phút",
         "Bài tự luận viết tay đủ 3 điểm"],
    ], widths=[0.72, 3.05, 0.85, 1.98], align_center=[0, 2], sp_after=8)

    s += box("NẾU CHỈ CÒN 1 NGÀY – LỘ TRÌNH “CẤP CỨU”", [
        "<b>Buổi sáng:</b> đọc hết Phần D (bảng tổng hợp + mẹo nhớ + bẫy đề) – khoảng 30 phút.",
        "<b>Buổi chiều:</b> làm 50 câu trắc nghiệm ở Phần E, chữa ngay – khoảng 60 phút.",
        "<b>Buổi tối:</b> đọc lại 8 câu Đúng/Sai và 3 bài tự luận mẫu (Câu 4, 5, 6); "
        "viết tay dàn ý câu tự luận về biện pháp bảo tồn – 45 phút.",
        "<b>Trước khi ngủ:</b> đọc lại mẹo nhớ ở mục D2 một lần, không học thêm nội dung mới.",
    ], "warn")

    s += h2("G3. Mười câu hỏi tự vấn cuối cùng", "G3")
    s += [P("Trước khi gấp tài liệu lại, hãy tự trả lời <b>không nhìn sách</b>. "
            "Nếu trả lời trôi chảy cả mười câu, bạn đã sẵn sàng cho bài kiểm tra.")]
    qs = [
        "Hiện thực lịch sử khác nhận thức lịch sử ở ba điểm nào?",
        "Vì sao nói “không có hiện thực lịch sử thì không có nhận thức lịch sử”?",
        "Sử học có hai chức năng gì? Cho một ví dụ cho mỗi chức năng.",
        "Ba nhiệm vụ của Sử học là gì? Nhiệm vụ nào gắn với tương lai?",
        "Bốn nguyên tắc của Sử học? Nguyên tắc nào quan trọng nhất và vì sao?",
        "Bốn bước thu thập – xử lí sử liệu? Bước nào hay bị đảo lộn nhất?",
        "Sử liệu sơ cấp khác sử liệu thứ cấp ở đâu? Cho một ví dụ mỗi loại.",
        "Vì sao phải học tập lịch sử suốt đời? Nêu ba lí do.",
        "Sử học có vai trò gì với công tác bảo tồn di sản?",
        "Du lịch tác động đến di sản theo mấy chiều? Nêu cả mặt tích cực và tiêu cực.",
    ]
    for i, q in enumerate(qs, 1):
        s += [Paragraph("<b>%d.</b> %s" % (i, q),
                        ParagraphStyle("gq", parent=S["body"], fontSize=9.3,
                                       leading=13.4, leftIndent=16, bulletIndent=0,
                                       spaceAfter=4))]

    # ---- trang ghi chú + lời kết (trang riêng) ----
    s += [PageBreak()]
    s += h3("G4. Ghi chú của bạn – nơi ghi lại những chỗ hay quên")
    s += [P("Hãy dùng phần này để ghi lại những nội dung <b>bạn</b> thấy khó nhớ nhất. "
            "Viết tay sẽ giúp bạn nhớ lâu hơn đọc lại nhiều lần.")]
    for _ in range(24):
        line = Table([[""]], colWidths=[CONTENT_W], rowHeights=[22])
        line.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.4,
                                   colors.HexColor("#C9D6E8")),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        s += [line]

    s += [Spacer(1, 10)]
    s += box("LỜI KẾT", [
        "Kiến thức lịch sử không phải là một danh sách sự kiện cần nhớ, mà là <b>cách chúng ta hiểu "
        "và ứng xử với quá khứ</b>. Khi bạn hiểu vì sao một sự kiện xảy ra, vì sao người xưa làm như vậy, "
        "và bài học đó nói gì với hôm nay – thì bạn đã học lịch sử đúng cách.",
        "Chúc bạn bình tĩnh, tự tin và làm bài thật tốt.",
    ], "ok")

    s += [Spacer(1, 10)]
    s += rule(GOLD, 1.2, 2)
    s += [Paragraph("HẾT TÀI LIỆU", ParagraphStyle("end", fontName="Head-B", fontSize=9.5,
                                                   leading=13, textColor=GOLD,
                                                   alignment=TA_CENTER))]
    return s
