# -*- coding: utf-8 -*-
"""PHỤ LỤC – Ghi chú biên soạn và hướng dẫn tái tạo tài liệu."""


def appendix():
    return [
        ("banner", "Phụ lục", "Ghi chú biên soạn, đối chiếu và tái tạo tài liệu"),
        ("lead",
         "Phần này dành cho giáo viên và người dùng tài liệu: nó nói rõ tài liệu được làm từ nguồn nào, "
         "phần nào là nguyên văn từ nguồn, phần nào là nội dung biên soạn thêm, và cách tái tạo tệp PDF."),

        ("h2", "1. Tệp nguồn và phạm vi"),
        ("p",
         "Tệp <b>LS10- MTGK1-26-27-HHT.docx</b> (32 KB) được phân tích trực tiếp từ cấu trúc XML của tài liệu Word. "
         "Kết quả: tệp gồm <b>45 khối nội dung</b>, trong đó có <b>hai bảng</b> là toàn bộ phần chuyên môn:"),
        ("bul", [
            "<b>Bảng 1 – Ma trận kiểm tra định kì giữa học kì 1, khối 10</b>, năm học 2026 – 2027, "
            "thời gian 45 phút: 10 dòng, phân bố theo chủ đề, đơn vị kiến thức, ba năng lực và ba cấp độ tư duy.",
            "<b>Bảng 2 – Bản đặc tả ma trận đề kiểm tra</b>: 10 dòng, diễn giải yêu cầu cần đạt và gắn với "
            "số hiệu từng câu hỏi.",
            "<b>Không có</b> nội dung câu hỏi, phương án lựa chọn hay đáp án trong tệp nguồn — đây là điểm "
            "quan trọng cần nói rõ.",
        ]),
        ("p",
         "Vì vậy, tài liệu này gồm hai lớp nội dung: (1) phần <b>nguyên văn từ nguồn</b> — cấu trúc đề, "
         "phân bố câu theo bài, các yêu cầu cần đạt, trọng số điểm; (2) phần <b>biên soạn</b> — hệ thống "
         "kiến thức của ba bài, đề kiểm tra tham khảo, đáp án, giải thích, kế hoạch ôn tập. Đề ở Phần VII "
         "được dựng đúng theo từng dòng của ma trận (đủ 20 câu nhiều lựa chọn, 2 câu đúng/sai với 4 ý mỗi câu, "
         "1 câu tự luận hai phần), nên có thể dùng ngay làm đề luyện."),

        ("h2", "2. Ghi chú kĩ thuật khi đọc ma trận"),
        ("p", "Trong quá trình đối chiếu, có ba điểm cần lưu ý:"),
        ("num", [
            "<b>Ô tỉ lệ ở dòng cuối.</b> Bảng đặc tả ghi <b>5%</b> cho NL3 – Biết (khớp với 0,5/10 điểm), "
            "còn bảng ma trận ghi <b>0,5%</b> — đây là lỗi đánh máy. Tương tự, NL3 – Vận dụng ghi <b>2,5%</b> "
            "thay vì <b>25%</b>. Tài liệu này dùng giá trị đúng theo điểm số.",
            "<b>Cách quy đổi điểm.</b> Với 20 câu nhiều lựa chọn (0,25 điểm/câu = 5,0), 2 câu đúng/sai "
            "(1,0 điểm/câu = 2,0) và 1 câu tự luận (3,0), tổng là 10,0 điểm và khớp với cả sáu dòng điểm "
            "trong ma trận khi câu tự luận được chia 1,0 điểm cho phần trình bày (NL1 – Biết) và 2,0 điểm "
            "cho phần vận dụng (NL3 – Vận dụng).",
            "<b>Số lệnh hỏi.</b> Ma trận ghi tổng <b>28 lệnh hỏi trắc nghiệm + 1 tự luận</b>; con số 28 "
            "gồm 20 câu nhiều lựa chọn và 8 ý đúng/sai (2 câu × 4 ý), không phải 28 câu hỏi riêng lẻ.",
        ]),
        ("box", "note" if False else "example", "Đối chiếu nhanh giữa nguồn và tài liệu",
         [("tbl", (
             ["Hạng mục", "Trong tệp nguồn", "Trong tài liệu này"],
             [
                 ["Cấu trúc đề", "20 TN + 2 Đ/S + 1 TL, 45 phút", "Giữ nguyên (Phần VII)"],
                 ["Số hiệu câu", "I.1–I.20, II.1a–d, II.2a–d, TL", "Giữ nguyên, có bảng đối chiếu (Bảng 1.2, 8.4)"],
                 ["Yêu cầu cần đạt", "Bản đặc tả, 2 chủ đề", "Trích và diễn giải ở mục 1 của mỗi bài"],
                 ["Trọng số", "6 dòng theo năng lực × cấp độ", "Bảng 1.3"],
                 ["Nội dung câu hỏi, đáp án", "Không có", "Biên soạn mới, bám đúng ma trận (Phần VII, VIII)"],
                 ["Hệ thống kiến thức", "Không có", "Biên soạn theo SGK Kết nối tri thức (Phần II–V)"],
             ],
             [34, 62, 80],
         ), None, {"font_size": 8.2, "first_col_bold": True})]),

        ("h2", "3. Cấu trúc tệp và cách tái tạo PDF"),
        ("p", "Tài liệu được sinh tự động bằng Python + ReportLab từ nội dung trong thư mục nguồn, "
              "nên có thể sửa nội dung và xuất lại bất cứ lúc nào:"),
        ("tbl", (
            ["Tệp / thư mục", "Vai trò"],
            [
                ["<b>build.py</b>", "Điểm vào: ghép các phần, dựng mục lục nhiều lượt, xuất PDF"],
                ["<b>lib/theme.py</b>", "Bảng màu, phông chữ, kiểu đoạn"],
                ["<b>lib/blocks.py</b>", "Khối trình bày: dải tiêu đề, hộp ghi nhớ, bảng, DSL nội dung"],
                ["<b>lib/document.py</b>", "Khuôn trang A4, đầu trang – chân trang, dấu trang PDF, mục lục"],
                ["<b>content/part*.py</b>", "Nội dung từng phần (Phần I – Phụ lục)"],
                ["<b>assets/fonts/</b>", "Bộ phông DejaVu Serif/Sans (đủ dấu tiếng Việt) và giấy phép"],
                ["<b>dist/</b>", "Tệp PDF thành phẩm"],
            ],
            [42, 134],
        ), None, {"font_size": 8.3}),
        ("p", "Lệnh tái tạo (cần Python 3.9 trở lên và gói <i>reportlab</i>):"),
        ("box", "example", None,
         [("p", "<font name='Sans' size='8.6'>pip install reportlab<br/>"
                "python build.py<br/>"
                "python build.py --output dist/ten-khac.pdf</font>")]),

        ("h2", "4. Phông chữ, giấy phép và giới hạn"),
        ("bul", [
            "Phông chữ: <b>DejaVu Serif</b> và <b>DejaVu Sans</b>, giấy phép tự do (xem "
            "<i>assets/fonts/LICENSE_DEJAVU</i>), có đủ bộ ký tự tiếng Việt.",
            "Nội dung kiến thức được biên soạn bám theo sách giáo khoa <i>Lịch sử 10 – Kết nối tri thức "
            "với cuộc sống</i> và bản đặc tả của đề; không sao chép nguyên văn sách giáo khoa.",
            "Đề kiểm tra ở Phần VII là <b>đề tham khảo</b>, không phải đề chính thức của trường. Nếu giáo viên "
            "có đề gốc, chỉ cần thay Phần VII–VIII, giữ nguyên Phần I–VI và IX–X.",
            "Các con số về di sản (8 di sản thế giới) tính đến năm 2025; nếu có di sản mới được UNESCO ghi danh, "
            "cần cập nhật Bảng 4.2.",
        ]),
        ("sp", 8),
        ("rule",),
        ("note",
         "Tài liệu được biên soạn phục vụ ôn tập giữa học kì I, năm học 2026 – 2027. "
         "Mọi góp ý về nội dung xin gửi tới giáo viên bộ môn Lịch sử."),
    ]
