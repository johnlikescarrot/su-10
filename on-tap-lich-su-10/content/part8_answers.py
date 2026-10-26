# -*- coding: utf-8 -*-
"""PHẦN VIII – Đáp án, giải thích chi tiết và biểu điểm."""

from .part7_exam import ESSAY, QUESTIONS, TRUE_FALSE

ANSWER_KEY = {
    1: "B", 2: "C", 3: "A", 4: "B", 5: "D", 6: "C", 7: "A", 8: "B", 9: "D", 10: "A",
    11: "C", 12: "A", 13: "B", 14: "C", 15: "A", 16: "D", 17: "B", 18: "A", 19: "C", 20: "D",
}

EXPLANATIONS = {
    1: ("B", "Đúng định nghĩa hiện thực lịch sử: toàn bộ những gì đã diễn ra, tồn tại khách quan. "
            "A là tri thức/nhận thức; C là ghi chép của nhà sử học (nhận thức); D là truyền miệng (một hình thức nhận thức)."),
    2: ("C", "Đối tượng của Sử học là quá khứ của xã hội loài người. A sai vì tự nhiên chỉ được xét trong "
            "quan hệ với con người; B sai vì tương lai không phải đối tượng nghiên cứu; D sai vì văn học dân gian "
            "chỉ là một nguồn tư liệu."),
    3: ("A", "Ba chức năng là khoa học – giáo dục – dự báo, nên “dự báo xu hướng phát triển” là đáp án đúng. "
            "B, C là chức năng của các lĩnh vực khác; D sai cả về chức năng lẫn khả năng (không thể tái hiện nguyên vẹn)."),
    4: ("B", "Sử học là khoa học vì có đối tượng xác định, phương pháp riêng, hệ thống tri thức và căn cứ sử liệu "
            "kiểm chứng được. A mô tả cách làm phiến diện; C sai vì quá khứ không thể thực nghiệm lại; D sai vì "
            "Sử học không nghiên cứu toàn bộ tự nhiên."),
    5: ("D", "Cần tách hai vế: sự kiện đã xảy ra là hiện thực; cách kể, cách lí giải là nhận thức. A gộp sai; "
            "B, C đảo ngược hai khái niệm."),
    6: ("C", "Lịch sử được con người nhận thức mang tính chủ quan, đa dạng và có thể bổ sung, sửa đổi. "
            "A, B là đặc điểm của hiện thực lịch sử; D sai vì nhận thức luôn có thể thiếu hoặc lệch."),
    7: ("A", "Bước 1 là lập danh mục nguồn cần thu thập. B là bước 4 (trình bày); C, D thuộc bước 3 (xử lí). "
            "Nhớ gói MỤC – THU – XỬ – TRÌNH."),
    8: ("B", "“Dấu vết, chứng cứ về quá khứ do con người để lại” là định nghĩa sử liệu. A là cái đã xảy ra; "
            "C là hiểu biết; D là một bộ phận của sử liệu, không phải toàn bộ khái niệm."),
    9: ("D", "Sử liệu thành văn là tư liệu ghi bằng chữ viết trên các chất liệu khác nhau (bia đá, sách, sắc phong…). "
            "A là sử liệu vật chất; B là truyền miệng; C là sử liệu hình ảnh, âm thanh."),
    10: ("A", "Hai lí do cốt lõi: tri thức lịch sử vô cùng, và nhận thức lịch sử luôn được bổ sung nhờ sử liệu, "
             "phương pháp mới. B, C, D là cách lí giải phiến diện hoặc sai."),
    11: ("C", "Bản chất là vận dụng bài học quá khứ để giải quyết vấn đề hiện tại và định hướng tương lai. "
             "A là ghi nhớ; B là sưu tầm; D là truyền đạt — đều chưa phải kết nối."),
    12: ("A", "Tri thức lịch sử là hiểu biết của con người về quá khứ. B là hiện thực; C là sử liệu/hiện vật; "
             "D thuộc lĩnh vực pháp luật."),
    13: ("B", "Chủ động học tập là tìm thêm nguồn, trải nghiệm và kiểm chứng. A, D thụ động; C phản khoa học "
             "vì tin ngay thông tin chưa kiểm chứng."),
    14: ("C", "Di sản văn hóa gồm vật thể và phi vật thể. A chỉ là một phần của di sản vật thể; B là cách phân "
             "loại theo lĩnh vực, không phải cấu trúc của khái niệm; D là các loại hiện vật cụ thể."),
    15: ("A", "Vịnh Hạ Long là di sản thiên nhiên thế giới (được mở rộng, gắn với quần đảo Cát Bà). "
             "B, C, D đều là di sản văn hóa."),
    16: ("D", "Sử học cung cấp tri thức khoa học về nguồn gốc, giá trị, hiện trạng — cơ sở để nhận diện, "
             "xếp hạng và đề xuất giải pháp bảo tồn. A, B, C phóng đại hoặc hiểu sai vai trò của Sử học."),
    17: ("B", "Lịch sử – văn hóa cung cấp tài nguyên du lịch và tạo sản phẩm đặc thù. A, D trái thực tế; "
             "C sai vì không “thay thế” tài nguyên tự nhiên mà bổ sung, cộng hưởng."),
    18: ("A", "Cố đô Huế là di sản văn hóa (quần thể di tích). B, C, D là tài nguyên du lịch tự nhiên: "
             "rừng quốc gia, vịnh biển, bãi biển."),
    19: ("C", "Du lịch tạo nguồn thu để trùng tu và nâng cao nhận thức cộng đồng. A, B, D đều là cách hiểu "
             "phản khoa học, biến du lịch thành lí do để buông lỏng bảo tồn."),
    20: ("D", "Quá tải và thương mại hóa là hai biểu hiện tiêu cực điển hình. A, B, C đều là tác động tích cực."),
}

