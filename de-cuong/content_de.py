"""Đề minh họa bám sát ma trận + đáp án chi tiết.

Mỗi câu trắc nghiệm: (đề, [đáp án đúng, nhiễu 1, nhiễu 2, nhiễu 3], vị trí đáp án, mức độ, giải thích).
Hàm `mcq` trong layout sẽ đặt đáp án đúng vào đúng vị trí A/B/C/D đã chỉ định.
"""

# Cấp độ của từng vị trí câu theo ma trận (I.1 → I.20)
LEVELS = (
    ["Bài 1 • Biết"] * 3 + ["Bài 1 • Hiểu"] + ["Bài 1 • Biết"] * 2
    + ["Bài 2 • Biết"] * 3 + ["Bài 2 • Hiểu"] * 2 + ["Bài 2 • Biết"] * 2
    + ["Bài 3 • Biết"] * 2 + ["Bài 3 • Hiểu"] + ["Bài 3 • Biết"] * 2 + ["Bài 3 • Hiểu"] * 2
)
TF_LEVELS = ["Hiểu", "Hiểu", "Biết", "Vận dụng"]

# =====================================================================
# ĐỀ MINH HỌA SỐ 1
# =====================================================================
DE1_KEYS = "BADCACBDABCDBADCADBC"

DE1_MCQ = [
    # ---------------- Bài 1 ----------------
    ("Hiện thực lịch sử là",
     ["toàn bộ những gì đã diễn ra trong quá khứ, tồn tại khách quan, độc lập với ý muốn của con người.",
      "những hiểu biết, tri thức của con người về quá khứ được trình bày theo nhiều cách khác nhau.",
      "những câu chuyện về quá khứ được lưu truyền bằng hình thức truyền miệng trong dân gian.",
      "những ghi chép của các nhà sử học về các sự kiện, nhân vật nổi bật trong quá khứ."],
     "Hiện thực lịch sử là cái <b>đã diễn ra</b>, tồn tại <b>khách quan</b>. {1}, {2}, {3} đều là lịch sử <b>được con người nhận thức</b>."),
    ("Sử học là",
     ["khoa học nghiên cứu về quá khứ của con người và xã hội loài người.",
      "khoa học nghiên cứu về sự hình thành và phát triển của Trái Đất.",
      "những gì đã diễn ra trong quá khứ của xã hội loài người.",
      "khoa học nghiên cứu về các hiện tượng tự nhiên và xã hội hiện tại."],
     "Định nghĩa SGK: Sử học là <b>khoa học nghiên cứu về quá khứ của con người và xã hội loài người</b>. Phương án {2} là khái niệm “lịch sử” (hiện thực lịch sử)."),
    ("Đối tượng nghiên cứu của Sử học là",
     ["quá khứ của con người và xã hội loài người trên mọi lĩnh vực.",
      "các hoạt động chính trị và quân sự của các triều đại phong kiến.",
      "những dự báo về sự phát triển của xã hội loài người trong tương lai.",
      "quá trình hình thành và biến đổi của thế giới tự nhiên."],
     "Đối tượng của Sử học là <b>toàn bộ quá khứ</b> của loài người, trên <b>mọi lĩnh vực</b> (không chỉ chính trị, quân sự)."),
    ("Nội dung nào sau đây là <b>lịch sử được con người nhận thức</b>?",
     ["Đoạn chép về chiến thắng Bạch Đằng năm 938 trong sách “Đại Việt sử kí toàn thư”.",
      "Trận chiến trên sông Bạch Đằng năm 938 do Ngô Quyền lãnh đạo.",
      "Quân Nam Hán bị đánh bại trên sông Bạch Đằng vào cuối năm 938.",
      "Ngô Quyền xưng vương, đóng đô ở Cổ Loa vào năm 939."],
     "Sự kiện “đã xảy ra” ({1}, {2}, {3}) là <b>hiện thực lịch sử</b>. Bản ghi chép trong sách sử là <b>hiểu biết của con người</b> về sự kiện → lịch sử được nhận thức."),
    ("Nhiệm vụ nào sau đây <b>không</b> phải là nhiệm vụ của Sử học?",
     ["Sáng tác nghệ thuật.", "Nhận thức.", "Giáo dục.", "Dự báo."],
     "Sử học có <b>3 nhiệm vụ</b>: nhận thức, giáo dục, dự báo (mẹo “NHÀ GIÁO DẠY”)."),
    ("Một trong những đặc điểm của lịch sử được con người nhận thức là",
     ["có thể chưa đầy đủ, chính xác và thay đổi khi có sử liệu mới.",
      "luôn phản ánh đầy đủ, chính xác hiện thực lịch sử.",
      "tồn tại khách quan, không phụ thuộc vào con người.",
      "chỉ có một cách hiểu, cách trình bày duy nhất."],
     "Lịch sử được nhận thức mang tính <b>chủ quan</b>, có thể <b>chưa đầy đủ</b>, <b>thay đổi</b> khi có sử liệu mới. {1}, {2}, {3} là đặc điểm của hiện thực lịch sử hoặc sai."),
    # ---------------- Bài 2 ----------------
    ("Bước đầu tiên trong quá trình sưu tầm, thu thập sử liệu là",
     ["xác định vấn đề và lập thư mục sử liệu cần sưu tầm.",
      "chọn lọc, phân loại các sử liệu đã thu thập được.",
      "xác minh, đánh giá độ tin cậy của sử liệu.",
      "trình bày kết quả nghiên cứu trước tập thể lớp."],
     "Thứ tự “<b>LẬP – SƯU – LỌC – XÉT</b>”: lập thư mục → sưu tầm → chọn lọc, phân loại → xác minh, đánh giá."),
    ("Sử liệu nào sau đây là <b>sử liệu gốc</b> (sơ cấp)?",
     ["Bản gốc Tuyên ngôn Độc lập do Chủ tịch Hồ Chí Minh soạn thảo năm 1945.",
      "Sách giáo khoa Lịch sử 10 viết về Cách mạng tháng Tám năm 1945.",
      "Bài báo năm 2025 phân tích ý nghĩa của Tuyên ngôn Độc lập.",
      "Bộ phim tài liệu dựng lại sự kiện ngày 2/9/1945."],
     "Sử liệu gốc <b>ra đời cùng thời</b>, gắn trực tiếp với sự kiện. {1}, {2}, {3} được tạo ra sau → sử liệu phái sinh (thứ cấp)."),
    ("Tri thức lịch sử có vai trò nào sau đây?",
     ["Giúp con người hiểu về cội nguồn, bản sắc dân tộc và đúc kết bài học kinh nghiệm.",
      "Giúp con người quyết định toàn bộ sự phát triển của xã hội trong tương lai.",
      "Chỉ có giá trị đối với những người làm công tác nghiên cứu lịch sử.",
      "Giúp con người thay đổi những sự kiện đã diễn ra trong quá khứ."],
     "Tri thức lịch sử giúp hiểu <b>cội nguồn, bản sắc</b>, rút <b>bài học kinh nghiệm</b>. {1}, {2} có từ tuyệt đối (“toàn bộ”, “chỉ”); {3} sai vì hiện thực lịch sử không thể thay đổi."),
    ("Vì sao mỗi người cần học tập, khám phá lịch sử suốt đời?",
     ["Vì tri thức lịch sử rộng lớn, đa dạng và luôn được bổ sung, đổi mới.",
      "Vì kiến thức lịch sử ở trường học đã đầy đủ, chỉ cần ôn lại.",
      "Vì lịch sử chỉ được ghi chép trong sách giáo khoa phổ thông.",
      "Vì hiện thực lịch sử luôn luôn thay đổi theo thời gian."],
     "Lí do cốt lõi: tri thức lịch sử <b>rộng lớn</b>, <b>luôn được bổ sung</b>; kiến thức nhà trường chỉ là cơ bản. {3} sai: hiện thực lịch sử không thay đổi, chỉ nhận thức thay đổi."),
    ("Bản chất của việc kết nối tri thức, bài học lịch sử vào cuộc sống là",
     ["vận dụng hiểu biết về quá khứ để giải thích, giải quyết vấn đề của hiện tại.",
      "ghi nhớ thật nhiều sự kiện, niên đại để đạt điểm cao trong kì thi.",
      "lặp lại nguyên vẹn những việc làm của người xưa trong mọi hoàn cảnh.",
      "tách biệt quá khứ với hiện tại để nghiên cứu một cách khách quan."],
     "Kết nối quá khứ – hiện tại: dùng tri thức, bài học lịch sử để <b>giải thích, giải quyết</b> vấn đề thực tiễn, <b>định hướng</b> tương lai."),
    ("Sau khi thu thập, để bảo đảm độ tin cậy của sử liệu, người học cần",
     ["đối chiếu, xác minh và đánh giá sử liệu.", "sử dụng ngay tất cả thông tin tìm được.",
      "chỉ dùng thông tin trên mạng xã hội.", "loại bỏ toàn bộ sử liệu truyền miệng."],
     "Bước xử lí: <b>phân tích, so sánh, đối chiếu, xác minh</b> để đánh giá độ tin cậy và giá trị của sử liệu."),
    ("Nơi lưu giữ, trưng bày các hiện vật, tư liệu lịch sử, giúp học sinh học tập lịch sử trực quan là",
     ["bảo tàng.", "rạp chiếu phim.", "trung tâm thương mại.", "công viên giải trí."],
     "<b>Bảo tàng</b> là nơi sưu tầm, lưu giữ, trưng bày hiện vật, tư liệu lịch sử – kênh học tập lịch sử hiệu quả."),
    # ---------------- Bài 3 ----------------
    ("Di sản văn hóa vật thể bao gồm",
     ["di tích lịch sử – văn hóa, danh lam thắng cảnh, di vật, cổ vật, bảo vật quốc gia.",
      "tiếng nói, chữ viết, ngữ văn dân gian, lễ hội truyền thống.",
      "nghệ thuật trình diễn dân gian, tập quán xã hội và tín ngưỡng.",
      "nghề thủ công truyền thống và tri thức dân gian."],
     "Di sản vật thể: “<b>TÍCH – THẮNG – VẬT – CỔ – BẢO</b>”. {1}, {2}, {3} là di sản văn hóa <b>phi vật thể</b>."),
    ("Di sản nào sau đây của Việt Nam được UNESCO ghi danh là <b>di sản thiên nhiên thế giới</b>?",
     ["Vịnh Hạ Long.", "Phố cổ Hội An.", "Thành nhà Hồ.", "Hoàng thành Thăng Long."],
     "Vịnh Hạ Long (1994, 2000) là di sản thiên nhiên thế giới. Hội An, Thành nhà Hồ, Hoàng thành Thăng Long là di sản văn hóa."),
    ("Sử học có vai trò như thế nào đối với công tác bảo tồn di sản văn hóa?",
     ["Cung cấp cơ sở khoa học để xác định giá trị và bảo tồn đúng nguyên gốc di sản.",
      "Trực tiếp quyết định việc khai thác di sản phục vụ mục đích kinh tế.",
      "Thay thế hoàn toàn vai trò của cộng đồng trong việc giữ gìn di sản.",
      "Làm mới, hiện đại hóa toàn bộ di sản cho phù hợp với cuộc sống hiện nay."],
     "Sử học nghiên cứu nguồn gốc, niên đại, giá trị → là <b>cơ sở khoa học</b> để bảo tồn, trùng tu <b>đúng nguyên gốc</b>."),
    ("Di sản văn hóa phi vật thể đại diện của nhân loại gắn với vùng đất Nghệ An – Hà Tĩnh được UNESCO ghi danh năm 2014 là",
     ["Dân ca Ví, Giặm Nghệ Tĩnh.", "Dân ca Quan họ Bắc Ninh.", "Nghệ thuật Bài Chòi.", "Nhã nhạc cung đình Huế."],
     "<b>Dân ca Ví, Giặm Nghệ Tĩnh</b> được UNESCO ghi danh tháng 11/2014."),
    ("Di sản thế giới <b>hỗn hợp</b> (văn hóa và thiên nhiên) duy nhất của Việt Nam là",
     ["Quần thể danh thắng Tràng An.", "Vườn quốc gia Phong Nha – Kẻ Bàng.",
      "Quần thể di tích Cố đô Huế.", "Khu đền tháp Mỹ Sơn."],
     "<b>Tràng An</b> (2014) là di sản hỗn hợp duy nhất. Phong Nha – Kẻ Bàng: thiên nhiên; Huế, Mỹ Sơn: văn hóa."),
    ("Các giá trị lịch sử, văn hóa có vai trò quan trọng đối với sự phát triển du lịch vì",
     ["là nguồn tài nguyên tạo nên sản phẩm du lịch đặc sắc, hấp dẫn.",
      "là yếu tố duy nhất quyết định sự phát triển của ngành du lịch.",
      "giúp ngành du lịch không cần đầu tư cơ sở hạ tầng.",
      "chỉ thu hút khách du lịch trong nước, không thu hút khách quốc tế."],
     "Lịch sử – văn hóa là <b>tài nguyên du lịch quan trọng</b>, tạo <b>sản phẩm đặc sắc</b>, quảng bá hình ảnh. {1}, {3} có từ tuyệt đối; {2} vô lí."),
    ("Biểu hiện nào sau đây là tác động <b>tiêu cực</b> của du lịch đối với công tác bảo tồn di tích?",
     ["Lượng khách quá tải khiến di tích bị xuống cấp, môi trường ô nhiễm.",
      "Nguồn thu từ du lịch được đầu tư trở lại cho trùng tu di tích.",
      "Giá trị của di tích được quảng bá rộng rãi trong và ngoài nước.",
      "Ý thức bảo vệ di sản của cộng đồng được nâng cao."],
     "Quá tải, xuống cấp, ô nhiễm là tác động tiêu cực (“3 T tiêu cực”). {1}, {2}, {3} là tác động tích cực."),
]

