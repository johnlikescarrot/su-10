# -*- coding: utf-8 -*-
"""Phần E – Ngân hàng câu hỏi có đáp án."""
from style import *
from reportlab.platypus import PageBreak


# (đề, [4 phương án], đáp án)
BAI1 = [
    ("Lịch sử được hiểu theo mấy nghĩa cơ bản?",
     ["Một nghĩa", "Hai nghĩa", "Ba nghĩa", "Bốn nghĩa"], "B"),
    ("Hiện thực lịch sử là gì?",
     ["Những hiểu biết của con người về quá khứ",
      "Toàn bộ những gì đã diễn ra trong quá khứ, tồn tại khách quan, không phụ thuộc vào ý muốn chủ quan của con người",
      "Những câu chuyện về quá khứ được kể lại",
      "Các công trình nghiên cứu về quá khứ"], "B"),
    ("Đặc điểm nào sau đây <b>KHÔNG</b> đúng với hiện thực lịch sử?",
     ["Chỉ có một và không thể thay đổi",
      "Tồn tại khách quan, độc lập với ý muốn của con người",
      "Có thể thay đổi khi con người phát hiện thêm sử liệu",
      "Đã diễn ra trong quá khứ"], "C"),
    ("“Lịch sử được con người nhận thức” là",
     ["toàn bộ những gì đã diễn ra trong quá khứ",
      "những hiểu biết của con người về hiện thực lịch sử, được trình bày, tái hiện theo những cách khác nhau",
      "những văn bản ghi chép về quá khứ do nhà nước ban hành",
      "những hiện vật còn lại của người xưa"], "B"),
    ("So với hiện thực lịch sử, lịch sử được con người nhận thức có đặc điểm nào?",
     ["Luôn phản ánh đúng và đầy đủ hiện thực lịch sử",
      "Tồn tại độc lập, khách quan với hiện thực lịch sử",
      "Không thể tái hiện đầy đủ hiện thực lịch sử",
      "Không thể thay đổi theo thời gian"], "C"),
    ("Vì sao cùng một sự kiện lịch sử lại có nhiều cách nhận thức khác nhau?",
     ["Vì hiện thực lịch sử thay đổi theo thời gian",
      "Vì lập trường, mục đích, trình độ và nguồn sử liệu của người nhận thức khác nhau",
      "Vì sử liệu lịch sử luôn bị làm giả",
      "Vì mỗi thế hệ không được học lịch sử"], "B"),
    ("Sử học là",
     ["khoa học nghiên cứu về quá khứ của loài người",
      "môn học thuộc lòng các sự kiện đã qua",
      "nghề chép sử của các triều đại",
      "tập hợp những câu chuyện truyền miệng về quá khứ"], "A"),
    ("Đối tượng nghiên cứu của Sử học là",
     ["các hiện tượng tự nhiên đã xảy ra",
      "toàn bộ quá khứ của loài người",
      "chỉ quá khứ của các quốc gia lớn",
      "các tác phẩm văn học cổ"], "B"),
    ("Nội dung nào sau đây <b>KHÔNG</b> thuộc đối tượng nghiên cứu của Sử học?",
     ["Quá khứ của một cá nhân",
      "Quá khứ của một cộng đồng người",
      "Những hiện tượng tự nhiên xảy ra ngoài tác động của con người",
      "Quá khứ của một quốc gia, khu vực"], "C"),
    ("Chức năng khoa học của Sử học là",
     ["giáo dục tư tưởng, đạo đức cho thế hệ trẻ",
      "khôi phục sự kiện lịch sử và phát hiện quy luật vận động, phát triển của lịch sử",
      "dự báo chính xác mọi sự kiện tương lai",
      "quảng bá du lịch và di sản văn hoá"], "B"),
    ("Chức năng xã hội của Sử học thể hiện ở việc",
     ["khôi phục chính xác hiện thực lịch sử",
      "phát hiện quy luật vận động của lịch sử",
      "giáo dục tư tưởng, đạo đức và rút ra bài học kinh nghiệm cho cuộc sống hiện tại",
      "xác định niên đại của di vật khảo cổ"], "C"),
    ("Nhiệm vụ nào sau đây <b>KHÔNG</b> phải là nhiệm vụ của Sử học?",
     ["Cung cấp tri thức khoa học về quá khứ",
      "Giáo dục, nêu gương",
      "Dự báo tương lai",
      "Sản xuất hàng hoá phục vụ thị trường"], "D"),
    ("Nhiệm vụ dự báo của Sử học được thực hiện trên cơ sở nào?",
     ["Cảm nhận chủ quan của nhà sử học",
      "Tổng kết thực tiễn, rút ra bài học kinh nghiệm",
      "Dự đoán ngẫu nhiên từ các sự kiện rời rạc",
      "Ý kiến của đa số người dân"], "B"),
    ("Nội dung nào phản ánh đúng các nguyên tắc cơ bản của Sử học?",
     ["Khách quan, chủ quan, trung thực, nhân văn",
      "Chủ quan, nhân văn, khách quan, trung thực",
      "Khách quan, trung thực, nhân văn, tiến bộ",
      "Trung thực, nhân văn, tiến bộ, chủ quan"], "C"),
    ("Nguyên tắc quan trọng nhất của Sử học là",
     ["khách quan", "nhân văn", "tiến bộ", "toàn diện"], "A"),
    ("Việc “không xuyên tạc, thêm bớt hoặc làm sai lệch hiện thực lịch sử” thể hiện nguyên tắc",
     ["khách quan", "trung thực", "tiến bộ", "nhân văn"], "B"),
    ("Việc nắm vững các nguyên tắc của Sử học có ý nghĩa nào sau đây?",
     ["Giúp nhà sử học hiểu rõ sứ mệnh, trách nhiệm, đạo đức của người viết lịch sử",
      "Giúp mọi người ghi nhớ được nhiều sự kiện hơn",
      "Giúp rút ngắn thời gian làm bài kiểm tra",
      "Giúp bảo tồn được mọi di sản mà không cần đầu tư"], "A"),
    ("Nhận định nào đúng về quan hệ giữa hiện thực lịch sử và nhận thức lịch sử?",
     ["Hiện thực lịch sử do nhận thức lịch sử tạo ra",
      "Không có hiện thực lịch sử thì không có nhận thức lịch sử",
      "Nhận thức lịch sử có trước hiện thực lịch sử",
      "Hai khái niệm hoàn toàn không liên quan đến nhau"], "B"),
    ("Việc làm nào sau đây thể hiện <b>lịch sử được con người nhận thức</b>?",
     ["Một viên gạch cổ còn nguyên vẹn tại di tích",
      "Bộ phim tái hiện chiến dịch Điện Biên Phủ",
      "Dấu tích hố bom còn in trên mặt đất",
      "Một bản đồ do người Pháp vẽ tại thực địa năm 1953"], "B"),
    ("Nhà sử học không thể quan sát trực tiếp đối tượng nghiên cứu của mình chủ yếu vì",
     ["đối tượng đã không còn hiện hữu, tồn tại khoảng cách giữa quá khứ và hiện tại",
      "nhà sử học thiếu phương tiện kĩ thuật",
      "sử liệu lịch sử quá ít",
      "không được phép tiếp cận hiện vật"], "A"),
]

