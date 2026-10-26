# -*- coding: utf-8 -*-
"""c_review.py — PHẦN 5: Ôn nhanh, kế hoạch, checklist, lỗi thường gặp."""
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from layout import (S, CW, h2, h3, p, bullets, numbered, card, data_table, quote,
                    band, NAVY, GOLD, RED, TEAL, GREY_L, GREY_M, WHITE, INK, MUTED,
                    CHECK, CROSS, ARROW, STAR, WARN)


FLASH = [
    ("Lịch sử là gì?", "Toàn bộ những gì đã diễn ra trong quá khứ; tồn tại khách quan, không thể thay đổi."),
    ("Sử học là gì?", "Khoa học nghiên cứu về lịch sử — quá trình phát sinh, phát triển của xã hội loài người."),
    ("Đối tượng của Sử học?", "Toàn bộ quá trình phát triển của xã hội loài người."),
    ("Ba chức năng của Sử học?", "Khoa học – Giáo dục – Xã hội (dự báo)."),
    ("Bốn nguyên tắc của Sử học?", "Khách quan – Toàn diện – Lịch sử cụ thể – Phát triển."),
    ("Hiện thực lịch sử là gì?", "Cái đã thực sự xảy ra, khách quan, duy nhất, không thể thay đổi."),
    ("Nhận thức lịch sử là gì?", "Hiểu biết của con người về quá khứ; chủ quan, đa dạng, có thể bổ sung."),
    ("Nêu 3 đặc điểm của nhận thức lịch sử.",
     "Chủ quan; có khoảng cách với hiện thực; đa dạng và không ngừng hoàn thiện."),
    ("Vì sao nhận thức lịch sử không trùng khít quá khứ?",
     "Vì con người tiếp cận gián tiếp qua sử liệu, bằng trình độ và lập trường riêng."),
    ("Tri thức lịch sử là gì?", "Hiểu biết về quá khứ, hình thành qua học tập, trải nghiệm, nghiên cứu."),
    ("Ba vai trò của tri thức lịch sử?",
     "Nhận thức – giáo dục nhân cách – bài học kinh nghiệm (thêm: nền tảng nghề, dự báo)."),
    ("Vì sao học lịch sử suốt đời?",
     "Tri thức vô hạn; nhận thức luôn đổi mới; cuộc sống biến đổi; nhu cầu hiểu biết không dừng."),
    ("Sử liệu là gì?", "Tài liệu, hiện vật, dấu vết phản ánh quá khứ, cung cấp thông tin về lịch sử."),
    ("Bốn loại hình sử liệu?", "Chữ viết – hiện vật – hình ảnh/nghe nhìn – truyền miệng (+ sử liệu số)."),
    ("Sử liệu gốc là gì?", "Ra đời cùng thời với sự kiện, do người trực tiếp liên quan tạo ra."),
    ("Sử liệu phái sinh là gì?", "Ra đời sau, dựa trên nguồn khác (sách giáo khoa, phim, bài tổng hợp)."),
    ("Ba câu hỏi vàng đánh giá nguồn?", "Ai tạo ra? Khi nào? Vì sao (mục đích)?"),
    ("Bước 1 của quy trình thu thập – xử lí?",
     "Xác định vấn đề, mục đích, xây dựng kế hoạch."),
    ("Bước 2?", "Thu thập thông tin, sử liệu (thư viện, bảo tàng, internet, điền dã, phỏng vấn)."),
    ("Bước 3?", "Xử lí: phân loại, đánh giá độ tin cậy, đối chiếu, loại bỏ thông tin sai, tổng hợp."),
    ("Bước 4?", "Trình bày kết quả (bài viết, sản phẩm số, thuyết trình) và kiểm tra, bổ sung."),
    ("Di sản văn hoá là gì?", "Giá trị vật chất và tinh thần do con người sáng tạo, gìn giữ, truyền lại."),
    ("Di sản văn hoá gồm mấy loại?", "Hai: vật thể và phi vật thể."),
    ("Ví dụ di sản vật thể?", "Cố đô Huế, Hội An, Mỹ Sơn, Hoàng thành Thăng Long, Kim Liên."),
    ("Ví dụ di sản phi vật thể?", "Nhã nhạc cung đình Huế, Hát Xoan, Dân ca Ví – Giặm Nghệ Tĩnh."),
    ("Ba di sản thiên nhiên/hỗn hợp tiêu biểu?",
     "Vịnh Hạ Long, Phong Nha – Kẻ Bàng (thiên nhiên); Tràng An (hỗn hợp)."),
    ("Vai trò 1 của Sử học với di sản?", "Nhận diện, làm rõ nguồn gốc, niên đại, giá trị của di sản."),
    ("Vai trò 2?", "Cung cấp cơ sở khoa học để xếp hạng, lập hồ sơ di sản."),
    ("Vai trò 3?", "Tư vấn, thẩm định phương án tu bổ, trùng tu, quy hoạch bảo tồn."),
    ("Vai trò 4?", "Giáo dục, truyền thông, quảng bá — nâng cao ý thức cộng đồng."),
    ("Vai trò 5?", "Đào tạo nhân lực, hoạch định chính sách, gắn bảo tồn với phát triển."),
    ("Lịch sử – văn hoá có vai trò gì với du lịch?",
     "Tạo sản phẩm, câu chuyện, thương hiệu, chiều sâu và bản sắc cho điểm đến."),
    ("Hai tác động tích cực của du lịch?",
     "Tạo nguồn thu trùng tu; quảng bá, tạo việc làm, làm sống lại nghề truyền thống."),
    ("Hai tác động tiêu cực?", "Quá tải gây xuống cấp; thương mại hoá làm biến dạng di tích, biến đổi văn hoá."),
    ("Sáu nhóm biện pháp bảo tồn?",
     "Pháp lý – quy hoạch – kĩ thuật – giáo dục – cộng đồng – tài chính."),
    ("Bốn di sản tiêu biểu ở Nghệ An?", "Kim Liên, Ví – Giặm, Pù Mát, Truông Bồn."),
]