DE1_TF = [
    dict(
        intro="Đọc đoạn tư liệu sau đây, trong mỗi ý a), b), c), d) thí sinh chọn đúng hoặc sai.",
        source="“Kho tàng tri thức lịch sử của nhân loại vô cùng rộng lớn, trong khi những hiểu biết được học ở nhà trường chỉ là "
               "những kiến thức cơ bản. Mặt khác, tri thức lịch sử luôn được bổ sung khi các nhà khoa học phát hiện thêm nguồn "
               "sử liệu mới. Vì thế, học tập, khám phá lịch sử là nhu cầu suốt đời của mỗi người. Việc học tập lịch sử có thể "
               "diễn ra ở nhiều nơi: qua sách báo, thư viện, bảo tàng, di tích, Internet…”",
        statements=[
            ("Theo đoạn tư liệu, việc học tập lịch sử chỉ có thể diễn ra trong nhà trường.", False),
            ("Tri thức lịch sử rộng lớn và luôn được bổ sung là lí do khiến mỗi người cần học tập lịch sử suốt đời.", True),
            ("Khi thu thập sử liệu, sau bước sưu tầm, thu thập cần tiến hành chọn lọc, phân loại và xác minh sử liệu.", True),
            ("Khi thấy một bài đăng trên mạng xã hội đưa thông tin trái ngược với sách sử về một sự kiện, học sinh nên tin ngay và "
             "chia sẻ vì đó là “phát hiện mới”.", False),
        ],
        explain=[
            "<b>a) Sai</b> – tư liệu nêu rõ học lịch sử “có thể diễn ra ở nhiều nơi” (sách báo, bảo tàng, di tích, Internet…).",
            "<b>b) Đúng</b> – đúng hai lí do được nêu trong tư liệu: tri thức rộng lớn + luôn được bổ sung.",
            "<b>c) Đúng</b> – thứ tự các bước: lập thư mục → sưu tầm → chọn lọc, phân loại → xác minh, đánh giá.",
            "<b>d) Sai</b> – cần <b>đối chiếu, xác minh</b> với nguồn tin cậy trước khi tin và chia sẻ; thông tin trên mạng có thể sai lệch, xuyên tạc.",
        ],
    ),
    dict(
        intro="Đọc đoạn tư liệu sau đây, trong mỗi ý a), b), c), d) thí sinh chọn đúng hoặc sai.",
        source="“Đô thị cổ Hội An được UNESCO ghi danh là Di sản văn hóa thế giới năm 1999. Từ đó, lượng khách du lịch đến Hội An "
               "tăng nhanh, mang lại nguồn thu lớn; một phần nguồn thu được dùng cho việc trùng tu, bảo tồn các ngôi nhà cổ, hội quán, "
               "đình chùa. Tuy nhiên, sự gia tăng nhanh chóng của khách du lịch cũng gây áp lực lớn lên di tích, cảnh quan và môi trường.”",
        statements=[
            ("Đô thị cổ Hội An là di sản văn hóa vật thể.", True),
            ("Theo đoạn tư liệu, du lịch chỉ mang lại tác động tích cực đối với công tác bảo tồn di tích.", False),
            ("Lịch sử – văn hóa là nguồn tài nguyên quan trọng để phát triển du lịch.", True),
            ("Để vừa phát triển du lịch vừa bảo tồn di sản, cần thu hút tối đa lượng khách, xây thêm nhiều công trình hiện đại "
             "ngay trong khu phố cổ.", False),
        ],
        explain=[
            "<b>a) Đúng</b> – Hội An là quần thể di tích (nhà cổ, hội quán, đình chùa) → di sản văn hóa vật thể.",
            "<b>b) Sai</b> – tư liệu nêu cả tác động tiêu cực: “gây áp lực lớn lên di tích, cảnh quan và môi trường”.",
            "<b>c) Đúng</b> – giá trị lịch sử – văn hóa là tài nguyên du lịch nhân văn, tạo sản phẩm du lịch đặc sắc.",
            "<b>d) Sai</b> – cần <b>kiểm soát lượng khách</b>, bảo tồn yếu tố gốc; xây công trình hiện đại trong khu phố cổ làm phá vỡ "
            "cảnh quan, tính xác thực của di sản.",
        ],
    ),
]

