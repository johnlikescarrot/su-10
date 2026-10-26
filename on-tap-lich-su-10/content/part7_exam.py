# -*- coding: utf-8 -*-
"""PHẦN VII – Đề kiểm tra tham khảo bám sát ma trận."""

QUESTIONS = [
    # (số, mã ma trận, câu hỏi, [A, B, C, D])
    (1, "I.1",
     "Hiện thực lịch sử là",
     ["những hiểu biết của con người về quá khứ.",
      "toàn bộ những gì đã diễn ra trong quá khứ, tồn tại một cách khách quan.",
      "những ghi chép của các nhà sử học về quá khứ.",
      "những câu chuyện được truyền miệng qua nhiều thế hệ."]),
    (2, "I.2",
     "Đối tượng nghiên cứu của Sử học là",
     ["các hiện tượng tự nhiên trong quá khứ.",
      "tương lai của xã hội loài người.",
      "toàn bộ quá khứ của xã hội loài người.",
      "các tác phẩm văn học dân gian."]),
    (3, "I.3",
     "Một trong ba chức năng của Sử học là",
     ["dự báo xu hướng phát triển của xã hội loài người.",
      "trực tiếp sản xuất ra của cải vật chất cho xã hội.",
      "quy định sự vận động của các quy luật tự nhiên.",
      "tái hiện nguyên vẹn mọi sự kiện như chúng đã diễn ra."]),
    (4, "I.4",
     "Vì sao nói Sử học là một khoa học?",
     ["Vì Sử học chỉ dựa vào những ghi chép của các nhà sử học.",
      "Vì Sử học có đối tượng, phương pháp nghiên cứu và hệ thống tri thức riêng, dựa trên sử liệu và có thể kiểm chứng.",
      "Vì Sử học có thể làm thí nghiệm để tái hiện quá khứ.",
      "Vì Sử học nghiên cứu toàn bộ hiện tượng tự nhiên và xã hội."]),
    (5, "I.5",
     "Cho đoạn tư liệu: “Chiến thắng Bạch Đằng năm 938 là sự kiện có thật; những lời kể khác nhau về "
     "chiến thắng ấy là cách con người nhận thức về sự kiện.” Nhận định nào sau đây đúng?",
     ["Cả hai đều là hiện thực lịch sử.",
      "“Sự kiện có thật” là lịch sử được con người nhận thức.",
      "“Những lời kể khác nhau” là hiện thực lịch sử.",
      "“Sự kiện có thật” là hiện thực lịch sử; “những lời kể khác nhau” là lịch sử được con người nhận thức."]),
    (6, "I.6",
     "Đặc điểm nào sau đây đúng với lịch sử được con người nhận thức?",
     ["Tồn tại khách quan, không phụ thuộc vào người nghiên cứu.",
      "Chỉ diễn ra một lần và không thể lặp lại.",
      "Mang tính chủ quan và có thể được bổ sung, sửa đổi khi có sử liệu mới.",
      "Luôn phản ánh đầy đủ, chính xác hiện thực lịch sử ngay từ đầu."]),
    (7, "I.7",
     "Bước đầu tiên trong quá trình sưu tầm, thu thập, xử lí thông tin và sử liệu là",
     ["lập danh mục các nguồn thông tin, sử liệu cần thu thập.",
      "viết báo cáo kết quả nghiên cứu.",
      "đối chiếu, so sánh các nguồn sử liệu.",
      "phân loại và sắp xếp sử liệu."]),
    (8, "I.8",
     "Những dấu vết, chứng cứ về quá khứ do con người để lại được gọi là",
     ["hiện thực lịch sử.", "sử liệu.", "tri thức lịch sử.", "di sản văn hóa."]),
    (9, "I.9",
     "Sử liệu thành văn là loại sử liệu",
     ["gồm những hiện vật do con người chế tác và sử dụng.",
      "được truyền miệng từ đời này sang đời khác.",
      "chỉ gồm hình ảnh, phim và băng ghi âm.",
      "được ghi chép bằng chữ viết trên các chất liệu khác nhau."]),
    (10, "I.10",
     "Vì sao con người cần học tập và khám phá lịch sử suốt đời?",
     ["Vì tri thức lịch sử là vô cùng; sử liệu mới và cách tiếp cận mới xuất hiện nên hiểu biết về quá khứ "
      "không ngừng được bổ sung, hoàn thiện.",
      "Vì nhà trường không dạy đầy đủ về lịch sử dân tộc.",
      "Vì chỉ người lớn mới cần hiểu biết lịch sử.",
      "Vì đó là điều kiện bắt buộc để thi đỗ."]),
    (11, "I.11",
     "Bản chất của việc kết nối tri thức, bài học lịch sử vào cuộc sống là",
     ["ghi nhớ thật nhiều sự kiện và niên đại.",
      "sưu tầm hiện vật lịch sử để trưng bày.",
      "vận dụng hiểu biết và bài học kinh nghiệm từ quá khứ để giải quyết những vấn đề của hiện tại, "
      "định hướng tương lai.",
      "kể lại các câu chuyện lịch sử cho người khác nghe."]),
    (12, "I.12",
     "Tri thức lịch sử là",
     ["những hiểu biết của con người về quá khứ.",
      "toàn bộ hiện thực lịch sử đã diễn ra.",
      "những hiện vật còn lại từ quá khứ.",
      "những quy định của pháp luật về bảo tồn di sản."]),
    (13, "I.13",
     "Việc làm nào sau đây thể hiện sự chủ động học tập, khám phá lịch sử?",
     ["Chỉ học thuộc nội dung trong sách giáo khoa trước kì thi.",
      "Tìm đọc thêm sách, tham quan di tích, ghi chép và kiểm chứng thông tin từ nhiều nguồn.",
      "Tin ngay mọi thông tin lịch sử được chia sẻ trên mạng xã hội.",
      "Chỉ tìm hiểu lịch sử khi được giao bài tập."]),
    (14, "I.14",
     "Di sản văn hóa bao gồm",
     ["di tích lịch sử và danh lam thắng cảnh.",
      "di sản thiên nhiên và di sản văn hóa.",
      "di sản văn hóa vật thể và di sản văn hóa phi vật thể.",
      "hiện vật bảo tàng và cổ vật."]),
    (15, "I.15",
     "Địa danh nào sau đây là di sản thiên nhiên thế giới ở nước ta?",
     ["Vịnh Hạ Long.", "Hoàng thành Thăng Long.", "Phố cổ Hội An.", "Thánh địa Mỹ Sơn."]),
    (16, "I.16",
     "Vì sao nói Sử học có vai trò quan trọng đối với công tác bảo tồn di sản?",
     ["Vì Sử học có thể tự mình trùng tu mọi di tích.",
      "Vì Sử học quyết định giá vé tham quan di tích.",
      "Vì Sử học thay thế được các ngành khoa học khác.",
      "Vì Sử học cung cấp tri thức khoa học về nguồn gốc, giá trị, hiện trạng di sản — cơ sở để nhận diện, "
      "xếp hạng và đề xuất giải pháp bảo tồn."]),
    (17, "I.17",
     "Nội dung nào sau đây phản ánh đúng vai trò của lịch sử – văn hóa đối với du lịch?",
     ["Làm giảm số lượng khách du lịch đến địa phương.",
      "Cung cấp tài nguyên, tạo nên sản phẩm du lịch đặc thù và hấp dẫn du khách.",
      "Thay thế hoàn toàn tài nguyên du lịch tự nhiên.",
      "Không có ảnh hưởng gì tới hoạt động du lịch."]),
    (18, "I.18",
     "Địa danh nào sau đây là tài nguyên du lịch văn hóa của nước ta?",
     ["Cố đô Huế.", "Vườn quốc gia Cúc Phương.", "Vịnh Hạ Long.", "Mũi Né."]),
    (19, "I.19",
     "Du lịch phát triển có tác động tích cực nào sau đây đến công tác bảo tồn di tích?",
     ["Làm giảm nhu cầu bảo tồn vì di tích đã được nhiều người biết đến.",
      "Thay thế được công tác nghiên cứu khoa học về di sản.",
      "Tạo nguồn thu để trùng tu, tôn tạo và nâng cao nhận thức của cộng đồng về di sản.",
      "Cho phép khai thác di tích mà không cần quy hoạch."]),
    (20, "I.20",
     "Biểu hiện nào sau đây là tác động tiêu cực của du lịch đối với di tích?",
     ["Di tích được trùng tu bằng nguồn thu từ du lịch.",
      "Người dân địa phương có thêm việc làm và thu nhập.",
      "Di sản được quảng bá rộng rãi tới du khách quốc tế.",
      "Di tích xuống cấp, bị xâm hại do quá tải du khách; bản sắc văn hóa bị thương mại hóa."]),
]