BAI2 = [
    ("Tri thức lịch sử là",
     ["những hiểu biết, kiến thức của con người về lịch sử, hình thành qua học tập, khám phá, nghiên cứu và trải nghiệm",
      "toàn bộ những gì đã diễn ra trong quá khứ",
      "những hiện vật cổ còn lưu giữ được",
      "ý kiến chủ quan của nhà nghiên cứu về quá khứ"], "A"),
    ("Một trong những vai trò của tri thức lịch sử đối với cá nhân là",
     ["giúp hiểu cội nguồn, bản sắc của bản thân và dân tộc",
      "giúp dự đoán chính xác kết quả kì thi",
      "giúp làm giàu nhanh chóng",
      "giúp thay thế kiến thức của các môn học khác"], "A"),
    ("Vì sao cần phải học tập và khám phá lịch sử suốt đời?",
     ["Vì tri thức lịch sử là vô hạn và nhận thức lịch sử luôn được bổ sung, điều chỉnh",
      "Vì chương trình nhà trường yêu cầu như vậy",
      "Vì ai cũng muốn trở thành nhà sử học",
      "Vì lịch sử là môn thi bắt buộc"], "A"),
    ("Bước đầu tiên của quy trình thu thập, xử lí thông tin và sử liệu là",
     ["sưu tầm, đọc và ghi chép thông tin",
      "lập thư mục và danh mục các nguồn sử liệu cần thu thập",
      "xác minh, đánh giá nguồn sử liệu",
      "chọn lọc, phân loại sử liệu"], "B"),
    ("“Phân loại, đánh giá, thẩm định, so sánh nguồn sử liệu đã thu thập được” là nội dung của",
     ["thu thập thông tin và sử liệu",
      "xử lí thông tin và sử liệu",
      "lập thư mục sử liệu",
      "phỏng vấn nhân chứng"], "B"),
    ("Quy trình thu thập, xử lí thông tin và sử liệu đúng là",
     ["Lập thư mục → Sưu tầm, ghi chép → Chọn lọc, phân loại → Xác minh, đánh giá",
      "Xác minh, đánh giá → Lập thư mục → Chọn lọc → Sưu tầm",
      "Chọn lọc, phân loại → Sưu tầm → Xác minh → Lập thư mục",
      "Sưu tầm → Lập thư mục → Xác minh → Chọn lọc"], "A"),
    ("Việc nào sau đây thuộc khâu <b>sưu tầm, thu thập</b> sử liệu?",
     ["Đối chiếu hai nguồn tài liệu mâu thuẫn nhau",
      "Ghi chép lại thông tin về nguồn gốc, xuất xứ của tài liệu",
      "Đánh giá độ tin cậy của tài liệu",
      "Tổng hợp dữ liệu để rút ra kết luận"], "B"),
    ("Nội dung nào sau đây <b>KHÔNG</b> thuộc khâu xử lí thông tin sử liệu?",
     ["Phân tích tài liệu",
      "So sánh các nguồn sử liệu",
      "Tìm kiếm và thu thập tài liệu liên quan",
      "Tổng hợp dữ liệu"], "C"),
    ("Sử liệu sơ cấp là",
     ["sử liệu được tạo ra đầu tiên, gần nhất hoặc gắn liền với thời gian xuất hiện của sự kiện",
      "sử liệu được tạo ra sau thời điểm xuất hiện của sự vật, hiện tượng",
      "công trình nghiên cứu tổng hợp về quá khứ",
      "bài báo khoa học viết về một sự kiện lịch sử"], "A"),
    ("Trong các tư liệu sau, tư liệu nào là <b>sử liệu sơ cấp</b>?",
     ["Cuốn sách giáo khoa Lịch sử 10",
      "Tấm bia đá dựng ngay sau khi sự kiện diễn ra",
      "Bài báo nghiên cứu về thời Lý",
      "Bộ phim tài liệu sản xuất năm 2020 về nhà Trần"], "B"),
    ("Trong các tư liệu sau, tư liệu nào là <b>sử liệu thứ cấp</b>?",
     ["Sắc phong của vua ban năm 1467",
      "Trống đồng khai quật tại Thanh Hoá",
      "Luận án nghiên cứu về văn minh Đại Việt xuất bản năm 2019",
      "Ảnh chụp hiện trường một sự kiện năm 1954"], "C"),
    ("Trống đồng Đông Sơn thuộc loại hình sử liệu nào?",
     ["Thành văn", "Hiện vật", "Lời nói – truyền khẩu", "Đa phương tiện"], "B"),
    ("Truyền thuyết Sơn Tinh – Thuỷ Tinh thuộc loại hình sử liệu nào?",
     ["Thành văn", "Hiện vật", "Lời nói – truyền khẩu", "Hình ảnh"], "C"),
    ("Khi thu thập tư liệu lịch sử trên internet, việc làm nào là cần thiết nhất?",
     ["Chỉ lấy thông tin từ trang xuất hiện đầu tiên",
      "Kiểm chứng nguồn gốc, tác giả và đối chiếu nhiều nguồn khác nhau",
      "Chỉ lấy thông tin từ mạng xã hội vì cập nhật nhanh",
      "Sao chép nguyên văn mà không cần ghi nguồn"], "B"),
    ("Bản chất của việc kết nối tri thức, bài học lịch sử vào cuộc sống là",
     ["học thuộc nhiều sự kiện để đạt điểm cao",
      "biến tri thức lịch sử thành năng lực và hành động, vận dụng vào giải quyết vấn đề hiện tại",
      "ghi nhớ tên các nhân vật lịch sử",
      "sưu tầm thật nhiều hiện vật cổ"], "B"),
]

