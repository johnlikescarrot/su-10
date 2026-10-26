# -*- coding: utf-8 -*-
"""Nội dung đề cương ôn tập Giữa học kì I – Lịch sử 10 (Kết nối tri thức).

Toàn bộ nội dung được tổ chức thành các "block" để build_pdf.py render ra PDF.
"""

from reportlab.lib.units import cm

BLOCKS = []

# =============================================================== PHẦN MỞ ĐẦU
BLOCKS += [
    ("banner", "PHẦN MỞ ĐẦU", "CẤU TRÚC ĐỀ &amp; CÁCH DÙNG TÀI LIỆU"),
    ("lead", "Tài liệu này bám sát <b>ma trận và bản đặc tả</b> của đề kiểm tra định kì giữa học kì I "
             "môn Lịch sử 10 (năm học 2026 – 2027): <b>20 câu trắc nghiệm nhiều lựa chọn + 2 câu trắc "
             "nghiệm đúng/sai (mỗi câu 4 ý) + 1 câu tự luận</b>, thời gian 45 phút. Toàn bộ kiến thức "
             "chỉ nằm trong <b>3 bài</b>: Bài 1, Bài 2 (Chủ đề 1 – Lịch sử và Sử học) và Bài 3 "
             "(Chủ đề 2 – Vai trò của Sử học)."),

    ("box", {"kind": "note", "title": "Về nguồn tài liệu",
             "lines": ["Văn bản gốc <i>“LS10- MTGK1-26-27-HHT.docx”</i> của tổ bộ môn gồm <b>ma trận đề</b> và "
                       "<b>bản đặc tả</b> (quy định chủ đề, nội dung, số lệnh hỏi và mức độ tư duy) chứ chưa có đề "
                       "và đáp án chi tiết. Vì vậy, Phần B của tài liệu này là <b>đề kiểm tra minh hoạ được biên "
                       "soạn bám đúng từng lệnh hỏi</b> trong bản đặc tả (I.1 – I.20, II.1a–d, II.2a–d, TL), còn "
                       "Phần C là đáp án và giải thích tương ứng. Nhờ vậy, khi đề chính thức được công bố, em vẫn "
                       "có sẵn đáp án cho mọi dạng câu mà ma trận đã dự báo."]}),

    ("h2", "1. Cấu trúc đề kiểm tra giữa học kì I"),
    ("table", {
        "header": ["Hình thức", "Số lượng", "Điểm", "Nội dung rơi vào"],
        "center": (1, 2),
        "widths": [4.4 * cm, 2.6 * cm, 1.8 * cm, 9.0 * cm],
        "rows": [
            ["Trắc nghiệm nhiều lựa chọn", "20 câu", "5,0",
             "Bài 1: 6 câu (I.1 – I.6) • Bài 2: 7 câu (I.7 – I.13) • Bài 3: 7 câu (I.14 – I.20)"],
            ["Trắc nghiệm Đúng/Sai", "2 câu<br/>(8 ý)", "2,0",
             "Câu II.1: Bài 2 (tri thức lịch sử, học tập suốt đời) • Câu II.2: Bài 3 (di sản, du lịch)"],
            ["Tự luận", "1 câu<br/>(2 ý)", "3,0",
             "Bài 3: ½ nhận biết (vai trò của Sử học với di sản) + ½ vận dụng (biện pháp bảo tồn, liên hệ)"],
            ["<b>Tổng</b>", "<b>28 lệnh hỏi</b>", "<b>10,0</b>", "Chủ đề 1 + Chủ đề 2, không có nội dung ngoài 3 bài"],
        ],
    }),
    ("small", "Ghi chú: cách chia điểm theo hình thức có thể xê dịch ±0,25 giữa các trường; phần quan trọng nhất "
              "vẫn là <b>tỉ lệ các mức độ tư duy</b> ở bảng dưới đây."),

    ("h2", "2. Tỉ lệ mức độ tư duy – học gì để “ăn” điểm"),
    ("table", {
        "header": ["Mức độ", "Tỉ lệ / điểm", "Dạng câu hỏi điển hình", "Cách học tương ứng"],
        "center": (1,),
        "widths": [2.6 * cm, 3.1 * cm, 6.3 * cm, 5.8 * cm],
        "rows": [
            ["<b>Nhận biết</b>", "≈ 50%<br/>(5,0 điểm)",
             "Nêu khái niệm, đặc điểm, chức năng, nhiệm vụ; kể tên di sản, địa danh du lịch; nhận diện "
             "hiện thực lịch sử / nhận thức lịch sử qua một sự kiện cụ thể.",
             "Học <b>định nghĩa + danh sách</b>; dùng bảng và mẹo viết tắt để nhớ đủ ý."],
            ["<b>Thông hiểu</b>", "≈ 25%<br/>(2,5 điểm)",
             "Giải thích khái niệm bằng lời của mình; phân biệt hai phạm trù; giải thích vì sao phải xử lí "
             "sử liệu, vì sao cần trùng tu theo khoa học, vì sao lịch sử – văn hoá là tài nguyên du lịch.",
             "Học theo <b>cặp đối lập</b> và luôn kèm <b>một ví dụ</b>; tự hỏi “vì sao?” sau mỗi ý."],
            ["<b>Vận dụng</b>", "≈ 25%<br/>(2,5 điểm)",
             "Đề xuất biện pháp bảo tồn, phát huy di sản; đánh giá tác động của du lịch; liên hệ địa phương; "
             "xử lí tình huống khai thác thông tin trên mạng.",
             "Học theo <b>công thức 4 bước</b> (xem mục A3.3); luyện viết 5 – 7 dòng cho mỗi tình huống."],
        ],
    }),

    ("h2", "3. Lộ trình ôn trong 3 ngày (mỗi ngày 45 – 60 phút)"),
    ("table", {
        "header": ["Thời điểm", "Việc cần làm", "Kết quả cần đạt"],
        "widths": [3.0 * cm, 8.9 * cm, 5.9 * cm],
        "rows": [
            ["<b>Ngày 1</b>", "Đọc mục A1 (Bài 1) + A2 (Bài 2). Tự vẽ lại sơ đồ 2 bài trên giấy A4. "
                              "Làm 13 câu trắc nghiệm I.1 – I.13.",
             "Nhớ 2 bảng: “Đối tượng – chức năng – nhiệm vụ” và bảng phân biệt hiện thực / nhận thức."],
            ["<b>Ngày 2</b>", "Đọc mục A3 (Bài 3) + bảng di sản UNESCO. Học các mẹo nhớ. Làm 7 câu I.14 – I.20 "
                              "và 2 câu đúng/sai.",
             "Kể được 5 vai trò của Sử học với di sản, 4 tác động tích cực và 4 tác động tiêu cực của du lịch."],
            ["<b>Ngày 3</b>", "Làm trọn đề trong 45 phút (bấm giờ), tự chấm theo Phần C, ghi lại các câu sai "
                              "vào một tờ “sổ tay lỗi”.",
             "Biết chính xác mình hay sai ở dạng nào để sửa."],
            ["<b>Trước thi 20 phút</b>", "Chỉ đọc: bảng “12 cặp từ khoá dễ nhầm”, mục “Bẫy trắc nghiệm”, "
                                          "và dàn ý tự luận.",
             "Vào phòng thi với 3 khung dàn ý trong đầu."],
        ],
    }),

    ("box", {"kind": "tip", "title": "3 nguyên tắc học nhanh – nhớ lâu",
             "lines": [
                 "- <b>Học theo cặp đối lập:</b> hiện thực ↔ nhận thức; khách quan ↔ chủ quan; bảo tồn ↔ phát huy; "
                 "tích cực ↔ tiêu cực. Não nhớ “cặp” tốt hơn nhớ “danh sách”.",
                 "- <b>Mỗi ý phải có một ví dụ:</b> nêu được định nghĩa mà không có ví dụ là dấu hiệu học vẹt – "
                 "và đề rất hay hỏi qua ví dụ.",
                 "- <b>Trả lời theo công thức “Nêu – Giải thích – Ví dụ / Liên hệ”:</b> đúng cả 3 tầng là ăn trọn điểm tự luận.",
             ]}),
    ("pagebreak",),
]

