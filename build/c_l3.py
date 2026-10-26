# -*- coding: utf-8 -*-
"""c_l3.py — BÀI 3: Vai trò của Sử học."""
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer
from layout import (S, CW, h2, h3, h4, p, bullets, numbered, card, data_table, quote,
                    band, CHECK, CROSS, ARROW, STAR, WARN)


def story():
    st = []
    st += band("3", "VAI TRÒ CỦA SỬ HỌC",
               "Bài 3 · Chủ đề 2: Vai trò của Sử học · 7 câu TN + 1 câu đúng/sai + 1 tự luận")

    st.append(h2("A. Khung xương: bài này chiếm ~40% điểm, và gần như toàn bộ điểm vận dụng"))
    rows = [
        ["Trục", "Nội dung", "Dạng câu sẽ hỏi"],
        ["<b>1. Di sản</b>", "Di sản văn hoá (vật thể / phi vật thể) và di sản thiên nhiên là gì, gồm những gì.",
         "Nhận biết, kể tên, phân loại (Câu 14, 15, 17, 18)."],
        ["<b>2. Sử học với bảo tồn</b>", "Sử học làm gì để bảo tồn và phát huy giá trị di sản.",
         "Hiểu, giải thích, nêu vai trò (Câu 16)."],
        ["<b>3. Sử học với du lịch</b>", "Vai trò của lịch sử – văn hoá với du lịch; tác động hai chiều của du lịch "
         "tới di tích; biện pháp bảo tồn.",
         "Hiểu và <b>vận dụng</b> — kể cả câu tự luận (Câu 19, 20, Đ/S 2, TL)."],
    ]
    st.append(data_table(rows, [36 * mm, 84 * mm, CW - 120 * mm]))

    # ---------------------------------------------------------------- di sản
    st.append(h2("B. Di sản văn hoá và di sản thiên nhiên"))
    st.append(h3("1. Khái niệm"))
    st += bullets([
        "<b>Di sản văn hoá</b> là hệ thống <b>giá trị vật chất và tinh thần</b> do con người sáng tạo, "
        "tích luỹ, gìn giữ và truyền lại qua các thế hệ; có giá trị lịch sử, văn hoá, khoa học, thẩm mĩ.",
        "<b>Di sản thiên nhiên</b> là những <b>giá trị tự nhiên</b> có giá trị nổi bật về cảnh quan, "
        "địa chất, địa mạo, đa dạng sinh học, được con người nhận diện và bảo vệ.",
    ])

    st.append(h3("2. Sơ đồ phân loại (vẽ đúng sơ đồ này là ăn chắc câu 14)"))
    rows = [
        ["<b>DI SẢN VĂN HOÁ</b>", "", ""],
        ["<b>Vật thể</b>", "<b>Phi vật thể</b>", "<b>Di sản thiên nhiên</b>"],
        ["• Di tích lịch sử – văn hoá<br/>• Danh lam thắng cảnh<br/>• Di vật, cổ vật<br/>• Bảo vật quốc gia",
         "• Tiếng nói, chữ viết<br/>• Tín ngưỡng, lễ hội<br/>• Nghệ thuật trình diễn<br/>• Nghề thủ công truyền thống<br/>"
         "• Tri thức dân gian, ẩm thực, trang phục",
         "• Vườn quốc gia, khu bảo tồn<br/>• Hang động, thắng cảnh tự nhiên<br/>• Khu dự trữ sinh quyển<br/>"
         "• Danh thắng địa chất, địa mạo"],
    ]
    from reportlab.platypus import Table, TableStyle
    from layout import NAVY, GOLD, GREY_L, GREY_M, WHITE
    t = Table([[Paragraph(c, S["tbl_hc"]) for c in rows[1]],
               [Paragraph(rows[2][0], S["tbl"]), Paragraph(rows[2][1], S["tbl"]), Paragraph(rows[2][2], S["tbl"])]],
              colWidths=[CW / 3] * 3)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("BACKGROUND", (0, 1), (-1, 1), GREY_L),
        ("BOX", (0, 0), (-1, -1), 0.6, GREY_M), ("INNERGRID", (0, 0), (-1, -1), 0.4, GREY_M),
    ]))
    st.append(t)
    st.append(Spacer(1, 5))

    st.append(h3("3. Di sản Việt Nam được UNESCO ghi danh (bảng tra nhanh — rất hay ra trong câu “kể tên”)"))
    rows = [
        ["Di sản", "Loại", "Năm"],
        ["Quần thể di tích Cố đô Huế", "Văn hoá thế giới (vật thể)", "1993"],
        ["Vịnh Hạ Long", "Thiên nhiên thế giới", "1994 (mở rộng 2000)"],
        ["Phố cổ Hội An", "Văn hoá thế giới (vật thể)", "1999"],
        ["Thánh địa Mỹ Sơn", "Văn hoá thế giới (vật thể)", "1999"],
        ["Vườn quốc gia Phong Nha – Kẻ Bàng", "Thiên nhiên thế giới", "2003"],
        ["Khu trung tâm Hoàng thành Thăng Long – Hà Nội", "Văn hoá thế giới", "2010"],
        ["Quần thể danh thắng Tràng An", "Hỗn hợp (văn hoá + thiên nhiên)", "2014"],
        ["Nhã nhạc cung đình Huế", "Phi vật thể đại diện của nhân loại", "2003"],
        ["Hát Xoan Phú Thọ", "Phi vật thể (cần bảo vệ khẩn cấp <font name='DJ'>→</font> đại diện)", "2011 <font name='DJ'>→</font> 2017"],
        ["Dân ca Ví, Giặm Nghệ Tĩnh", "Phi vật thể đại diện của nhân loại", "2014"],
        ["Mộc bản triều Nguyễn · Bia tiến sĩ Văn Miếu · Châu bản triều Nguyễn",
         "Di sản tư liệu (Chương trình Ký ức thế giới)", "2009 · 2011 · 2014"],
    ]
    st.append(data_table(rows, [78 * mm, 62 * mm, CW - 140 * mm], align_center=[2]))
    st.append(Spacer(1, 3))
    st.append(p("<b>Cách nhớ nhanh 4 cái tên “kinh điển”:</b> Huế – Hội An – Mỹ Sơn (văn hoá vật thể), "
                "Hạ Long – Phong Nha (thiên nhiên), Tràng An (hỗn hợp). "
                "Nhã nhạc Huế (2003) và Ví – Giặm Nghệ Tĩnh (2014) là hai di sản phi vật thể rất hay xuất hiện "
                "trong đề.", S["small"]))

    # ---------------------------------------------------------------- bảo tồn
    st.append(h2("C. Vai trò của Sử học với bảo tồn và phát huy giá trị di sản"))
    st.append(p("Học theo <b>5 vai trò, xếp từ “nhận diện” đến “phát triển”</b> — như một dây chuyền:"))
    rows = [
        ["#", "Vai trò", "Nội dung cụ thể", "Ví dụ"],
        ["<b>1</b>", "<b>Nhận diện, định giá trị</b>",
         "Nghiên cứu làm rõ <b>nguồn gốc, niên đại, giá trị lịch sử – văn hoá – khoa học – thẩm mĩ</b> của di sản. "
         "Đây là bước “định danh”: biết nó là gì, quý ở đâu.",
         "Xác định niên đại thành cổ Vinh, giá trị kiến trúc của Kinh thành Huế"],
        ["<b>2</b>", "<b>Cung cấp cơ sở khoa học cho xếp hạng, lập hồ sơ</b>",
         "Luận cứ khoa học để lập hồ sơ di tích quốc gia, quốc gia đặc biệt, hồ sơ trình UNESCO.",
         "Hồ sơ Hoàng thành Thăng Long; hồ sơ Ví – Giặm"],
        ["<b>3</b>", "<b>Tư vấn, thẩm định tu bổ – trùng tu – quy hoạch</b>",
         "Đề xuất phương án bảo tồn đúng nguyên tắc (giữ tối đa yếu tố gốc, không làm giả di sản); "
         "phản biện các phương án “tôn tạo” làm sai lệch di tích.",
         "Phục dựng điện Kính Thiên; tu bổ Ngọ Môn"],
        ["<b>4</b>", "<b>Giáo dục, truyền thông, quảng bá</b>",
         "Chuyển giá trị di sản thành bài học, câu chuyện, sản phẩm truyền thông; nâng cao ý thức và "
         "sự tham gia của cộng đồng.",
         "Giáo dục di sản trong trường học; bảo tàng ảo; tour “kể chuyện”"],
        ["<b>5</b>", "<b>Đào tạo nhân lực, hoạch định chính sách, gắn bảo tồn với phát triển</b>",
         "Đào tạo cán bộ bảo tồn, hướng dẫn viên; cung cấp luận cứ cho chính sách; biến di sản thành "
         "nguồn lực phát triển bền vững.",
         "Du lịch di sản ở Ninh Bình, Quảng Nam"],
    ]
    st.append(data_table(rows, [9 * mm, 42 * mm, 74 * mm, CW - 125 * mm], align_center=[0]))

    st.append(card("meo", [
        Paragraph("<b>Công thức 5 chữ V:</b> <b>V</b>iệc 1 – <b>V</b>ẽ bản đồ giá trị <font name='DJ'>→</font> <b>V</b>iệc 2 – "
                  "<b>V</b>ào hồ sơ xếp hạng <font name='DJ'>→</font> <b>V</b>iệc 3 – <b>V</b>á (tu bổ) đúng cách <font name='DJ'>→</font> "
                  "<b>V</b>iệc 4 – <b>V</b>ang danh (giáo dục, quảng bá) <font name='DJ'>→</font> <b>V</b>iệc 5 – "
                  "<b>V</b>ững bền (phát triển).", S["small"]),
        Paragraph("Hoặc nhớ gọn theo dây chuyền: <b>HIỂU <font name='DJ'>→</font> GHI DANH <font name='DJ'>→</font> GIỮ <font name='DJ'>→</font> GIỚI THIỆU <font name='DJ'>→</font> GẮN VỚI PHÁT TRIỂN</b>.",
                  S["small"]),
    ], title="Mẹo nhớ 5 vai trò"))

    # ---------------------------------------------------------------- du lịch
    st.append(h2("D. Sử học với sự phát triển du lịch"))
    st.append(h3("1. Du lịch văn hoá là gì?"))
    st.append(p("Là loại hình du lịch dựa trên việc <b>khai thác các giá trị văn hoá – lịch sử</b> "
                "(di tích, lễ hội, làng nghề, ẩm thực, nghệ thuật, phong tục) để tạo ra trải nghiệm cho du khách. "
                "Du lịch văn hoá là một trong những loại hình phát triển nhanh nhất thế giới, vì du khách "
                "ngày càng muốn “hiểu” chứ không chỉ “xem”."))

    st.append(h3("2. Năm đóng góp của lịch sử – văn hoá cho du lịch"))
    st += numbered([
        "<b>Tạo ra sản phẩm và tuyến, điểm du lịch đặc sắc.</b> Di tích, lễ hội, làng nghề chính là “nguyên liệu” "
        "của sản phẩm du lịch; không có di sản thì nhiều địa phương không có gì để bán.",
        "<b>Cung cấp “câu chuyện” cho điểm đến.</b> Du khách trả tiền cho <i>ý nghĩa</i>, không chỉ cho cảnh đẹp; "
        "tri thức lịch sử chính là nội dung thuyết minh, là chiều sâu của trải nghiệm.",
        "<b>Xác định giá trị để định vị thương hiệu.</b> Biết di sản của mình độc đáo ở đâu để xây dựng "
        "thương hiệu điểm đến (Huế: di sản cố đô; Ninh Bình: Tràng An – Bái Đính; Nghệ An: quê Bác – Ví Giặm).",
        "<b>Đào tạo nguồn nhân lực.</b> Hướng dẫn viên, nhà thiết kế sản phẩm, người làm du lịch cộng đồng "
        "cần tri thức lịch sử – văn hoá để làm nghề đúng.",
        "<b>Bảo tồn để phát triển bền vững.</b> Sử học giúp khai thác vừa phải, đúng giá trị, tránh "
        "“thương mại hoá” và làm biến dạng di sản.",
    ])

    st.append(h3("3. Tác động hai chiều của du lịch đến di tích (bảng phải thuộc)"))
    rows = [
        ["Tác động <b>tích cực</b>", "Tác động <b>tiêu cực</b>"],
        ["• Tạo nguồn thu để trùng tu, bảo tồn (kinh phí “tái đầu tư”)<br/>"
         "• Quảng bá hình ảnh di sản, nâng cao tự hào và ý thức bảo vệ<br/>"
         "• Tạo việc làm, sinh kế cho cộng đồng địa phương<br/>"
         "• Thúc đẩy nghiên cứu, số hoá, nâng cấp hạ tầng<br/>"
         "• Góp phần gìn giữ và làm sống lại nghề truyền thống, lễ hội",
         "• <b>Quá tải</b> khách <font name='DJ'>→</font> xuống cấp, xâm hại hiện vật, ô nhiễm, đông đúc<br/>"
         "• <b>Thương mại hoá</b>: xây mới tràn lan, “làm giả” không gian di tích<br/>"
         "• Biến đổi văn hoá bản địa, mất tính thiêng của lễ hội<br/>"
         "• Rác thải, tiếng ồn, vi phạm quy định tại di tích<br/>"
         "• Lợi ích không đến cộng đồng <font name='DJ'>→</font> xung đột, giảm động lực bảo tồn"],
    ]
    from reportlab.platypus import Table, TableStyle
    from layout import NAVY, TEAL, RED, TEAL_L, RED_L, GREY_M, WHITE
    t = Table(rows, colWidths=[CW / 2] * 2)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BACKGROUND", (0, 0), (0, -1), TEAL_L), ("BACKGROUND", (1, 0), (1, -1), RED_L),
        ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL), ("LINEBEFORE", (1, 0), (1, -1), 3, RED),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY_M),
        ("FONTSIZE", (0, 0), (-1, -1), 8.4),
    ]))
    from reportlab.lib.styles import ParagraphStyle
    conv = [[Paragraph(rows[0][0], ParagraphStyle("a", fontName="BVPB", fontSize=8.8, leading=12, textColor=TEAL)),
             Paragraph(rows[0][1], ParagraphStyle("b", fontName="BVPB", fontSize=8.8, leading=12, textColor=RED))],
            [[Paragraph(x.strip(), S["small"]) for x in rows[1][0].split("<br/>")],
             [Paragraph(x.strip().replace("• ", ""), S["small"], bulletText="•") for x in rows[1][1].split("<br/>")]]]
    conv[0] = [Paragraph("TÁC ĐỘNG TÍCH CỰC", ParagraphStyle("a", fontName="BVPB", fontSize=9, leading=12, textColor=TEAL)),
               Paragraph("TÁC ĐỘNG TIÊU CỰC", ParagraphStyle("b", fontName="BVPB", fontSize=9, leading=12, textColor=RED))]
    t = Table(conv, colWidths=[CW / 2] * 2)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BACKGROUND", (0, 0), (0, -1), TEAL_L), ("BACKGROUND", (1, 0), (1, -1), RED_L),
        ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL), ("LINEBEFORE", (1, 0), (1, -1), 3, RED),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY_M), ("LINEBELOW", (0, 0), (-1, 0), 0.5, GREY_M),
    ]))
    st.append(t)
    st.append(Spacer(1, 4))

    st.append(h3("4. Sáu nhóm biện pháp bảo tồn và phát huy di sản (dùng cho câu vận dụng)"))
    rows = [
        ["Nhóm biện pháp", "Nội dung", "Ví dụ cụ thể"],
        ["<b>1. Pháp lý – chính sách</b>", "Hoàn thiện luật, quy chế; xếp hạng, khoanh vùng bảo vệ; xử phạt nghiêm",
         "Luật Di sản văn hoá; quy chế khu di tích"],
        ["<b>2. Quy hoạch – quản lý</b>", "Quy hoạch không gian, kiểm soát xây dựng quanh di tích, "
         "giới hạn sức chứa, phân luồng khách", "Đặt giới hạn lượt khách/ngày; vùng đệm di tích"],
        ["<b>3. Khoa học – kĩ thuật</b>", "Tu bổ đúng nguyên tắc, ứng dụng công nghệ số hoá, 3D, giám sát "
         "nhiệt độ – độ ẩm, bảo quản hiện vật", "Số hoá 3D Kinh thành Huế; bảo tàng ảo"],
        ["<b>4. Giáo dục – truyền thông</b>", "Đưa di sản vào trường học; tuyên truyền, hướng dẫn ứng xử văn minh; "
         "quảng bá trên nền tảng số", "Chương trình “giáo dục di sản”; mã QR thuyết minh"],
        ["<b>5. Cộng đồng – xã hội</b>", "Phát huy vai trò cộng đồng làm chủ, hưởng lợi; gắn bảo tồn với sinh kế; "
         "khuyến khích tình nguyện viên", "Du lịch cộng đồng ở làng cổ; hợp tác xã nghề truyền thống"],
        ["<b>6. Tài chính – hợp tác</b>", "Quỹ bảo tồn, xã hội hoá, hợp tác quốc tế, tái đầu tư từ du lịch",
         "Quỹ bảo tồn di sản; tài trợ UNESCO"],
    ]
    st.append(data_table(rows, [40 * mm, 78 * mm, CW - 118 * mm]))
    st.append(Spacer(1, 3))
    st.append(p("<b>Mẹo nhớ 6 nhóm:</b> <b>LUẬT – QUY HOẠCH – KĨ THUẬT – GIÁO DỤC – CỘNG ĐỒNG – TIỀN</b>. "
                "Khi làm câu vận dụng, chỉ cần chọn 2–3 nhóm và <b>nêu chủ thể + cách làm + kết quả mong đợi</b> "
                "là bài đã đạt điểm tối đa.", S["small"]))

    # ---------------------------------------------------------------- địa phương
    st.append(h2("E. Liên hệ địa phương: Nghệ An (rất có thể vào câu tự luận)"))
    rows = [
        ["Di sản ở Nghệ An", "Loại", "Hướng khai thác – bảo tồn"],
        ["<b>Khu di tích Kim Liên</b> (Nam Đàn) — Di tích quốc gia đặc biệt, quê Chủ tịch Hồ Chí Minh",
         "Di tích lịch sử – văn hoá (vật thể)",
         "Giáo dục truyền thống; tour “về quê Bác”; số hoá tư liệu, kiểm soát lượng khách mùa cao điểm"],
        ["<b>Dân ca Ví, Giặm Nghệ Tĩnh</b> — UNESCO ghi danh 2014",
         "Di sản văn hoá phi vật thể",
         "Truyền dạy trong trường học, câu lạc bộ; biểu diễn phục vụ du lịch; ghi âm, số hoá làn điệu"],
        ["<b>Vườn quốc gia Pù Mát</b> và <b>Khu dự trữ sinh quyển miền Tây Nghệ An</b>",
         "Di sản thiên nhiên",
         "Du lịch sinh thái có kiểm soát; giáo dục môi trường; bảo vệ đa dạng sinh học"],
        ["<b>Di tích Truông Bồn</b> (Đô Lương) — nơi 13 chiến sĩ TNXP hy sinh năm 1968",
         "Di tích lịch sử (vật thể)",
         "Giáo dục lý tưởng; lễ tri ân; bảo quản hiện vật, chỉnh trang không gian tưởng niệm"],
        ["<b>Thành cổ Vinh</b>, <b>Đền Cuông</b> (Diễn Châu), <b>hang Thẩm Ồm</b> (Quỳ Châu)",
         "Di tích lịch sử – văn hoá, di chỉ khảo cổ",
         "Nghiên cứu khảo cổ; kết nối thành tuyến du lịch nội thành; chống xâm hại di tích"],
    ]
    st.append(data_table(rows, [62 * mm, 34 * mm, CW - 96 * mm]))
    st.append(Spacer(1, 3))
    st.append(p("Chỉ cần nhớ <b>4 cái tên: Kim Liên – Ví Giặm – Pù Mát – Truông Bồn</b>. Bốn cái tên này "
                "đủ để trả lời mọi câu hỏi liên hệ địa phương, ở cả dạng tự luận và trắc nghiệm.", S["small"]))

    st.append(card("thi", [
        Paragraph("<b>Công thức 3 câu cho mọi câu hỏi liên hệ (địa phương / thực tiễn):</b>", S["small"]),
        Paragraph("<b>(1) Nêu di sản + giá trị:</b> “Di tích Kim Liên là di tích quốc gia đặc biệt, gắn với "
                  "thân thế và sự nghiệp Chủ tịch Hồ Chí Minh…”.", S["small"]),
        Paragraph("<b>(2) Nêu vai trò của Sử học:</b> “Sử học nghiên cứu làm rõ giá trị, lập hồ sơ khoa học, "
                  "tư vấn tu bổ, giáo dục truyền thống…”.", S["small"]),
        Paragraph("<b>(3) Nêu việc em/cộng đồng làm:</b> cụ thể, có chủ thể — “nhà trường tổ chức học tập tại "
                  "di tích; đoàn thanh niên hướng dẫn khách; em tham gia viết bài quảng bá bằng mã QR…”.", S["small"]),
    ]))

    st.append(card("bay", [
        Paragraph("<b>Bẫy 1.</b> “Bảo tồn là giữ nguyên, không được khai thác” <font name='DJ'>→</font> <b>Sai</b>: bảo tồn phải gắn với "
                  "phát huy giá trị, nhưng khai thác phải bền vững.", S["small"]),
        Paragraph("<b>Bẫy 2.</b> Xếp Vịnh Hạ Long vào di sản <b>văn hoá</b> <font name='DJ'>→</font> <b>Sai</b>: đây là di sản <b>thiên nhiên</b>. "
                  "Tràng An mới là di sản <b>hỗn hợp</b>.", S["small"]),
        Paragraph("<b>Bẫy 3.</b> Xếp “Nhã nhạc cung đình Huế” vào di sản <b>vật thể</b> <font name='DJ'>→</font> <b>Sai</b>: phi vật thể.", S["small"]),
        Paragraph("<b>Bẫy 4.</b> Trả lời biện pháp chung chung (“cần tuyên truyền, giáo dục”) mà không nêu "
                  "<b>ai làm, làm thế nào</b> <font name='DJ'>→</font> mất điểm vận dụng.", S["small"]),
    ]))

    st.append(card("chot", [
        Paragraph("<b>Sử học không “trông coi” di sản — Sử học trả lời câu hỏi “di sản này quý ở đâu”, "
                  "và chính câu trả lời ấy là cơ sở để bảo tồn, để làm du lịch và để giáo dục.</b>", S["small"]),
    ], title="Chốt bài"))

    # ---------------------------------------------------------------- tự kiểm tra
    st.append(h2("G. Tự kiểm tra 6 câu"))
    rows = [
        ["Câu hỏi", "Trả lời gọn"],
        ["1. Di sản văn hoá gồm mấy loại?", "Hai: vật thể và phi vật thể."],
        ["2. Kể 3 di sản thiên nhiên thế giới của Việt Nam.", "Vịnh Hạ Long, Phong Nha – Kẻ Bàng (và Tràng An là hỗn hợp)."],
        ["3. Vai trò đầu tiên của Sử học với di sản?", "Nhận diện, làm rõ nguồn gốc, niên đại và giá trị của di sản."],
        ["4. Du lịch tác động tiêu cực thế nào?", "Quá tải, xuống cấp, thương mại hoá, biến dạng không gian di tích."],
        ["5. Nêu 3 nhóm biện pháp bảo tồn.", "Pháp lý – quy hoạch – kĩ thuật (hoặc giáo dục, cộng đồng, tài chính)."],
        ["6. Một di sản ở Nghệ An và giá trị của nó?", "Ví dụ: Kim Liên (giá trị lịch sử – văn hoá gắn với Hồ Chí Minh)."],
    ]
    st.append(data_table(rows, [62 * mm, CW - 62 * mm]))
    return st