TF_ANSWERS = {
    ("II.1", "a"): ("Đ", "Đúng định nghĩa tri thức lịch sử."),
    ("II.1", "b"): ("S", "Còn nhiều kênh khác: bảo tàng, di tích, sách, internet có kiểm chứng, trải nghiệm; "
                          "tri thức lịch sử lại luôn được bổ sung nên không thể “đủ” nếu chỉ học ở trường."),
    ("II.1", "c"): ("Đ", "Đúng định nghĩa sử liệu."),
    ("II.1", "d"): ("S", "Phải dùng nhiều nguồn, đối chiếu và kiểm chứng; một nguồn duy nhất không đủ độ tin cậy."),
    ("II.2", "a"): ("Đ", "Đúng cấu trúc khái niệm di sản văn hóa."),
    ("II.2", "b"): ("S", "Du lịch có cả tác động tiêu cực: quá tải, xuống cấp, thương mại hóa, ô nhiễm."),
    ("II.2", "c"): ("Đ", "Đúng vai trò cơ bản của Sử học với bảo tồn."),
    ("II.2", "d"): ("S", "Bảo tồn cần tổng hợp giải pháp: quy hoạch, giới hạn sức chứa, đầu tư, giáo dục, "
                         "chia sẻ lợi ích cộng đồng, giám sát."),
}