# =============================================================== PHẦN A
BLOCKS += [
    ("banner", "PHẦN A", "KIẾN THỨC TRỌNG TÂM – 3 BÀI, 2 CHỦ ĐỀ"),

    # ---------------------------------------------------------------- BÀI 1
    ("banner2", "CHỦ ĐỀ 1 • LỊCH SỬ VÀ SỬ HỌC", "BÀI 1 – HIỆN THỰC LỊCH SỬ VÀ LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC"),

    ("h2", "A1.1. Hai khái niệm nền tảng"),
    ("kv", [
        ("<b>Lịch sử</b>",
         "Là <b>toàn bộ quá trình phát triển của xã hội loài người</b> từ khi con người xuất hiện đến nay, bao gồm "
         "mọi hoạt động của con người trong mọi lĩnh vực (kinh tế, chính trị, văn hoá, xã hội, quân sự…). "
         "“Lịch sử” còn được dùng để chỉ <b>một khoa học</b> – tức Sử học."),
        ("<b>Sử học</b>",
         "Là <b>khoa học nghiên cứu về quá khứ của xã hội loài người</b> – quá khứ của nhân loại nói chung và của "
         "từng quốc gia, dân tộc, cộng đồng người nói riêng."),
        ("<b>Sử liệu</b>",
         "Là <b>nguồn tư liệu hình thành trong quá khứ hoặc liên quan đến quá khứ</b> (chữ viết, hiện vật, hình ảnh, "
         "lời kể…). Sử liệu là “nguyên liệu” để nhà sử học nhận thức và tái hiện lịch sử."),
    ]),

    ("box", {"kind": "mnemonic", "title": "Mẹo phân biệt nhanh",
             "lines": [
                 "<b>LỊCH SỬ = cái đã xảy ra</b> (một quá trình) → trả lời câu hỏi “Đã có gì?”.",
                 "<b>SỬ HỌC = nghề/ngành đi tìm cái đã xảy ra</b> (một khoa học) → trả lời câu hỏi “Tìm hiểu bằng cách nào?”.",
                 "<b>SỬ LIỆU = bằng chứng của cái đã xảy ra</b> → trả lời câu hỏi “Dựa vào đâu để biết?”.",
             ]}),

    ("h2", "A1.2. Đối tượng – chức năng – nhiệm vụ của Sử học"),
    ("table", {
        "header": ["Nội dung", "Cần nhớ", "Ví dụ / cách diễn đạt"],
        "widths": [3.0 * cm, 7.4 * cm, 7.4 * cm],
        "rows": [
            ["<b>Đối tượng</b>", "Quá khứ của xã hội loài người: con người, các sự kiện, hiện tượng và quá trình "
                                 "lịch sử diễn ra trong quá khứ.",
             "Nhà sử học nghiên cứu Cách mạng tháng Tám 1945, không nghiên cứu… tương lai."],
            ["<b>Chức năng</b>", "<b>Hai chức năng:</b><br/>1. <b>Chức năng khoa học</b> – nhận thức, khám phá, "
                                 "giải thích quá khứ, cung cấp tri thức khoa học.<br/>2. <b>Chức năng xã hội</b> – "
                                 "giáo dục tư tưởng, đạo đức, truyền thống; phục vụ cuộc sống và sự phát triển cộng đồng.",
             "“Sử học vừa là khoa học, vừa là công cụ giáo dục và phục vụ xã hội.”"],
            ["<b>Nhiệm vụ</b>", "– Nhận thức đúng quá khứ;<br/>– Tái hiện quá khứ một cách khách quan, khoa học;<br/>"
                                 "– Rút ra quy luật và bài học kinh nghiệm;<br/>– Dự báo, định hướng;<br/>"
                                 "– Góp phần giáo dục thế hệ trẻ, bảo tồn di sản, phục vụ xây dựng và bảo vệ Tổ quốc.",
             "Câu hỏi hay gặp: “Nhiệm vụ nào sau đây <b>không</b> phải của Sử học?” – đáp án thường là “sáng tạo ra "
             "quá khứ”, “thay đổi quá khứ”, “dự đoán chính xác tuyệt đối tương lai”."],
        ],
    }),
    ("box", {"kind": "mnemonic", "title": "Mẹo nhớ “ĐỐI – CHỨC – NHIỆM”",
             "lines": [
                 "<b>ĐỐI</b> tượng = QUÁ KHỨ (của xã hội loài người).",
                 "<b>CHỨC</b> năng = <b>2</b> chữ: <b>KHOA HỌC</b> + <b>XÃ HỘI</b>.",
                 "<b>NHIỆM</b> vụ = <b>TÁI – RÚT – DẠY</b>: TÁI hiện quá khứ → RÚT ra quy luật, bài học → "
                 "giáo DẠY, phục vụ đất nước.",
             ]}),

    ("h2", "A1.3. Hiện thực lịch sử"),
    ("p", "<b>Khái niệm:</b> Hiện thực lịch sử là <b>toàn bộ những gì đã diễn ra trong quá khứ</b>, tồn tại một cách "
          "khách quan, <b>không phụ thuộc vào ý muốn và nhận thức của con người</b>."),
    ("p", "<b>Ba đặc điểm phải nhớ:</b>"),
    ("nums", [
        "<b>Khách quan</b> – đã xảy ra thì không thể phủ nhận, không thể thay đổi bằng ý chí.",
        "<b>Duy nhất, không lặp lại</b> – mỗi sự kiện chỉ diễn ra một lần, ở một thời điểm, một không gian xác định; "
        "“lịch sử không có chữ nếu”.",
        "<b>Tồn tại độc lập với nhận thức</b> – dù con người biết hay chưa biết, nhận thức đúng hay sai, sự kiện vẫn là sự thật.",
    ]),
    ("p", "<b>Ví dụ:</b> Chiến thắng Bạch Đằng năm 938; Cách mạng tháng Tám năm 1945; Chiến tranh thế giới thứ hai "
          "(1939 – 1945); sự ra đời của nước Việt Nam Dân chủ Cộng hoà ngày 2-9-1945 – tất cả đều là hiện thực lịch sử."),
    ("box", {"kind": "note", "title": "Câu chốt để dùng khi làm bài",
             "lines": ["“Hiện thực lịch sử là <b>cái đã có</b>; con người chỉ có thể nhận thức nó <b>đúng hơn</b>, "
                       "chứ không thể làm lại hay sửa chữa nó.”"]}),

    ("h2", "A1.4. Lịch sử được con người nhận thức"),
    ("p", "<b>Khái niệm:</b> Lịch sử được con người nhận thức là <b>những hiểu biết của con người về hiện thực lịch sử</b>, "
          "được hình thành qua nghiên cứu, học tập, trải nghiệm và được thể hiện trong sách vở, bài giảng, công trình "
          "khoa học, bảo tàng, phim ảnh, di tích…"),
    ("p", "<b>Bốn đặc điểm phải nhớ:</b>"),
    ("nums", [
        "<b>Mang tính chủ quan</b> – phụ thuộc vào trình độ, quan điểm, mục đích của người nhận thức; cùng một sự kiện "
        "có thể có nhiều cách hiểu, cách đánh giá khác nhau.",
        "<b>Gắn chặt với sử liệu</b> – sử liệu càng phong phú, càng xác thực thì nhận thức càng đầy đủ, chính xác.",
        "<b>Có tính kế thừa và không ngừng hoàn thiện</b> – khi có sử liệu mới, phương pháp mới, nhận thức cũ được "
        "bổ sung, đính chính, thậm chí bị thay đổi.",
        "<b>Không bao giờ phản ánh đầy đủ tuyệt đối</b> hiện thực lịch sử – luôn tồn tại “khoảng cách” giữa quá khứ "
        "và hiểu biết về quá khứ.",
    ]),
    ("p", "<b>Ví dụ:</b> Hiểu biết về Hai Bà Trưng được thể hiện qua chính sử, truyền thuyết, tranh dân gian, phim, "
          "bài giảng – mỗi kênh là một “lăng kính” nhận thức khác nhau; hay những đánh giá khác nhau về một nhân vật "
          "lịch sử trong các công trình nghiên cứu."),

    ("h2", "A1.5. Bảng phân biệt – TRỌNG TÂM SỐ 1 CỦA BÀI"),
    ("table", {
        "header": ["Tiêu chí", "HIỆN THỰC LỊCH SỬ", "LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC"],
        "widths": [2.9 * cm, 7.3 * cm, 7.6 * cm],
        "rows": [
            ["<b>Bản chất</b>", "Toàn bộ những gì đã thực sự diễn ra trong quá khứ.",
             "Sự hiểu biết, sự phản ánh của con người về quá khứ đó."],
            ["<b>Tính chất</b>", "Khách quan, duy nhất, không lặp lại, <b>không thể thay đổi</b>.",
             "Chủ quan, đa dạng, <b>có thể bổ sung – điều chỉnh</b>."],
            ["<b>Phụ thuộc vào</b>", "Không phụ thuộc ý muốn, nhận thức của con người.",
             "Phụ thuộc quan điểm, trình độ, mục đích của người nhận thức; chất lượng sử liệu; phương pháp nghiên cứu."],
            ["<b>Số lượng</b>", "Chỉ có <b>một</b> – sự thật lịch sử.",
             "Có thể có <b>nhiều phiên bản</b> khác nhau, thậm chí trái ngược."],
            ["<b>Vị trí</b>", "Là <b>khách thể</b> – đối tượng cần được nhận thức.",
             "Là <b>kết quả</b> của hoạt động nhận thức."],
            ["<b>Ví dụ</b>", "Ngày 2-9-1945, tại Quảng trường Ba Đình (Hà Nội), Chủ tịch Hồ Chí Minh đọc Tuyên ngôn "
                             "Độc lập, khai sinh nước Việt Nam Dân chủ Cộng hoà.",
             "Các trang viết, bài giảng, phim tài liệu, bảo tàng và những cách đánh giá khác nhau về ý nghĩa của sự kiện ấy."],
        ],
    }),
    ("box", {"kind": "mnemonic", "title": "Mẹo nhớ 1 câu",
             "lines": ["<b>Hiện thực = CÁI ĐÃ CÓ (một bản, khách quan, không sửa được).</b><br/>"
                       "<b>Nhận thức = CÁI TA BIẾT (nhiều bản, chủ quan, sửa được khi có sử liệu mới).</b>"]}),

    ("h2", "A1.6. Mối quan hệ giữa hai phạm trù (câu hỏi “hiểu” rất hay ra)"),
    ("bullets", [
        "Hiện thực lịch sử <b>quy định</b> nội dung nhận thức: nhận thức phải tôn trọng sự thật khách quan, không được "
        "bóp méo, không được “tô hồng” hay “bôi đen”.",
        "Nhận thức lịch sử là <b>sự phản ánh</b> hiện thực nhưng <b>không phải bản sao</b> – nên cần liên tục kiểm chứng, "
        "đối chiếu, tranh luận khoa học.",
        "Vì thế, <b>Sử học là khoa học không ngừng hoàn thiện</b> và <b>học lịch sử là quá trình suốt đời</b> "
        "(cầu nối sang Bài 2).",
    ]),

    ("h2", "A1.7. Vì sao Sử học là một khoa học? (dạng câu I.4)"),
    ("table", {
        "header": ["Căn cứ", "Nội dung"],
        "widths": [4.2 * cm, 13.6 * cm],
        "rows": [
            ["Có đối tượng riêng", "Quá khứ của xã hội loài người – khách thể tồn tại khách quan."],
            ["Có hệ thống lý thuyết, khái niệm", "Hiện thực lịch sử, nhận thức lịch sử, sử liệu, chức năng – nhiệm vụ, "
                                                 "phương pháp lịch sử…"],
            ["Có phương pháp nghiên cứu", "Phương pháp lịch sử (diễn biến theo thời gian), phương pháp lô-gích, "
                                          "so sánh, thống kê, khảo cổ học, phỏng vấn nhân chứng…"],
            ["Có khả năng kiểm chứng", "Kết luận khoa học phải dựa trên sử liệu, có thể đối chiếu, phản bác và "
                                       "được bổ sung khi có sử liệu mới."],
        ],
    }),

    ("box", {"kind": "warn", "title": "4 bẫy trắc nghiệm của Bài 1",
             "lines": [
                 "- Nhầm “lịch sử” (quá trình) với “Sử học” (khoa học) → đọc kỹ chủ ngữ của câu hỏi.",
                 "- “Khách quan” chỉ dùng cho <b>hiện thực lịch sử</b>; “chủ quan” dùng cho <b>nhận thức lịch sử</b>.",
                 "- Khi đề hỏi “đặc điểm <b>không</b> đúng của nhận thức lịch sử”, đáp án sai thường là “duy nhất, "
                 "không lặp lại” (đó là đặc điểm của hiện thực).",
                 "- Nhận thức lịch sử <b>không</b> phải là “bản sao y nguyên” của quá khứ, cũng <b>không</b> hoàn toàn "
                 "tuỳ ý (vì còn bị sử liệu ràng buộc).",
             ]}),
    ("pagebreak", 9),
]