DE1_TL = dict(
    question=("<b>a)</b> Kể tên các loại hình di sản văn hóa. Nêu mối quan hệ giữa Sử học với công tác bảo tồn và phát huy giá trị "
              "di sản văn hóa, di sản thiên nhiên. <i>(1,0 điểm)</i><br/>"
              "<b>b)</b> Là học sinh, em hãy đề xuất những biện pháp để bảo tồn và phát huy giá trị của một di sản văn hóa ở địa phương em "
              "(Nghệ An). <i>(2,0 điểm)</i>"),
    rubric=[
        ["a) 1,0 đ", "• Di sản văn hóa <b>vật thể</b>: di tích lịch sử – văn hóa, danh lam thắng cảnh, di vật, cổ vật, bảo vật quốc gia.", "0,25"],
        ["", "• Di sản văn hóa <b>phi vật thể</b>: tiếng nói, chữ viết, ngữ văn dân gian, nghệ thuật trình diễn dân gian, tập quán xã hội, "
             "tín ngưỡng, lễ hội truyền thống, nghề thủ công truyền thống, tri thức dân gian. <i>(Có thể nêu thêm di sản tư liệu theo Luật 2024.)</i>", "0,25"],
        ["", "• Di sản là <b>nguồn sử liệu quan trọng</b> để nghiên cứu, khôi phục và hiểu rõ quá khứ.", "0,25"],
        ["", "• Sử học cung cấp <b>cơ sở khoa học</b> (nguồn gốc, niên đại, giá trị…) để <b>nhận diện, bảo tồn đúng nguyên gốc và phát huy</b> "
             "giá trị di sản (tuyên truyền, quảng bá, gắn với du lịch).", "0,25"],
        ["b) 2,0 đ", "• Giới thiệu đúng di sản lựa chọn. VD: <b>Dân ca Ví, Giặm Nghệ Tĩnh</b> – di sản văn hóa phi vật thể đại diện của nhân loại (2014); "
                     "hoặc <b>Khu di tích Kim Liên</b> – di tích quốc gia đặc biệt.", "0,25"],
        ["", "• <b>Tìm hiểu, học tập</b>: chủ động tìm hiểu giá trị lịch sử, văn hóa của di sản; tham gia học hát Ví, Giặm, CLB dân ca, "
             "hoạt động trải nghiệm tại di tích.", "0,5"],
        ["", "• <b>Hành động bảo vệ</b>: tham quan có văn hóa (không xả rác, viết vẽ bậy, không xâm hại hiện vật, cảnh quan); "
             "tham gia tình nguyện dọn vệ sinh, chăm sóc di tích.", "0,5"],
        ["", "• <b>Tuyên truyền, quảng bá</b>: làm video, poster, bài viết giới thiệu di sản trên mạng xã hội; làm hướng dẫn viên nhí; "
             "vận động gia đình, bạn bè cùng tham gia bảo vệ di sản.", "0,5"],
        ["", "• <b>Kiến nghị</b>: đề xuất nhà trường, địa phương đưa di sản vào hoạt động giáo dục, số hóa tư liệu; phát hiện, "
             "báo cáo, lên án hành vi xâm hại di sản.", "0,25"],
    ],
    model=(
        "Quê hương Nghệ An của em có di sản <b>Dân ca Ví, Giặm Nghệ Tĩnh</b>, được UNESCO ghi danh là Di sản văn hóa phi vật thể đại diện "
        "của nhân loại năm 2014. Đây là tiếng hát tâm hồn, kết tinh đời sống lao động, tình cảm của người dân xứ Nghệ. Để bảo tồn và phát huy "
        "giá trị di sản này, là học sinh, em sẽ: <b>(1)</b> chủ động tìm hiểu nguồn gốc, đặc điểm, giá trị của Ví, Giặm; học hát và tham gia "
        "câu lạc bộ dân ca của trường, biểu diễn trong các dịp văn nghệ; <b>(2)</b> tôn trọng, giữ gìn nguyên vẹn lời ca, làn điệu, "
        "không “biến tấu” làm mất bản sắc; <b>(3)</b> làm video ngắn, bài đăng giới thiệu Ví, Giặm trên mạng xã hội, giới thiệu di sản "
        "với bạn bè, du khách; <b>(4)</b> vận động gia đình, bạn bè tham gia các hội thi, liên hoan dân ca; <b>(5)</b> đề xuất nhà trường "
        "mời nghệ nhân về truyền dạy, đưa Ví, Giặm vào hoạt động ngoại khóa. Bảo tồn di sản là trách nhiệm của mỗi người, "
        "em sẽ góp phần để Ví, Giặm mãi vang trong đời sống hôm nay."
    ),
)

