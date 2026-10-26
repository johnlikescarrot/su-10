# -*- coding: utf-8 -*-
"""PHẦN VI – Kĩ năng làm bài và chiến lược 45 phút."""


def part_vi():
    return [
        ("banner", "Phần VI", "Kĩ năng làm bài và chiến lược 45 phút"),
        ("lead",
         "Kiến thức đã đủ mà làm bài sai kĩ thuật thì vẫn mất điểm oan. Phần này hướng dẫn cách chia thời gian, "
         "cách xử lí từng dạng câu và cách viết tự luận để “ăn” trọn thang điểm."),

        ("h2", "1. Phân bổ 45 phút"),
        ("tbl", (
            ["Chặng", "Việc làm", "Thời gian", "Ghi chú"],
            [
                ["1", "Đọc lướt toàn đề, đánh dấu câu chắc chắn / câu cần nghĩ", "2 phút", "Chưa làm bài"],
                ["2", "20 câu trắc nghiệm nhiều lựa chọn", "15 phút", "Khoảng 45 giây/câu"],
                ["3", "2 câu trắc nghiệm đúng/sai (8 ý)", "7 phút", "Khoảng 50 giây/ý"],
                ["4", "1 câu tự luận", "18 phút", "3 phút lập dàn ý, 15 phút viết"],
                ["5", "Soát bài, tô lại đáp án, kiểm tra mã đề", "3 phút", "Không đổi đáp án nếu không có căn cứ"],
            ],
            [14, 86, 26, 50],
        ), None, {"font_size": 8.4, "align_center_cols": (0, 2),
                  "caption": "Bảng 6.1. Phân bổ thời gian cho 45 phút."}),
        ("p",
         "Nguyên tắc vàng: <b>không để câu khó níu chân</b>. Gặp câu chưa chắc, khoanh dấu, chọn phương án "
         "tạm và đi tiếp. Một câu trắc nghiệm chỉ đáng 15–20 giây suy nghĩ thêm; nếu vượt quá, hãy quay lại sau."),

        ("h2", "2. Bảy kĩ thuật làm trắc nghiệm nhiều lựa chọn"),
        ("num", [
            "<b>Đọc hết câu hỏi trước khi đọc phương án.</b> Tự trả lời trong đầu rồi mới xem A, B, C, D — "
            "tránh bị phương án “hấp dẫn” dẫn dắt.",
            "<b>Gạch chân từ khóa.</b> Chú ý các từ phủ định và giới hạn: <i>không</i>, <i>ngoại trừ</i>, "
            "<i>trước tiên</i>, <i>quan trọng nhất</i>, <i>chỉ</i>, <i>luôn</i>, <i>chủ yếu</i>.",
            "<b>Loại trừ theo từng cặp.</b> Với câu hỏi khái niệm, thường hai phương án nói cùng một ý "
            "nhưng một cái sai thuật ngữ — loại cái sai thuật ngữ trước.",
            "<b>Cảnh giác phương án tuyệt đối.</b> “Luôn luôn”, “hoàn toàn”, “chỉ có”, “mọi” thường là bẫy. "
            "Trong lịch sử, sự kiện gắn với điều kiện cụ thể nên hiếm có cái tuyệt đối.",
            "<b>Đọc kĩ phương án “tất cả các ý trên”.</b> Chỉ chọn khi đã kiểm tra từng ý phía trên đều đúng.",
            "<b>Với câu hỏi tình huống:</b> xác định khái niệm nào đang được kiểm tra (hiện thực? nhận thức? "
            "sử liệu?), rồi phân tích từng vế của đoạn văn theo khái niệm ấy.",
            "<b>Chọn đáp án “đúng nhất”, không phải “đúng một phần”.</b> Nhiều phương án có vẻ đúng nhưng "
            "không trả lời trực tiếp câu hỏi.",
        ]),

        ("h2", "3. Cách làm trắc nghiệm đúng/sai"),
        ("p",
         "Mỗi câu có 4 ý a, b, c, d và được chấm theo số ý đúng (1 ý = 0,1; 2 ý = 0,25; 3 ý = 0,5; 4 ý = 1,0). "
         "Vì thế chiến lược là <b>xét từng ý độc lập</b>, không suy đoán theo “cụm”."),
        ("bul", [
            "Đọc cả 4 ý một lượt để nắm chủ đề, sau đó quay lại xét từng ý.",
            "Mỗi ý thường kiểm tra <b>một</b> chi tiết: một định nghĩa, một đặc điểm, một vai trò, một cách làm. "
            "Hãy chỉ ra chi tiết ấy đúng hay sai.",
            "Cẩn thận với ý có từ <b>“chỉ”</b>, <b>“duy nhất”</b>, <b>“luôn”</b> — phần lớn là sai.",
            "Ý có mệnh đề <b>“vì vậy”, “do đó”</b> phải kiểm tra cả nguyên nhân lẫn kết luận; một vế sai là cả ý sai.",
            "Nếu phân vân, hãy tự hỏi: “Nếu ý này đúng thì có phản ví dụ nào trong bài không?”",
        ]),
        ("box", "trap", "Ba lỗi hay gặp ở phần đúng/sai",
         [("bul", [
             "<b>Suy diễn theo câu trước:</b> thấy hai ý đầu đúng thì ý sau cũng đánh đúng. Mỗi ý phải xét riêng.",
             "<b>Bỏ qua một vế:</b> ý có hai mệnh đề, chỉ kiểm tra mệnh đề đầu.",
             "<b>Không dám đánh “Sai”:</b> nhiều học sinh có tâm lí “đề cho câu này chắc đúng”, dẫn tới sai cả cụm.",
         ])]),

        ("h2", "4. Cách viết bài tự luận 3,0 điểm"),
        ("h3", "4.1. Quy trình 18 phút"),
        ("num", [
            "<b>Xác định yêu cầu (1 phút):</b> gạch chân các lệnh: <i>trình bày</i>, <i>phân tích</i>, "
            "<i>giải thích</i>, <i>liên hệ</i>, <i>đề xuất</i>. Mỗi lệnh ứng với một phần bài.",
            "<b>Lập dàn ý (2 phút):</b> ghi ra giấy nháp 4–6 gạch đầu dòng, kèm ví dụ sẽ dùng.",
            "<b>Viết (13 phút):</b> mở bài 2–3 câu, thân bài theo từng ý (mỗi ý 3–4 câu: nêu – chứng – kết), "
            "kết bài 2–3 câu.",
            "<b>Soát (2 phút):</b> kiểm tra chính tả, dấu câu, và quan trọng nhất: đã trả lời đủ các lệnh chưa.",
        ]),
        ("h3", "4.2. Bốn lệnh và cách đáp ứng"),
        ("tbl", (
            ["Lệnh trong đề", "Việc phải làm", "Dấu hiệu đạt"],
            [
                ["Trình bày", "Nêu các nội dung, sắp xếp theo thứ tự logic, không cần bàn sâu", "Đủ ý, có thứ tự, có ví dụ"],
                ["Phân tích", "Tách một vấn đề thành các mặt rồi chỉ ra quan hệ giữa chúng", "Có “mặt thứ nhất… mặt thứ hai…”, có lí giải"],
                ["Giải thích", "Trả lời “vì sao”, dùng căn cứ (khái niệm, sự kiện, quy luật)", "Có từ “vì”, “do”, dẫn chứng cụ thể"],
                ["Liên hệ / đề xuất", "Gắn nội dung bài học với thực tế địa phương, bản thân; nêu giải pháp khả thi", "Có địa danh/việc làm cụ thể, không chung chung"],
            ],
            [30, 84, 62],
        ), None, {"font_size": 8.4, "first_col_bold": True,
                  "caption": "Bảng 6.2. Bốn lệnh thường gặp trong câu tự luận."}),
        ("h3", "4.3. Cách ghi điểm từng phần"),
        ("bul", [
            "<b>Mở bài</b> chỉ cần khẳng định vấn đề, đừng kể lể. Ví dụ: “Sử học có vai trò đặc biệt quan trọng "
            "đối với công tác bảo tồn và phát huy giá trị di sản.”",
            "<b>Mỗi ý một đoạn</b>, mở đầu bằng câu chủ đề in đậm ý, sau đó chứng minh bằng ví dụ, "
            "kết bằng hệ quả.",
            "<b>Luôn có ví dụ.</b> Một bài có 4 ý mà không có ví dụ nào thường chỉ đạt 60–70% điểm của phần ấy.",
            "<b>Phần vận dụng phải cụ thể:</b> nêu tên di sản, địa phương; giải pháp phải làm được "
            "(ai làm, làm gì), không viết “cần nâng cao nhận thức” rồi hết.",
            "<b>Trình bày sạch, chia đoạn, gạch đầu dòng cho ý phụ</b> — giám khảo chấm nhanh, bài rõ ràng dễ được điểm.",
        ]),
        ("h2", "5. Sáu lỗi mất điểm oan"),
        ("tbl", (
            ["Lỗi", "Hậu quả", "Cách tránh"],
            [
                ["Không đọc hết câu, bỏ qua từ “không”", "Chọn đúng phương án nhưng sai yêu cầu", "Gạch chân từ khóa trước khi chọn"],
                ["Tô đáp án lệch dòng", "Mất cả loạt câu", "Tô theo từng cụm 5 câu, kiểm tra số thứ tự"],
                ["Sa vào câu khó quá lâu", "Hết giờ, mất phần tự luận", "Đánh dấu và quay lại; tự luận luôn làm trước khi soát"],
                ["Tự luận không có ví dụ", "Mất 30–40% điểm phần vận dụng", "Luôn chuẩn bị sẵn 2 ví dụ: một di sản, một địa phương"],
                ["Viết lan man, không đúng lệnh", "Không được điểm dù viết dài", "Bám sát bốn lệnh: trình bày, phân tích, giải thích, liên hệ"],
                ["Không soát bài", "Sai chính tả, thiếu ý, mất 0,25–0,5 điểm", "Dành 3 phút cuối soát từ trên xuống"],
            ],
            [54, 62, 60],
        ), None, {"font_size": 8.4,
                  "caption": "Bảng 6.3. Sáu lỗi phổ biến và cách phòng."}),
        ("box", "tip", "Mẹo tâm lí phòng thi",
         [("p", "Khi gặp câu làm mình “tắc”, hãy thở chậm ba nhịp, đọc lại câu hỏi và tự hỏi: "
                "“Câu này đang kiểm tra khái niệm nào trong ba bài?”. Xác định được khái niệm là gần như "
                "chắc chắn loại được hai phương án sai.")]),
    ]
