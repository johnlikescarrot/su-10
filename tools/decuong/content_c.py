# -*- coding: utf-8 -*-
"""Phần C – Chủ đề 2: Vai trò của Sử học (Bài 3)."""
from style import *
from reportlab.platypus import PageBreak


def build():
    s = []
    s += h1("C", "CHỦ ĐỀ 2 – VAI TRÒ CỦA SỬ HỌC", "C")
    s += [P("<b>Bài 3 – Vai trò của Sử học</b> là bài <b>quan trọng nhất</b> trong đề giữa học kì 1. "
            "Chỉ riêng bài này đã chiếm <b>7 câu trắc nghiệm + 1 câu Đúng/Sai + 1 câu tự luận = 5,75 điểm</b>. "
            "Cấu trúc của bài rất rõ ràng, chỉ gồm <b>hai mối quan hệ lớn</b>:")]
    s += [caption("Sơ đồ C.0 – Toàn cảnh Bài 3")]
    s += mindmap("VAI TRÒ CỦA SỬ HỌC", [
        ("SỬ HỌC ↔ DI SẢN", ["Sử học khẳng định <b>giá trị</b> di sản",
                             "Cơ sở khoa học cho <b>bảo tồn</b>",
                             "Bảo tồn: giữ gìn, tái tạo, lưu truyền",
                             "Tác động tới kinh tế – xã hội địa phương"]),
        ("SỬ HỌC ↔ DU LỊCH", ["Lịch sử – văn hoá là <b>tài nguyên</b> du lịch",
                              "Du lịch <b>quảng bá</b> di sản",
                              "Du lịch <b>tạo nguồn thu</b> tái đầu tư bảo tồn",
                              "Du lịch quá mức <b>gây hại</b> di sản"]),
    ], sub="Hai mối quan hệ đều là quan hệ <b>hai chiều</b> – hãy nhớ kĩ chữ “hai chiều”, đây là chìa khoá ăn điểm")

    # ------------------------------------------------------------ C1
    s += h2("C1. Sử học với công tác bảo tồn và phát huy giá trị di sản", "C1")

    s += h3("C1.1. Một số khái niệm phải nắm")
    s += tb([
        ["Khái niệm", "Nội dung"],
        ["<b>Di sản văn hoá</b>",
         "Là hệ thống các giá trị vật chất và tinh thần do con người sáng tạo ra, được lưu truyền từ thế hệ này sang thế hệ khác. "
         "Gồm <b>di sản văn hoá vật thể</b> và <b>di sản văn hoá phi vật thể</b>."],
        ["<b>Di sản văn hoá vật thể</b>",
         "Là những sản phẩm vật chất có giá trị lịch sử, văn hoá, khoa học, gồm <b>di tích lịch sử – văn hoá, "
         "danh lam thắng cảnh, di vật, cổ vật, bảo vật quốc gia</b>."],
        ["<b>Di sản văn hoá phi vật thể</b>",
         "Là sản phẩm tinh thần gắn với cộng đồng, cá nhân, được lưu truyền bằng <b>trí nhớ, truyền miệng, truyền nghề, "
         "trình diễn</b>… như tiếng nói, chữ viết, lối sống, lễ hội, trang phục, nghệ thuật trình diễn, tri thức dân gian, "
         "nghề thủ công truyền thống."],
        ["<b>Di sản thiên nhiên</b>",
         "Là những giá trị của tự nhiên có ý nghĩa đặc biệt về khoa học, thẩm mĩ, văn hoá – lịch sử, "
         "gồm <b>danh lam thắng cảnh, vườn quốc gia, khu bảo tồn thiên nhiên, di sản thiên nhiên thế giới</b>."],
        ["<b>Bảo tồn</b>",
         "Là hoạt động <b>giữ gìn, bảo vệ, tu bổ, phục dựng</b> để di sản không bị mai một, hư hỏng và được lưu truyền lâu dài."],
        ["<b>Phát huy giá trị</b>",
         "Là việc <b>khai thác, sử dụng, quảng bá</b> các giá trị của di sản vào đời sống (giáo dục, du lịch, văn hoá…) "
         "một cách bền vững."],
    ], widths=[1.6, 4.9], sp_after=8)

    s += h3("C1.2. Mối quan hệ giữa Sử học và công tác bảo tồn, phát huy giá trị di sản")
    s += [P("Giá trị của một di sản được thể hiện ở <b>nhiều khía cạnh</b>: lịch sử, văn hoá, kiến trúc, mĩ thuật, "
            "khoa học… <b>Việc sử dụng những phương pháp nghiên cứu của Sử học – với tư cách là một khoa học có tính "
            "liên ngành – đóng vai trò quan trọng nhất trong việc khẳng định giá trị của di sản.</b> "
            "Những kết quả nghiên cứu của Sử học là <b>cơ sở khoa học vững chắc</b> cho công tác bảo tồn và phát huy "
            "giá trị di sản.")]
    s += box("CÂU CHỐT PHẢI THUỘC NGUYÊN VĂN Ý", [
        "“Sử học <b>xác định giá trị đích thực</b> của di sản, là <b>cơ sở khoa học</b> cho công tác bảo tồn và phát huy giá trị di sản.”",
        "Ba việc Sử học làm được cho di sản: <b>(1) xác định giá trị</b> – niên đại, nguồn gốc, ý nghĩa; "
        "<b>(2) cung cấp căn cứ khoa học</b> để tu bổ, phục dựng đúng; "
        "<b>(3) đề xuất phương án bảo tồn</b> phù hợp.",
    ], "tip")

    s += [P("Sơ đồ dưới đây mô tả <b>chuỗi giá trị</b> từ nghiên cứu sử học đến bảo tồn:")]
    s += tb([
        ["Bước", "Sử học làm gì?", "Kết quả"],
        ["<b>1. Nhận diện</b>", "Xác định niên đại, nguồn gốc, chủ sở hữu, quá trình tồn tại của di sản", "Biết di sản “là gì”"],
        ["<b>2. Định giá</b>", "Đánh giá các giá trị lịch sử, văn hoá, kiến trúc, khoa học, thẩm mĩ", "Biết di sản “quý ở đâu”"],
        ["<b>3. Tư vấn</b>", "Đề xuất phương án bảo tồn, tu bổ, phục dựng phù hợp với giá trị gốc", "Biết “giữ thế nào cho đúng”"],
        ["<b>4. Phát huy</b>", "Xây dựng nội dung trưng bày, thuyết minh, quảng bá, giáo dục", "Đưa di sản vào đời sống"],
    ], widths=[1.1, 3.6, 1.8], sp_after=8)

    s += h3("C1.3. Vai trò của công tác bảo tồn và phát huy giá trị di sản")
    s += [P("Với mỗi loại hình di sản, công tác bảo tồn lại có vai trò khác nhau. Bảng dưới đây là "
            "<b>“bản đồ” để trả lời mọi câu hỏi dạng “vai trò của bảo tồn đối với…”</b>:")]
    s += tb([
        ["Loại hình di sản", "Thách thức đặt ra", "Vai trò của công tác bảo tồn"],
        ["<b>Di sản văn hoá vật thể</b><br/><font size=7.6>(thành quách, lăng tẩm, đền, tháp, cung điện, nhà cổ… xây bằng đất, đá, gạch, gỗ, tre, nứa, lá)</font>",
         "Dễ bị <b>biến dạng, xuống cấp, hư hỏng</b> theo thời gian và do tác động của tự nhiên, con người",
         "Góp phần <b>quan trọng nhất</b> trong việc <b>hạn chế và khắc phục</b> những tác động tiêu cực của điều kiện tự nhiên và của con người; "
         "<b>kéo dài tuổi thọ</b> của di sản"],
        ["<b>Di sản văn hoá phi vật thể</b><br/><font size=7.6>(lễ hội, dân ca, nghề truyền thống, tri thức dân gian…)</font>",
         "Đối mặt với nhiều <b>thách thức và nguy cơ mai một</b>; dễ mất khi người nắm giữ qua đời",
         "Nhờ các biện pháp <b>sưu tầm, lưu giữ, truyền nghề, trình diễn</b>, di sản được <b>tái tạo, giữ gìn và lưu truyền</b> từ thế hệ này sang thế hệ khác"],
        ["<b>Di sản thiên nhiên</b><br/><font size=7.6>(vịnh, hang động, vườn quốc gia, khu bảo tồn)</font>",
         "Bị khai thác quá mức, ô nhiễm, mất cân bằng sinh thái",
         "Góp phần <b>phát triển đa dạng sinh học</b>, làm <b>tăng giá trị khoa học</b> của di sản"],
        ["<b>Tất cả các loại hình</b>", "Bị mai một, mất bản sắc, bị thương mại hoá",
         "Góp phần <b>phát triển kinh tế – xã hội địa phương</b>; <b>duy trì kí ức và bản sắc cộng đồng</b>; "
         "<b>giáo dục thế hệ trẻ</b>; bảo vệ sự <b>đa dạng văn hoá</b> và <b>đa dạng sinh học</b>"],
    ], widths=[1.85, 1.85, 2.8], sp_after=6)

    s += box("MẸO NHỚ VAI TRÒ CỦA BẢO TỒN: “KÉO – GIỮ – TĂNG – NUÔI”", [
        "<b>KÉO</b> dài tuổi thọ di sản vật thể · <b>GIỮ</b> và truyền lại di sản phi vật thể · "
        "<b>TĂNG</b> giá trị khoa học, đa dạng sinh học của di sản thiên nhiên · <b>NUÔI</b> kinh tế – xã hội địa phương.",
    ], "tip")

    # ------------------------------------------------------------ C2
    s += h2("C2. Sử học với sự phát triển du lịch", "C2")

    s += h3("C2.1. Vai trò của lịch sử – văn hoá đối với sự phát triển du lịch")
    s += [P("Những giá trị về lịch sử và văn hoá của mỗi dân tộc, của toàn nhân loại là <b>nguồn tài nguyên "
            "quý báu của du lịch</b>, đặc biệt là <b>du lịch văn hoá</b>. Cụ thể:")]
    s += numlist([
        "<b>Cung cấp tài nguyên du lịch</b>: di tích, di sản, lễ hội, làng nghề, ẩm thực, kiến trúc… "
        "tạo nên các sản phẩm du lịch đặc sắc.",
        "<b>Tạo sức hút và bản sắc riêng</b> cho điểm đến: du khách đến không chỉ để ngắm cảnh mà để "
        "<b>hiểu và trải nghiệm</b> văn hoá bản địa.",
        "<b>Cung cấp tri thức</b> để quảng bá, thuyết minh, xây dựng nội dung du lịch, "
        "thúc đẩy du lịch phát triển <b>bền vững</b>.",
        "<b>Góp phần quảng bá hình ảnh đất nước</b>, con người Việt Nam ra thế giới.",
        "<b>Cung cấp bài học kinh nghiệm</b> trong tổ chức, quản lí và phát triển du lịch.",
    ])

    s += h3("C2.2. Vai trò của du lịch đối với công tác bảo tồn di tích, di sản")
    s += [P("Chiều ngược lại cũng rất quan trọng – và đây chính là nội dung của <b>câu tự luận vận dụng</b>:")]
    s += bullets([
        "<b>Thôi thúc bảo tồn:</b> nhu cầu tham quan, tìm hiểu, trải nghiệm của du khách khiến chính quyền và "
        "nhân dân địa phương <b>gìn giữ, bảo tồn, phục dựng, phát huy</b> giá trị di tích, di sản.",
        "<b>Tạo nguồn lực tài chính:</b> một phần <b>doanh thu du lịch</b> được tái đầu tư vào việc bảo tồn, "
        "tôn tạo, phục dựng và quản lí di tích, di sản.",
        "<b>Hồi sinh di sản phi vật thể:</b> các loại hình như dân ca, lễ hội, nghề truyền thống được "
        "<b>sưu tầm, nghiên cứu, phục dựng, truyền dạy</b> để phục vụ du khách.",
        "<b>Nâng cao nhận thức:</b> du khách và cộng đồng hiểu, trân trọng giá trị di sản hơn; "
        "người dân địa phương tự hào và có động lực gìn giữ.",
        "<b>Quảng bá giá trị:</b> đưa di sản đến gần công chúng trong và ngoài nước.",
    ])

    s += box("MẶT TRÁI – TÁC ĐỘNG TIÊU CỰC CỦA DU LỊCH", [
        "• <b>Khai thác quá mức</b> làm di tích xuống cấp, quá tải (sức chứa bị vượt).",
        "• <b>Thương mại hoá</b> lễ hội, biến di sản thành hàng hoá, làm mất tính thiêng và bản sắc.",
        "• <b>Xây dựng tuỳ tiện</b> quanh di tích, phá vỡ cảnh quan, không gian di sản.",
        "• <b>Ô nhiễm, rác thải, tiếng ồn</b> ảnh hưởng môi trường và đời sống cộng đồng.",
        "• <b>Xâm hại, trộm cắp cổ vật</b>, hành vi thiếu văn hoá tại di tích.",
        "→ Định hướng đúng: <b>phát triển du lịch gắn với bảo tồn</b>, kiểm soát sức chứa, chia sẻ lợi ích cho cộng đồng.",
    ], "warn")

    s += compare("Sử học – Lịch sử, văn hoá", "Du lịch", [
        ("Vai trò với bên kia", "<b>Cung cấp tài nguyên, tri thức, bản sắc</b> cho du lịch",
         "<b>Cung cấp nguồn lực, thị trường, động lực</b> để bảo tồn"),
        ("Kết quả tích cực", "Du lịch có chiều sâu văn hoá, phát triển bền vững",
         "Di sản được tu bổ, phục dựng, quảng bá, truyền dạy"),
        ("Rủi ro", "Bị “sân khấu hoá”, làm sai lệch giá trị gốc",
         "Khai thác quá mức làm di sản xuống cấp, thương mại hoá"),
        ("Giải pháp", "Nghiên cứu kĩ, xây dựng nội dung trung thực, khoa học",
         "Phát triển du lịch bền vững, gắn với bảo tồn"),
    ], wl=1.45, wr=1.45, wc=0.85)

    # ------------------------------------------------------------ C3
    s += h2("C3. Di sản Việt Nam – “vốn liếng” để làm câu hỏi liên hệ", "C3")
    s += [P("Đề thường yêu cầu <b>kể tên một số địa danh là tài nguyên du lịch</b> hoặc <b>kể tên các loại hình "
            "di sản văn hoá</b>. Dưới đây là bộ dữ liệu tối thiểu – học thuộc để “ghi điểm nhanh”.")]

    s += [caption("Bảng C.1 – Các loại hình di sản và ví dụ ở Việt Nam")]
    s += tb([
        ["Loại hình", "Ví dụ ở Việt Nam"],
        ["<b>Di sản văn hoá vật thể</b><br/><font size=7.6>(di tích lịch sử – văn hoá, danh lam thắng cảnh)</font>",
         "Quần thể di tích Cố đô Huế · Phố cổ Hội An · Thánh địa Mỹ Sơn · Hoàng thành Thăng Long · "
         "Thành nhà Hồ · Văn Miếu – Quốc Tử Giám · Dinh Độc Lập · Địa đạo Củ Chi · Cố đô Hoa Lư"],
        ["<b>Di sản văn hoá phi vật thể</b>",
         "Nhã nhạc cung đình Huế · Không gian văn hoá Cồng chiêng Tây Nguyên · Dân ca Quan họ Bắc Ninh · "
         "Ca trù · Hát Xoan Phú Thọ · Đờn ca tài tử Nam Bộ · Dân ca Ví, Giặm Nghệ Tĩnh · "
         "Tín ngưỡng thờ Mẫu Tam phủ · Hội Bài chòi · Thực hành Then · Nghệ thuật Xòe Thái"],
        ["<b>Di sản thiên nhiên</b>",
         "Vịnh Hạ Long (Quảng Ninh) · Vườn quốc gia Phong Nha – Kẻ Bàng (Quảng Bình) · "
         "Quần thể danh thắng Tràng An (Ninh Bình – di sản hỗn hợp) · Vườn quốc gia Cúc Phương · "
         "Vườn quốc gia Cát Tiên · Cao nguyên đá Đồng Văn"],
        ["<b>Tài nguyên du lịch</b><br/><font size=7.6>(địa danh nổi tiếng)</font>",
         "Hạ Long · Sa Pa · Đà Lạt · Nha Trang · Phú Quốc · Huế · Hội An · Mỹ Sơn · Tràng An · "
         "Phong Nha – Kẻ Bàng · Hà Nội · Thành phố Hồ Chí Minh · Cần Thơ"],
    ], widths=[1.75, 4.75], sp_after=6)

    s += [P("<b>Đặc biệt chú ý Nghệ An – quê hương em:</b> Di sản văn hoá phi vật thể <b>Dân ca Ví, Giặm Nghệ Tĩnh</b> "
            "được UNESCO ghi danh năm <b>2014</b>; khu di tích <b>Kim Liên – Nam Đàn</b> gắn với Chủ tịch Hồ Chí Minh; "
            "di tích <b>Đền Cuông</b>, <b>Thành cổ Vinh</b>, <b>Làng Sen</b>, <b>Núi Quyết</b>… "
            "Đây là những ví dụ rất “ăn điểm” khi làm câu liên hệ địa phương.")]

    # ------------------------------------------------------------ C4
    s += h2("C4. Biện pháp bảo tồn và phát huy giá trị di sản", "C4")
    s += [P("Đây là nội dung <b>vận dụng cao</b> – xuất hiện ở <b>câu tự luận 2,0 điểm</b> và ở các ý “d” của câu Đúng/Sai. "
            "Hãy nhớ theo <b>5 nhóm giải pháp</b> để có thể triển khai thành 5 ý khi viết:")]
    s += tb([
        ["Nhóm giải pháp", "Nội dung cụ thể"],
        ["<b>1. Nhận thức – giáo dục</b>",
         "Tuyên truyền, giáo dục trong nhà trường và cộng đồng; đưa di sản vào chương trình học; "
         "tổ chức tham quan, trải nghiệm để học sinh hiểu và yêu di sản."],
        ["<b>2. Thể chế – pháp luật</b>",
         "Thực hiện nghiêm Luật Di sản văn hoá; quy hoạch, khoanh vùng bảo vệ; "
         "xử lí nghiêm hành vi xâm hại, trộm cắp cổ vật."],
        ["<b>3. Khoa học – kĩ thuật</b>",
         "Tu bổ, tôn tạo theo đúng nguyên tắc <b>giữ tối đa giá trị gốc</b>; ứng dụng công nghệ số "
         "(số hoá, 3D, bảo tàng ảo, định vị số) để lưu giữ và quảng bá."],
        ["<b>4. Kinh tế – du lịch</b>",
         "Phát triển <b>du lịch bền vững</b>, kiểm soát sức chứa; dùng một phần doanh thu tái đầu tư bảo tồn; "
         "gắn di sản với sinh kế của người dân."],
        ["<b>5. Cộng đồng</b>",
         "Trao quyền và <b>chia sẻ lợi ích</b> cho cộng đồng địa phương; tôn vinh, hỗ trợ <b>nghệ nhân</b> truyền dạy; "
         "khuyến khích người trẻ tham gia."],
    ], widths=[1.55, 4.95], sp_after=6)
    s += box("MẸO NHỚ 5 NHÓM GIẢI PHÁP: “NHẬN – LUẬT – KHOA – TIỀN – DÂN”", [
        "<b>NHẬN</b> thức · <b>LUẬT</b> pháp · <b>KHOA</b> học – kĩ thuật · <b>TIỀN</b> (nguồn lực, du lịch) · <b>DÂN</b> (cộng đồng).",
        "Khi viết tự luận, mỗi nhóm viết 1–2 câu → tự động có 5 ý, đủ điểm tối đa.",
    ], "tip")

    s += box("TRẢ LỜI NHANH – 8 CÂU TỰ KIỂM TRA BÀI 3", [
        "1. Sử học có vai trò gì với di sản? → <b>Khẳng định giá trị, là cơ sở khoa học cho bảo tồn.</b>",
        "2. Di sản văn hoá gồm mấy loại? → <b>2</b>: vật thể và phi vật thể.",
        "3. Di sản nào dễ bị mai một nhất? → <b>Di sản văn hoá phi vật thể.</b>",
        "4. Bảo tồn di sản thiên nhiên góp phần gì? → <b>Phát triển đa dạng sinh học, tăng giá trị khoa học.</b>",
        "5. Du lịch có vai trò gì với bảo tồn? → <b>Tạo động lực, nguồn thu, quảng bá, hồi sinh di sản phi vật thể.</b>",
        "6. Mặt trái của du lịch? → <b>Khai thác quá mức, thương mại hoá, xuống cấp di tích.</b>",
        "7. Kể 3 di sản vật thể ở Việt Nam? → <b>Huế, Hội An, Mỹ Sơn</b> (hoặc Hoàng thành Thăng Long, Thành nhà Hồ).",
        "8. Kể 3 địa danh du lịch? → <b>Hạ Long, Sa Pa, Đà Lạt</b> (hoặc Phú Quốc, Nha Trang, Tràng An).",
    ], "ok")
    return s
