# -*- coding: utf-8 -*-
"""Phần D – Tổng hợp ghi nhớ nhanh."""
from style import *
from reportlab.platypus import PageBreak


def build():
    s = []
    s += h1("D", "TỔNG HỢP GHI NHỚ NHANH", "D")
    s += [P("Đây là phần <b>“cứu cánh” trước giờ thi</b>. Nếu chỉ còn 30 phút, hãy đọc mục D. "
            "Toàn bộ ba bài được nén lại thành bảng, mẹo nhớ và danh sách bẫy – đúng những gì đề hay hỏi nhất.")]

    # ------------------------------------------------------------ D1
    s += h2("D1. Bảng tổng hợp 3 bài trong một trang", "D1")
    s += tb([
        ["Nội dung", "Bài 1", "Bài 2", "Bài 3"],
        ["<b>Khái niệm trung tâm</b>", "Hiện thực lịch sử – Nhận thức lịch sử – Sử học",
         "Tri thức lịch sử – Sử liệu", "Di sản – Bảo tồn – Du lịch"],
        ["<b>Câu hỏi cốt lõi</b>", "Lịch sử là gì? Sử học là gì?",
         "Học lịch sử để làm gì? Học như thế nào?", "Sử học có ích gì cho đời sống?"],
        ["<b>Số mục lớn</b>", "2 mục: (1) Lịch sử, hiện thực & nhận thức; (2) Sử học",
         "2 mục: (1) Tri thức lịch sử; (2) Học tập & khám phá suốt đời",
         "2 mục: (1) Sử học với di sản; (2) Sử học với du lịch"],
        ["<b>Con số phải nhớ</b>", "<b>2</b> nghĩa của lịch sử; <b>2</b> chức năng; <b>3</b> nhiệm vụ; <b>4</b> nguyên tắc",
         "<b>4</b> bước quy trình; <b>2</b> loại sử liệu (sơ cấp/thứ cấp); <b>5</b> loại hình",
         "<b>2</b> loại di sản văn hoá; <b>2</b> chiều Sử học ↔ du lịch; <b>5</b> nhóm giải pháp"],
        ["<b>Dạng câu hay ra</b>", "Định nghĩa, phân biệt, chức năng – nhiệm vụ",
         "Thứ tự bước, phân loại sử liệu, “vì sao học suốt đời”", "Vai trò, tác động hai chiều, biện pháp"],
        ["<b>Điểm trong đề</b>", "1,50", "2,75", "5,75"],
    ], widths=[1.35, 1.85, 1.85, 1.85], sp_after=8)

    # ------------------------------------------------------------ D2
    s += h2("D2. Bộ mẹo nhớ – học một lần, nhớ cả đời", "D2")
    s += [P("Mỗi mẹo dưới đây đều được xây dựng theo nguyên tắc <b>“ý – hình – âm”</b>: có ý nghĩa, có hình ảnh, "
            "có vần điệu. Đây là cách não bộ ghi nhớ hiệu quả nhất.")]

    s += tb([
        ["Nội dung cần nhớ", "Mẹo", "Cách diễn giải"],
        ["Hai nghĩa của lịch sử", "<b>“THẬT – HIỂU”</b>",
         "<b>THẬT</b> = hiện thực lịch sử (cái đã xảy ra) · <b>HIỂU</b> = nhận thức lịch sử (cái ta hiểu)"],
        ["Phân biệt hiện thực / nhận thức", "<b>“MỘT THẬT – NHIỀU HIỂU”</b>",
         "Hiện thực chỉ có <b>một</b>; nhận thức có <b>nhiều</b> cách"],
        ["Ba nhiệm vụ Sử học", "<b>“NHẬN – GIÁO – DỰ”</b>",
         "<b>Nhận</b> thức · <b>Giáo</b> dục, nêu gương · <b>Dự</b> báo"],
        ["Hai chức năng Sử học", "<b>“KHOA – XÃ”</b>",
         "<b>Khoa</b> học (nhận thức) · <b>Xã</b> hội (giáo dục)"],
        ["Bốn nguyên tắc Sử học", "<b>“KHÁCH TRUNG NHÂN TIẾN”</b>",
         "<b>Khách</b> quan · <b>Trung</b> thực · <b>Nhân</b> văn · <b>Tiến</b> bộ<br/>"
         "<i>(Khách quan là nguyên tắc quan trọng nhất)</i>"],
        ["Đối tượng Sử học", "<b>“CÁ – NHÓM – CỘNG – NƯỚC – KHU – LOÀI”</b>",
         "Cá nhân → nhóm → cộng đồng → quốc gia → khu vực → nhân loại"],
        ["Bốn bước thu thập – xử lí", "<b>“MỤC – SƯU – LỌC – MINH”</b>",
         "Lập thư <b>mục</b> · <b>Sưu</b> tầm & ghi chép · Chọn <b>lọc</b>, phân loại · Xác <b>minh</b>, đánh giá"],
        ["Hai khâu lớn", "<b>“TÌM – CHẾ”</b>",
         "<b>Tìm</b> = sưu tầm, thu thập · <b>Chế</b> = xử lí thông tin, sử liệu"],
        ["Vì sao học suốt đời", "<b>“VÔ – ĐỘNG – NĂNG – HỘI”</b>",
         "Tri thức <b>vô</b> hạn · thực tiễn <b>động</b> · phát triển <b>năng</b> lực · <b>hội</b> nhập"],
        ["Hai loại sử liệu", "<b>“SƠ – THỨ”</b> (Sơ = Số 1 = bằng chứng mạnh nhất)",
         "<b>Sơ</b> cấp: tạo ra đầu tiên, gần sự kiện nhất · <b>Thứ</b> cấp: tạo ra sau, là công trình nghiên cứu"],
        ["Năm loại hình sử liệu", "<b>“VĂN – VẬT – ẢNH – LỜI – SỐ”</b>",
         "<b>Văn</b> (thành văn) · <b>Vật</b> (hiện vật) · <b>Ảnh</b> (hình ảnh) · <b>Lời</b> (truyền khẩu) · <b>Số</b> (đa phương tiện)"],
        ["Vai trò Sử học với di sản", "<b>“XÁC – CƠ – ĐỀ”</b>",
         "<b>Xác</b> định giá trị · làm <b>cơ</b> sở khoa học · <b>Đề</b> xuất phương án bảo tồn"],
        ["Vai trò bảo tồn", "<b>“KÉO – GIỮ – TĂNG – NUÔI”</b>",
         "<b>Kéo</b> dài tuổi thọ · <b>Giữ</b> & truyền di sản phi vật thể · <b>Tăng</b> giá trị khoa học, đa dạng sinh học · <b>Nuôi</b> kinh tế địa phương"],
        ["Hai chiều Sử học ↔ du lịch", "<b>“TÀI NGUYÊN – NGUỒN LỰC”</b>",
         "Lịch sử – văn hoá cho du lịch <b>tài nguyên</b>; du lịch cho bảo tồn <b>nguồn lực</b> (tiền, người, sự quan tâm)"],
        ["Năm nhóm giải pháp bảo tồn", "<b>“NHẬN – LUẬT – KHOA – TIỀN – DÂN”</b>",
         "<b>Nhận</b> thức · <b>Luật</b> pháp · <b>Khoa</b> học – kĩ thuật · <b>Tiền</b> (nguồn lực, du lịch) · <b>Dân</b> (cộng đồng)"],
    ], widths=[1.55, 1.75, 3.2], sp_after=8)

    s += box("CÁCH DÙNG MẸO NHỚ HIỆU QUẢ", [
        "Đừng chỉ <b>đọc</b> mẹo – hãy <b>viết lại từ khoá</b> rồi tự mở rộng thành nội dung đầy đủ. "
        "Nếu mở rộng được, bạn đã hiểu; nếu không, hãy quay lại mục tương ứng.",
        "Kĩ thuật <b>1-2-3</b>: nhìn mẹo (1 giây) → nói to nội dung (2 câu) → viết ra giấy (30 giây). "
        "Lặp lại 3 lần cách nhau 1 ngày là nhớ dài hạn.",
    ], "tip")

    # ------------------------------------------------------------ D3
    s += h2("D3. Bẫy đề và từ khoá “nhận diện nhanh”", "D3")
    s += [P("Đề trắc nghiệm thường không khó về kiến thức mà khó vì <b>đánh lừa bằng một từ</b>. "
            "Bảng dưới đây tổng hợp các cặp dễ nhầm nhất.")]

    s += [caption("Bảng D.1 – Các cặp khái niệm dễ nhầm")]
    s += tb([
        ["Cặp dễ nhầm", "Phân biệt bằng một câu"],
        ["<b>Hiện thực lịch sử</b> vs <b>Nhận thức lịch sử</b>",
         "Hiện thực = <b>đã xảy ra</b>, một và bất biến. Nhận thức = <b>được hiểu/kể lại</b>, nhiều và có thể đổi."],
        ["<b>Sử liệu sơ cấp</b> vs <b>sử liệu thứ cấp</b>",
         "Sơ cấp = <b>ra đời cùng/gần thời điểm sự kiện</b>. Thứ cấp = <b>ra đời sau</b>, thường là nghiên cứu."],
        ["<b>Thu thập sử liệu</b> vs <b>Xử lí sử liệu</b>",
         "Thu thập = <b>tìm, gom, ghi chép</b>. Xử lí = <b>phân loại, đánh giá, so sánh, tổng hợp</b>."],
        ["<b>Chức năng</b> vs <b>Nhiệm vụ</b> của Sử học",
         "Chức năng = <b>2</b> (khoa học, xã hội) – “Sử học <i>làm được gì</i>”. "
         "Nhiệm vụ = <b>3</b> (nhận thức, giáo dục – nêu gương, dự báo) – “Sử học <i>phải làm gì</i>”."],
        ["<b>Bảo tồn</b> vs <b>Phát huy</b>",
         "Bảo tồn = <b>giữ, tu bổ, phục dựng</b>. Phát huy = <b>khai thác, quảng bá, đưa vào đời sống</b>."],
        ["<b>Di sản văn hoá vật thể</b> vs <b>phi vật thể</b>",
         "Vật thể = <b>sờ được</b> (đình, chùa, tháp, phố cổ). Phi vật thể = <b>sống trong cộng đồng</b> (dân ca, lễ hội, nghề)."],
        ["<b>Di sản văn hoá</b> vs <b>di sản thiên nhiên</b>",
         "Văn hoá = <b>do con người tạo ra</b>. Thiên nhiên = <b>do tự nhiên tạo ra</b>, con người bảo vệ."],
        ["<b>Du lịch tác động tới bảo tồn</b> vs <b>bảo tồn tác động tới du lịch</b>",
         "Du lịch → bảo tồn: <b>động lực, tiền, quảng bá</b>. Bảo tồn → du lịch: <b>tài nguyên, sức hút</b>."],
    ], widths=[1.9, 4.6], sp_after=8)

    s += [caption("Bảng D.2 – Từ khoá trong câu hỏi → nghĩ ngay tới")]
    s += tb([
        ["Nếu đề nói…", "Hãy nghĩ ngay tới…"],
        ["“khách quan, không phụ thuộc ý muốn con người”, “chỉ có một”, “không thể thay đổi”",
         "<b>Hiện thực lịch sử</b>"],
        ["“được trình bày, tái hiện theo nhiều cách”, “có thể thay đổi”, “không tái hiện đầy đủ”",
         "<b>Lịch sử được con người nhận thức</b>"],
        ["“khôi phục sự kiện”, “phát hiện quy luật vận động”", "<b>Chức năng khoa học</b> của Sử học"],
        ["“giáo dục tư tưởng, đạo đức”, “rút ra bài học kinh nghiệm”", "<b>Chức năng xã hội</b> của Sử học"],
        ["“cung cấp tri thức khoa học”", "<b>Nhiệm vụ nhận thức</b>"],
        ["“nêu gương”, “hướng tới giá trị tốt đẹp”", "<b>Nhiệm vụ giáo dục</b>"],
        ["“tổng kết thực tiễn”, “góp phần dự báo tương lai”", "<b>Nhiệm vụ dự báo</b>"],
        ["“dựa trên sử liệu”, “không phiến diện, một chiều”", "<b>Nguyên tắc khách quan</b>"],
        ["“không xuyên tạc, thêm bớt, làm sai lệch”", "<b>Nguyên tắc trung thực</b>"],
        ["“phục vụ cuộc sống”, “xây dựng xã hội văn minh, tiến bộ”", "<b>Nguyên tắc tiến bộ</b>"],
        ["“lập thư mục”, “danh mục nguồn sử liệu”", "<b>Bước 1</b> của quy trình"],
        ["“xác minh”, “thẩm định”, “độ tin cậy”", "<b>Bước 4</b> / khâu <b>xử lí</b> sử liệu"],
        ["“tạo ra đầu tiên”, “gắn liền thời gian sự kiện”, “bằng chứng quan trọng nhất”", "<b>Sử liệu sơ cấp</b>"],
        ["“tạo ra sau”, “công trình nghiên cứu”, “bài báo”", "<b>Sử liệu thứ cấp</b>"],
        ["“khẳng định giá trị di sản”, “cơ sở khoa học cho bảo tồn”", "<b>Vai trò của Sử học với di sản</b>"],
        ["“nguồn tài nguyên quý báu của du lịch”", "<b>Vai trò của lịch sử – văn hoá với du lịch</b>"],
        ["“doanh thu được tái đầu tư”, “thôi thúc gìn giữ”", "<b>Vai trò của du lịch với bảo tồn</b>"],
        ["“khai thác quá mức”, “thương mại hoá”, “xuống cấp”", "<b>Tác động tiêu cực của du lịch</b>"],
    ], widths=[3.9, 2.6], sp_after=8)

    # ------------------------------------------------------------ D4
    s += h2("D4. Mười lăm nhận định “Đúng – Sai” kinh điển", "D4")
    s += [P("Dạng câu Đúng/Sai trong đề là dạng <b>dễ mất điểm hàng loạt</b>: một ý sai có thể kéo cả cụm. "
            "Hãy luyện 15 nhận định dưới đây – mỗi nhận định đều nhắm vào một bẫy quen thuộc.")]
    s += tb([
        ["#", "Nhận định", "Đ/S", "Giải thích"],
        ["1", "Hiện thực lịch sử có thể thay đổi khi có thêm sử liệu mới.", "<b>S</b>",
         "Hiện thực <b>không đổi</b>; chỉ <b>nhận thức</b> thay đổi."],
        ["2", "Lịch sử được con người nhận thức luôn phản ánh đúng và đầy đủ hiện thực lịch sử.", "<b>S</b>",
         "Không bao giờ tái hiện <b>đầy đủ</b>; có thể sai lệch do chủ quan."],
        ["3", "Hiện thực lịch sử tồn tại khách quan, không phụ thuộc ý muốn con người.", "<b>Đ</b>",
         "Đúng theo định nghĩa."],
        ["4", "Sử học chỉ nghiên cứu quá khứ của các quốc gia, không nghiên cứu cá nhân.", "<b>S</b>",
         "Đối tượng gồm cả <b>cá nhân, nhóm, cộng đồng</b>."],
        ["5", "Sử học có hai chức năng cơ bản là khoa học và xã hội.", "<b>Đ</b>",
         "Khoa học (nhận thức) và xã hội (giáo dục)."],
        ["6", "Nguyên tắc khách quan là nguyên tắc quan trọng nhất của Sử học.", "<b>Đ</b>",
         "Vì sứ mệnh của Sử học là tái hiện lại hiện thực lịch sử."],
        ["7", "Trong quy trình thu thập – xử lí sử liệu, bước xác minh, đánh giá được thực hiện trước bước sưu tầm.", "<b>S</b>",
         "Phải <b>sưu tầm trước</b> rồi mới xác minh. Thứ tự: Mục – Sưu – Lọc – Minh."],
        ["8", "Sử liệu sơ cấp được coi là bằng chứng quan trọng nhất khi phục dựng quá khứ.", "<b>Đ</b>",
         "Vì ra đời gần sự kiện nhất."],
        ["9", "Thông tin trên mạng xã hội về lịch sử luôn là sử liệu đáng tin cậy.", "<b>S</b>",
         "Phải <b>kiểm chứng</b> nguồn gốc, đối chiếu nhiều nguồn."],
        ["10", "Di sản văn hoá phi vật thể dễ bị mai một hơn di sản vật thể.", "<b>Đ</b>",
         "Vì gắn với con người truyền dạy; người nắm giữ mất thì di sản mất."],
        ["11", "Nghiên cứu Sử học là cơ sở khoa học cho công tác bảo tồn di sản.", "<b>Đ</b>",
         "Sử học xác định giá trị, niên đại → bảo tồn đúng."],
        ["12", "Du lịch chỉ có tác động tích cực đến di sản.", "<b>S</b>",
         "Còn <b>tiêu cực</b>: quá tải, thương mại hoá, xâm hại di tích."],
        ["13", "Một phần doanh thu du lịch có thể được tái đầu tư cho bảo tồn di tích.", "<b>Đ</b>",
         "Đây là vai trò quan trọng của du lịch."],
        ["14", "Học tập lịch sử chỉ cần thiết ở bậc phổ thông.", "<b>S</b>",
         "Phải học <b>suốt đời</b> vì tri thức vô hạn và luôn đổi mới."],
        ["15", "Việc kết nối tri thức lịch sử vào cuộc sống chỉ có ý nghĩa với người làm nghề sử.", "<b>S</b>",
         "Có ý nghĩa với <b>mọi người</b>: hiểu hiện tại, dự báo tương lai, ứng xử văn hoá."],
    ], widths=[0.35, 3.0, 0.5, 2.65], align_center=[0, 2], sp_after=8)

    s += box("XỬ LÍ CÂU ĐÚNG/SAI TRONG 15 GIÂY", [
        "Bước 1: Xác định <b>chủ thể</b> (nói về cái gì) và <b>phạm vi</b> (“chỉ”, “luôn”, “mọi”).",
        "Bước 2: Săn <b>từ tuyệt đối</b>: “chỉ”, “luôn luôn”, “tất cả”, “duy nhất”, “không bao giờ” → "
        "nếu thấy vô lí thì đáp án thường là <b>SAI</b>.",
        "Bước 3: Kiểm tra <b>quan hệ nhân – quả</b> có bị đảo không (bẫy phổ biến nhất).",
    ], "warn")

    return s