TRUE_FALSE = [
    (1, "II.1", "Bài 2 – Tri thức lịch sử và cuộc sống",
     ["Tri thức lịch sử là những hiểu biết của con người về quá khứ.",
      "Chỉ cần học lịch sử ở nhà trường là đủ để hiểu biết đầy đủ về quá khứ.",
      "Sử liệu là những dấu vết, chứng cứ về quá khứ do con người để lại.",
      "Khi sưu tầm tư liệu, chỉ cần dùng một nguồn duy nhất vì mọi nguồn đều đáng tin như nhau."]),
    (2, "II.2", "Bài 3 – Vai trò của Sử học",
     ["Di sản văn hóa gồm di sản văn hóa vật thể và di sản văn hóa phi vật thể.",
      "Du lịch phát triển chỉ mang lại tác động tích cực cho di sản.",
      "Sử học cung cấp tri thức về nguồn gốc, giá trị của di sản, làm cơ sở cho công tác bảo tồn.",
      "Muốn bảo tồn di tích lâu dài thì chỉ cần tăng giá vé tham quan."]),
]

ESSAY = (
    "a) Trình bày vai trò của Sử học đối với công tác bảo tồn và phát huy giá trị di sản văn hóa, "
    "di sản thiên nhiên. (1,0 điểm)\n"
    "b) Chọn một di sản văn hóa hoặc di sản thiên nhiên ở địa phương em (hoặc ở Việt Nam) mà em biết. "
    "Trình bày ngắn gọn giá trị của di sản đó và đề xuất ba giải pháp để bảo tồn, phát huy giá trị "
    "di sản gắn với phát triển du lịch bền vững. (2,0 điểm)"
)