# ---------------------------------------------------------------- BÀI 2
BLOCKS += [
    ("banner2", "CHỦ ĐỀ 1 • LỊCH SỬ VÀ SỬ HỌC", "BÀI 2 – TRI THỨC LỊCH SỬ VÀ CUỘC SỐNG"),

    ("h2", "A2.1. Tri thức lịch sử là gì?"),
    ("p", "<b>Khái niệm:</b> Tri thức lịch sử là <b>những hiểu biết về quá khứ</b> của xã hội loài người (sự kiện, nhân vật, "
          "quá trình, quy luật vận động…) mà con người tích luỹ được qua học tập, nghiên cứu và trải nghiệm."),
    ("p", "<b>Vai trò:</b>"),
    ("bullets", [
        "Giúp mỗi người hiểu mình, hiểu dân tộc, hiểu thế giới và vị trí của mình trong dòng chảy thời gian.",
        "Hình thành nhân cách, bản lĩnh, lòng tự hào và trách nhiệm với cộng đồng.",
        "Cung cấp bài học kinh nghiệm, quy luật để ra quyết định đúng trong hiện tại.",
        "Là nền tảng tri thức của nhiều ngành nghề: du lịch, báo chí, giáo dục, văn hoá, ngoại giao, bảo tồn…",
    ]),

    ("h2", "A2.2. Sử liệu – “nguyên liệu” của nhận thức lịch sử"),
    ("table", {
        "header": ["Cách phân loại", "Loại sử liệu", "Đặc điểm", "Ví dụ"],
        "widths": [3.3 * cm, 3.5 * cm, 6.2 * cm, 4.8 * cm],
        "rows": [
            ["<b>Theo giá trị / nguồn gốc</b>", "Sử liệu gốc (sơ cấp)",
             "Ra đời ngay tại thời điểm hoặc gần sự kiện; do người chứng kiến, người tham gia tạo ra. Giá trị cao nhất.",
             "Bia đá, văn bản gốc, nhật ký, ảnh chụp, hiện vật khảo cổ."],
            ["", "Sử liệu phái sinh (thứ cấp)",
             "Ra đời sau sự kiện, dựa trên sử liệu gốc; có thể đã qua chọn lọc, lí giải của tác giả.",
             "Sách giáo khoa, bài nghiên cứu, phim tài liệu dựng lại."],
            ["<b>Theo hình thức</b>", "Chữ viết – vật chất – hình ảnh/nghe nhìn – truyền miệng",
             "Mỗi loại có thế mạnh riêng; cần kết hợp nhiều loại để kiểm chứng chéo.",
             "Văn bia / trống đồng / phim tư liệu / truyền thuyết, lời kể nhân chứng."],
        ],
    }),
    ("box", {"kind": "tip", "title": "3 câu hỏi vàng để đánh giá một nguồn tin",
             "lines": ["<b>Ai nói?</b> (người trong cuộc, chuyên gia, hay người lan truyền?) → "
                       "<b>Nói khi nào, ở đâu?</b> (gần sự kiện hay rất lâu sau?) → "
                       "<b>Dựa trên cái gì?</b> (có dẫn nguồn, có bằng chứng, có kiểm chứng được không?)"]}),

    ("h2", "A2.3. Quy trình 4 bước thu thập và xử lí thông tin, sử liệu – TRỌNG TÂM SỐ 2"),
    ("table", {
        "header": ["Bước", "Việc cần làm", "Ví dụ: dự án “Di sản quê em”", "Lỗi thường gặp"],
        "widths": [2.3 * cm, 6.0 * cm, 5.6 * cm, 3.9 * cm],
        "rows": [
            ["<b>1. Xác định vấn đề</b>",
             "Xác định rõ câu hỏi / nhiệm vụ học tập, phạm vi không gian – thời gian, mục đích và sản phẩm cần có.",
             "“Di tích X được xây dựng khi nào, thờ ai, có giá trị gì với làng tôi?”",
             "Đề tài quá rộng, không có câu hỏi trọng tâm."],
            ["<b>2. Thu thập thông tin, sử liệu</b>",
             "Lập kế hoạch và tìm ở <b>nhiều nguồn</b>: sách – báo, bảo tàng, di tích, internet, nhân chứng; "
             "ghi chép, chụp ảnh, ghi âm và ghi rõ nguồn.",
             "Đọc sách địa chí, chụp bia đá, phỏng vấn người cao tuổi trong làng.",
             "Chỉ dùng một nguồn; lấy thông tin không rõ xuất xứ."],
            ["<b>3. Xử lí thông tin, sử liệu</b>",
             "Phân loại, so sánh, <b>kiểm chứng chéo</b>, đánh giá độ tin cậy, loại bỏ thông tin sai, sắp xếp theo "
             "trình tự thời gian và lô-gích.",
             "Đối chiếu nội dung bia với sách và lời kể; chỗ nào mâu thuẫn thì ghi lại để kiểm tra tiếp.",
             "Tin ngay mọi thứ trên mạng; bỏ qua mâu thuẫn giữa các nguồn."],
            ["<b>4. Trình bày kết quả</b>",
             "Viết báo cáo / thuyết trình / sơ đồ; <b>trích dẫn nguồn</b>; nêu ý nghĩa và bài học.",
             "Bài báo cáo 3 trang kèm ảnh và danh mục nguồn tham khảo.",
             "Không trích nguồn; “chép – dán” không chọn lọc."],
        ],
    }),
    ("box", {"kind": "mnemonic", "title": "Mẹo nhớ 4 bước",
             "lines": ["<b>XÁC – THU – XỬ – TRÌNH</b> &nbsp;(biến thể dễ nhớ: <b>HỎI – TÌM – LỌC – VIẾT</b>)<br/>"
                       "Xác định vấn đề → Thu thập → Xử lí → Trình bày kết quả."]}),

    ("h2", "A2.4. Vì sao phải học tập và khám phá lịch sử suốt đời? – TRỌNG TÂM SỐ 3"),
    ("nums", [
        "<b>Tri thức lịch sử rộng lớn vô cùng</b> – nhà trường chỉ dạy một phần rất nhỏ; muốn hiểu sâu phải học tiếp.",
        "<b>Nhận thức lịch sử luôn được bổ sung, điều chỉnh</b> – có sử liệu mới, phương pháp mới, kiến thức cũ có thể "
        "trở nên lạc hậu, thậm chí sai.",
        "<b>Cuộc sống luôn vận động, biến đổi</b> – hiện tại là sản phẩm của quá khứ; hiểu quá khứ để hiểu hiện tại "
        "và dự báo tương lai.",
        "<b>Hoàn thiện bản thân và nâng cao năng lực nghề nghiệp</b> – tư duy phản biện, kĩ năng phân tích, khả năng "
        "thích ứng, cơ hội việc làm trong các ngành cần tri thức văn hoá – lịch sử.",
        "<b>Bảo vệ bản sắc dân tộc và chống thông tin sai lệch</b> – phân biệt đúng – sai trước các luận điệu xuyên tạc "
        "lịch sử; hội nhập mà không hoà tan.",
    ]),
    ("box", {"kind": "mnemonic", "title": "Mẹo nhớ 5 lý do",
             "lines": ["<b>RỘNG – ĐỔI – SỐNG – NGHỀ – NƯỚC</b><br/>"
                       "Tri thức <b>RỘNG</b> → nhận thức luôn <b>ĐỔI</b> → cuộc <b>SỐNG</b> vận động → "
                       "<b>NGHỀ</b> nghiệp, bản thân → đất <b>NƯỚC</b>, bản sắc dân tộc."]}),

    ("h2", "A2.5. Bản chất của việc kết nối tri thức lịch sử vào cuộc sống"),
    ("p", "<b>Bản chất:</b> không phải là học thuộc sự kiện để trả bài, mà là <b>biến tri thức lịch sử thành công cụ "
          "để hiểu, lí giải và hành động trong hiện tại</b> – dùng bài học kinh nghiệm, quy luật và giá trị của quá khứ "
          "để giải quyết những vấn đề của cuộc sống hôm nay."),
    ("table", {
        "header": ["Mức độ", "Biểu hiện", "Ví dụ"],
        "widths": [3.4 * cm, 6.6 * cm, 7.8 * cm],
        "rows": [
            ["<b>1. Hiểu – giải thích</b>", "Dùng tri thức lịch sử để lí giải một sự kiện, hiện tượng, vấn đề thời sự.",
             "Giải thích vì sao nhiều nước đề cao giá trị hoà bình sau hai cuộc chiến tranh thế giới."],
            ["<b>2. Vận dụng – liên hệ</b>", "Rút ra bài học và liên hệ với bản thân, gia đình, địa phương.",
             "Từ truyền thống “uống nước nhớ nguồn” → tham gia chăm sóc đài tưởng niệm liệt sĩ của xã."],
            ["<b>3. Đề xuất – hành động</b>", "Đề xuất giải pháp, thực hiện dự án, tuyên truyền, vận động cộng đồng.",
             "Làm dự án số hoá thông tin di tích địa phương; viết bài tuyên truyền bảo vệ di sản."],
        ],
    }),
    ("table", {
        "header": ["Vấn đề của cuộc sống", "Bài học từ lịch sử", "Cách vận dụng"],
        "widths": [4.2 * cm, 6.6 * cm, 7.0 * cm],
        "rows": [
            ["Chiến tranh – xung đột", "Hậu quả tàn khốc của chiến tranh; giá trị của hoà bình, đoàn kết.",
             "Ủng hộ giải pháp hoà bình; phản đối bạo lực; tôn trọng sự khác biệt."],
            ["Dịch bệnh, thiên tai", "Kinh nghiệm chống dịch, trị thuỷ, đắp đê của cha ông.",
             "Bình tĩnh, tin vào khoa học, đoàn kết cộng đồng, chuẩn bị ứng phó."],
            ["Biến đổi khí hậu", "Tri thức thích ứng tự nhiên, canh tác bền vững.",
             "Sống thân thiện môi trường, tiết kiệm, bảo vệ rừng và nguồn nước."],
            ["Bảo tồn di sản", "Truyền thống trọng di sản, “ăn quả nhớ kẻ trồng cây”.",
             "Tham quan học tập, giữ gìn di tích, phản đối hành vi xâm hại di sản."],
        ],
    }),

    ("h2", "A2.6. Học lịch sử qua những kênh nào?"),
    ("bullets", [
        "Sách, báo, tạp chí, công trình nghiên cứu, sách giáo khoa – nguồn nền tảng, có kiểm duyệt.",
        "Bảo tàng, di tích, di sản, nhà truyền thống – học qua hiện vật và không gian thực.",
        "Phim tài liệu, phim lịch sử, ảnh tư liệu – trực quan nhưng cần phân biệt tư liệu và hư cấu.",
        "Internet, mạng xã hội, thư viện số – tiện lợi nhưng <b>phải kiểm chứng</b>.",
        "Nhân chứng, lời kể, truyền thuyết – giàu cảm xúc nhưng cần đối chiếu.",
        "Học qua dự án, trải nghiệm, câu lạc bộ, cuộc thi tìm hiểu lịch sử – nhớ lâu nhất.",
    ]),
    ("box", {"kind": "warn", "title": "Cảnh báo khi khai thác thông tin trên internet",
             "lines": [
                 "- Ưu tiên nguồn chính thống: bảo tàng, cơ quan văn hoá, trường đại học, nhà xuất bản, tạp chí khoa học.",
                 "- Luôn kiểm chứng chéo ít nhất <b>2 – 3 nguồn</b> trước khi sử dụng; ghi rõ nguồn khi trích dẫn.",
                 "- Cảnh giác với thông tin “giật gân”, không có tác giả, không ngày tháng, hoặc nội dung xuyên tạc, "
                 "bóp méo lịch sử; không chia sẻ thông tin chưa kiểm chứng.",
                 "- Tôn trọng bản quyền, không “chép – dán” nguyên văn mà không ghi nguồn.",
             ]}),
    ]