BAI3 = [
    ("Vai trò quan trọng nhất của Sử học đối với di sản là",
     ["khẳng định giá trị của di sản, làm cơ sở khoa học cho công tác bảo tồn",
      "tổ chức các lễ hội tại di tích",
      "xây dựng cơ sở hạ tầng du lịch",
      "quảng cáo hình ảnh di sản ra nước ngoài"], "A"),
    ("Di sản văn hoá được chia thành mấy loại hình cơ bản?",
     ["2 loại (vật thể và phi vật thể)", "3 loại", "4 loại", "5 loại"], "A"),
    ("Di sản nào sau đây là <b>di sản văn hoá phi vật thể</b>?",
     ["Phố cổ Hội An", "Dân ca Quan họ Bắc Ninh", "Vịnh Hạ Long", "Thánh địa Mỹ Sơn"], "B"),
    ("Di sản nào sau đây là <b>di sản thiên nhiên</b>?",
     ["Hoàng thành Thăng Long", "Vườn quốc gia Phong Nha – Kẻ Bàng",
      "Nhã nhạc cung đình Huế", "Thành nhà Hồ"], "B"),
    ("Di sản nào sau đây là <b>di sản văn hoá vật thể</b>?",
     ["Nghệ thuật Xòe Thái", "Hội Bài chòi",
      "Quần thể di tích Cố đô Huế", "Tín ngưỡng thờ Mẫu Tam phủ"], "C"),
    ("Công tác bảo tồn có vai trò gì đối với di sản văn hoá vật thể?",
     ["Tái tạo lại hoàn toàn thành một di sản mới",
      "Hạn chế và khắc phục tác động tiêu cực của tự nhiên và con người, kéo dài tuổi thọ di sản",
      "Thay thế di sản cũ bằng công trình hiện đại",
      "Chuyển di sản thành hàng hoá du lịch"], "B"),
    ("Nhờ đâu mà các di sản văn hoá phi vật thể được tái tạo, giữ gìn và lưu truyền?",
     ["Nhờ sưu tầm, lưu giữ, truyền nghề, trình diễn",
      "Nhờ xây dựng thêm các công trình mới",
      "Nhờ khai thác tối đa để thu vé tham quan",
      "Nhờ việc mở rộng đô thị"], "A"),
    ("Bảo tồn và phát huy giá trị di sản thiên nhiên góp phần",
     ["phát triển đa dạng sinh học và tăng giá trị khoa học của di sản",
      "thay đổi khí hậu toàn cầu",
      "làm mất đi cảnh quan tự nhiên",
      "tăng diện tích đất xây dựng"], "A"),
    ("Những giá trị về lịch sử và văn hoá có vai trò gì đối với sự phát triển du lịch?",
     ["Là nguồn tài nguyên quý báu, tạo nên sức hút và bản sắc riêng của điểm đến",
      "Là trở ngại vì làm chậm việc xây dựng",
      "Chỉ có ý nghĩa với du lịch nước ngoài",
      "Không có liên quan gì đến du lịch"], "A"),
    ("Du lịch có vai trò nào sau đây đối với công tác bảo tồn di tích?",
     ["Làm di tích xuống cấp nhanh hơn trong mọi trường hợp",
      "Tạo động lực gìn giữ và nguồn thu được tái đầu tư cho bảo tồn",
      "Thay thế hoàn toàn vai trò của nhà nước",
      "Không có tác động gì"], "B"),
    ("Tác động tiêu cực nào của du lịch đối với di sản văn hoá?",
     ["Tăng nguồn thu cho địa phương",
      "Quảng bá hình ảnh đất nước",
      "Khai thác quá mức, thương mại hoá lễ hội, xâm hại di tích",
      "Nâng cao nhận thức của du khách"], "C"),
    ("Để phát triển du lịch bền vững, cần",
     ["khai thác tối đa lượng khách để tăng doanh thu",
      "gắn phát triển du lịch với bảo tồn, kiểm soát sức chứa và chia sẻ lợi ích cho cộng đồng",
      "xây dựng nhiều công trình hiện đại quanh di tích",
      "hạn chế mọi hoạt động tham quan"], "B"),
    ("Biện pháp nào sau đây <b>KHÔNG</b> phù hợp để bảo tồn di sản?",
     ["Tuyên truyền, giáo dục nâng cao nhận thức cộng đồng",
      "Ứng dụng công nghệ số để lưu giữ và quảng bá di sản",
      "Xây dựng công trình mới che khuất, thay thế di tích cũ",
      "Tu bổ, tôn tạo theo nguyên tắc giữ tối đa giá trị gốc"], "C"),
    ("Việc làm nào của học sinh góp phần bảo tồn di sản ở địa phương?",
     ["Tham gia lễ hội, tìm hiểu và tuyên truyền về di sản quê hương",
      "Khắc tên mình lên di tích để lưu niệm",
      "Bán cổ vật tìm được cho khách du lịch",
      "Không quan tâm vì đó là việc của nhà nước"], "A"),
    ("Di sản văn hoá phi vật thể của Nghệ An – Hà Tĩnh được UNESCO ghi danh là",
     ["Nhã nhạc cung đình Huế", "Dân ca Ví, Giặm Nghệ Tĩnh",
      "Đờn ca tài tử Nam Bộ", "Hát Xoan Phú Thọ"], "B"),
]

# --------------------------------------------------------------------------
# Cân bằng phân bố đáp án (tránh "dồn B", tránh D quá ít)
# --------------------------------------------------------------------------
# Các câu đã được giải thích bằng chữ cái cụ thể ở mục E4.2 -> giữ nguyên thứ tự
LOCKED = {1, 3, 9, 14, 20, 24, 26, 27, 30, 31, 36, 41, 45, 48}

