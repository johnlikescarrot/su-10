# -*- coding: utf-8 -*-
"""PHẦN I – Định hướng ôn tập (phân tích ma trận và bản đặc tả)."""




def part_i():
    return [
        ("banner", "Phần I", "Định hướng ôn tập: đọc đúng ma trận, học đúng trọng tâm"),
        ("lead",
         "Trước khi học thuộc bất cứ nội dung nào, hãy đọc kĩ phần này. Ma trận và bản đặc tả "
         "trong tệp nguồn cho biết chính xác bài nào được hỏi, hỏi ở mức độ nào và chiếm bao nhiêu "
         "điểm. Học theo ma trận giúp em dồn sức đúng chỗ thay vì học tràn lan."),

        ("h2", "1. Tệp nguồn có gì?"),
        ("p",
         "Tệp <b>LS10- MTGK1-26-27-HHT.docx</b> là bộ công cụ kiểm tra của giáo viên, gồm "
         "<b>hai bảng</b>: (1) <b>Ma trận kiểm tra định kì giữa học kì 1 – khối 10</b>, năm học "
         "2026 – 2027, thời gian 45 phút; (2) <b>Bảng đặc tả ma trận đề kiểm tra</b> – diễn giải "
         "ma trận thành các yêu cầu cần đạt cụ thể, gắn mỗi yêu cầu với số hiệu câu hỏi."),
        ("p",
         "Tên tệp cho biết: <b>LS10</b> – Lịch sử lớp 10; <b>MTGK1</b> – ma trận giữa kì 1; "
         "<b>26-27</b> – năm học 2026 – 2027. Bản thân tệp <b>không chứa nội dung câu hỏi và đáp án</b>; "
         "vì thế Phần VII và Phần VIII của đề cương này là đề kiểm tra tham khảo được biên soạn "
         "bám đúng từng dòng của ma trận, kèm đáp án và giải thích chi tiết."),

        ("tbl", (
            ["Nội dung", "Thông tin trong tệp nguồn"],
            [
                ["Cấu trúc đề", "20 câu trắc nghiệm nhiều lựa chọn + 2 câu trắc nghiệm đúng/sai (mỗi câu 4 ý) + 1 câu tự luận"],
                ["Số lệnh hỏi", "28 lệnh hỏi trắc nghiệm (20 câu + 8 ý đúng/sai) và 1 câu tự luận"],
                ["Thời gian", "45 phút"],
                ["Phạm vi", "Chủ đề 1 – Lịch sử và Sử học (Bài 1, Bài 2); Chủ đề 2 – Vai trò của Sử học (Bài 3)"],
                ["Năng lực", "NL1 – Tìm hiểu lịch sử; NL2 – Nhận thức và tư duy lịch sử; NL3 – Vận dụng kiến thức, kĩ năng"],
                ["Cấp độ tư duy", "Biết – Hiểu – Vận dụng"],
            ],
            [34, 142],
        ), None, {"first_col_bold": True, "caption": "Bảng 1.1. Thông tin rút ra từ ma trận và bản đặc tả."}),

        ("h2", "2. Ma trận chi tiết: từng câu hỏi thuộc bài nào?"),
        ("p",
         "Bảng dưới đây là bản “giải mã” đầy đủ của ma trận. Cột <b>Câu</b> giữ nguyên kí hiệu "
         "trong tệp gốc: <b>I.</b> là phần trắc nghiệm nhiều lựa chọn, <b>II.</b> là phần trắc nghiệm "
         "đúng/sai (a, b, c, d là bốn ý), <b>TL</b> là tự luận. Điểm mỗi câu được tính theo hình thức "
         "đề: 0,25 điểm/câu trắc nghiệm, 1,0 điểm/câu đúng/sai, 3,0 điểm/câu tự luận."),
        ("tbl", (
            ["Câu", "Đơn vị kiến thức", "Năng lực", "Cấp độ", "Điểm"],
            [
                ["I.1, I.2, I.3", "Bài 1 – khái niệm lịch sử; đối tượng, chức năng, nhiệm vụ của Sử học", "NL1", "Biết", "0,75"],
                ["I.4", "Bài 1 – giải thích khái niệm Sử học", "NL1", "Hiểu", "0,25"],
                ["I.5, I.6", "Bài 1 – phân biệt hiện thực lịch sử và lịch sử được con người nhận thức", "NL2", "Hiểu", "0,50"],
                ["I.7, I.8, I.9", "Bài 2 – các bước thu thập, xử lí thông tin, sử liệu", "NL1", "Biết", "0,75"],
                ["I.10, I.11", "Bài 2 – sự cần thiết học tập suốt đời; bản chất kết nối tri thức vào cuộc sống", "NL1", "Hiểu", "0,50"],
                ["I.12, I.13", "Bài 2 – nhận diện tri thức lịch sử và cách học tập chủ động", "NL2", "Biết", "0,50"],
                ["II.1a", "Bài 2 – nhận diện khái niệm tri thức lịch sử", "NL2", "Biết", "0,25"],
                ["II.1b", "Bài 2 – lí do học tập suốt đời", "NL2", "Hiểu", "0,25"],
                ["II.1c", "Bài 2 – nhận diện sử liệu", "NL3", "Biết", "0,25"],
                ["II.1d", "Bài 2 – vận dụng nguyên tắc xử lí tư liệu", "NL3", "Vận dụng", "0,25"],
                ["I.14, I.15", "Bài 3 – loại hình di sản; địa danh là tài nguyên du lịch", "NL1", "Biết", "0,50"],
                ["I.16", "Bài 3 – vai trò của Sử học với bảo tồn di sản", "NL1", "Hiểu", "0,25"],
                ["I.17, I.18", "Bài 3 – vai trò của lịch sử – văn hóa với du lịch", "NL2", "Biết", "0,50"],
                ["I.19, I.20", "Bài 3 – tác động của du lịch đến bảo tồn di tích", "NL2", "Hiểu", "0,50"],
                ["II.2a", "Bài 3 – nhận diện loại hình di sản văn hóa", "NL2", "Biết", "0,25"],
                ["II.2b", "Bài 3 – đánh giá tác động hai chiều của du lịch", "NL2", "Hiểu", "0,25"],
                ["II.2c", "Bài 3 – nhận diện vai trò của Sử học", "NL3", "Biết", "0,25"],
                ["II.2d", "Bài 3 – vận dụng vào bảo tồn và phát triển du lịch bền vững", "NL3", "Vận dụng", "0,25"],
                ["TL.a", "Bài 3 – trình bày vai trò của Sử học với di sản", "NL1", "Biết", "1,00"],
                ["TL.b", "Bài 3 – liên hệ, đề xuất giải pháp bảo tồn gắn với du lịch", "NL3", "Vận dụng", "2,00"],
            ],
            [26, 88, 20, 24, 18],
        ), None, {"font_size": 8.2, "align_center_cols": (0, 2, 3, 4),
                  "caption": "Bảng 1.2. Đối chiếu từng lệnh hỏi với đơn vị kiến thức, năng lực và cấp độ tư duy."}),

        ("h2", "3. Trọng số điểm: học gì trước, học gì kĩ?"),
        ("tbl", (
            ["Năng lực – cấp độ", "Số lệnh hỏi", "Điểm", "Tỉ lệ"],
            [
                ["NL1 – Biết", "8 câu + ½ tự luận", "3,00", "30%"],
                ["NL1 – Hiểu", "4 câu", "1,00", "10%"],
                ["NL2 – Biết", "6 câu", "1,50", "15%"],
                ["NL2 – Hiểu", "6 câu", "1,50", "15%"],
                ["NL3 – Biết", "2 câu", "0,50", "5%"],
                ["NL3 – Vận dụng", "2 câu + ½ tự luận", "2,50", "25%"],
                ["Tổng", "28 lệnh hỏi + 1 tự luận", "10,00", "100%"],
            ],
            [78, 40, 26, 32],
        ), None, {"align_center_cols": (1, 2, 3), "first_col_bold": True,
                  "caption": "Bảng 1.3. Trọng số theo ma trận (dòng tổng được tính lại cho khớp điểm)."}),
        ("p",
         "Ba nhận xét quan trọng rút ra từ bảng trên:"),
        ("num", [
            "<b>65% số điểm nằm ở mức Biết và Hiểu.</b> Chỉ cần nắm chắc khái niệm, đặc điểm, "
            "chức năng, các bước và danh mục di sản là đã có khoảng 6,5 điểm. Đây là phần “học là có điểm”.",
            "<b>25% số điểm là Vận dụng</b>, tập trung vào hai câu đúng/sai (II.1d, II.2d) và "
            "<b>2,0 điểm</b> của bài tự luận. Muốn điểm cao phải luyện cách liên hệ, đề xuất giải pháp.",
            "<b>Bài 3 chiếm tới 5,75 điểm</b> (7 câu trắc nghiệm + 1 câu đúng/sai + cả bài tự luận), "
            "trong khi Bài 1 chỉ 1,50 điểm. Nếu thời gian eo hẹp, ưu tiên Bài 3 rồi mới đến Bài 2, Bài 1.",
        ]),

        ("h2", "4. Cách dùng đề cương này trong 7 ngày"),
        ("num", [
            "<b>Lượt 1 – Hiểu (ngày 1–3):</b> đọc Phần II, III, IV. Với mỗi mục, che phần chữ, "
            "tự trả lời câu hỏi ở tiêu đề trước khi đọc tiếp. Đánh dấu bút chì vào chỗ chưa nhớ.",
            "<b>Lượt 2 – Nhớ (ngày 4–5):</b> học thuộc Bảng tổng hợp ở Phần V và các hộp “Mẹo nhớ”. "
            "Tự viết lại sơ đồ từng bài trên giấy trắng, không nhìn sách.",
            "<b>Lượt 3 – Luyện (ngày 6):</b> làm Phần VII trong đúng 45 phút, không mở tài liệu. "
            "Chấm bằng Phần VIII, ghi lại từng câu sai và lí do sai.",
            "<b>Lượt 4 – Vá lỗ hổng (ngày 7):</b> chỉ học lại những mục ứng với câu sai, làm lại "
            "30 câu tự kiểm tra ở Phần IX, đọc lại Phần VI (kĩ năng làm bài) trước khi thi.",
        ]),
        ("box", "tip", "Nguyên tắc học hiệu quả",
         [("p", "Học theo ba câu hỏi: <b>Đây là gì? Vì sao quan trọng? Khác gì với cái dễ nhầm?</b> "
                "Trả lời được cả ba là hiểu, không cần học thuộc lòng từng chữ. Với mỗi khái niệm, "
                "hãy tự lấy <b>một ví dụ riêng</b> — ví dụ do mình nghĩ ra nhớ lâu hơn ví dụ trong sách.")],
         ),
        ("sp", 2),
        ("box", "memo", "Ba con số cần nhớ về đề",
         [("bul", [
             "<b>45 phút</b> – thời gian làm bài.",
             "<b>28 lệnh hỏi trắc nghiệm + 1 tự luận</b> – cấu trúc đề.",
             "<b>30% – 10% – 15% – 15% – 5% – 25%</b> – sáu mức trọng số theo năng lực và cấp độ.",
         ])]),
    ]