# ---------------------------------------------------------------- BÀI 3
BLOCKS += [
    ("banner3", "CHỦ ĐỀ 2 • VAI TRÒ CỦA SỬ HỌC", "BÀI 3 – VAI TRÒ CỦA SỬ HỌC"),

    ("h2", "A3.1. Di sản văn hoá và di sản thiên nhiên – khái niệm, phân loại"),
    ("p", "<b>Di sản văn hoá</b> là hệ thống các giá trị vật chất và tinh thần do con người sáng tạo, tích luỹ và "
          "truyền lại qua các thế hệ. <b>Di sản thiên nhiên</b> là các giá trị cảnh quan, địa chất, địa mạo, đa dạng "
          "sinh học có giá trị nổi bật về khoa học, thẩm mĩ, văn hoá – lịch sử."),
    ("table", {
        "header": ["Loại di sản", "Nội dung", "Ví dụ ở Việt Nam"],
        "widths": [3.5 * cm, 7.6 * cm, 6.7 * cm],
        "rows": [
            ["<b>Văn hoá vật thể</b>",
             "Di tích lịch sử – văn hoá, danh lam thắng cảnh, công trình kiến trúc, di vật, cổ vật, bảo vật quốc gia.",
             "Hoàng thành Thăng Long, Quần thể di tích Cố đô Huế, phố cổ Hội An, Thánh địa Mỹ Sơn, Thành nhà Hồ, "
             "Văn Miếu – Quốc Tử Giám."],
            ["<b>Văn hoá phi vật thể</b>",
             "Tiếng nói, chữ viết, phong tục, tập quán, lễ hội, âm nhạc, nghệ thuật biểu diễn, tri thức dân gian, "
             "nghề thủ công truyền thống.",
             "Nhã nhạc cung đình Huế, Không gian văn hoá cồng chiêng Tây Nguyên, Dân ca quan họ Bắc Ninh, Ca trù, "
             "Hội Gióng, Tín ngưỡng thờ cúng Hùng Vương."],
            ["<b>Thiên nhiên</b>",
             "Cảnh quan thiên nhiên, địa chất, đa dạng sinh học có giá trị nổi bật.",
             "Vịnh Hạ Long – Cát Bà, Vườn quốc gia Phong Nha – Kẻ Bàng, Quần thể danh thắng Tràng An, "
             "Cao nguyên đá Đồng Văn."],
            ["<b>Tư liệu (mở rộng)</b>",
             "Tài liệu chữ viết, bia, mộc bản, châu bản có giá trị thông tin đặc biệt.",
             "Mộc bản triều Nguyễn, Bia đá Văn Miếu, Châu bản triều Nguyễn."],
        ],
    }),

    ("h2", "A3.2. Vai trò của Sử học với công tác bảo tồn và phát huy giá trị di sản – TRỌNG TÂM SỐ 4"),
    ("p", "<b>Năm vai trò cốt lõi:</b>"),
    ("table", {
        "header": ["Vai trò", "Nội dung cụ thể"],
        "widths": [4.0 * cm, 13.8 * cm],
        "rows": [
            ["<b>1. Nhận diện</b>",
             "Xác định sự tồn tại, nguồn gốc, niên đại, chủ sở hữu và các giá trị (lịch sử, văn hoá, khoa học, "
             "thẩm mĩ, kinh tế) của di sản. Không có tri thức lịch sử thì di sản chỉ là “vật cũ”."],
            ["<b>2. Đánh giá – xếp hạng</b>",
             "Cung cấp căn cứ khoa học để lập hồ sơ, xếp hạng di tích (cấp tỉnh, quốc gia, quốc gia đặc biệt) "
             "và đề nghị UNESCO ghi danh."],
            ["<b>3. Bảo tồn</b>",
             "Định hướng trùng tu, tôn tạo, phục dựng <b>đúng nguyên trạng</b>, đúng vật liệu, đúng kĩ thuật truyền "
             "thống; cảnh báo nguy cơ xuống cấp, xâm hại và các phương án sai (bê tông hoá, “làm mới” di tích)."],
            ["<b>4. Giáo dục – phát huy</b>",
             "Cung cấp nội dung cho giáo dục truyền thống, tham quan học tập, thuyết minh; nâng cao ý thức và "
             "trách nhiệm của cộng đồng; đưa di sản trở lại đời sống."],
            ["<b>5. Quảng bá – khai thác bền vững</b>",
             "Xây dựng nội dung thuyết minh, sản phẩm du lịch, số hoá di sản; gắn di sản với phát triển kinh tế – "
             "xã hội, tạo sinh kế cho cộng đồng địa phương."],
        ],
    }),
    ("box", {"kind": "note", "title": "Chiều ngược lại (rất dễ mất điểm nếu bỏ qua)",
             "lines": ["Di sản cũng là <b>nguồn sử liệu quan trọng</b> của Sử học: di tích, hiện vật, bia ký cung cấp "
                       "<b>bằng chứng vật chất</b> để nhận thức quá khứ. Vì vậy <b>bảo tồn di sản chính là bảo tồn "
                       "“tư liệu sống” cho Sử học</b>."]}),
    ("box", {"kind": "mnemonic", "title": "Mẹo nhớ 5 vai trò",
             "lines": ["<b>NHẬN – XẾP – GIỮ – DẠY – QUẢNG</b><br/>"
                       "NHẬN diện → XẾP hạng → GIỮ (bảo tồn) → DẠY (giáo dục) → QUẢNG bá & khai thác."]}),

    ("h2", "A3.3. Biện pháp bảo tồn, phát huy di sản (dùng cho câu tự luận phần vận dụng)"),
    ("table", {
        "header": ["Nhóm biện pháp", "Nội dung – việc làm cụ thể"],
        "widths": [4.2 * cm, 13.6 * cm],
        "rows": [
            ["<b>1. Tuyên truyền, giáo dục</b>",
             "Đưa giáo dục di sản vào nhà trường; tổ chức tham quan học tập, cuộc thi tìm hiểu, ngày hội di sản; "
             "truyền thông trên mạng xã hội; hướng dẫn du khách ứng xử văn minh."],
            ["<b>2. Hoàn thiện pháp luật, quy hoạch, quản lý</b>",
             "Thực hiện Luật Di sản văn hoá; phân cấp quản lý rõ ràng; thanh tra, xử phạt nghiêm hành vi xâm hại, "
             "buôn bán cổ vật; quy hoạch bảo tồn gắn với quy hoạch phát triển."],
            ["<b>3. Bảo tồn theo khoa học</b>",
             "Trùng tu theo nguyên tắc nguyên trạng, có hồ sơ khoa học, chuyên gia và vật liệu phù hợp; "
             "không “làm mới”, không bê tông hoá; bảo vệ cả cảnh quan và không gian văn hoá xung quanh."],
            ["<b>4. Huy động nguồn lực</b>",
             "Ngân sách nhà nước, xã hội hoá, quỹ bảo tồn, tài trợ, hợp tác quốc tế (UNESCO, các tổ chức phi "
             "chính phủ); ứng dụng công nghệ số hoá, lưu trữ dữ liệu di sản."],
            ["<b>5. Phát huy gắn với du lịch bền vững</b>",
             "Giới hạn sức chứa, quản lý lượng khách, xây dựng sản phẩm đặc trưng, chia sẻ lợi ích với cộng đồng, "
             "phát triển du lịch có trách nhiệm."],
            ["<b>6. Cộng đồng làm chủ</b>",
             "Trao quyền và tạo sinh kế cho người dân sống trong/gần di sản để họ “sống được bằng di sản” → "
             "tự nguyện, bền vững trong bảo vệ."],
        ],
    }),
    ("box", {"kind": "tip", "title": "Công thức 4 bước cho câu hỏi vận dụng (2 điểm)",
             "lines": ["<b>Bước 1 – Nhận diện vấn đề:</b> “Bảo tồn di sản X đang đứng trước nguy cơ…” (1 câu).<br/>"
                       "<b>Bước 2 – Nêu 3 – 4 biện pháp</b>, mỗi biện pháp viết theo cấu trúc “làm gì – để làm gì” "
                       "(ý chính ăn điểm).<br/>"
                       "<b>Bước 3 – Liên hệ địa phương / bản thân:</b> việc em và trường em có thể làm ngay.<br/>"
                       "<b>Bước 4 – Khẳng định trách nhiệm:</b> “bảo vệ di sản là bảo vệ ký ức và bản sắc dân tộc”."]}),

    ("h2", "A3.4. Sử học với sự phát triển du lịch – TRỌNG TÂM SỐ 5"),
    ("h3", "a. Tài nguyên du lịch của Việt Nam"),
    ("bullets", [
        "<b>Tài nguyên tự nhiên:</b> Vịnh Hạ Long, Sa Pa – Fansipan, Phong Nha – Kẻ Bàng, Tràng An, Mũi Né, "
        "Đà Lạt, các bãi biển miền Trung…",
        "<b>Tài nguyên nhân văn (lịch sử – văn hoá):</b> di tích lịch sử – văn hoá, lễ hội truyền thống, làng nghề, "
        "ẩm thực, âm nhạc – nghệ thuật dân gian, kiến trúc đô thị cổ…",
    ]),
    ("h3", "b. Vai trò của tri thức lịch sử – văn hoá đối với du lịch"),
    ("nums", [
        "<b>Là nguồn tài nguyên:</b> lịch sử – văn hoá tạo nên sản phẩm du lịch đặc sắc, khác biệt và khó sao chép.",
        "<b>Cung cấp nội dung, câu chuyện cho điểm đến:</b> làm tăng giá trị trải nghiệm, kéo dài thời gian lưu trú "
        "và mức chi tiêu của du khách.",
        "<b>Nâng cao chất lượng nguồn nhân lực:</b> hướng dẫn viên, thuyết minh viên có tri thức sâu sẽ hấp dẫn, "
        "chuyên nghiệp hơn.",
        "<b>Cơ sở để quy hoạch, xây dựng sản phẩm:</b> du lịch di sản, du lịch văn hoá, du lịch cộng đồng, du lịch "
        "học đường, du lịch tâm linh…",
        "<b>Quảng bá hình ảnh quốc gia, dân tộc</b> và thúc đẩy giao lưu văn hoá; tạo việc làm, thu nhập cho cộng đồng.",
    ]),
    ("h3", "c. Tác động của du lịch đến công tác bảo tồn di tích, di sản (bảng hai chiều – RẤT HAY RA THI)"),
    ("table", {
        "header": ["Tác động tích cực", "Tác động tiêu cực"],
        "widths": [8.9 * cm, 8.9 * cm],
        "rows": [
            ["Tạo nguồn thu để trùng tu, tôn tạo, bảo tồn di tích.",
             "Lượng khách quá tải gây xuống cấp, xâm hại di tích, hư hại hiện vật."],
            ["Nâng cao ý thức, niềm tự hào và trách nhiệm của cộng đồng với di sản.",
             "Thương mại hoá, “sân khấu hoá” lễ hội làm biến dạng, mất bản sắc văn hoá."],
            ["Tạo sinh kế, việc làm, giảm nghèo; thúc đẩy kinh tế – xã hội địa phương.",
             "Xây dựng ồ ạt, bê tông hoá, phá vỡ cảnh quan và không gian di sản."],
            ["Quảng bá giá trị di sản, thu hút đầu tư, hợp tác quốc tế trong bảo tồn.",
             "Ô nhiễm môi trường, rác thải, tiếng ồn; nguy cơ thất truyền nghề, lễ hội truyền thống."],
            ["Góp phần “hồi sinh” nghề truyền thống, phục dựng lễ hội, tạo động lực sưu tầm – nghiên cứu.",
             "Lợi ích không đến cộng đồng → xung đột, người dân mất động lực bảo vệ di sản."],
        ],
    }),
    ("box", {"kind": "mnemonic", "title": "Mẹo nhớ hai chiều",
             "lines": ["<b>Tích cực = TIỀN – Ý THỨC – SINH KẾ – QUẢNG BÁ</b><br/>"
                       "<b>Tiêu cực = QUÁ TẢI – BIẾN DẠNG – BÊ TÔNG – Ô NHIỄM</b>"]}),
    ("h3", "d. Giải pháp phát triển du lịch gắn với bảo tồn"),
    ("bullets", [
        "Quy hoạch hợp lý, xác định <b>sức chứa</b> và giới hạn lượng khách tại các điểm nhạy cảm.",
        "Giáo dục, nâng cao nhận thức và ứng xử văn minh của du khách và cộng đồng.",
        "Chia sẻ lợi ích từ du lịch cho cộng đồng địa phương; khuyến khích người dân tham gia bảo tồn.",
        "Đa dạng hoá sản phẩm theo hướng văn hoá – trải nghiệm, tránh chỉ khai thác “chụp ảnh, check-in”.",
        "Ứng dụng công nghệ số: vé điện tử, tham quan ảo, thuyết minh đa ngôn ngữ, giám sát tải lượng khách.",
        "Tăng cường thanh tra, xử lí nghiêm các hành vi xâm hại di sản và kinh doanh trái phép.",
    ]),

    ("h2", "A3.5. Sử học với một số ngành, lĩnh vực khác (đọc để hiểu, dễ ra câu hỏi phụ)"),
    ("table", {
        "header": ["Lĩnh vực", "Vai trò của tri thức lịch sử"],
        "widths": [4.4 * cm, 13.4 * cm],
        "rows": [
            ["Báo chí – truyền thông", "Cung cấp thông tin nền chính xác, bối cảnh và chiều sâu cho tin tức; góp phần "
                                       "chống tin giả, xuyên tạc lịch sử."],
            ["Công nghiệp văn hoá", "Cung cấp chất liệu cho điện ảnh, xuất bản, âm nhạc, thời trang, trò chơi, "
                                    "mĩ thuật… tạo sản phẩm sáng tạo mang bản sắc."],
            ["Giáo dục", "Nội dung dạy học, giáo dục truyền thống, giáo dục di sản, hình thành nhân cách công dân."],
            ["Ngoại giao – chính sách", "Bài học kinh nghiệm trong ứng xử quốc tế; “ngoại giao văn hoá”; cung cấp "
                                        "căn cứ khoa học cho các vấn đề chủ quyền, biên giới, biển đảo."],
            ["Bảo tồn và phát triển", "Như mục A3.2 – cơ sở khoa học cho mọi hoạt động bảo tồn, phát huy giá trị."],
        ],
    }),

    ("h2", "A3.6. Một số di sản Việt Nam được UNESCO ghi danh (mốc thời gian dễ nhớ)"),
    ("table", {
        "header": ["Năm", "Di sản", "Loại"],
        "center": (0,),
        "widths": [1.9 * cm, 10.6 * cm, 5.3 * cm],
        "rows": [
            ["1993", "Quần thể di tích Cố đô Huế", "Văn hoá vật thể"],
            ["1994 (mở rộng 2000, 2023)", "Vịnh Hạ Long – Cát Bà", "Thiên nhiên"],
            ["1999", "Phố cổ Hội An; Thánh địa Mỹ Sơn", "Văn hoá vật thể"],
            ["2003", "Nhã nhạc cung đình Huế; Vườn quốc gia Phong Nha – Kẻ Bàng", "Phi vật thể; Thiên nhiên"],
            ["2005", "Không gian văn hoá cồng chiêng Tây Nguyên", "Phi vật thể"],
            ["2009", "Dân ca quan họ Bắc Ninh; Ca trù", "Phi vật thể"],
            ["2010", "Hoàng thành Thăng Long; Hội Gióng", "Vật thể; Phi vật thể"],
            ["2011", "Thành nhà Hồ", "Văn hoá vật thể"],
            ["2012", "Tín ngưỡng thờ cúng Hùng Vương", "Phi vật thể"],
            ["2014", "Quần thể danh thắng Tràng An", "Di sản hỗn hợp"],
        ],
    }),
    ("box", {"kind": "mnemonic", "title": "Dãy năm “thần chú”",
             "lines": ["<b>93 Huế – 94 Hạ Long – 99 Hội An &amp; Mỹ Sơn – 2003 Nhã nhạc &amp; Phong Nha – "
                       "2010 Thăng Long – 2011 Thành Hồ – 2014 Tràng An.</b>"]}),
    ("small", "Số liệu mang tính tham khảo (cập nhật đến 2024); khi làm bài chỉ cần nhớ các mốc chính và biết phân "
              "loại vật thể / phi vật thể / thiên nhiên."),
    ("pagebreak", 9),
]