from qbank import balance

# Các câu đã được giải thích bằng chữ cái cụ thể ở mục E4.2 -> giữ nguyên đáp án
LOCKED = {1, 3, 9, 14, 20, 24, 26, 27, 30, 31, 36, 41, 45, 48}
LOCKED_IDX = {
    1: {n - 1 for n in LOCKED if 1 <= n <= 20},
    21: {n - 21 for n in LOCKED if 21 <= n <= 35},
    36: {n - 36 for n in LOCKED if 36 <= n <= 50},
}
_TARGET_BY_START = {
    1:  {"A": 5, "B": 5, "C": 5, "D": 5},   # Bài 1 – 20 câu
    21: {"A": 4, "B": 4, "C": 4, "D": 3},   # Bài 2 – 15 câu
    36: {"A": 4, "B": 4, "C": 3, "D": 4},   # Bài 3 – 15 câu
}


def rebalance(data, start):
    """Cân bằng phân bố đáp án cho từng nhóm câu."""
    return balance(data, _TARGET_BY_START[start], LOCKED_IDX[start])


TF = [
    ("1", "Trong giờ học, hai bạn tranh luận. Bạn A nói: “Hiện thực lịch sử chỉ có một và không thể thay đổi.” "
          "Bạn B nói: “Nhận thức lịch sử cũng chỉ có một, vì sự thật thì chỉ có một.”",
     ["Hiện thực lịch sử tồn tại khách quan, không phụ thuộc vào ý muốn chủ quan của con người.",
      "Khi có thêm sử liệu mới, hiện thực lịch sử sẽ thay đổi theo.",
      "Nhận thức lịch sử có thể được bổ sung, điều chỉnh khi phát hiện sử liệu mới.",
      "Nhận thức lịch sử luôn phản ánh đầy đủ và chính xác hiện thực lịch sử."]),
    ("2", "Một bạn học sinh cho rằng: “Sử học chỉ là môn học thuộc lòng các sự kiện đã qua, "
          "không có giá trị gì với cuộc sống hiện tại.”",
     ["Sử học là khoa học nghiên cứu về quá khứ của loài người.",
      "Đối tượng nghiên cứu của Sử học chỉ là các sự kiện chính trị, quân sự của các quốc gia.",
      "Sử học có hai chức năng cơ bản là chức năng khoa học và chức năng xã hội.",
      "Một trong những nhiệm vụ của Sử học là dự báo tương lai thông qua tổng kết thực tiễn."]),
    ("3", "Khi viết lại một sự kiện lịch sử, một tác giả đã lược bỏ những chi tiết bất lợi "
          "cho nhân vật mà mình yêu thích.",
     ["Việc làm trên vi phạm nguyên tắc trung thực của Sử học.",
      "Việc làm trên vi phạm nguyên tắc khách quan của Sử học.",
      "Nguyên tắc tiến bộ của Sử học cho phép lược bỏ chi tiết nếu mục đích là tốt.",
      "Nguyên tắc khách quan đòi hỏi nhà sử học không nhận thức phiến diện, một chiều."]),
    ("4", "Một nhóm học sinh được giao tìm hiểu về phố cổ Hội An. Nhóm trưởng đề xuất: "
          "“Đầu tiên cứ lên mạng lấy thông tin, sau đó mới lập danh mục tài liệu cần tìm.”",
     ["Đề xuất của nhóm trưởng là đúng quy trình thu thập, xử lí thông tin và sử liệu.",
      "Bước đầu tiên của quy trình là lập thư mục và danh mục các nguồn sử liệu cần thu thập.",
      "Việc xác minh, đánh giá nguồn sử liệu được thực hiện sau khi đã thu thập và phân loại.",
      "Thông tin lấy từ mạng xã hội luôn có độ tin cậy cao nên không cần kiểm chứng."]),
    ("5", "Một người cho rằng: “Học lịch sử chỉ cần thiết ở trường phổ thông, "
          "ra trường rồi thì không cần học nữa.”",
     ["Tri thức lịch sử là vô hạn, vì vậy cần học tập và khám phá lịch sử suốt đời.",
      "Nhận thức lịch sử có thể thay đổi khi có sử liệu mới được phát hiện.",
      "Chỉ những người làm nghề sử mới cần cập nhật tri thức lịch sử.",
      "Học lịch sử suốt đời góp phần hình thành kĩ năng đánh giá, kiểm chứng nguồn thông tin."]),
    ("6", "Một di tích cổ đang bị xuống cấp. Chính quyền địa phương dự kiến phá bỏ di tích "
          "để xây khu thương mại.",
     ["Di tích trên thuộc loại hình di sản văn hoá vật thể.",
      "Việc phá bỏ di tích để xây khu thương mại là biện pháp bảo tồn phù hợp.",
      "Nghiên cứu của Sử học giúp xác định giá trị của di tích, làm cơ sở cho công tác bảo tồn.",
      "Công tác bảo tồn chỉ có ý nghĩa về văn hoá, không liên quan đến kinh tế."]),
    ("7", "Một điểm du lịch đón lượng khách vượt quá sức chứa. Doanh thu tăng mạnh "
          "nhưng nhiều di tích bị xâm hại.",
     ["Du lịch mang lại nguồn thu có thể được tái đầu tư cho công tác bảo tồn.",
      "Khai thác du lịch quá mức có thể gây tác động tiêu cực đến di sản.",
      "Doanh thu tăng chứng tỏ việc khai thác du lịch đang diễn ra bền vững.",
      "Cần kiểm soát sức chứa và gắn phát triển du lịch với bảo tồn."]),
    ("8", "Một nhóm học sinh đề xuất kế hoạch bảo tồn di sản địa phương gồm: số hoá tư liệu, "
          "tổ chức cho học sinh tham quan di tích, vận động người dân không xả rác tại di tích.",
     ["Việc số hoá tư liệu là ứng dụng khoa học – công nghệ vào bảo tồn.",
      "Tổ chức tham quan giúp nâng cao nhận thức của học sinh về di sản.",
      "Vận động người dân giữ gìn di tích là biện pháp thuộc nhóm giải pháp về cộng đồng.",
      "Bảo tồn di sản chỉ là trách nhiệm của cơ quan nhà nước."]),
]