# =====================================================================
# ĐỀ MINH HỌA SỐ 2
# =====================================================================
DE2_KEYS = "CABDDBACBDACDABCBDAC"

DE2_MCQ = [
    # ---------------- Bài 1 ----------------
    ("Lịch sử được con người nhận thức là",
     ["những hiểu biết, tri thức của con người về hiện thực lịch sử.",
      "toàn bộ những gì đã diễn ra trong quá khứ của loài người.",
      "những sự kiện tồn tại khách quan, không phụ thuộc vào con người.",
      "quá trình hình thành và phát triển của tự nhiên."],
     "Lịch sử được nhận thức = <b>hiểu biết, tri thức</b> của con người về quá khứ. {1}, {2} là hiện thực lịch sử."),
    ("Sử học có hai chức năng cơ bản là",
     ["chức năng khoa học và chức năng xã hội.", "chức năng giáo dục và chức năng dự báo.",
      "chức năng kinh tế và chức năng chính trị.", "chức năng nhận thức và chức năng giáo dục."],
     "Mẹo “<b>KHOA – XÃ</b>”. Nhận thức, giáo dục, dự báo là <b>nhiệm vụ</b> (không phải chức năng)."),
    ("Nguyên tắc cơ bản của Sử học là",
     ["khách quan, trung thực, tiến bộ.", "kế thừa, chọn lọc, sáng tạo.",
      "đoàn kết, bình đẳng, tương trợ.", "tự nguyện, công khai, dân chủ."],
     "Mẹo “<b>K – T – T</b>”: Khách quan – Trung thực – Tiến bộ."),
    ("Vì sao cùng một sự kiện lịch sử nhưng các nhà sử học lại có thể có những nhận thức khác nhau?",
     ["Do nguồn sử liệu, quan điểm, mục đích và phương pháp nghiên cứu khác nhau.",
      "Do bản thân sự kiện lịch sử luôn thay đổi theo thời gian.",
      "Do hiện thực lịch sử phụ thuộc vào ý muốn của nhà sử học.",
      "Do mỗi sự kiện lịch sử đều diễn ra nhiều lần khác nhau."],
     "Hiện thực lịch sử là duy nhất, khách quan, không đổi ({1}, {2}, {3} sai). Khác biệt nằm ở <b>người nhận thức</b>: sử liệu, quan điểm, phương pháp."),
    ("Hiện thực lịch sử có đặc điểm nào sau đây?",
     ["Tồn tại khách quan, duy nhất và không thể thay đổi.",
      "Mang tính chủ quan, phụ thuộc vào người ghi chép.",
      "Có thể thay đổi khi phát hiện thêm sử liệu mới.",
      "Được trình bày theo nhiều cách khác nhau."],
     "Hiện thực lịch sử: <b>khách quan – duy nhất – không đổi</b>. {1}, {2}, {3} là đặc điểm của lịch sử được nhận thức."),
    ("Nội dung nào sau đây là <b>hiện thực lịch sử</b>?",
     ["Ngày 2/9/1945, Chủ tịch Hồ Chí Minh đọc Tuyên ngôn Độc lập tại Quảng trường Ba Đình.",
      "Bài giảng của giáo viên về sự kiện Chủ tịch Hồ Chí Minh đọc Tuyên ngôn Độc lập.",
      "Bức tranh vẽ lại cảnh Chủ tịch Hồ Chí Minh đọc Tuyên ngôn Độc lập.",
      "Bài báo viết về ý nghĩa của bản Tuyên ngôn Độc lập năm 1945."],
     "Sự kiện <b>đã diễn ra</b> là hiện thực lịch sử; bài giảng, tranh, bài báo là lịch sử được nhận thức."),
    # ---------------- Bài 2 ----------------
    ("Trống đồng Ngọc Lũ thuộc loại sử liệu nào sau đây?",
     ["Sử liệu hiện vật.", "Sử liệu chữ viết.", "Sử liệu truyền miệng.", "Sử liệu hình ảnh."],
     "Trống đồng là di vật, hiện vật khảo cổ → <b>sử liệu hiện vật</b>."),
    ("Lời kể của nhân chứng về một sự kiện lịch sử thuộc loại sử liệu nào?",
     ["Sử liệu truyền miệng.", "Sử liệu hiện vật.", "Sử liệu chữ viết.", "Sử liệu kiến trúc."],
     "Lời kể, truyền thuyết, ca dao… thuộc <b>sử liệu truyền miệng</b>."),
    ("Câu “Dân ta phải biết sử ta / Cho tường gốc tích nước nhà Việt Nam” là của",
     ["Hồ Chí Minh.", "Lê Văn Hưu.", "Ngô Sĩ Liên.", "Lê Quý Đôn."],
     "Trích tác phẩm “Lịch sử nước ta” (1942) của <b>Hồ Chí Minh</b>."),
    ("Biểu hiện nào sau đây thể hiện việc học tập lịch sử suốt đời?",
     ["Thường xuyên đọc sách, tham quan bảo tàng, di tích để tìm hiểu lịch sử.",
      "Chỉ học lịch sử khi chuẩn bị cho các kì kiểm tra, thi cử.",
      "Học thuộc lòng nội dung sách giáo khoa và không tìm hiểu thêm.",
      "Ngừng tìm hiểu lịch sử sau khi tốt nghiệp trung học phổ thông."],
     "Học suốt đời là học <b>thường xuyên, chủ động</b>, qua <b>nhiều kênh</b>, không giới hạn ở trường học hay thi cử."),
    ("Vì sao cần phải xác minh, đối chiếu sử liệu trước khi sử dụng?",
     ["Vì sử liệu có thể chưa đầy đủ, sai lệch hoặc mang tính chủ quan.",
      "Vì mọi sử liệu đều đã chính xác tuyệt đối.",
      "Vì sử liệu gốc luôn kém tin cậy hơn sử liệu phái sinh.",
      "Vì quy định chỉ được sử dụng sử liệu hình ảnh."],
     "Xác minh để bảo đảm thông tin <b>chính xác, khách quan</b>; sử liệu có thể sai lệch, chủ quan, bị xuyên tạc."),
    ("Để tìm kiếm sử liệu phục vụ học tập lịch sử, học sinh có thể đến",
     ["thư viện, bảo tàng, trung tâm lưu trữ, di tích.", "siêu thị, chợ, cửa hàng.",
      "sân vận động, nhà thi đấu.", "bến xe, nhà ga, sân bay."],
     "Nơi lưu giữ sử liệu: <b>thư viện, bảo tàng, lưu trữ, di tích</b>, nhân chứng, Internet chính thống."),
    ("Bài học lịch sử nào được vận dụng trong công cuộc bảo vệ chủ quyền biển, đảo Việt Nam hiện nay?",
     ["Phát huy sức mạnh khối đại đoàn kết toàn dân tộc.", "Đóng cửa, không quan hệ với các nước.",
      "Dựa hoàn toàn vào sự giúp đỡ của bên ngoài.", "Chỉ sử dụng biện pháp quân sự."],
     "Bài học <b>đại đoàn kết dân tộc</b>, kết hợp sức mạnh dân tộc với thời đại; {1}, {2}, {3} trái với truyền thống và có từ tuyệt đối."),
    # ---------------- Bài 3 ----------------
    ("Di sản văn hóa nào sau đây là di sản văn hóa <b>phi vật thể</b>?",
     ["Nhã nhạc cung đình Huế.", "Hoàng thành Thăng Long.", "Thành nhà Hồ.", "Trống đồng Ngọc Lũ."],
     "Nhã nhạc (UNESCO 2003) là nghệ thuật trình diễn → <b>phi vật thể</b>. Các phương án còn lại là di sản vật thể."),
    ("Thành nhà Hồ (Thanh Hóa) được UNESCO ghi danh là",
     ["Di sản văn hóa thế giới.", "Di sản thiên nhiên thế giới.",
      "Di sản hỗn hợp thế giới.", "Di sản phi vật thể đại diện của nhân loại."],
     "Thành nhà Hồ là <b>Di sản văn hóa thế giới</b> (2011)."),
    ("Vì sao công tác bảo tồn di sản cần có sự tham gia của Sử học?",
     ["Vì Sử học giúp làm rõ nguồn gốc, niên đại, giá trị để bảo tồn đúng nguyên gốc.",
      "Vì Sử học có thể thay thế các ngành khoa học khác trong bảo tồn.",
      "Vì chỉ có nhà sử học mới được phép tham quan di sản.",
      "Vì Sử học giúp hiện đại hóa toàn bộ di sản."],
     "Sử học cung cấp <b>cơ sở khoa học</b> (nguồn gốc, niên đại, giá trị) → bảo tồn, trùng tu đúng nguyên gốc, giữ tính xác thực."),
    ("Khu di tích Kim Liên (Nghệ An) gắn với cuộc đời thời niên thiếu của",
     ["Chủ tịch Hồ Chí Minh.", "Phan Bội Châu.", "Lê Hồng Phong.", "Nguyễn Du."],
     "Kim Liên là <b>quê hương Chủ tịch Hồ Chí Minh</b>, gồm cụm di tích Hoàng Trù (quê ngoại) và làng Sen (quê nội)."),
    ("Loại hình nào sau đây <b>không</b> thuộc di sản văn hóa vật thể?",
     ["Lễ hội truyền thống.", "Di tích lịch sử – văn hóa.", "Danh lam thắng cảnh.", "Bảo vật quốc gia."],
     "Lễ hội truyền thống thuộc di sản <b>phi vật thể</b>."),
    ("Sử học có vai trò như thế nào đối với sự phát triển du lịch?",
     ["Cung cấp tri thức lịch sử – văn hóa chính xác để xây dựng sản phẩm, nội dung thuyết minh du lịch.",
      "Quyết định toàn bộ giá vé và doanh thu của các điểm du lịch.",
      "Thay thế công việc của các hướng dẫn viên du lịch.",
      "Làm cho mọi di tích đều trở thành khu vui chơi giải trí."],
     "Sử học cung cấp <b>thông tin, tri thức chính xác</b> → xây dựng sản phẩm du lịch, thuyết minh, quảng bá."),
    ("Ý nào sau đây thể hiện tác động <b>tích cực</b> của du lịch đối với công tác bảo tồn di tích?",
     ["Tạo nguồn thu để tái đầu tư cho bảo tồn, trùng tu di tích.",
      "Gây quá tải, làm di tích xuống cấp nhanh chóng.",
      "Thương mại hóa làm biến dạng giá trị của di sản.",
      "Gây ô nhiễm môi trường tại khu di tích."],
     "“3 T tích cực”: <b>Tiền</b> (nguồn thu) – Tiếng (quảng bá) – Thức (ý thức). {1}, {2}, {3} là tác động tiêu cực."),
]