SAMPLE_ESSAY = [
    ("p", "<b>Mở bài.</b> Sử học không chỉ nghiên cứu quá khứ mà còn trực tiếp góp phần giữ gìn và làm sống "
           "lại những giá trị di sản. Vai trò ấy thể hiện ở cả phương diện khoa học, thực tiễn và giáo dục."),
    ("p", "<b>1. Cung cấp tri thức khoa học về di sản.</b> Sử học làm rõ nguồn gốc, quá trình hình thành, "
           "chủ thể sáng tạo, giá trị lịch sử – văn hóa – khoa học – thẩm mĩ và hiện trạng của di sản. "
           "Ví dụ, nhờ nghiên cứu sử học, Khu trung tâm Hoàng thành Thăng Long được nhận diện là dấu tích "
           "kinh đô của các triều đại Lý – Trần – Lê."),
    ("p", "<b>2. Là căn cứ để nhận diện, đánh giá và xếp hạng di sản.</b> Hồ sơ khoa học do nhà sử học, "
           "nhà bảo tàng lập là cơ sở để công nhận di tích cấp tỉnh, cấp quốc gia, di sản thế giới; đồng thời "
           "xác định mức độ xuống cấp để ưu tiên nguồn lực."),
    ("p", "<b>3. Đề xuất, tư vấn giải pháp bảo tồn, tôn tạo, phục dựng.</b> Sử học phân định đâu là yếu tố gốc "
           "phải giữ, đâu là phần có thể can thiệp, theo các nguyên tắc: tính xác thực, tính toàn vẹn và "
           "can thiệp tối thiểu. Thiếu căn cứ ấy, việc trùng tu dễ biến di tích thành công trình “làm mới”."),
    ("p", "<b>4. Giáo dục, truyền thông nâng cao nhận thức cộng đồng.</b> Khi người dân hiểu giá trị di sản, "
           "họ tự giác giữ gìn — đây là lớp bảo vệ bền vững nhất, không hàng rào nào thay thế được."),
    ("p", "<b>5. Gắn bảo tồn với phát huy giá trị.</b> Sử học đưa di sản trở lại đời sống qua trưng bày, "
           "giáo dục, du lịch và sản phẩm văn hóa, để di sản “sống” chứ không chỉ được giữ trong tủ kính."),
    ("p", "<b>b) Liên hệ: Phố cổ Hội An (Quảng Nam).</b>"),
    ("p", "<b>Giá trị:</b> Hội An là đô thị cổ – thương cảng từng sầm uất của Đàng Trong thế kỉ XVI – XVIII, "
           "nơi giao thoa kiến trúc Việt – Hoa – Nhật; quần thể nhà cổ, hội quán, chùa Cầu, giếng cổ cùng "
           "các nghề truyền thống và lễ hội tạo nên một chỉnh thể văn hóa còn khá nguyên vẹn, là bài học sống "
           "động về giao lưu và hội nhập văn hóa."),
    ("p", "<b>Ba giải pháp:</b>"),
    ("bul", [
        "<b>Quy hoạch và giới hạn sức chứa:</b> xác định số khách tối đa trong khu phố cổ, phân luồng theo "
        "khung giờ, mở rộng tuyến tham quan sang các điểm vệ tinh để giảm áp lực lên khu lõi.",
        "<b>Đầu tư trở lại cho bảo tồn, tu bổ đúng kĩ thuật:</b> trích một phần doanh thu du lịch cho trùng tu; "
        "ưu tiên vật liệu và kĩ thuật truyền thống; chống mối mọt, ngập úng cho nhà cổ; giám sát chặt việc "
        "cải tạo, sửa chữa của hộ dân.",
        "<b>Giáo dục du khách và chia sẻ lợi ích với cộng đồng:</b> nội quy ứng xử, thuyết minh về giá trị "
        "di sản; khuyến khích người dân làm homestay, bán sản phẩm thủ công, biểu diễn nghệ thuật truyền thống "
        "để họ vừa hưởng lợi vừa trở thành người bảo vệ di sản.",
    ]),
    ("p", "<b>Liên hệ bản thân.</b> Là học sinh, em có thể tìm hiểu kĩ về di sản địa phương, tham gia các buổi "
           "giới thiệu di sản, ứng xử văn minh khi tham quan và truyền đạt lại cho bạn bè, người thân — bắt đầu "
           "từ những việc nhỏ như không xả rác, không chạm vào hiện vật."),
    ("p", "<b>Kết bài.</b> Sử học vừa là “người kể chuyện” vừa là “người bảo vệ” di sản. Mỗi giải pháp đúng đắn "
           "hôm nay là cách để thế hệ sau vẫn còn cơ hội gặp lại những giá trị mà cha ông đã dày công giữ gìn."),
]