TF_ANS = [
    ["II.1", "a–<b>Đ</b>", "b–<b>S</b>", "c–<b>Đ</b>", "d–<b>S</b>",
     "b sai vì hiện thực không đổi; d sai vì nhận thức không bao giờ đầy đủ"],
    ["II.2", "a–<b>Đ</b>", "b–<b>S</b>", "c–<b>Đ</b>", "d–<b>Đ</b>",
     "b sai vì đối tượng gồm mọi lĩnh vực và cả cá nhân, cộng đồng"],
    ["II.3", "a–<b>Đ</b>", "b–<b>Đ</b>", "c–<b>S</b>", "d–<b>Đ</b>",
     "c sai: không có nguyên tắc nào cho phép bóp méo sự thật"],
    ["II.4", "a–<b>S</b>", "b–<b>Đ</b>", "c–<b>Đ</b>", "d–<b>S</b>",
     "a sai vì phải lập danh mục trước; d sai vì phải kiểm chứng"],
    ["II.5", "a–<b>Đ</b>", "b–<b>Đ</b>", "c–<b>S</b>", "d–<b>Đ</b>",
     "c sai: mọi người đều cần, không riêng người làm nghề sử"],
    ["II.6", "a–<b>Đ</b>", "b–<b>S</b>", "c–<b>Đ</b>", "d–<b>S</b>",
     "b sai vì phá di tích là xâm hại di sản; d sai vì bảo tồn còn góp phần phát triển kinh tế"],
    ["II.7", "a–<b>Đ</b>", "b–<b>Đ</b>", "c–<b>S</b>", "d–<b>Đ</b>",
     "c sai: doanh thu tăng nhưng di tích bị xâm hại là dấu hiệu KHÔNG bền vững"],
    ["II.8", "a–<b>Đ</b>", "b–<b>Đ</b>", "c–<b>Đ</b>", "d–<b>S</b>",
     "d sai: bảo tồn là trách nhiệm của cả cộng đồng, trong đó có học sinh"],
]