# ---------------------------------------------------------------- TỔNG HỢP
BLOCKS += [
    ("banner", "PHẦN A (tiếp)", "SƠ ĐỒ TƯ DUY TÓM TẮT &amp; BẢNG TỪ KHOÁ DỄ NHẦM"),
    ("h2", "A4. Ba bài trong một trang"),
    ("table", {
        "header": ["Bài", "Trục 1", "Trục 2", "Trục 3"],
        "widths": [2.7 * cm, 5.1 * cm, 5.1 * cm, 4.9 * cm],
        "rows": [
            ["<b>Bài 1</b><br/>Hiện thực lịch sử &amp; nhận thức lịch sử",
             "<b>Khái niệm:</b> lịch sử (quá trình) – Sử học (khoa học) – sử liệu (bằng chứng).",
             "<b>Đối tượng – Chức năng – Nhiệm vụ:</b> quá khứ / khoa học + xã hội / tái hiện – rút bài học – "
             "giáo dục, phục vụ.",
             "<b>Hai phạm trù:</b> hiện thực (khách quan, duy nhất, không lặp lại) ↔ nhận thức (chủ quan, đa dạng, "
             "bổ sung được)."],
            ["<b>Bài 2</b><br/>Tri thức lịch sử &amp; cuộc sống",
             "<b>Tri thức &amp; sử liệu:</b> gốc / phái sinh; chữ viết – vật chất – hình ảnh – truyền miệng.",
             "<b>Quy trình:</b> XÁC – THU – XỬ – TRÌNH (4 bước).",
             "<b>Học suốt đời:</b> RỘNG – ĐỔI – SỐNG – NGHỀ – NƯỚC; <b>kết nối cuộc sống:</b> hiểu – vận dụng – hành động."],
            ["<b>Bài 3</b><br/>Vai trò của Sử học",
             "<b>Di sản:</b> vật thể / phi vật thể / thiên nhiên / tư liệu.",
             "<b>Với bảo tồn:</b> NHẬN – XẾP – GIỮ – DẠY – QUẢNG + 6 nhóm biện pháp.",
             "<b>Với du lịch:</b> 5 vai trò; tác động 2 chiều (TIỀN – Ý THỨC – SINH KẾ – QUẢNG BÁ / QUÁ TẢI – "
             "BIẾN DẠNG – BÊ TÔNG – Ô NHIỄM)."],
        ],
    }),

    ("h2", "A5. 12 cặp từ khoá dễ nhầm – đọc trước khi vào phòng thi"),
    ("table", {
        "header": ["Cặp dễ nhầm", "Phân biệt trong 1 câu"],
        "widths": [4.4 * cm, 13.4 * cm],
        "rows": [
            ["Lịch sử / Sử học", "Lịch sử là <b>quá trình</b> đã diễn ra; Sử học là <b>khoa học</b> nghiên cứu quá trình đó."],
            ["Hiện thực lịch sử / Nhận thức lịch sử", "Một bên là <b>sự thật khách quan</b>, một bên là <b>hiểu biết chủ quan</b> về sự thật ấy."],
            ["Khách quan / Chủ quan", "Khách quan = <b>không</b> phụ thuộc con người (hiện thực); chủ quan = <b>phụ thuộc</b> con người (nhận thức)."],
            ["Sử liệu gốc / Sử liệu phái sinh", "Gốc ra đời <b>cùng thời</b> sự kiện; phái sinh ra đời <b>sau</b>, dựa trên nguồn gốc."],
            ["Thu thập / Xử lí thông tin", "Thu thập = <b>tìm và ghi lại</b>; xử lí = <b>kiểm chứng, chọn lọc, sắp xếp</b>."],
            ["Di sản vật thể / Phi vật thể", "Vật thể <b>cầm nắm được</b> (di tích, hiện vật); phi vật thể là <b>giá trị tinh thần</b> (lễ hội, nhạc, nghề)."],
            ["Di sản văn hoá / Di sản thiên nhiên", "Văn hoá do <b>con người</b> tạo ra; thiên nhiên do <b>tự nhiên</b> tạo ra (có thể có bàn tay con người quản lý)."],
            ["Bảo tồn / Phát huy", "Bảo tồn = <b>giữ</b> cho di sản không mất đi; phát huy = <b>làm cho giá trị ấy sống</b> trong đời sống hôm nay."],
            ["Tài nguyên tự nhiên / Nhân văn", "Tự nhiên: biển, núi, hang động; nhân văn: di tích, lễ hội, làng nghề, ẩm thực."],
            ["Trùng tu / “Làm mới”", "Trùng tu đúng là <b>giữ nguyên trạng</b>; “làm mới”, bê tông hoá là <b>sai</b>, làm mất giá trị di sản."],
            ["Tri thức lịch sử / Tin đồn lịch sử", "Tri thức phải <b>kiểm chứng</b> bằng sử liệu; tin đồn chỉ dựa trên lan truyền, cảm xúc."],
            ["Di sản hỗn hợp", "Vừa có giá trị <b>văn hoá</b> vừa có giá trị <b>thiên nhiên</b> (ví dụ: Quần thể danh thắng Tràng An)."],
        ],
    }),
]

