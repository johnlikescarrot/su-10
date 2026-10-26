# -*- coding: utf-8 -*-
"""c_l2.py — BÀI 2: Tri thức lịch sử và cuộc sống."""
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer
from layout import (S, CW, h2, h3, h4, p, bullets, numbered, card, data_table, quote,
                    band, CHECK, CROSS, ARROW, STAR, WARN)


def story():
    st = []
    st += band("2", "TRI THỨC LỊCH SỬ VÀ CUỘC SỐNG",
               "Bài 2 · Chủ đề 1: Lịch sử và Sử học · 7 câu trắc nghiệm + 1 câu đúng/sai")

    st.append(h2("A. Khung xương: 3 trục, 1 quy trình"))
    rows = [
        ["Trục", "Nội dung", "Dạng câu sẽ hỏi"],
        ["<b>1. Tri thức lịch sử và vai trò</b>",
         "Tri thức lịch sử là gì; nó giúp gì cho con người và xã hội.",
         "Nêu khái niệm, nêu vai trò (Câu 7)."],
        ["<b>2. Học tập, khám phá lịch sử suốt đời</b>",
         "Vì sao phải học suốt đời; học bằng cách nào; kết nối tri thức vào cuộc sống ra sao.",
         "Giải thích “vì sao”, nhận diện biểu hiện đúng (Câu 10, 11)."],
        ["<b>3. Sử liệu và quy trình 4 bước</b>",
         "Sử liệu là gì, phân loại, đánh giá độ tin cậy; quy trình thu thập – xử lí thông tin.",
         "Nhận biết thứ tự bước, phân loại sử liệu, đánh giá nguồn (Câu 8, 9, 12, 13 + câu Đ/S 1)."],
    ]
    st.append(data_table(rows, [46 * mm, 78 * mm, CW - 124 * mm]))

    # ---------------------------------------------------------------- tri thức
    st.append(h2("B. Tri thức lịch sử và vai trò của nó"))
    st.append(h3("1. Khái niệm"))
    st.append(p("<b>Tri thức lịch sử</b> là <b>những hiểu biết của con người về quá khứ</b> — về sự kiện, "
                "nhân vật, quá trình, quy luật và bài học lịch sử — được hình thành qua <b>học tập, "
                "trải nghiệm và nghiên cứu</b>. Tri thức lịch sử không phải “mớ sự kiện rời rạc”, mà là "
                "<b>hệ thống hiểu biết có lí lẽ</b>, giúp con người giải thích và ứng xử với thực tại."))

    st.append(h3("2. Năm vai trò (học theo cụm “Hiểu mình – Hiểu người – Làm người – Làm nghề – Dự báo”)"))
    rows = [
        ["Vai trò", "Nội dung", "Ví dụ"],
        ["<b>1. Nhận thức</b>",
         "Cơ sở để hiểu đúng về quá khứ của bản thân, gia đình, dân tộc và nhân loại; phân biệt đúng – sai "
         "trong các nguồn thông tin.",
         "Hiểu vì sao người Việt có tục thờ cúng tổ tiên."],
        ["<b>2. Giáo dục, hình thành nhân cách</b>",
         "Bồi đắp lòng yêu nước, tự hào dân tộc, tinh thần trách nhiệm, lẽ sống, lòng khoan dung.",
         "Học về các anh hùng liệt sĩ ở Truông Bồn."],
        ["<b>3. Bài học kinh nghiệm</b>",
         "Cung cấp tri thức cho hoạt động thực tiễn: giữ nước, dựng nước, quản lí xã hội, kinh doanh, ứng xử.",
         "Bài học “lấy dân làm gốc”, “đoàn kết toàn dân”."],
        ["<b>4. Nền tảng nghề nghiệp</b>",
         "Là cơ sở tri thức của nhiều ngành: du lịch, bảo tồn di sản, báo chí, giáo dục, văn hoá, xuất bản, "
         "thiết kế sáng tạo.",
         "Hướng dẫn viên du lịch di sản, cán bộ bảo tàng."],
        ["<b>5. Dự báo, định hướng</b>",
         "Từ quy luật quá khứ để dự báo xu hướng, chủ động chuẩn bị cho tương lai.",
         "Dự báo tác động của biến đổi khí hậu từ dữ liệu lịch sử khí tượng."],
    ]
    st.append(data_table(rows, [40 * mm, 78 * mm, CW - 118 * mm]))

    # ---------------------------------------------------------------- suốt đời
    st.append(h2("C. Vì sao phải học tập và khám phá lịch sử suốt đời?"))
    st.append(p("Đây là câu hỏi “vì sao” điển hình — phải trả lời bằng <b>4 lí do bản chất</b>, "
                "không trả lời bằng lí do “để thi”:"))
    st += numbered([
        "<b>Tri thức lịch sử là vô hạn và không ngừng được bổ sung.</b> Không ai, không trường học nào "
        "dạy hết lịch sử trong 12 năm.",
        "<b>Nhận thức lịch sử luôn vận động.</b> Sử liệu mới, phương pháp mới (khảo cổ, số hoá, phân tích "
        "khoa học) liên tục làm thay đổi cách hiểu cũ.",
        "<b>Cuộc sống và thế giới luôn biến đổi.</b> Mỗi vấn đề mới (dịch bệnh, biến đổi khí hậu, xung đột, "
        "chuyển đổi số) đòi hỏi nhìn lại quá khứ để tìm lời giải.",
        "<b>Nhu cầu của con người không có điểm dừng.</b> Học để hiểu mình, để ra quyết định đúng, "
        "để hội nhập và tôn trọng sự khác biệt văn hoá.",
    ])
    st.append(h3("Cách học suốt đời (biết để vận dụng, không cần thuộc)"))
    st.append(p("Đọc sách – báo – tạp chí; xem phim tài liệu; tham quan bảo tàng, di tích; sưu tầm và ghi chép; "
                "phỏng vấn nhân chứng; tham gia câu lạc bộ lịch sử; học trực tuyến, khai thác bảo tàng số, "
                "kho tư liệu số; đi du lịch có tìm hiểu văn hoá. <b>Điểm chung:</b> học ở mọi nơi, mọi lúc, "
                "gắn với trải nghiệm thật.", S["small"]))

    st.append(h3("“Kết nối tri thức lịch sử vào cuộc sống” nghĩa là gì?"))
    rows = [
        ["Mức độ", "Biểu hiện", "Ví dụ"],
        ["<b>Thấp</b>", "Ghi nhớ, kể lại sự kiện", "Kể lại diễn biến chiến dịch Điện Biên Phủ."],
        ["<b>Trung bình</b>", "Giải thích vấn đề hiện tại bằng tri thức quá khứ",
         "Giải thích vì sao làng nghề truyền thống ở quê hương mai một."],
        ["<b>Cao</b>", "Vận dụng bài học để đề xuất, hành động, ứng xử phù hợp",
         "Đề xuất phương án bảo tồn và quảng bá di tích địa phương; ứng xử văn minh tại di tích."],
    ]
    st.append(data_table(rows, [26 * mm, 66 * mm, CW - 92 * mm]))

    # ---------------------------------------------------------------- sử liệu
    st.append(h2("D. Sử liệu — “nguyên liệu thô” của mọi nhận thức lịch sử"))
    st.append(h3("1. Khái niệm"))
    st.append(p("<b>Sử liệu</b> là <b>những tài liệu, hiện vật, dấu vết… phản ánh về quá khứ</b>, cung cấp "
                "thông tin để con người nhận thức, tái hiện và nghiên cứu lịch sử. Không có sử liệu thì "
                "không có Sử học — chỉ có phỏng đoán."))

    st.append(h3("2. Phân loại theo loại hình (4 loại cơ bản + 1 loại hiện đại)"))
    rows = [
        ["Loại hình", "Gồm những gì", "Ví dụ"],
        ["<b>Chữ viết</b>", "Sách, văn bia, sắc lệnh, thư từ, nhật ký, báo chí, văn bản hành chính",
         "Bia Vĩnh Lăng, <i>Đại Việt sử ký toàn thư</i>, Châu bản triều Nguyễn"],
        ["<b>Hiện vật</b>", "Công cụ lao động, đồ dùng, vũ khí, trang sức, di tích, kiến trúc",
         "Trống đồng Đông Sơn, rìu đá Hoà Bình, gốm Bát Tràng"],
        ["<b>Hình ảnh – nghe nhìn</b>", "Tranh, ảnh, bản đồ, phim, ghi âm", "Ảnh tư liệu chiến tranh, phim tài liệu"],
        ["<b>Truyền miệng</b>", "Truyền thuyết, ca dao, dân ca, hồi ký truyền miệng, lời kể nhân chứng",
         "Sự tích Hồ Gươm, dân ca Ví – Giặm"],
        ["<b>Sử liệu số</b><br/><i>(hiện đại)</i>", "Tư liệu số hoá, cơ sở dữ liệu, bảo tàng ảo, ảnh vệ tinh",
         "Kho tư liệu số của bảo tàng, bản đồ số"],
    ]
    st.append(data_table(rows, [34 * mm, 76 * mm, CW - 110 * mm]))

    st.append(h3("3. Phân loại theo nguồn gốc — phần dễ mất điểm nhất"))
    rows = [
        ["", "<b>Sử liệu gốc</b> (sơ cấp)", "<b>Sử liệu phái sinh</b> (thứ cấp)"],
        ["Ai tạo ra", "Người <b>trực tiếp</b> chứng kiến, tham gia, hoặc tạo ra <b>cùng thời</b> với sự kiện",
         "Người <b>đi sau</b>, dựa trên sử liệu khác để kể lại, phân tích, tổng hợp"],
        ["Thời điểm", "Ra đời <b>cùng thời</b> hoặc ngay sau sự kiện", "Ra đời <b>sau</b> sự kiện, thường rất lâu"],
        ["Giá trị", "Độ tin cậy cao về sự kiện cụ thể, nhưng vẫn có thể phiến diện",
         "Có tính hệ thống, tổng hợp, dễ đọc; nhưng đã qua “lăng kính” của người kể"],
        ["Ví dụ", "Bia đá khắc năm 1433; nhật ký của người trong cuộc; ảnh chụp tại hiện trường",
         "Sách giáo khoa; bài báo tổng hợp; phim tài liệu hiện đại; bài viết trên mạng xã hội"],
    ]
    st.append(data_table(rows, [22 * mm, (CW - 22 * mm) / 2, (CW - 22 * mm) / 2], zebra=False))
    st.append(Spacer(1, 4))
    st.append(card("meo", [
        Paragraph("<b>GỐC = NGƯỜI TRONG CUỘC.</b> <b>PHÁI SINH = NGƯỜI KỂ LẠI.</b>", S["small"]),
        Paragraph("Câu hỏi dạng “nguồn nào là sử liệu gốc?” <font name='DJ'>→</font> hãy tự hỏi: <i>vật/tài liệu đó có được tạo ra "
                  "ngay tại thời điểm sự kiện, bởi người liên quan trực tiếp không?</i> Nếu là sách giáo khoa, "
                  "phim hiện đại, bài blog <font name='DJ'>→</font> <b>không phải</b> sử liệu gốc.", S["small"]),
    ], title="Mẹo phân biệt trong 5 giây"))

    st.append(h3("4. Ba câu hỏi vàng để đánh giá một nguồn sử liệu"))
    rows = [
        ["Câu hỏi", "Cần xác định", "Vì sao quan trọng"],
        ["<b>AI?</b>", "Tác giả là ai, có phải người trong cuộc, có uy tín chuyên môn không",
         "Xác định mức độ liên quan và năng lực của người tạo nguồn"],
        ["<b>KHI NÀO?</b>", "Nguồn ra đời lúc nào, cách sự kiện bao lâu",
         "Càng xa sự kiện, nguy cơ sai lệch và “tam sao thất bản” càng lớn"],
        ["<b>VÌ SAO?</b>", "Mục đích tạo nguồn: ghi chép, tuyên truyền, kiếm lợi, giải trí…",
         "Mục đích quyết định cách chọn lọc và tô đậm thông tin"],
    ]
    st.append(data_table(rows, [24 * mm, 84 * mm, CW - 108 * mm]))
    st.append(p("Ngoài ra cần kiểm tra: nguồn có <b>được công bố, lưu trữ đáng tin</b> không; "
                "thông tin có <b>đối chiếu được</b> với nguồn khác không; có <b>dấu hiệu chỉnh sửa, cắt ghép</b> không. "
                "<b>Tuyệt đối không</b> đánh giá độ tin cậy bằng số lượt thích, lượt chia sẻ hay hình thức trình bày đẹp.",
                S["small"]))

    # ---------------------------------------------------------------- quy trình
    st.append(h2("E. Quy trình 4 bước: thu thập và xử lí thông tin, sử liệu"))
    st.append(p("Đây là nội dung chắc chắn có câu hỏi (Câu 9 và câu Đ/S 1). Học theo <b>thứ tự</b> và "
                "<b>nội dung từng bước</b>."))
    rows = [
        ["Bước", "Tên bước", "Việc phải làm", "Sản phẩm"],
        ["<b>1</b>", "<b>Xác định vấn đề</b>, mục đích",
         "Chọn đề tài; đặt câu hỏi nghiên cứu; xác định phạm vi không gian – thời gian; lập kế hoạch, "
         "phân công, dự kiến phương pháp",
         "Đề cương nhiệm vụ, câu hỏi nghiên cứu"],
        ["<b>2</b>", "<b>Thu thập</b> thông tin, sử liệu",
         "Tìm ở thư viện, bảo tàng, trung tâm lưu trữ, internet, điền dã; phỏng vấn nhân chứng; ghi chép, "
         "chụp ảnh, sao lục; <b>ghi rõ nguồn</b> từng tư liệu",
         "Tập sử liệu có ghi nguồn"],
        ["<b>3</b>", "<b>Xử lí</b> thông tin, sử liệu",
         "Phân loại (loại hình, gốc/phái sinh); đánh giá độ tin cậy; đối chiếu, so sánh các nguồn; "
         "loại bỏ thông tin sai, phiến diện; tổng hợp, khái quát",
         "Bảng phân loại, nhận xét độ tin cậy"],
        ["<b>4</b>", "<b>Trình bày</b> kết quả",
         "Viết bài, làm sản phẩm số/poster/video, thuyết trình; nêu rõ nguồn; kiểm tra lại và bổ sung "
         "sau phản hồi",
         "Báo cáo, sản phẩm học tập"],
    ]
    st.append(data_table(rows, [13 * mm, 40 * mm, 78 * mm, CW - 131 * mm], align_center=[0]))
    st.append(Spacer(1, 4))
    st.append(card("meo", [
        Paragraph("<b>Bốn chữ Đ:</b> <b>ĐỊNH</b> (xác định vấn đề) <font name='DJ'>→</font> <b>ĐI</b> (thu thập) <font name='DJ'>→</font> "
                  "<b>ĐỌC – ĐÁNH GIÁ</b> (xử lí) <font name='DJ'>→</font> <b>ĐÚC KẾT</b> (trình bày).", S["small"]),
        Paragraph("Câu hỏi “bước đầu tiên là gì?” <font name='DJ'>→</font> luôn là <b>xác định vấn đề, mục đích</b>. "
                  "Câu hỏi “bước nào quan trọng nhất để loại bỏ thông tin sai?” <font name='DJ'>→</font> <b>xử lí, đánh giá sử liệu</b>.", S["small"]),
    ], title="Mẹo nhớ quy trình"))

    st.append(card("bay", [
        Paragraph("<b>Bẫy 1.</b> “Bước đầu tiên là thu thập sử liệu” <font name='DJ'>→</font> <b>Sai</b> (phải xác định vấn đề trước).", S["small"]),
        Paragraph("<b>Bẫy 2.</b> “Sử liệu càng nhiều càng tốt, không cần đánh giá” <font name='DJ'>→</font> <b>Sai</b>: "
                  "nhiều nguồn nhưng không đánh giá còn nguy hiểm hơn ít nguồn đáng tin.", S["small"]),
        Paragraph("<b>Bẫy 3.</b> “Khi hai nguồn mâu thuẫn, chọn nguồn mình thích” <font name='DJ'>→</font> <b>Sai</b>: "
                  "phải đối chiếu, so sánh bối cảnh, tìm nguồn thứ ba, ưu tiên nguồn gốc.", S["small"]),
        Paragraph("<b>Bẫy 4.</b> “Sử liệu phái sinh không có giá trị” <font name='DJ'>→</font> <b>Sai</b>: nó có giá trị tổng hợp, "
                  "hệ thống hoá — chỉ cần biết nó đã qua lăng kính người kể.", S["small"]),
    ]))

    st.append(card("chot", [
        Paragraph("Nhận thức lịch sử = <b>SỬ LIỆU</b> + <b>PHƯƠNG PHÁP</b> + <b>THÁI ĐỘ KHÁCH QUAN</b>. "
                  "Thiếu một trong ba, kết quả chỉ là ý kiến.", S["small"]),
    ], title="Chốt bài"))

    # ---------------------------------------------------------------- tự kiểm tra
    st.append(h2("G. Tự kiểm tra 6 câu"))
    rows = [
        ["Câu hỏi", "Trả lời gọn"],
        ["1. Tri thức lịch sử là gì?", "Những hiểu biết của con người về quá khứ, hình thành qua học tập, trải nghiệm, nghiên cứu."],
        ["2. Sử liệu là gì?", "Tài liệu, hiện vật, dấu vết phản ánh quá khứ, cung cấp thông tin về lịch sử."],
        ["3. Kể 4 loại hình sử liệu.", "Chữ viết – hiện vật – hình ảnh/nghe nhìn – truyền miệng (thêm: sử liệu số)."],
        ["4. Phân biệt sử liệu gốc và phái sinh.", "Gốc: cùng thời, người trong cuộc. Phái sinh: ra đời sau, dựa trên nguồn khác."],
        ["5. Nêu 4 bước của quy trình.", "Xác định vấn đề <font name='DJ'>→</font> Thu thập <font name='DJ'>→</font> Xử lí, đánh giá <font name='DJ'>→</font> Trình bày kết quả."],
        ["6. Vì sao phải học lịch sử suốt đời?", "Tri thức vô hạn, nhận thức luôn đổi mới, cuộc sống biến đổi, nhu cầu hiểu biết không dừng."],
    ]
    st.append(data_table(rows, [62 * mm, CW - 62 * mm]))
    return st