def build():
    s = []
    s += h1("E", "NGÂN HÀNG CÂU HỎI CÓ ĐÁP ÁN", "E")
    s += [P("Phần này gồm <b>50 câu trắc nghiệm nhiều lựa chọn</b>, <b>8 câu trắc nghiệm Đúng/Sai</b> "
            "(32 ý) và <b>6 câu tự luận</b> có dàn ý – tổng cộng <b>64 câu hỏi, tương đương 88 lệnh hỏi</b>. "
            "Toàn bộ câu hỏi được biên soạn <b>bám sát đúng ma trận và bảng đặc tả</b> ở Phần A: "
            "đúng tỉ lệ bài, đúng cấp độ tư duy, đúng dạng câu.")]
    s += box("CÁCH DÙNG NGÂN HÀNG CÂU HỎI", [
        "<b>Lượt 1:</b> Làm toàn bộ câu hỏi <b>không xem đáp án</b>, ghi câu sai ra giấy.",
        "<b>Lượt 2:</b> Đối chiếu đáp án ở cuối phần E, đọc kĩ phần giải thích các câu sai.",
        "<b>Lượt 3:</b> Sau 2–3 ngày, làm lại <b>chỉ những câu đã sai</b> – đây là bước tạo trí nhớ dài hạn.",
        "Mục tiêu: mỗi câu trắc nghiệm làm trong <b>trung bình 45 giây</b>, đúng từ 45/50 câu trở lên.",
    ], "tip")

    # ---------------------------------------------------------- Phần I
    s += h2("E1. Phần I – Trắc nghiệm nhiều lựa chọn (50 câu)", "E1")

    blocks = [("E1.1. Bài 1 – Hiện thực lịch sử và lịch sử được con người nhận thức (câu 1 – 20)",
               BAI1, 1),
              ("E1.2. Bài 2 – Tri thức lịch sử và cuộc sống (câu 21 – 35)", BAI2, 21),
              ("E1.3. Bài 3 – Vai trò của Sử học (câu 36 – 50)", BAI3, 36)]
    for title, data, start in blocks:
        s += h3(title)
        for i, (stem, opts, ans) in enumerate(rebalance(data, start)):
            s += [mcq(str(start + i), stem, opts)]

    # ---------------------------------------------------------- Phần II
    s += [PageBreak()]
    s += h2("E2. Phần II – Trắc nghiệm Đúng/Sai (8 câu, 32 ý)", "E2")
    s += [P("Mỗi câu gồm một tình huống và bốn ý a), b), c), d). Thí sinh xác định mỗi ý "
            "<b>Đúng</b> hay <b>Sai</b>. Đây là dạng câu chiếm <b>2,0 điểm</b> trong đề thật, "
            "và cũng là dạng dễ mất điểm nhất nếu đọc không kĩ.")]
    for num, ctx, sts in TF:
        s += [tf_item(num, ctx, sts)]

    # ---------------------------------------------------------- Phần III
    s += [PageBreak()]
    s += h2("E3. Phần III – Tự luận (6 câu, có dàn ý và bài mẫu)", "E3")

    s += essay("1", "Khái niệm, đối tượng, chức năng, nhiệm vụ của Sử học (mức độ: Biết)",
               "Trình bày khái niệm Sử học; nêu đối tượng nghiên cứu, chức năng và nhiệm vụ của Sử học.",
               ["<b>Khái niệm:</b> Sử học là khoa học nghiên cứu về quá khứ của loài người; "
                "khôi phục hiện thực lịch sử và phát hiện quy luật phát sinh, phát triển.",
                "<b>Đối tượng:</b> toàn bộ quá khứ của loài người – cá nhân, nhóm, cộng đồng, quốc gia, khu vực, nhân loại; "
                "trên mọi lĩnh vực chính trị, kinh tế, xã hội, văn hoá, quân sự, ngoại giao…",
                "<b>Chức năng:</b> khoa học (khôi phục sự kiện, phát hiện quy luật) và xã hội "
                "(giáo dục tư tưởng, đạo đức; rút ra bài học kinh nghiệm).",
                "<b>Nhiệm vụ:</b> nhận thức (cung cấp tri thức khoa học), giáo dục – nêu gương, "
                "dự báo (tổng kết thực tiễn, dự báo tương lai).",
                "<b>Kết luận:</b> Sử học là một khoa học thực sự, có ích cho đời sống con người."],
               )

    s += essay("2", "Phân biệt hiện thực lịch sử và nhận thức lịch sử (mức độ: Hiểu)",
               "Phân biệt hiện thực lịch sử và lịch sử được con người nhận thức. "
               "Vì sao cùng một sự kiện lịch sử lại có nhiều cách nhận thức khác nhau?",
               ["<b>Khái niệm:</b> nêu định nghĩa hai khái niệm.",
                "<b>Khác nhau:</b> hiện thực – khách quan, duy nhất, bất biến, không quan sát trực tiếp; "
                "nhận thức – vừa khách quan vừa chủ quan, đa dạng, có thể thay đổi, không tái hiện đầy đủ.",
                "<b>Giống/liên hệ:</b> đều liên quan đến quá khứ; hiện thực có trước, nhận thức có sau; "
                "không có hiện thực thì không có nhận thức.",
                "<b>Vì sao nhiều cách nhận thức:</b> khoảng cách thời gian; nguồn sử liệu khác nhau; "
                "lập trường, mục đích, trình độ của người nhận thức; nhu cầu của thời đại.",
                "<b>Liên hệ:</b> vì vậy cần học tập suốt đời và kiểm chứng sử liệu."],
               )

    s += essay("3", "Quy trình thu thập, xử lí sử liệu và việc học lịch sử suốt đời (mức độ: Biết – Hiểu)",
               "Nêu các bước trong việc thu thập, xử lí thông tin và sử liệu. "
               "Vì sao phải học tập và khám phá lịch sử suốt đời?",
               ["<b>Quy trình 4 bước:</b> lập thư mục, danh mục sử liệu → sưu tầm, đọc và ghi chép → "
                "chọn lọc, phân loại → xác minh, đánh giá.",
                "<b>Hai khâu lớn:</b> sưu tầm, thu thập (tìm, ghi chép, phân loại nguồn) và "
                "xử lí (phân tích, đánh giá – thẩm định, so sánh, tổng hợp).",
                "<b>Vì sao học suốt đời:</b> tri thức vô hạn và luôn được bổ sung; thực tiễn luôn vận động; "
                "phát triển năng lực, kĩ năng bản thân; đáp ứng yêu cầu của xã hội học tập và công dân toàn cầu.",
                "<b>Liên hệ bản thân:</b> chủ động đọc sách, tham quan bảo tàng, kiểm chứng thông tin trên mạng."],
               )

    s += essay("4", "Vai trò của Sử học với công tác bảo tồn và phát huy giá trị di sản (mức độ: Hiểu – Vận dụng)",
               "Phân tích vai trò của Sử học đối với công tác bảo tồn và phát huy giá trị di sản văn hoá, "
               "di sản thiên nhiên. Lấy ví dụ ở Việt Nam.",
               ["<b>Mở bài:</b> khẳng định Sử học là cơ sở khoa học của công tác bảo tồn.",
                "<b>Xác định giá trị di sản:</b> niên đại, nguồn gốc, giá trị lịch sử – văn hoá – kiến trúc – khoa học; "
                "nhờ đó di sản được nhìn nhận đúng và được xếp hạng, công nhận.",
                "<b>Cung cấp căn cứ khoa học để bảo tồn:</b> tu bổ, phục dựng đúng nguyên tắc giữ tối đa giá trị gốc; "
                "tránh làm sai lệch, “mới hoá” di sản.",
                "<b>Phân loại và đề xuất phương án:</b> vật thể – phi vật thể – thiên nhiên có cách bảo tồn khác nhau.",
                "<b>Phát huy giá trị:</b> xây dựng nội dung trưng bày, thuyết minh, giáo dục, quảng bá, du lịch.",
                "<b>Ví dụ:</b> nghiên cứu của Sử học góp phần khẳng định giá trị Hoàng thành Thăng Long, "
                "phục dựng cột đá chùa Dạm, bảo tồn Dân ca Ví, Giặm Nghệ Tĩnh.",
                "<b>Kết bài:</b> bảo tồn mà không có cơ sở sử học sẽ là “bảo tồn mù”; ngược lại Sử học "
                "chỉ có ý nghĩa khi góp phần giữ gìn di sản cho cộng đồng."],
               sample="<b>Bài làm:</b> Sử học có vai trò đặc biệt quan trọng với công tác bảo tồn và phát huy "
                      "giá trị di sản. Trước hết, Sử học <b>xác định giá trị đích thực</b> của di sản: "
                      "niên đại, nguồn gốc, chủ nhân, ý nghĩa lịch sử – văn hoá – kiến trúc. "
                      "Không có những kết quả nghiên cứu ấy, di sản chỉ là một công trình cũ, thậm chí bị coi là "
                      "“vật cản” của phát triển. Thứ hai, Sử học <b>cung cấp căn cứ khoa học</b> cho việc tu bổ, "
                      "phục dựng, bảo đảm nguyên tắc giữ tối đa giá trị gốc, tránh “mới hoá” di sản. "
                      "Thứ ba, Sử học giúp <b>đề xuất phương án bảo tồn phù hợp</b> với từng loại hình: "
                      "di sản vật thể cần chống xuống cấp, di sản phi vật thể cần sưu tầm – truyền dạy, "
                      "di sản thiên nhiên cần bảo vệ đa dạng sinh học. Cuối cùng, kết quả nghiên cứu là chất liệu "
                      "để <b>phát huy</b> di sản qua trưng bày, giáo dục và du lịch. Ở Việt Nam, nghiên cứu lịch sử "
                      "đã góp phần khẳng định giá trị Hoàng thành Thăng Long, phục dựng cột đá chùa Dạm, "
                      "hay xây dựng hồ sơ để Dân ca Ví, Giặm Nghệ Tĩnh được UNESCO ghi danh. "
                      "Có thể nói, Sử học chính là “bộ xương sống” khoa học của mọi hoạt động bảo tồn.")

    s += essay("5", "Tác động của du lịch đối với công tác bảo tồn di tích, di sản (mức độ: Hiểu – Vận dụng)",
               "Phân tích tác động của du lịch đối với công tác bảo tồn di tích lịch sử, di sản văn hoá. "
               "Theo em, cần làm gì để phát triển du lịch bền vững gắn với bảo tồn?",
               ["<b>Tác động tích cực:</b> thôi thúc chính quyền và nhân dân gìn giữ, bảo tồn, phục dựng; "
                "doanh thu được tái đầu tư cho tu bổ, tôn tạo, quản lí; di sản phi vật thể được sưu tầm, truyền dạy; "
                "nâng cao nhận thức và quảng bá giá trị di sản.",
                "<b>Tác động tiêu cực:</b> khai thác quá mức, quá tải; thương mại hoá lễ hội; xây dựng tuỳ tiện "
                "phá vỡ cảnh quan; ô nhiễm, xâm hại di tích, trộm cắp cổ vật.",
                "<b>Nguyên nhân:</b> chạy theo lợi nhuận, thiếu quy hoạch, ý thức du khách và cộng đồng chưa cao.",
                "<b>Giải pháp:</b> quy hoạch và kiểm soát sức chứa; gắn du lịch với bảo tồn; chia sẻ lợi ích cho cộng đồng; "
                "giáo dục du khách; ứng dụng công nghệ số; xử lí nghiêm hành vi xâm hại.",
                "<b>Kết bài:</b> du lịch và bảo tồn phải là “đôi bạn đồng hành”, không phải hai lực lượng đối lập."],
               sample="<b>Bài làm:</b> Du lịch có tác động <b>hai chiều</b> đối với công tác bảo tồn di tích, di sản. "
                      "Về mặt tích cực, nhu cầu tham quan, tìm hiểu của du khách đã <b>thôi thúc</b> chính quyền và "
                      "nhân dân địa phương gìn giữ, tu bổ, phục dựng di tích; một phần doanh thu du lịch được "
                      "<b>tái đầu tư</b> vào công tác bảo tồn, quản lí và tôn tạo. Nhiều di sản phi vật thể như dân ca, "
                      "lễ hội, nghề truyền thống đã được sưu tầm, phục dựng và truyền dạy trở lại nhờ du lịch. "
                      "Du lịch còn góp phần quảng bá giá trị di sản và nâng cao nhận thức cộng đồng. "
                      "Tuy nhiên, khi bị khai thác quá mức, du lịch lại trở thành mối đe doạ: di tích quá tải, "
                      "xuống cấp; lễ hội bị thương mại hoá, mất tính thiêng; cảnh quan bị phá vỡ bởi các công trình "
                      "xây dựng tuỳ tiện; rác thải và hành vi xâm hại di tích gia tăng. "
                      "Vì vậy, để phát triển bền vững cần quy hoạch và <b>kiểm soát sức chứa</b>, gắn phát triển du lịch "
                      "với bảo tồn, chia sẻ lợi ích cho cộng đồng địa phương, tôn vinh nghệ nhân, giáo dục du khách và "
                      "xử lí nghiêm các hành vi xâm hại di sản. Có như vậy, du lịch mới thực sự là <b>nguồn lực</b> "
                      "nuôi dưỡng di sản thay vì bào mòn di sản.")

    s += essay("6", "Đề xuất biện pháp bảo tồn, phát huy di sản ở địa phương (mức độ: Vận dụng cao)",
               "Em hãy đề xuất các biện pháp bảo tồn và phát huy giá trị di sản văn hoá, di sản thiên nhiên "
               "ở địa phương em. Liên hệ trách nhiệm của học sinh.",
               ["<b>Nhận thức – giáo dục:</b> tuyên truyền, đưa di sản vào trường học, tổ chức tham quan, trải nghiệm.",
                "<b>Thể chế – pháp luật:</b> thực hiện Luật Di sản văn hoá, quy hoạch khoanh vùng, xử lí nghiêm vi phạm.",
                "<b>Khoa học – kĩ thuật:</b> tu bổ theo nguyên tắc giữ giá trị gốc; số hoá, bảo tàng ảo, 3D.",
                "<b>Kinh tế – du lịch:</b> du lịch bền vững, kiểm soát sức chứa, tái đầu tư doanh thu, gắn di sản với sinh kế.",
                "<b>Cộng đồng:</b> trao quyền, chia sẻ lợi ích, tôn vinh nghệ nhân, khuyến khích người trẻ.",
                "<b>Trách nhiệm học sinh:</b> tìm hiểu di sản quê hương; tham gia lễ hội, hoạt động tình nguyện; "
                "không xả rác, không khắc vẽ lên di tích; tuyên truyền cho bạn bè, gia đình; chia sẻ, quảng bá di sản "
                "trên mạng một cách trung thực, có trách nhiệm."],
               sample="<b>Bài làm:</b> Bảo tồn di sản là việc làm cần thiết và cấp bách, nhất là ở địa phương – nơi "
                      "di sản đang chịu áp lực của đô thị hoá và du lịch. Trước hết cần <b>nâng cao nhận thức</b>: "
                      "tuyên truyền trong trường học và cộng đồng, tổ chức cho học sinh tham quan, trải nghiệm để "
                      "hiểu và yêu di sản. Song song, phải <b>thực thi nghiêm pháp luật</b> về di sản, quy hoạch "
                      "khoanh vùng bảo vệ và xử lí nghiêm các hành vi xâm hại. Về khoa học – kĩ thuật, cần tu bổ theo "
                      "nguyên tắc giữ tối đa giá trị gốc, đồng thời <b>số hoá</b> tư liệu, xây dựng bảo tàng ảo để vừa "
                      "lưu giữ vừa quảng bá. Về kinh tế, nên phát triển <b>du lịch bền vững</b>, kiểm soát sức chứa, "
                      "dùng một phần doanh thu tái đầu tư cho bảo tồn và gắn di sản với sinh kế của người dân. "
                      "Quan trọng nhất là <b>trao quyền cho cộng đồng</b>: người dân phải được hưởng lợi và tự hào "
                      "về di sản thì mới gìn giữ được lâu dài. Là học sinh, em có thể bắt đầu từ những việc nhỏ: "
                      "tìm hiểu di sản quê hương, tham gia lễ hội và hoạt động tình nguyện, không xả rác hay khắc vẽ "
                      "lên di tích, và tuyên truyền để bạn bè, gia đình cùng chung tay.")

    # ---------------------------------------------------------- Đáp án
    s += [PageBreak()]
    s += h2("E4. Đáp án và giải thích", "E4")
    s += [P("Đối chiếu đáp án dưới đây, sau đó đọc kĩ phần <b>giải thích các câu dễ sai</b> – "
            "đó chính là những chỗ đề thật sẽ “gài bẫy”.")]

    s += h3("E4.1. Đáp án 50 câu trắc nghiệm")
    pairs, cnt = [], {"A": 0, "B": 0, "C": 0, "D": 0}
    for data, start in [(BAI1, 1), (BAI2, 21), (BAI3, 36)]:
        for i, (_, _, ans) in enumerate(rebalance(data, start)):
            pairs.append((str(start + i), ans))
            cnt[ans] += 1
    s += [answer_grid(pairs, per_row=10), Spacer(1, 8)]

    s += [P("<b>Thống kê đáp án:</b> A = %d câu, B = %d câu, C = %d câu, D = %d câu. "
            "Phân bố đã được cân bằng có chủ đích để bạn không thể “đoán mò” theo thói quen; "
            "khi làm bài thật, hãy dựa vào kiến thức chứ đừng dựa vào tần suất xuất hiện của đáp án."
            % (cnt["A"], cnt["B"], cnt["C"], cnt["D"]))]

    s += h3("E4.2. Giải thích các câu dễ sai")
    explain = [
        ("Câu 3", "“Đặc điểm nào KHÔNG đúng với hiện thực lịch sử?” → <b>C</b>. "
                  "Hiện thực lịch sử <b>không thể thay đổi</b>; khi phát hiện sử liệu mới thì "
                  "<b>nhận thức</b> thay đổi, không phải hiện thực. Đây là bẫy kinh điển."),
        ("Câu 9", "“Nội dung nào KHÔNG thuộc đối tượng của Sử học?” → <b>C</b>. "
                  "Sử học nghiên cứu <b>hoạt động của con người</b> và sự tương tác của con người với tự nhiên; "
                  "hiện tượng tự nhiên thuần tuý không có bàn tay con người thì không phải đối tượng."),
        ("Câu 14", "Các nguyên tắc cơ bản → <b>C</b>. Nhớ mẹo “KHÁCH – TRUNG – NHÂN – TIẾN”. "
                   "Phương án A và D có “chủ quan” – <b>chủ quan không bao giờ là nguyên tắc</b> của Sử học."),
        ("Câu 20", "Không quan sát trực tiếp → <b>A</b>. Lí do gốc là <b>khoảng cách thời gian</b> "
                   "và đối tượng không còn hiện hữu, không phải vì thiếu phương tiện."),
        ("Câu 24", "Bước đầu tiên → <b>B</b> (lập thư mục, danh mục). Nhiều bạn chọn A vì “sưu tầm” "
                   "là việc nhìn thấy đầu tiên, nhưng phải <b>biết cần tìm gì</b> trước đã."),
        ("Câu 26", "Thứ tự đúng → <b>A</b>. Nhớ “MỤC – SƯU – LỌC – MINH”; mọi phương án khác đều đặt "
                   "<b>xác minh trước khi thu thập</b> – điều không thể làm được."),
        ("Câu 27", "Thuộc khâu sưu tầm → <b>B</b> (ghi chép nguồn gốc, xuất xứ). Đối chiếu (A), đánh giá (C), "
                   "tổng hợp (D) đều là <b>xử lí</b>."),
        ("Câu 30 – 31", "Sơ cấp/thứ cấp → <b>B</b> và <b>C</b>. Mẹo: <b>sơ cấp = “số 1” = ra đời đầu tiên</b>. "
                        "Bia đá dựng ngay sau sự kiện → sơ cấp; luận án xuất bản 2019 nghiên cứu về quá khứ → thứ cấp."),
        ("Câu 36", "Vai trò quan trọng nhất của Sử học với di sản → <b>A</b>. Tổ chức lễ hội (B), xây hạ tầng (C), "
                   "quảng cáo (D) là việc của ngành du lịch – văn hoá, không phải <b>vai trò khoa học</b> của Sử học."),
        ("Câu 41", "Bảo tồn di sản vật thể → <b>B</b>. Từ khoá “hạn chế và khắc phục tác động tiêu cực”, "
                   "“kéo dài tuổi thọ” là nguyên văn tinh thần SGK."),
        ("Câu 45", "Du lịch với bảo tồn → <b>B</b>. Phương án A dùng từ tuyệt đối “mọi trường hợp” → sai. "
                   "Đây là bẫy từ tuyệt đối rất hay gặp."),
        ("Câu 48", "Biện pháp KHÔNG phù hợp → <b>C</b>. “Xây công trình mới che khuất, thay thế di tích cũ” là "
                   "<b>xâm hại</b> di sản, trái với nguyên tắc giữ tối đa giá trị gốc."),
    ]
    s += tb([["Câu", "Giải thích"]] + [[a, b] for a, b in explain],
            widths=[0.8, 5.7], sp_after=8)

    s += h3("E4.3. Đáp án 8 câu Đúng/Sai")
    s += tb([["Câu", "a", "b", "c", "d", "Ghi chú nhanh"]] + TF_ANS,
            widths=[0.55, 0.6, 0.6, 0.6, 0.6, 3.05], align_center=[0, 1, 2, 3, 4], sp_after=8)

    s += box("QUY TẮC CHẤM ĐIỂM DẠNG ĐÚNG/SAI CẦN BIẾT", [
        "Trong đề thật, mỗi câu Đúng/Sai gồm 4 ý và được chấm theo <b>số ý đúng</b> (thang điểm bậc thang, "
        "thường là 0,1 – 0,25 – 0,5 – 1,0 cho mỗi câu).",
        "Vì vậy chiến lược tối ưu là <b>trả lời tất cả các ý</b>, kể cả khi chưa chắc – một ý đúng vẫn có điểm, "
        "không có điểm trừ.",
        "Đọc kĩ <b>chủ thể</b> và <b>từ tuyệt đối</b> trước khi quyết định.",
    ], "note")

    return s