def story():
    st = []
    st += band("5", "ÔN NHANH & CHIẾN LƯỢC",
               "Sơ đồ tư duy · 36 flashcard · kế hoạch 5 ngày · checklist · 10 lỗi mất điểm")


    st.append(h2("A. Sơ đồ tư duy tổng kết — 3 bài trên một trang"))
    st.append(p("Đọc sơ đồ theo chiều từ trên xuống, mỗi nhánh là một “ngăn kí ức”. "
                "Khi vào phòng thi, hãy nhẩm lại đúng sơ đồ này rồi mới đi vào từng câu hỏi.", S["small"]))

    branches = [
        ("BÀI 1 · HIỆN THỰC LỊCH SỬ & NHẬN THỨC",
         [("Lịch sử", "đã diễn ra · khách quan · không thể thay đổi"),
          ("Sử học", "đối tượng: toàn bộ xã hội loài người"),
          ("3 chức năng", "Khoa học – Giáo dục – Xã hội"),
          ("4 nguyên tắc", "Khách quan · Toàn diện · Cụ thể · Phát triển"),
          ("Hiện thực LS", "một · khách quan · bất biến"),
          ("Nhận thức LS", "chủ quan · có khoảng cách · đa dạng · bổ sung được")]),
        ("BÀI 2 · TRI THỨC LỊCH SỬ & CUỘC SỐNG",
         [("Tri thức LS", "hiểu biết về quá khứ → 5 vai trò"),
          ("Học suốt đời", "vô hạn · luôn đổi mới · cuộc sống biến đổi · nhu cầu"),
          ("Sử liệu", "chữ viết · hiện vật · hình ảnh · truyền miệng · số"),
          ("Nguồn gốc", "gốc (cùng thời) / phái sinh (kể lại)"),
          ("Đánh giá", "Ai? – Khi nào? – Vì sao?"),
          ("Quy trình", "Xác định → Thu thập → Xử lí → Trình bày")]),
        ("BÀI 3 · VAI TRÒ CỦA SỬ HỌC",
         [("Di sản", "văn hoá (vật thể / phi vật thể) · thiên nhiên"),
          ("Sử học & bảo tồn", "định giá → hồ sơ → tu bổ → giáo dục → phát triển"),
          ("Sử học & du lịch", "sản phẩm · câu chuyện · thương hiệu · nhân lực"),
          ("Tác động", "+ thu, quảng bá, việc làm  /  − quá tải, thương mại hoá"),
          ("Biện pháp", "pháp lý · quy hoạch · kĩ thuật · giáo dục · cộng đồng · tài chính"),
          ("Địa phương", "Kim Liên · Ví – Giặm · Pù Mát · Truông Bồn")]),
    ]

    heads = [Paragraph(t, ParagraphStyle("bm", fontName="BVPB", fontSize=8.6, leading=11.6,
                                         textColor=WHITE, alignment=1)) for t, _ in branches]
    cols = []
    for title, items in branches:
        inner = []
        for k, v in items:
            inner.append(Paragraph(
                '<font name="BVPB" color="#16325C">%s</font><br/>'
                '<font color="#3C4658">%s</font>' % (k, v),
                ParagraphStyle("bn", fontName="BVP", fontSize=7.9, leading=11.4,
                               spaceAfter=4.5, alignment=0)))
        cols.append(inner)
    t = Table([heads, cols], colWidths=[CW / 3] * 3)
    accents = [NAVY, TEAL, colors.HexColor("#8A5B12")]
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
             ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
             ("BOX", (0, 0), (-1, -1), 0.6, GREY_M), ("INNERGRID", (0, 0), (-1, -1), 0.4, GREY_M),
             ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#FBFCFE"))]
    for i in range(3):
        style.append(("BACKGROUND", (i, 0), (i, 0), accents[i]))
    t.setStyle(TableStyle(style))
    st.append(t)
    st.append(Spacer(1, 4))

    st.append(h2("B. 36 flashcard — ôn cách quãng, mỗi lần 10 phút"))
    st.append(p("Cách dùng: gấp tờ giấy theo chiều dọc, che cột “Trả lời”, đọc câu hỏi và tự trả lời thành tiếng. "
                "Đánh dấu những câu chưa nhớ; lần sau chỉ ôn những câu đã đánh dấu.", S["small"]))
    rows = [["#", "Câu hỏi", "Trả lời"]]
    for i, (q, a) in enumerate(FLASH, 1):
        rows.append([str(i), q, a])
    st.append(data_table(rows, [10 * mm, 56 * mm, CW - 66 * mm], align_center=[0]))

    st.append(h2("C. Kế hoạch ôn 5 ngày (mỗi ngày 30–40 phút)"))
    rows = [
        ["Ngày", "Nội dung", "Sản phẩm phải có sau buổi học"],
        ["<b>Ngày 1</b>", "<b>Bài 1</b> — toàn bộ mục A, B, C, D. Vẽ sơ đồ 3 trục ra giấy A4.",
         "01 sơ đồ tay + bảng so sánh 7 tiêu chí chép lại không nhìn sách"],
        ["<b>Ngày 2</b>", "<b>Bài 2</b> — tri thức lịch sử, học suốt đời, sử liệu, quy trình 4 bước.",
         "01 sơ đồ quy trình 4 bước + bảng gốc/phái sinh"],
        ["<b>Ngày 3</b>", "<b>Bài 3</b> — di sản, vai trò của Sử học, du lịch, biện pháp bảo tồn.",
         "Bảng 5 vai trò + bảng 6 nhóm biện pháp + 4 di sản Nghệ An"],
        ["<b>Ngày 4</b>", "Làm <b>Phần 4</b>: 20 câu TN + 2 câu Đ/S (bấm giờ 25 phút). Chấm, ghi lại câu sai.",
         "Danh sách câu sai + mục kiến thức tương ứng"],
        ["<b>Ngày 5</b>", "Viết <b>câu tự luận</b> trong 15 phút; đọc bài mẫu, so dàn ý. Ôn 36 flashcard.",
         "01 bài tự luận viết tay + 36 flashcard đã trả lời được"],
        ["<b>Trước giờ thi 15 phút</b>", "Chỉ đọc: bảng đáp án nhanh, 10 lỗi mất điểm, 4 di sản Nghệ An.",
         "Tâm thế: bình tĩnh, đọc kĩ từ khoá “không đúng / ngoại trừ”"],
    ]
    st.append(data_table(rows, [26 * mm, 82 * mm, CW - 108 * mm]))

    st.append(h2("D. Checklist “tôi đã nắm” — đánh dấu khi trả lời được mà không cần mở sách"))
    checks = [
        "Phân biệt được lịch sử, Sử học, sử liệu, tri thức lịch sử.",
        "Nêu được đối tượng, ba chức năng, nhiệm vụ, bốn nguyên tắc của Sử học.",
        "So sánh được hiện thực lịch sử và nhận thức lịch sử bằng 5 tiêu chí trở lên.",
        "Giải thích được vì sao nhận thức lịch sử luôn có khoảng cách với quá khứ.",
        "Nêu được 3 vai trò của tri thức lịch sử và 4 lí do phải học lịch sử suốt đời.",
        "Phân loại được sử liệu theo loại hình và theo nguồn gốc (gốc / phái sinh).",
        "Nêu đúng thứ tự và nội dung 4 bước của quy trình thu thập – xử lí thông tin, sử liệu.",
        "Đánh giá được độ tin cậy của một nguồn bằng ba câu hỏi Ai – Khi nào – Vì sao.",
        "Phân loại được di sản văn hoá vật thể, phi vật thể và di sản thiên nhiên, có ví dụ.",
        "Kể tên được ít nhất 6 di sản của Việt Nam được UNESCO ghi danh và đúng loại.",
        "Trình bày được 5 vai trò của Sử học với bảo tồn, phát huy di sản.",
        "Giải thích được vai trò của lịch sử – văn hoá với du lịch và nêu tác động hai chiều.",
        "Nêu được 6 nhóm biện pháp bảo tồn, mỗi nhóm có một ví dụ cụ thể.",
        "Liên hệ được 4 di sản ở Nghệ An và giá trị của từng di sản.",
        "Viết được câu tự luận 3 điểm trong 15 phút, đủ 4 khối: khái niệm – vai trò – liên hệ – biện pháp.",
    ]
    rows = [["", "Nội dung cần nắm", "Tự đánh giá"]]
    for i, c in enumerate(checks, 1):
        rows.append([str(i), c, "<font name='DJ'>☐</font> Chưa  ·  <font name='DJ'>☐</font> Gần  ·  <font name='DJ'>☐</font> Chắc"])
    st.append(data_table(rows, [9 * mm, CW - 9 * mm - 44 * mm, 44 * mm], align_center=[0]))
    st.append(Spacer(1, 3))
    st.append(p("Nếu còn ô “Chưa” ở dòng 1–8: quay lại Phần 1–2. Nếu còn ở dòng 9–14: quay lại Phần 3. "
                "Nếu dòng 15 còn “Chưa”: viết lại bài tự luận thêm một lần nữa — đây là dòng ăn điểm lớn nhất.",
                S["small"]))

    st.append(h2("E. 10 lỗi khiến học sinh mất điểm oan"))
    errs = [
        ("Nhầm “lịch sử” với “Sử học”.",
         "Lịch sử = cái đã xảy ra; Sử học = khoa học nghiên cứu cái đã xảy ra."),
        ("Cho rằng hiện thực lịch sử thay đổi theo thời gian.",
         "Chỉ nhận thức thay đổi; hiện thực thì cố định."),
        ("Nói “nhận thức lịch sử chủ quan nên không đáng tin”.",
         "Chủ quan là thuộc tính; nhờ sử liệu và phương pháp, nhận thức tiến gần chân lý."),
        ("Đồng nhất truyền thuyết với hiện thực lịch sử.",
         "Truyền thuyết là một hình thức nhận thức dân gian, không phải bản ghi sự kiện."),
        ("Chọn “thu thập sử liệu” là bước đầu tiên của quy trình.",
         "Bước đầu tiên là xác định vấn đề và lập kế hoạch."),
        ("Đánh giá nguồn theo số lượt chia sẻ, hình thức đẹp.",
         "Đánh giá theo tác giả, thời gian, mục đích, khả năng đối chiếu."),
        ("Xếp Vịnh Hạ Long vào di sản văn hoá; xếp Nhã nhạc vào vật thể.",
         "Hạ Long = thiên nhiên; Nhã nhạc = phi vật thể."),
        ("Không đọc kĩ từ khoá “không đúng / ngoại trừ”.",
         "Khoanh tròn chữ KHÔNG trước khi chọn đáp án."),
        ("Câu tự luận chỉ trình bày lí thuyết, không liên hệ.",
         "Thiếu phần liên hệ là mất khoảng 1,0–1,25 điểm."),
        ("Biện pháp nêu chung chung, không có chủ thể.",
         "Mỗi biện pháp phải trả lời: ai làm, làm thế nào, kết quả gì."),
    ]
    rows = [["#", "Lỗi", "Cách sửa"]]
    for i, (e, f) in enumerate(errs, 1):
        rows.append([str(i), "<b>" + e + "</b>", f])
    st.append(data_table(rows, [9 * mm, 76 * mm, CW - 85 * mm], align_center=[0]))

    st.append(h2("F. Ba đề tự luận luyện thêm (có gợi ý hướng làm)"))
    rows = [
        ["Đề", "Gợi ý hướng làm"],
        ["<b>Đề 1.</b> Vì sao nói “tri thức lịch sử có vai trò quan trọng đối với cuộc sống của mỗi người”? "
         "Lấy ví dụ từ việc học tập của bản thân.",
         "Nêu khái niệm <font name='DJ'>→</font> 3 vai trò (nhận thức, nhân cách, bài học kinh nghiệm) <font name='DJ'>→</font> ví dụ cá nhân: chọn ngành nghề, "
         "ứng xử ở di tích, đánh giá tin tức trên mạng."],
        ["<b>Đề 2.</b> Trình bày quy trình thu thập và xử lí thông tin, sử liệu. Vận dụng để xây dựng kế hoạch "
         "tìm hiểu một di tích ở địa phương em.",
         "Nêu 4 bước (đúng thứ tự) <font name='DJ'>→</font> vận dụng cụ thể: chọn di tích, câu hỏi nghiên cứu, nguồn sẽ dùng, "
         "cách đánh giá, sản phẩm dự kiến."],
        ["<b>Đề 3.</b> Phân tích tác động của du lịch đối với công tác bảo tồn di tích lịch sử – văn hoá. "
         "Liên hệ với một điểm du lịch ở Nghệ An và đề xuất giải pháp.",
         "Bảng tích cực/tiêu cực <font name='DJ'>→</font> liên hệ (Kim Liên, Pù Mát) <font name='DJ'>→</font> giải pháp theo 6 nhóm: quy hoạch, kĩ thuật, "
         "giáo dục, cộng đồng, tài chính, pháp lý."],
    ]
    st.append(data_table(rows, [76 * mm, CW - 76 * mm]))

    st.append(card("chot", [
        Paragraph("<b>Ba câu thần chú trước khi vào phòng thi:</b>", S["small"]),
        Paragraph("1. Đọc kĩ từ khoá — <b>KHÔNG</b> nghĩa là phải tìm cái sai.", S["small"]),
        Paragraph("2. Khái niệm phải <b>đủ dấu hiệu bản chất</b>, không chọn phương án “đúng một nửa”.", S["small"]),
        Paragraph("3. Tự luận: <b>khái niệm <font name='DJ'>→</font> vai trò <font name='DJ'>→</font> liên hệ <font name='DJ'>→</font> biện pháp</b>.", S["small"]),
    ], title="Trước giờ thi"))
    return st