DE2_TF = [
    dict(
        intro="Đọc đoạn tư liệu sau đây, trong mỗi ý a), b), c), d) thí sinh chọn đúng hoặc sai.",
        source="“Để thực hiện dự án tìm hiểu về phong trào Xô viết Nghệ Tĩnh (1930 – 1931), nhóm học sinh lớp 10A đã lập danh mục "
               "các tài liệu cần tìm; đến Bảo tàng Xô viết Nghệ Tĩnh để chụp ảnh hiện vật, đọc các văn bản lưu trữ; phỏng vấn "
               "các cụ cao tuổi trong làng về những câu chuyện được truyền lại. Sau đó, nhóm phân loại, đối chiếu các nguồn tư liệu "
               "trước khi viết báo cáo.”",
        statements=[
            ("Việc lập danh mục tài liệu cần tìm là bước đầu tiên trong quá trình sưu tầm sử liệu của nhóm.", True),
            ("Những câu chuyện do các cụ cao tuổi kể lại thuộc loại sử liệu hiện vật.", False),
            ("Bảo tàng là một trong những nơi lưu giữ sử liệu phục vụ học tập, khám phá lịch sử.", True),
            ("Nếu các nguồn tư liệu có thông tin mâu thuẫn, nhóm nên chọn thông tin hấp dẫn nhất để báo cáo mà không cần đối chiếu.", False),
        ],
        explain=[
            "<b>a) Đúng</b> – bước 1 “Lập thư mục sử liệu” (LẬP – SƯU – LỌC – XÉT).",
            "<b>b) Sai</b> – lời kể là <b>sử liệu truyền miệng</b>, không phải hiện vật.",
            "<b>c) Đúng</b> – bảo tàng lưu giữ, trưng bày hiện vật, tư liệu lịch sử.",
            "<b>d) Sai</b> – phải <b>đối chiếu, xác minh</b>, chọn thông tin có độ tin cậy cao nhất, bảo đảm nguyên tắc khách quan, trung thực.",
        ],
    ),
    dict(
        intro="Đọc đoạn tư liệu sau đây, trong mỗi ý a), b), c), d) thí sinh chọn đúng hoặc sai.",
        source="“Năm 2014, Quần thể danh thắng Tràng An (Ninh Bình) được UNESCO ghi danh là Di sản văn hóa và thiên nhiên thế giới. "
               "Nơi đây không chỉ có cảnh quan núi đá vôi, hang động kì vĩ mà còn có nhiều dấu tích khảo cổ về con người thời tiền sử và "
               "các di tích gắn với kinh đô Hoa Lư thế kỉ X. Hằng năm, Tràng An thu hút hàng triệu lượt khách du lịch.”",
        statements=[
            ("Quần thể danh thắng Tràng An là di sản thế giới hỗn hợp.", True),
            ("Sử học không có vai trò gì đối với Tràng An vì đây là một danh thắng thiên nhiên.", False),
            ("Các dấu tích khảo cổ ở Tràng An là nguồn sử liệu quan trọng để nghiên cứu lịch sử.", True),
            ("Để phát huy giá trị Tràng An bền vững, cần kiểm soát lượng khách, bảo vệ môi trường và để cộng đồng tham gia bảo tồn.", True),
        ],
        explain=[
            "<b>a) Đúng</b> – được ghi danh với cả tiêu chí văn hóa và thiên nhiên → di sản hỗn hợp (duy nhất ở Việt Nam).",
            "<b>b) Sai</b> – Tràng An có giá trị lịch sử – văn hóa (khảo cổ tiền sử, kinh đô Hoa Lư); Sử học giúp xác định, bảo tồn, phát huy các giá trị đó.",
            "<b>c) Đúng</b> – di sản là <b>nguồn sử liệu</b> quan trọng (quan hệ hai chiều Sử học – di sản).",
            "<b>d) Đúng</b> – đây là các biện pháp phát triển du lịch bền vững, hài hòa giữa khai thác và bảo tồn.",
        ],
    ),
]