def part_viii():
    items = [
        ("banner", "Phần VIII", "Đáp án – Giải thích chi tiết – Biểu điểm"),
        ("lead",
         "Đáp án được trình bày theo đúng thứ tự đề, kèm lí do chọn và lí do loại các phương án còn lại. "
         "Khi chấm bài của mình, đừng chỉ đánh dấu đúng/sai: hãy ghi lại <b>vì sao</b> mình chọn sai — đó mới là "
         "phần giúp tăng điểm nhanh nhất."),

        ("h2", "1. Đáp án phần I – Trắc nghiệm nhiều lựa chọn"),
    ]

    rows = []
    for i in range(0, 20, 2):
        a, b = i + 1, i + 2
        rows.append([f"Câu {a}", f"<b>{ANSWER_KEY[a]}</b>", f"Câu {b}", f"<b>{ANSWER_KEY[b]}</b>"])
    items.append(("tbl", (
        ["Câu", "Đáp án", "Câu", "Đáp án"], rows, [38, 50, 38, 50],
    ), None, {"font_size": 9.2, "align_center_cols": (0, 1, 2, 3),
              "caption": "Bảng 8.1. Đáp án 20 câu trắc nghiệm nhiều lựa chọn."}))

    items.append(("h2", "2. Giải thích chi tiết từng câu"))
    items.append(("note", "<i>Mỗi mục gồm: đáp án đúng và căn cứ; các phương án còn lại sai ở đâu.</i>"))
    for num, code, question, options in QUESTIONS:
        letter, why = EXPLANATIONS[num]
        items.append(("p", f"<b>Câu {num} (mã {code}) – {letter}.</b> {why}"))

    items += [
        ("h2", "3. Đáp án phần II – Trắc nghiệm đúng/sai"),
        ("tbl", (
            ["Câu", "Ý", "Đáp án", "Căn cứ"],
            [[f"Câu {num}", f"{letter})", f"<b>{TF_ANSWERS[(code, letter)][0]}</b>",
              TF_ANSWERS[(code, letter)][1]]
             for num, code, _topic, st in TRUE_FALSE for letter, _t in zip("abcd", st)],
            [16, 10, 20, 130],
        ), None, {"font_size": 8.4, "align_center_cols": (0, 1, 2),
                  "caption": "Bảng 8.2. Đáp án 8 ý đúng/sai."}),
        ("p",
         "<b>Cách tính điểm phần II:</b> mỗi câu 1,0 điểm, chia theo số ý đúng — 1 ý đúng được 0,1 điểm; "
         "2 ý đúng được 0,25 điểm; 3 ý đúng được 0,5 điểm; 4 ý đúng được 1,0 điểm. Vì vậy, khi làm bài, "
         "hãy cố xác định chắc chắn từng ý thay vì bỏ trống."),

        ("h2", "4. Đáp án và biểu điểm câu tự luận"),
        ("box", "def", "Đề bài",
         [("p", ESSAY.replace("\n", "<br/>"))]),
        ("h3", "4.1. Bài làm tham khảo"),
    ]
    items.extend(SAMPLE_ESSAY)

    items += [
        ("h3", "4.2. Biểu điểm chi tiết (tổng 3,0 điểm)"),
        ("tbl", (
            ["Phần", "Yêu cầu", "Điểm"],
            [
                ["Mở bài", "Khẳng định vai trò của Sử học với bảo tồn, phát huy giá trị di sản", "0,25"],
                ["Ý 1", "Cung cấp tri thức khoa học về nguồn gốc, giá trị, hiện trạng di sản (có ví dụ)", "0,25"],
                ["Ý 2", "Là căn cứ nhận diện, đánh giá, xếp hạng, lập hồ sơ di sản", "0,25"],
                ["Ý 3", "Đề xuất, tư vấn giải pháp bảo tồn theo nguyên tắc xác thực – toàn vẹn – can thiệp tối thiểu", "0,25"],
                ["Kết bài", "Khẳng định lại, liên hệ trách nhiệm thế hệ trẻ", "0,25"],
                ["Vận dụng 1", "Chọn được di sản cụ thể, nêu đúng và đủ giá trị (tên, loại, giá trị tiêu biểu)", "0,5"],
                ["Vận dụng 2", "Ba giải pháp khả thi, gắn bảo tồn với du lịch bền vững (mỗi giải pháp 0,33)", "1,0"],
                ["Vận dụng 3", "Lập luận, liên hệ bản thân, diễn đạt mạch lạc", "0,25"],
                ["Tổng", "", "3,0"],
            ],
            [30, 128, 18],
        ), None, {"font_size": 8.4, "align_center_cols": (2,), "first_col_bold": True,
                  "caption": "Bảng 8.3. Biểu điểm câu tự luận."}),
        ("note",
         "<b>Lưu ý khi chấm:</b> học sinh không nhất thiết phải trình bày đúng năm ý như bài mẫu; nếu nêu được "
         "4 ý có căn cứ và ví dụ vẫn đạt điểm tối đa của phần a. Ở phần b, giải pháp phải cụ thể (ai làm, làm gì) "
         "mới được tính điểm; các câu chung chung như “cần nâng cao nhận thức” chỉ được tối đa 0,25 điểm."),

        ("h2", "5. Bảng tự đánh giá sau khi làm bài"),
        ("tbl", (
            ["Câu", "Mã ma trận", "Điểm", "Em làm đúng?", "Ghi chú (lí do sai)"],
            [[f"{n}", code, "0,25", "□ Đúng  □ Sai", ""] for n, code, *_ in QUESTIONS] +
            [["II.1", "II.1a–d", "1,0", "□ Đúng  □ Sai", ""],
             ["II.2", "II.2a–d", "1,0", "□ Đúng  □ Sai", ""],
             ["TL", "TL.a–b", "3,0", "□ Đúng  □ Sai", ""],
             ["<b>Tổng</b>", "", "<b>10,0</b>", "", ""]],
            [16, 34, 18, 46, 62],
        ), None, {"font_size": 8.2, "align_center_cols": (0, 1, 2), "zebra": True,
                  "caption": "Bảng 8.4. In ra và điền sau mỗi lần luyện đề."}),
        ("box", "tip", "Cách dùng bảng tự đánh giá",
         [("p", "Sau khi chấm, hãy cộng điểm theo từng bài (Bài 1: câu 1–6; Bài 2: câu 7–13 + II.1; "
                "Bài 3: câu 14–20 + II.2 + tự luận). Bài nào dưới 60% thì phải học lại bài đó trước khi "
                "làm đề tiếp theo. Đây là cách học “đúng chỗ đau” thay vì học lại từ đầu.")]),
    ]
    return items