# =============================================================== PHẦN B – ĐỀ
BLOCKS += [
    ("banner", "PHẦN B", "ĐỀ KIỂM TRA MINH HOẠ – BÁM SÁT MA TRẬN"),
    ("small", "Đề được biên soạn đúng cấu trúc 45 phút: 20 câu trắc nghiệm nhiều lựa chọn (5,0 điểm) + 2 câu trắc "
              "nghiệm đúng/sai (2,0 điểm) + 1 câu tự luận (3,0 điểm). Nội dung phủ đủ 28 lệnh hỏi theo bản đặc tả: "
              "Bài 1 (I.1 – I.6), Bài 2 (I.7 – I.13, II.1), Bài 3 (I.14 – I.20, II.2, TL). "
              "<b>Hãy bấm giờ 45 phút và làm trọn vẹn trước khi xem đáp án.</b>"),
    ("h3", "A. TRẮC NGHIỆM NHIỀU LỰA CHỌN (20 câu – 5,0 điểm)"),
    ("small", "Chọn một phương án đúng nhất trong mỗi câu."),

    ("q", "<b>Câu 1.</b> Sử học là gì?"),
    ("opt", ["<b>A.</b> Toàn bộ quá trình phát triển của xã hội loài người từ khi xuất hiện đến nay.",
             "<b>B.</b> Khoa học nghiên cứu về quá khứ của xã hội loài người.",
             "<b>C.</b> Những hiểu biết của con người về tương lai của xã hội.",
             "<b>D.</b> Tập hợp các truyền thuyết, truyện kể dân gian về quá khứ."]),

    ("q", "<b>Câu 2.</b> Đối tượng nghiên cứu của Sử học là"),
    ("opt", ["<b>A.</b> những vấn đề đang diễn ra trong hiện tại.",
             "<b>B.</b> quy luật vận động của thế giới tự nhiên.",
             "<b>C.</b> quá khứ của xã hội loài người.",
             "<b>D.</b> các tác phẩm văn học nghệ thuật."]),

    ("q", "<b>Câu 3.</b> Hai chức năng cơ bản của Sử học là"),
    ("opt", ["<b>A.</b> chức năng khoa học và chức năng xã hội.",
             "<b>B.</b> chức năng kinh tế và chức năng quân sự.",
             "<b>C.</b> chức năng dự báo thời tiết và chức năng bảo vệ môi trường.",
             "<b>D.</b> chức năng lập pháp và chức năng tư pháp."]),

    ("q", "<b>Câu 4.</b> Vì sao nói Sử học là một khoa học?"),
    ("opt", ["<b>A.</b> Vì Sử học ghi chép lại toàn bộ truyền thuyết dân gian.",
             "<b>B.</b> Vì Sử học do các nhà văn, nhà thơ sáng tạo nên.",
             "<b>C.</b> Vì Sử học chỉ dựa vào cảm xúc và trí nhớ của người viết.",
             "<b>D.</b> Vì Sử học có đối tượng nghiên cứu riêng, có hệ thống lí thuyết, phương pháp nghiên cứu và "
                   "khả năng kiểm chứng."]),

    ("q", "<b>Câu 5.</b> Hiện thực lịch sử là"),
    ("opt", ["<b>A.</b> những hiểu biết của con người về quá khứ.",
             "<b>B.</b> những câu chuyện được kể lại theo trí nhớ của nhân chứng.",
             "<b>C.</b> toàn bộ những gì đã diễn ra trong quá khứ, tồn tại một cách khách quan.",
             "<b>D.</b> những tài liệu, hiện vật đang được lưu giữ trong bảo tàng."]),

    ("q", "<b>Câu 6.</b> Đặc điểm nào sau đây đúng với lịch sử được con người nhận thức?"),
    ("opt", ["<b>A.</b> Khách quan, duy nhất và không lặp lại.",
             "<b>B.</b> Mang tính chủ quan, có thể được bổ sung và điều chỉnh.",
             "<b>C.</b> Hoàn toàn không phụ thuộc vào nguồn sử liệu.",
             "<b>D.</b> Không bao giờ thay đổi, kể cả khi có sử liệu mới."]),

    ("q", "<b>Câu 7.</b> Trong quy trình thu thập và xử lí thông tin, sử liệu, việc đầu tiên cần làm là"),
    ("opt", ["<b>A.</b> xác định vấn đề cần tìm hiểu.",
             "<b>B.</b> trình bày kết quả nghiên cứu.",
             "<b>C.</b> xử lí các thông tin đã thu thập được.",
             "<b>D.</b> tìm kiếm thông tin trên internet."]),

    ("q", "<b>Câu 8.</b> Nguồn tư liệu nào sau đây được xếp vào loại sử liệu gốc?"),
    ("opt", ["<b>A.</b> Sách giáo khoa Lịch sử lớp 10.",
             "<b>B.</b> Bài giảng của giáo viên trên lớp.",
             "<b>C.</b> Bản gốc “Tuyên ngôn Độc lập” năm 1945.",
             "<b>D.</b> Phim tài liệu dựng lại cảnh Cách mạng tháng Tám năm 1945."]),

    ("q", "<b>Câu 9.</b> Cho các bước: (1) Xử lí thông tin, sử liệu; (2) Xác định vấn đề cần tìm hiểu; "
          "(3) Trình bày kết quả; (4) Thu thập thông tin, sử liệu. Trình tự đúng là"),
    ("opt", ["<b>A.</b> (1) → (2) → (3) → (4).",
             "<b>B.</b> (2) → (4) → (1) → (3).",
             "<b>C.</b> (2) → (1) → (4) → (3).",
             "<b>D.</b> (4) → (1) → (2) → (3)."]),

    ("q", "<b>Câu 10.</b> Vì sao sau khi thu thập thông tin, sử liệu ta phải tiến hành xử lí?"),
    ("opt", ["<b>A.</b> Để có thật nhiều tư liệu cho bài viết dài hơn.",
             "<b>B.</b> Để sao chép nguyên văn vào bài làm.",
             "<b>C.</b> Để rút ngắn thời gian hoàn thành sản phẩm.",
             "<b>D.</b> Để loại bỏ thông tin sai lệch, đánh giá độ tin cậy, bảo đảm tính khách quan và chính xác."]),

    ("q", "<b>Câu 11.</b> Việc học tập và khám phá lịch sử suốt đời là cần thiết vì"),
    ("opt", ["<b>A.</b> tri thức lịch sử rất rộng lớn và nhận thức lịch sử luôn được bổ sung, điều chỉnh.",
             "<b>B.</b> chỉ cần học lịch sử khi chuẩn bị thi.",
             "<b>C.</b> mọi sự kiện lịch sử đã được ghi chép đầy đủ và không bao giờ thay đổi.",
             "<b>D.</b> lịch sử chỉ dành cho các nhà nghiên cứu chuyên nghiệp."]),

    ("q", "<b>Câu 12.</b> Nhận định nào sau đây đúng về tri thức lịch sử?"),
    ("opt", ["<b>A.</b> Là bản sao y nguyên của quá khứ và không bao giờ thay đổi.",
             "<b>B.</b> Chỉ gồm những sự kiện được ghi trong sách giáo khoa.",
             "<b>C.</b> Là những hiểu biết của con người về quá khứ, được tích luỹ và không ngừng bổ sung, hoàn thiện.",
             "<b>D.</b> Chỉ có giá trị trong các kì thi, không liên quan đến đời sống."]),

    ("q", "<b>Câu 13.</b> Việc làm nào sau đây thể hiện sự kết nối tri thức lịch sử vào cuộc sống?"),
    ("opt", ["<b>A.</b> Học thuộc lòng năm tháng của các sự kiện để trả bài.",
             "<b>B.</b> Vận dụng bài học về giá trị hoà bình để lí giải một cuộc xung đột đang diễn ra trên thế giới.",
             "<b>C.</b> Chép lại nguyên văn một bài viết trên mạng vào vở.",
             "<b>D.</b> Chỉ xem phim lịch sử để giải trí."]),

    ("q", "<b>Câu 14.</b> Vai trò cơ bản của Sử học đối với công tác bảo tồn di sản là"),
    ("opt", ["<b>A.</b> cung cấp cơ sở khoa học để nhận diện, đánh giá giá trị và định hướng bảo tồn di sản.",
             "<b>B.</b> trang trí cho di tích trở nên đẹp và mới hơn.",
             "<b>C.</b> thay thế hoàn toàn công tác bảo tồn di sản.",
             "<b>D.</b> tổ chức lễ hội để thu hút khách du lịch."]),

    ("q", "<b>Câu 15.</b> Di sản nào sau đây là di sản văn hoá phi vật thể?"),
    ("opt", ["<b>A.</b> Vịnh Hạ Long.", "<b>B.</b> Hoàng thành Thăng Long.",
             "<b>C.</b> Nhã nhạc cung đình Huế.", "<b>D.</b> Thành nhà Hồ."]),

    ("q", "<b>Câu 16.</b> Công tác trùng tu, tôn tạo di tích cần dựa trên kết quả nghiên cứu của Sử học vì"),
    ("opt", ["<b>A.</b> để di tích trông mới hơn và hấp dẫn du khách hơn.",
             "<b>B.</b> để giữ đúng nguyên trạng, bảo đảm giá trị lịch sử – văn hoá và tránh làm sai lệch di sản.",
             "<b>C.</b> để tiết kiệm tối đa kinh phí trùng tu.",
             "<b>D.</b> để thay thế vật liệu cũ bằng vật liệu bê tông hiện đại."]),

    ("q", "<b>Câu 17.</b> Địa danh nào sau đây là tài nguyên du lịch nhân văn?"),
    ("opt", ["<b>A.</b> Vịnh Hạ Long.", "<b>B.</b> Vườn quốc gia Phong Nha – Kẻ Bàng.",
             "<b>C.</b> Sa Pa – Fansipan.", "<b>D.</b> Phố cổ Hội An."]),

    ("q", "<b>Câu 18.</b> Loại hình du lịch gắn với việc tìm hiểu, trải nghiệm di tích, lễ hội, làng nghề truyền thống "
          "được gọi là"),
    ("opt", ["<b>A.</b> du lịch sinh thái.", "<b>B.</b> du lịch nghỉ dưỡng.",
             "<b>C.</b> du lịch văn hoá (du lịch di sản).", "<b>D.</b> du lịch mạo hiểm."]),

    ("q", "<b>Câu 19.</b> Ý nào sau đây phản ánh đúng vai trò của lịch sử – văn hoá đối với sự phát triển du lịch?"),
    ("opt", ["<b>A.</b> Là nguồn tài nguyên tạo nên sản phẩm du lịch đặc sắc, đồng thời cung cấp nội dung, câu chuyện "
                   "cho điểm đến.",
             "<b>B.</b> Làm cho các điểm du lịch trở nên giống nhau hơn.",
             "<b>C.</b> Chỉ dùng để trang trí khách sạn, nhà hàng.",
             "<b>D.</b> Không có vai trò vì du khách chỉ quan tâm cảnh đẹp tự nhiên."]),

    ("q", "<b>Câu 20.</b> Biểu hiện nào sau đây là tác động tiêu cực của du lịch đến di sản?"),
    ("opt", ["<b>A.</b> Tạo nguồn thu để trùng tu, tôn tạo di tích.",
             "<b>B.</b> Nâng cao ý thức bảo vệ di sản của cộng đồng địa phương.",
             "<b>C.</b> Quảng bá giá trị di sản ra thế giới.",
             "<b>D.</b> Khai thác quá mức khiến di tích xuống cấp, bị “thương mại hoá” và mất bản sắc."]),

    ("h3", "B. TRẮC NGHIỆM ĐÚNG/SAI (2 câu – 2,0 điểm)", 9),
    ("small", "Trong mỗi câu, hãy ghi <b>Đ</b> (đúng) hoặc <b>S</b> (sai) cho từng nhận định a), b), c), d)."),

    ("q", "<b>Câu 1 (II.1).</b> Cho các nhận định về tri thức lịch sử và việc học tập lịch sử:"),
    ("opt", ["<b>a)</b> Tri thức lịch sử là những hiểu biết của con người về quá khứ, được tích luỹ qua học tập, "
                    "nghiên cứu và trải nghiệm.",
             "<b>b)</b> Cần học tập, khám phá lịch sử suốt đời vì tri thức lịch sử rất rộng lớn và nhận thức lịch sử "
                    "luôn được bổ sung, điều chỉnh.",
             "<b>c)</b> Kết nối tri thức lịch sử với cuộc sống chỉ là việc học thuộc các sự kiện để làm bài kiểm tra.",
             "<b>d)</b> Khi làm dự án “Di sản quê em”, nhóm học sinh đối chiếu thông tin trên bia đá với sách địa chí "
                    "và lời kể của nhân chứng trước khi viết báo cáo – đó là biểu hiện của việc xử lí và kiểm chứng "
                    "sử liệu."]),

    ("q", "<b>Câu 2 (II.2).</b> Cho các nhận định về vai trò của Sử học:"),
    ("opt", ["<b>a)</b> Sử học cung cấp cơ sở khoa học cho việc nhận diện, đánh giá và bảo tồn di sản văn hoá, "
                    "di sản thiên nhiên.",
             "<b>b)</b> Du lịch chỉ gây tác động tiêu cực đến di sản nên cần hạn chế phát triển du lịch.",
             "<b>c)</b> Di sản văn hoá vật thể bao gồm di tích lịch sử – văn hoá, danh lam thắng cảnh, di vật, "
                    "cổ vật, bảo vật quốc gia.",
             "<b>d)</b> Để phát triển du lịch bền vững cần giới hạn sức chứa, chia sẻ lợi ích cho cộng đồng và "
                    "giáo dục ứng xử văn minh cho du khách."]),

    ("h3", "C. TỰ LUẬN (1 câu – 3,0 điểm)", 9),
    ("q", "<b>Câu 1.</b>"),
    ("p", "<b>a)</b> (1,0 điểm) Trình bày vai trò của Sử học đối với công tác bảo tồn và phát huy giá trị di sản "
          "văn hoá, di sản thiên nhiên."),
    ("p", "<b>b)</b> (2,0 điểm) Là học sinh, em sẽ làm gì để góp phần bảo tồn và phát huy giá trị của một di sản "
          "ở địa phương em? Nêu ít nhất <b>03</b> việc làm cụ thể và giải thích ngắn gọn ý nghĩa của mỗi việc làm."),
    ("box", {"kind": "tip", "title": "Gợi ý phân bổ thời gian trong 45 phút",
             "lines": ["20 câu trắc nghiệm: <b>15 phút</b> (1,5 phút/câu, câu dễ làm trước) → 2 câu đúng/sai: "
                       "<b>8 phút</b> → tự luận: <b>20 phút</b> → còn <b>2 phút</b> rà lại phiếu trả lời và "
                       "kiểm tra lỗi chính tả, lỗi diễn đạt."]}),
    ("h3", "D. PHIẾU TRẢ LỜI (photocopy hoặc kẻ lại để làm bài)", 7),
    ("table", {
        "header": ["Câu"] + [str(i) for i in range(1, 11)],
        "center": tuple(range(0, 11)),
        "widths": [2.2 * cm] + [1.48 * cm] * 10,
        "rows": [["<b>Chọn</b>", "", "", "", "", "", "", "", "", "", ""]],
        "row_h": [0.85 * cm, 0.95 * cm],
    }),
    ("table", {
        "header": ["Câu"] + [str(i) for i in range(11, 21)],
        "center": tuple(range(0, 11)),
        "widths": [2.2 * cm] + [1.48 * cm] * 10,
        "rows": [["<b>Chọn</b>", "", "", "", "", "", "", "", "", "", ""]],
        "row_h": [0.85 * cm, 0.95 * cm],
    }),
    ("table", {
        "header": ["Đúng/Sai", "a", "b", "c", "d", "Ghi chú"],
        "center": (0, 1, 2, 3, 4),
        "widths": [2.6 * cm, 2.0 * cm, 2.0 * cm, 2.0 * cm, 2.0 * cm, 7.2 * cm],
        "rows": [["<b>II.1</b>", "", "", "", "", ""],
                 ["<b>II.2</b>", "", "", "", "", ""]],
        "row_h": [0.85 * cm, 0.9 * cm, 0.9 * cm],
    }),
    ("small", "Mẹo: ghi đáp án theo hàng ngang (1–10, 11–20) để khi rà lại chỉ cần so một lượt, tránh lệch dòng — "
              "lỗi phổ biến nhất khi tô phiếu trả lời."),
    ("pagebreak",),
]