DE2_TL = dict(
    question=("<b>a)</b> Nêu vai trò của lịch sử – văn hóa đối với sự phát triển du lịch. <i>(1,0 điểm)</i><br/>"
              "<b>b)</b> Du lịch có tác động như thế nào đến công tác bảo tồn di tích lịch sử, văn hóa? Em hãy đề xuất một số việc làm "
              "để vận động mọi người xung quanh cùng tham gia bảo vệ di sản. <i>(2,0 điểm)</i>"),
    rubric=[
        ["a) 1,0 đ", "• Lịch sử – văn hóa là <b>nguồn tài nguyên du lịch quan trọng</b> (tài nguyên nhân văn), cơ sở hình thành du lịch văn hóa, lịch sử, tâm linh, lễ hội.", "0,5"],
        ["", "• Tạo nên <b>sản phẩm du lịch đặc sắc, hấp dẫn</b>, mang bản sắc riêng; <b>quảng bá hình ảnh</b> đất nước, con người; thúc đẩy kinh tế.", "0,5"],
        ["b) 2,0 đ", "• <b>Tích cực</b>: tạo nguồn thu tái đầu tư bảo tồn; quảng bá giá trị di sản; nâng cao ý thức cộng đồng; tạo việc làm, sinh kế.", "0,5"],
        ["", "• <b>Tiêu cực</b>: quá tải làm di tích xuống cấp; ô nhiễm môi trường; thương mại hóa làm biến dạng giá trị; xây dựng sai lệch.", "0,5"],
        ["", "• <b>Việc làm vận động</b>: chia sẻ thông tin, video về giá trị di sản trên mạng xã hội; nhắc nhở người thân, bạn bè ứng xử văn minh "
             "khi tham quan; tổ chức/tham gia buổi ngoại khóa, cuộc thi tìm hiểu di sản.", "0,5"],
        ["", "• Tham gia tình nguyện bảo vệ, làm sạch di tích; làm hướng dẫn viên nhí; phản ánh hành vi xâm hại tới cơ quan chức năng; "
             "bản thân gương mẫu thực hiện.", "0,5"],
    ],
    model=None,
)