def part_vii():
    items = [
        ("banner", "Phần VII", "Đề kiểm tra tham khảo – Giữa học kì I, Lịch sử 10"),
        ("examhead", (
            "ĐỀ KIỂM TRA GIỮA HỌC KÌ I – NĂM HỌC 2026 – 2027",
            "Môn: Lịch sử – Lớp 10 · Thời gian làm bài: 45 phút (không kể thời gian giao đề)",
            [("Hình thức", "Trắc nghiệm nhiều lựa chọn + trắc nghiệm đúng/sai + tự luận"),
             ("Cấu trúc", "20 câu nhiều lựa chọn (5,0 điểm) · 2 câu đúng/sai, mỗi câu 4 ý (2,0 điểm) · 1 câu tự luận (3,0 điểm)"),
             ("Phạm vi", "Chủ đề 1 (Bài 1, Bài 2) và Chủ đề 2 (Bài 3) – sách Kết nối tri thức với cuộc sống"),
             ("Thang điểm", "10 điểm, làm tròn đến 0,25")],
            "Đề được biên soạn bám đúng ma trận và bản đặc tả trong tệp nguồn: mỗi câu tương ứng một dòng "
            "của ma trận (mã câu ghi trong Phần VIII). Học sinh làm bài trong 45 phút, không sử dụng tài liệu.")),

        ("qgroup", "PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (20 câu · 5,0 điểm)"),
        ("note", "<i>Chọn một phương án đúng nhất trong mỗi câu. Mỗi câu trả lời đúng được 0,25 điểm.</i>"),
    ]

    for num, _code, question, options in QUESTIONS:
        items.append(("q", f"<b>Câu {num}.</b> {question}"))
        items.append(("opts", options))

    items += [
        ("qgroup", "PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu · 2,0 điểm)"),
        ("note", "<i>Trong mỗi câu, hãy xác định mỗi nhận định là Đúng (Đ) hay Sai (S). "
                 "Cách tính điểm mỗi câu: đúng 1 ý được 0,1 điểm; 2 ý được 0,25 điểm; 3 ý được 0,5 điểm; "
                 "4 ý được 1,0 điểm.</i>"),
    ]
    for num, _code, topic, statements in TRUE_FALSE:
        items.append(("q", f"<b>Câu {num}.</b> Cho các nhận định sau về {topic.lower()}:"))
        items.append(("stmt", [(letter, text) for letter, text in zip("abcd", statements)]))

    items += [
        ("qgroup", "PHẦN III. TỰ LUẬN (1 câu · 3,0 điểm)"),
        ("q", f"<b>Câu 1.</b> {ESSAY.splitlines()[0]}"),
        ("p", ESSAY.splitlines()[1]),
        ("sp", 10),
        ("rule",),
        ("note", "Hết — Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm."),
    ]
    return items