# =============================================================== PHẦN C – ĐÁP ÁN
BLOCKS += [
    ("banner", "PHẦN C", "ĐÁP ÁN – GIẢI THÍCH – BIỂU ĐIỂM"),

    ("h2", "C1. Đáp án nhanh 20 câu trắc nghiệm"),
    ("table", {
        "header": ["Câu"] + [str(i) for i in range(1, 11)],
        "center": tuple(range(0, 11)),
        "widths": [2.2 * cm] + [1.48 * cm] * 10,
        "rows": [["<b>Đáp án</b>", "B", "C", "A", "D", "C", "B", "A", "C", "B", "D"]],
    }),
    ("table", {
        "header": ["Câu"] + [str(i) for i in range(11, 21)],
        "center": tuple(range(0, 11)),
        "widths": [2.2 * cm] + [1.48 * cm] * 10,
        "rows": [["<b>Đáp án</b>", "A", "C", "B", "A", "C", "B", "D", "C", "A", "D"]],
    }),

    ("h2", "C2. Giải thích chi tiết từng câu"),
    ("ans", "<b>Câu 1 – B.</b> Sử học là khoa học nghiên cứu quá khứ của xã hội loài người. Phương án A nói về "
            "<i>lịch sử</i> (quá trình), C nói về tương lai, D chỉ là một loại nguồn tư liệu."),
    ("ans", "<b>Câu 2 – C.</b> Đối tượng nghiên cứu của Sử học là quá khứ của xã hội loài người (con người, sự kiện, "
            "hiện tượng, quá trình lịch sử)."),
    ("ans", "<b>Câu 3 – A.</b> Sử học có hai chức năng: <b>khoa học</b> (nhận thức, khám phá, cung cấp tri thức) và "
            "<b>xã hội</b> (giáo dục, phục vụ cuộc sống). Các phương án còn lại là chức năng của ngành khác."),
    ("ans", "<b>Câu 4 – D.</b> Một ngành được coi là khoa học khi có đối tượng nghiên cứu riêng, hệ thống lí thuyết, "
            "phương pháp nghiên cứu và khả năng kiểm chứng. A, B, C đều mô tả cách làm thiếu căn cứ khoa học."),
    ("ans", "<b>Câu 5 – C.</b> Hiện thực lịch sử là toàn bộ những gì đã diễn ra trong quá khứ, tồn tại khách quan, "
            "không phụ thuộc ý muốn con người. A là <i>nhận thức</i> lịch sử; B, D chỉ là một phần nguồn tư liệu."),
    ("ans", "<b>Câu 6 – B.</b> Lịch sử được con người nhận thức mang tính <b>chủ quan</b>, phụ thuộc quan điểm, "
            "trình độ, sử liệu và có thể được bổ sung, điều chỉnh. A là đặc điểm của hiện thực lịch sử; C, D sai "
            "vì nhận thức luôn gắn với sử liệu và luôn thay đổi khi có sử liệu mới."),
    ("ans", "<b>Câu 7 – A.</b> Quy trình 4 bước: xác định vấn đề → thu thập thông tin, sử liệu → xử lí → trình bày "
            "kết quả. Bước 1 luôn là xác định vấn đề (câu hỏi nghiên cứu)."),
    ("ans", "<b>Câu 8 – C.</b> Sử liệu gốc ra đời cùng thời hoặc gần sự kiện, do người trong cuộc tạo ra. A, B, D "
            "đều là sử liệu phái sinh (ra đời sau, dựa trên sử liệu gốc)."),
    ("ans", "<b>Câu 9 – B.</b> Trình tự: (2) xác định vấn đề → (4) thu thập → (1) xử lí → (3) trình bày kết quả, "
            "tức mẹo nhớ <b>XÁC – THU – XỬ – TRÌNH</b>."),
    ("ans", "<b>Câu 10 – D.</b> Mục đích của xử lí là phân loại, kiểm chứng chéo, đánh giá độ tin cậy, loại bỏ thông "
             "tin sai để bảo đảm tính khách quan, chính xác. A, B, C đều là cách làm phản khoa học."),
    ("ans", "<b>Câu 11 – A.</b> Tri thức lịch sử vô cùng rộng lớn, nhận thức lịch sử luôn được bổ sung, điều chỉnh, "
             "cuộc sống luôn vận động → phải học suốt đời."),
    ("ans", "<b>Câu 12 – C.</b> Tri thức lịch sử là hiểu biết về quá khứ, được tích luỹ và không ngừng hoàn thiện. "
             "A sai (không phải bản sao y nguyên); B, D thu hẹp và hạ thấp giá trị của tri thức lịch sử."),
    ("ans", "<b>Câu 13 – B.</b> Kết nối tri thức lịch sử vào cuộc sống là dùng bài học lịch sử để lí giải, ứng xử "
             "trước vấn đề của hiện tại. A, C, D chỉ dừng ở học thuộc, sao chép hoặc giải trí."),
    ("ans", "<b>Câu 14 – A.</b> Sử học cung cấp cơ sở khoa học để nhận diện, đánh giá giá trị, lập hồ sơ, xếp hạng "
             "và định hướng bảo tồn di sản; nó không thay thế công tác bảo tồn."),
    ("ans", "<b>Câu 15 – C.</b> Nhã nhạc cung đình Huế là di sản văn hoá <b>phi vật thể</b>; Vịnh Hạ Long là di sản "
             "thiên nhiên; Hoàng thành Thăng Long và Thành nhà Hồ là di sản văn hoá vật thể."),
    ("ans", "<b>Câu 16 – B.</b> Nghiên cứu lịch sử xác định niên đại, nguyên liệu, kĩ thuật, giá trị gốc của di tích "
             "→ trùng tu đúng nguyên trạng, tránh “làm mới”, bê tông hoá, làm sai lệch di sản."),
    ("ans", "<b>Câu 17 – D.</b> Phố cổ Hội An là tài nguyên du lịch <b>nhân văn</b> (di sản văn hoá); A, B, C là tài "
             "nguyên du lịch tự nhiên."),
    ("ans", "<b>Câu 18 – C.</b> Đó là <b>du lịch văn hoá</b> (du lịch di sản) – loại hình khai thác các giá trị "
             "lịch sử, văn hoá của điểm đến."),
    ("ans", "<b>Câu 19 – A.</b> Lịch sử – văn hoá là nguồn tài nguyên, đồng thời cung cấp nội dung, câu chuyện, "
             "ý nghĩa cho điểm đến, giúp sản phẩm du lịch đặc sắc và khó sao chép."),
    ("ans", "<b>Câu 20 – D.</b> Khai thác quá mức gây xuống cấp, thương mại hoá, biến dạng, mất bản sắc là tác động "
             "tiêu cực; A, B, C là tác động tích cực."),

    ("h2", "C3. Đáp án trắc nghiệm Đúng/Sai"),
    ("table", {
        "header": ["Câu", "a", "b", "c", "d"],
        "center": (0, 1, 2, 3, 4),
        "widths": [3.0 * cm, 3.7 * cm, 3.7 * cm, 3.7 * cm, 3.7 * cm],
        "rows": [["<b>II.1</b>", "Đ", "Đ", "S", "Đ"],
                 ["<b>II.2</b>", "Đ", "S", "Đ", "Đ"]],
    }),
    ("ans", "<b>II.1 – a) Đ.</b> Đúng theo khái niệm tri thức lịch sử."),
    ("ans", "<b>II.1 – b) Đ.</b> Đúng: tri thức rộng lớn + nhận thức luôn được bổ sung, điều chỉnh là hai lí do "
            "cốt lõi của việc học suốt đời."),
    ("ans", "<b>II.1 – c) S.</b> Sai: kết nối tri thức lịch sử với cuộc sống là <b>vận dụng</b> vào giải thích, "
            "ứng xử, hành động thực tiễn, không phải học thuộc để trả bài."),
    ("ans", "<b>II.1 – d) Đ.</b> Đúng: đối chiếu nhiều nguồn (bia đá – sách – nhân chứng) chính là bước xử lí, "
            "kiểm chứng sử liệu."),
    ("ans", "<b>II.2 – a) Đ.</b> Đúng: đây là vai trò nền tảng của Sử học với di sản."),
    ("ans", "<b>II.2 – b) S.</b> Sai: du lịch có cả tác động tích cực (nguồn thu, ý thức, sinh kế, quảng bá) và "
            "tiêu cực; vấn đề là <b>phát triển bền vững</b> gắn với bảo tồn, không phải hạn chế du lịch."),
    ("ans", "<b>II.2 – c) Đ.</b> Đúng theo cách phân loại di sản văn hoá vật thể."),
    ("ans", "<b>II.2 – d) Đ.</b> Đúng: giới hạn sức chứa, chia sẻ lợi ích và giáo dục ứng xử là ba giải pháp cốt lõi "
            "của du lịch bền vững."),

    ("h2", "C4. Đáp án và biểu điểm câu tự luận"),
    ("h3", "a) Vai trò của Sử học với công tác bảo tồn, phát huy di sản (1,0 điểm)"),
    ("bullets", [
        "<b>Nhận diện giá trị:</b> xác định nguồn gốc, niên đại, giá trị lịch sử – văn hoá – khoa học – thẩm mĩ "
        "của di sản (0,25 điểm).",
        "<b>Cơ sở khoa học để xếp hạng, lập hồ sơ</b> di tích cấp tỉnh/quốc gia/quốc gia đặc biệt và đề nghị UNESCO "
        "ghi danh (0,25 điểm).",
        "<b>Định hướng bảo tồn, trùng tu đúng nguyên trạng</b>, phát hiện nguy cơ xuống cấp, xâm hại, ngăn chặn các "
        "phương án sai như bê tông hoá, “làm mới” di tích (0,25 điểm).",
        "<b>Giáo dục truyền thống, nâng cao ý thức cộng đồng và quảng bá, khai thác bền vững</b> giá trị di sản gắn "
        "với du lịch, tạo sinh kế (0,25 điểm).",
        "(Nêu được 2 – 3 ý đúng, diễn đạt rõ: 0,5 – 0,75 điểm; nếu chỉ nêu tên vai trò mà không giải thích: tối đa 0,5.)",
    ]),
    ("h3", "b) Việc làm của học sinh (2,0 điểm) – dàn ý tham khảo"),
    ("p", "<b>Mở đoạn (0,25):</b> Giới thiệu ngắn về một di sản ở địa phương (tên di sản, loại di sản, giá trị nổi bật)."),
    ("p", "<b>Thân đoạn (1,5):</b> mỗi việc làm trình bày theo cấu trúc “<b>làm gì – như thế nào – để làm gì</b>”. "
          "Gợi ý 5 nhóm việc làm:"),
    ("nums", [
        "<b>Tìm hiểu và tuyên truyền:</b> sưu tầm tư liệu về di sản, viết bài/thiết kế infographic, đăng trên "
        "trang của trường, thuyết trình trong giờ sinh hoạt lớp → giúp bạn bè hiểu và tự hào về di sản.",
        "<b>Tham gia bảo vệ trực tiếp:</b> cùng Đoàn trường dọn vệ sinh, nhổ cỏ, không viết vẽ lên di tích, "
        "nhắc nhở người khác không xâm hại → giữ cảnh quan và giá trị di sản.",
        "<b>Học tập qua trải nghiệm:</b> tham gia chuyến tham quan học tập, làm bài thu hoạch, đóng vai hướng dẫn "
        "viên nhí → biến kiến thức thành hiểu biết thật.",
        "<b>Số hoá và sáng tạo:</b> chụp ảnh, quay video, tạo bản đồ số/tour ảo về di sản, viết bài song ngữ → "
        "quảng bá rộng rãi, thu hút du khách có trách nhiệm.",
        "<b>Vận động cộng đồng:</b> cùng gia đình, hàng xóm giữ gìn lễ hội, nghề truyền thống; phản ánh với chính "
        "quyền khi thấy di sản bị xâm hại → bảo vệ bền vững, lâu dài.",
    ]),
    ("p", "<b>Kết đoạn (0,25):</b> Khẳng định trách nhiệm của thế hệ trẻ: “Bảo vệ di sản là bảo vệ ký ức, bản sắc "
          "và tương lai của dân tộc”."),
    ("small", "Lưu ý chấm: nêu đủ 3 việc làm <b>cụ thể</b> (0,75) + giải thích được ý nghĩa từng việc (0,75) + "
              "liên hệ đúng di sản địa phương và diễn đạt mạch lạc (0,5). Bài chỉ nêu chung chung "
              "(“bảo vệ di sản”, “tuyên truyền”) mà không có việc làm cụ thể: không quá 1,0 điểm."),

    ("box", {"kind": "note", "title": "Mẫu câu dùng ngay (viết sẵn – chỉ cần thay tên di sản)",
             "lines": [
                 "<b>Mở bài:</b> “Trên địa bàn xã/huyện/tỉnh … có di tích …, một di sản văn hoá vật thể gắn với "
                 "sự kiện … Đây không chỉ là điểm đến quen thuộc mà còn là ‘trang sử bằng đá’ của quê hương em.”",
                 "<b>Thân bài:</b> “Trước hết, em cùng các bạn trong Câu lạc bộ Lịch sử của trường đã … nhằm … "
                 "Thứ hai, … Thứ ba, …”",
                 "<b>Kết bài:</b> “Những việc làm ấy tuy nhỏ nhưng góp phần giữ cho ký ức của cha ông không bị "
                 "phai mờ. Bảo vệ di sản hôm nay chính là trao lại cho mai sau một phần bản sắc của dân tộc.”",
             ]}),

    ("h2", "C5. Chiến thuật phòng thi &amp; lỗi cần tránh"),
    ("table", {
        "header": ["Tình huống", "Cách xử lí"],
        "widths": [6.6 * cm, 11.2 * cm],
        "rows": [
            ["Gặp câu trắc nghiệm “lạ”", "Đọc kĩ từ <b>không</b>, <b>ngoại trừ</b>, <b>trước tiên</b>, <b>chủ yếu</b>. "
                                        "Loại phương án sai rõ ràng trước, còn 2 phương án thì chọn phương án "
                                        "khớp với khái niệm trong SGK."],
            ["Phân vân giữa 2 phương án", "Chọn phương án <b>đúng bản chất khái niệm</b>, không chọn phương án "
                                          "“nghe hay” nhưng thiếu căn cứ; tránh phương án tuyệt đối hoá "
                                          "(“chỉ”, “mọi”, “hoàn toàn”, “không bao giờ”)."],
            ["Câu đúng/sai", "Mỗi ý phải xét <b>độc lập</b>, không suy ra từ ý trước. Ý có từ “chỉ”, “duy nhất”, "
                             "“hoàn toàn” thường là <b>Sai</b>."],
            ["Tự luận", "Bám 3 tầng: <b>Nêu – Giải thích – Liên hệ</b>. Chia ý rõ ràng, mỗi ý một đoạn ngắn hoặc "
                        "gạch đầu dòng; đừng viết một khối văn dài."],
            ["Hết giờ mà còn câu trống", "Không bỏ trống: loại trừ rồi chọn; ở phần đúng/sai, ý nào không chắc "
                                         "vẫn phải ghi Đ hoặc S."],
        ],
    }),

    ("h2", "C6. Checklist 10 giây trước khi vào phòng thi"),
    ("bullets", [
        "Tôi phân biệt được <b>lịch sử – Sử học – sử liệu</b> chưa?",
        "Tôi nhớ <b>2 chức năng</b> và <b>3 nhiệm vụ</b> của Sử học chưa?",
        "Tôi kể được <b>3 đặc điểm hiện thực lịch sử</b> và <b>4 đặc điểm nhận thức lịch sử</b> chưa?",
        "Tôi nhớ <b>4 bước XÁC – THU – XỬ – TRÌNH</b> chưa?",
        "Tôi nêu được <b>5 lí do RỘNG – ĐỔI – SỐNG – NGHỀ – NƯỚC</b> chưa?",
        "Tôi nhớ <b>5 vai trò NHẬN – XẾP – GIỮ – DẠY – QUẢNG</b> chưa?",
        "Tôi phân loại được <b>vật thể / phi vật thể / thiên nhiên</b> chưa?",
        "Tôi nêu được <b>tác động tích cực và tiêu cực</b> của du lịch chưa?",
        "Tôi có <b>3 việc làm cụ thể</b> cho câu tự luận vận dụng chưa?",
        "Tôi đã ăn sáng, mang bút, thước, máy tính (nếu được dùng) và đến đúng giờ chưa?",
    ]),
    ("pagebreak", 9),
    ("banner", "PHỤ LỤC", "3 SƠ ĐỒ TƯ DUY DẠNG CHỮ – TỰ CHÉP LẠI LÀ NHỚ"),
    ("small", "Cách dùng: che phần nhánh, tự viết lại từ khoá gốc; mỗi sơ đồ chỉ cần 3 phút. Nếu viết đúng "
              "toàn bộ nhánh, em đã nắm được 80% nội dung bài."),
    ("trees", [
        ("SƠ ĐỒ 1 – BÀI 1", [
            "LỊCH SỬ & SỬ HỌC",
            "├ Khái niệm",
            "│ ├ Lịch sử = quá trình",
            "│ ├ Sử học = khoa học",
            "│ └ Sử liệu = bằng chứng",
            "├ Sử học",
            "│ ├ Đối tượng: quá khứ",
            "│ ├ Chức năng:",
            "│ │  khoa học + xã hội",
            "│ └ Nhiệm vụ:",
            "│    tái hiện – rút bài học",
            "│    – giáo dục, phục vụ",
            "└ Hai phạm trù",
            "  ├ Hiện thực: khách quan,",
            "  │  duy nhất, không lặp lại,",
            "  │  không sửa được",
            "  └ Nhận thức: chủ quan,",
            "     đa dạng, gắn sử liệu,",
            "     bổ sung được",
        ]),
        ("SƠ ĐỒ 2 – BÀI 2", [
            "TRI THỨC LỊCH SỬ",
            "├ Sử liệu",
            "│ ├ Gốc / phái sinh",
            "│ └ Chữ – vật chất –",
            "│   hình ảnh – lời kể",
            "├ Quy trình 4 bước",
            "│ XÁC → THU → XỬ → TRÌNH",
            "├ Học suốt đời",
            "│ RỘNG – ĐỔI – SỐNG",
            "│ – NGHỀ – NƯỚC",
            "└ Kết nối cuộc sống",
            "  ├ Hiểu – giải thích",
            "  ├ Vận dụng – liên hệ",
            "  └ Đề xuất – hành động",
            "",
            "Kiểm chứng nguồn tin:",
            "Ai nói? Khi nào?",
            "Dựa vào đâu?",
        ]),
        ("SƠ ĐỒ 3 – BÀI 3", [
            "VAI TRÒ CỦA SỬ HỌC",
            "├ Di sản",
            "│ ├ Vật thể / phi vật thể",
            "│ └ Thiên nhiên / hỗn hợp",
            "├ Với bảo tồn",
            "│ NHẬN – XẾP – GIỮ",
            "│ – DẠY – QUẢNG",
            "├ Biện pháp",
            "│ Tuyên truyền – pháp luật",
            "│ – khoa học – nguồn lực",
            "│ – du lịch bền vững",
            "│ – cộng đồng làm chủ",
            "└ Với du lịch",
            "  ├ Tích cực: TIỀN –",
            "  │  Ý THỨC – SINH KẾ –",
            "  │  QUẢNG BÁ",
            "  └ Tiêu cực: QUÁ TẢI –",
            "     BIẾN DẠNG – BÊ TÔNG",
            "     – Ô NHIỄM",
        ]),
    ]),
    ("box", {"kind": "tip", "title": "Cách tự kiểm tra bằng sơ đồ",
             "lines": ["Gấp đôi tờ giấy: nửa trái ghi từ khoá gốc, nửa phải tự viết các nhánh. Viết sai nhánh nào "
                       "thì quay lại đúng mục A tương ứng – đó chính là phần em cần ôn thêm, không cần đọc lại cả bài."]}),
    ("box", {"kind": "note", "title": "Lời chúc",
             "lines": ["Ba bài, hai chủ đề, một tấm bản đồ trong đầu – và 45 phút chỉ là dịp để em kể lại câu chuyện "
                       "ấy thật rõ ràng. <b>Chúc em làm bài tự tin và đạt kết quả cao!</b>"]}),
]
