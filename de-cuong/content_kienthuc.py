"""Phần I–II: Cấu trúc đề & Kiến thức trọng tâm (Bài 1, 2, 3 – KNTT)."""
from reportlab.platypus import PageBreak, Spacer

from layout import (
    AMBER, BLUE, CREAM, GREEN, LILAC, MINT, NAVY, PURPLE, RED, ROSE, SKY,
    H1, H2, H3, P, box, bullets, numbered, table,
)


# =====================================================================
# PHẦN I. GIẢI MÃ MA TRẬN ĐỀ
# =====================================================================
def phan_ma_tran():
    f = []
    f += H1("PHẦN I. GIẢI MÃ MA TRẬN – BIẾT ĐỀ THI HỎI GÌ, HỌC ĐÚNG TRỌNG TÂM",
            sub="Phân tích từ tệp LS10- MTGK1-26-27-HHT.docx (Ma trận + Bảng đặc tả đề kiểm tra giữa HKI)")

    f += box("Lưu ý quan trọng về tệp nguồn", [
        P("Tệp <b>LS10- MTGK1-26-27-HHT.docx</b> gồm 2 bảng: <b>Ma trận đề</b> và <b>Bảng đặc tả</b>. "
          "Tệp quy định <b>cấu trúc, phạm vi, cấp độ tư duy</b> và <b>vị trí từng câu hỏi</b>, nhưng "
          "<b>không chứa nội dung câu hỏi hay đáp án cụ thể</b>. Vì vậy đề cương này:"),
        *bullets([
            "Trình bày đầy đủ <b>mọi yêu cầu cần đạt</b> trong Bảng đặc tả, kèm kiến thức để đáp ứng từng yêu cầu.",
            "Biên soạn <b>2 đề minh họa hoàn chỉnh bám sát 100% ma trận</b> (đúng số câu, đúng vị trí "
            "I.1–I.20, II.1a–d, II.2a–d, câu tự luận; đúng bài và cấp độ), <b>có đáp án và giải thích chi tiết</b>.",
            "Bổ sung <b>ngân hàng 30 câu</b> theo từng bài và <b>40 câu hỏi – đáp nhanh</b> để luyện trí nhớ.",
        ]),
    ], color=RED, bg=ROSE, icon="⚠")

    f += H2("1. Thông tin chung về bài kiểm tra")
    f += table([
        ["Mục", "Nội dung"],
        ["Môn / Khối", "Lịch sử 10 – bộ sách <b>Kết nối tri thức với cuộc sống</b>"],
        ["Năm học / Kì", "2026 – 2027 / Kiểm tra định kì <b>giữa học kì I</b>"],
        ["Thời gian", "<b>45 phút</b>"],
        ["Hình thức", "<b>20</b> câu trắc nghiệm nhiều lựa chọn + <b>2</b> câu trắc nghiệm Đúng/Sai (mỗi câu 4 ý a, b, c, d) "
                      "+ <b>1</b> câu tự luận → tổng <b>28 lệnh hỏi trắc nghiệm + 1 tự luận</b>"],
        ["Phạm vi", "Chủ đề 1 – Lịch sử và Sử học (<b>Bài 1, Bài 2</b>); Chủ đề 2 – Vai trò của Sử học (<b>Bài 3</b>)"],
    ], [1.2, 4.2], bold_first_col=True)

    f += H2("2. Cách tính điểm (suy ra từ ma trận)")
    f += table([
        ["Phần", "Số lệnh hỏi", "Điểm mỗi lệnh", "Tổng điểm"],
        ["I. Trắc nghiệm nhiều lựa chọn", "20 câu", "0,25", "<b>5,0</b>"],
        ["II. Trắc nghiệm Đúng/Sai", "2 câu × 4 ý = 8 ý", "0,25", "<b>2,0</b>"],
        ["III. Tự luận", "1 câu (½ Biết + ½ Vận dụng)", "1,0 + 2,0", "<b>3,0</b>"],
        ["<b>Tổng</b>", "28 lệnh TN + 1 TL", "", "<b>10,0</b>"],
    ], [2.4, 2, 1.2, 1], center_cols=(1, 2, 3))

    f += H2("3. Mỗi bài “nặng” bao nhiêu điểm? → Ưu tiên ôn tập")
    f += table([
        ["Bài", "Vị trí câu hỏi trong đề", "Điểm", "Tỉ lệ", "Mức ưu tiên"],
        ["Bài 1. Hiện thực lịch sử và lịch sử được con người nhận thức",
         "I.1 → I.6", "1,5", "15%", "★★☆"],
        ["Bài 2. Tri thức lịch sử và cuộc sống",
         "I.7 → I.13; II.1 (a, b, c, d)", "2,75", "27,5%", "★★☆"],
        ["Bài 3. Vai trò của Sử học",
         "I.14 → I.20; II.2 (a, b, c, d); <b>toàn bộ câu tự luận</b>", "<b>5,75</b>", "<b>57,5%</b>", "<b>★★★</b>"],
    ], [3.2, 2.6, 0.7, 0.7, 0.9], center_cols=(2, 3, 4))
    f += box("Chiến lược", [
        *bullets([
            "<b>Bài 3 chiếm hơn một nửa số điểm</b> và có cả câu tự luận 3 điểm → học kĩ nhất: các loại hình di sản, "
            "vai trò của Sử học với bảo tồn di sản, vai trò lịch sử – văn hóa với du lịch, tác động của du lịch, "
            "<b>biện pháp bảo tồn (phần vận dụng 2 điểm)</b>.",
            "Bài 1 và Bài 2 chủ yếu ở mức <b>Biết – Hiểu</b>: học thuộc khái niệm, đối tượng, chức năng, nhiệm vụ, "
            "các bước thu thập – xử lí sử liệu, lí do học lịch sử suốt đời.",
            "Mức <b>Biết chiếm 50%</b> số điểm (5,0 đ), <b>Hiểu 25%</b> (2,5 đ), <b>Vận dụng 25%</b> (2,5 đ) "
            "→ thuộc bài chắc chắn đã đạt nửa số điểm.",
        ]),
    ], color=GREEN, bg=MINT, icon="◉")

    f += H2("4. Phân bố câu hỏi theo năng lực và cấp độ tư duy")
    f += table([
        ["Năng lực", "Biết", "Hiểu", "Vận dụng"],
        ["NL1: Tìm hiểu lịch sử", "8 lệnh + ½ TL = 3,0 đ", "4 lệnh = 1,0 đ", "0"],
        ["NL2: Nhận thức và tư duy lịch sử", "6 lệnh = 1,5 đ", "6 lệnh = 1,5 đ", "0"],
        ["NL3: Vận dụng kiến thức, kĩ năng", "2 lệnh = 0,5 đ", "0", "2 lệnh + ½ TL = 2,5 đ"],
        ["<b>Cộng</b>", "<b>5,0 đ (50%)</b>", "<b>2,5 đ (25%)</b>", "<b>2,5 đ (25%)</b>"],
    ], [2.6, 1.8, 1.4, 1.8], center_cols=(1, 2, 3))

    f += H2("5. Bảng đặc tả → Danh sách “phải làm được” (tự đánh dấu khi đã thuộc)")
    rows = [["Bài", "Mức độ", "Yêu cầu cần đạt (trích Bảng đặc tả)", "Xem mục"]]
    rows += [
        ["Bài 1", "Biết", "☐ Trình bày được khái niệm <b>lịch sử, sử học</b>.<br/>"
                          "☐ Nêu được <b>đối tượng, chức năng, nhiệm vụ</b> của Sử học.<br/>"
                          "☐ Nhận diện được <b>hiện thực lịch sử</b> và <b>lịch sử được con người nhận thức</b> qua sự kiện cụ thể.<br/>"
                          "☐ Chỉ ra được <b>đặc điểm</b> của lịch sử được con người nhận thức.", "II.A"],
        ["Bài 1", "Hiểu", "☐ Giải thích được khái niệm sử học.<br/>"
                          "☐ Phân biệt được hiện thực lịch sử và lịch sử được con người nhận thức qua tình huống cụ thể.", "II.A"],
        ["Bài 2", "Biết", "☐ Nêu được <b>các bước</b> thu thập, xử lí thông tin và sử liệu.<br/>"
                          "☐ Biết cách sưu tầm, thu thập, xử lí thông tin, sử liệu để học tập, khám phá lịch sử.", "II.B"],
        ["Bài 2", "Hiểu", "☐ Giải thích được <b>sự cần thiết phải học tập và khám phá lịch sử suốt đời</b>.<br/>"
                          "☐ Hiểu bản chất của việc <b>kết nối tri thức, bài học lịch sử vào cuộc sống</b>.", "II.B"],
        ["Bài 2", "Vận dụng", "☐ Vận dụng kiến thức, bài học lịch sử để giải thích vấn đề thời sự trong nước và thế giới, "
                              "vấn đề thực tiễn (mức đơn giản).<br/>"
                              "☐ Quan tâm, yêu thích, tham gia hoạt động tìm hiểu lịch sử, văn hóa Việt Nam và thế giới.", "II.B"],
        ["Bài 3", "Biết", "☐ Nêu được <b>mối quan hệ giữa Sử học với bảo tồn, phát huy</b> giá trị di sản văn hóa, di sản thiên nhiên.<br/>"
                          "☐ Kể tên được một số <b>địa danh là tài nguyên du lịch</b> của nước ta.<br/>"
                          "☐ Kể tên được <b>các loại hình di sản văn hóa</b>.", "II.C"],
        ["Bài 3", "Hiểu", "☐ Hiểu rõ <b>vai trò của Sử học</b> với bảo tồn và phát huy giá trị di sản.<br/>"
                          "☐ Giải thích <b>vai trò của lịch sử – văn hóa đối với du lịch</b> qua tình huống cụ thể.<br/>"
                          "☐ Phân tích <b>tác động của du lịch</b> đối với bảo tồn di tích lịch sử, văn hóa.", "II.C"],
        ["Bài 3", "Vận dụng", "☐ <b>Đề xuất biện pháp</b> bảo tồn, phát huy giá trị của di sản.<br/>"
                              "☐ Có ý thức <b>vận động mọi người</b> cùng bảo vệ di sản văn hóa, di sản thiên nhiên.", "II.C"],
    ]
    f += table(rows, [0.7, 0.85, 5.2, 0.6], center_cols=(0, 1, 3), valign="TOP")
    return f


# =====================================================================
# PHẦN II. KIẾN THỨC TRỌNG TÂM
# =====================================================================
def bai_1():
    f = []
    f += H1("PHẦN II. KIẾN THỨC TRỌNG TÂM", color=BLUE)
    f += H1("A. BÀI 1 – HIỆN THỰC LỊCH SỬ VÀ LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC",
            sub="Chủ đề 1: Lịch sử và Sử học • Đề thi: câu I.1 → I.6 (1,5 điểm)")

    f += H2("1. Lịch sử là gì?")
    f += bullets([
        "<b>Lịch sử</b> là <b>tất cả những gì đã diễn ra trong quá khứ</b> của xã hội loài người, từ khi con người "
        "xuất hiện đến nay (theo nghĩa rộng: quá khứ của mọi sự vật, hiện tượng như lịch sử Trái Đất, lịch sử một ngôi trường…).",
        "Thuật ngữ “lịch sử” được hiểu theo <b>3 nghĩa</b>:",
    ])
    f += table([
        ["Nghĩa", "Nội dung", "Ví dụ"],
        ["① Hiện thực lịch sử", "Những gì đã thực sự diễn ra trong quá khứ", "Trận Bạch Đằng năm 938 do Ngô Quyền chỉ huy"],
        ["② Lịch sử được con người nhận thức",
         "Hiểu biết, tri thức của con người về quá khứ, được trình bày theo những cách khác nhau",
         "Đoạn chép về trận Bạch Đằng trong <i>Đại Việt sử kí toàn thư</i>; bài giảng; bộ phim lịch sử"],
        ["③ Sử học (khoa học lịch sử)", "Ngành khoa học nghiên cứu về quá khứ của loài người",
         "Công trình nghiên cứu của các nhà sử học về thời Ngô"],
    ], [1.5, 2.6, 2.6], bold_first_col=True)

    f += H2("2. Hiện thực lịch sử và lịch sử được con người nhận thức")
    f += box("Định nghĩa phải thuộc nguyên văn", [
        P("<b>Hiện thực lịch sử</b> là <b>toàn bộ những gì đã diễn ra trong quá khứ</b>, tồn tại <b>khách quan</b>, "
          "<b>độc lập với ý muốn chủ quan</b> của con người."),
        P("<b>Lịch sử được con người nhận thức</b> là <b>những hiểu biết, tri thức của con người về hiện thực lịch sử</b>, "
          "được trình bày, tái hiện theo nhiều cách khác nhau (lời kể, chữ viết, tranh ảnh, phim, sách…)."),
    ], color=RED, bg=ROSE, icon="✎")
    f += H3("So sánh để phân biệt (dạng câu hỏi “Hiểu” rất hay ra)")
    f += table([
        ["Tiêu chí", "Hiện thực lịch sử", "Lịch sử được con người nhận thức"],
        ["Bản chất", "Cái <b>đã xảy ra</b> trong quá khứ", "Cái con người <b>biết, hiểu, kể lại</b> về quá khứ"],
        ["Tính chất", "<b>Khách quan</b>, độc lập với ý muốn con người", "Mang dấu ấn <b>chủ quan</b> của người nhận thức"],
        ["Số lượng", "<b>Duy nhất</b>, chỉ diễn ra <b>một lần</b>", "<b>Nhiều</b> cách hiểu, cách trình bày khác nhau"],
        ["Khả năng thay đổi", "<b>Không thể thay đổi</b>", "<b>Có thể thay đổi</b>, bổ sung khi có sử liệu, phương pháp mới"],
        ["Mức độ phản ánh", "—", "Có thể <b>chưa đầy đủ, chưa chính xác</b> so với hiện thực"],
        ["Ví dụ", "Ngày 2/9/1945, Chủ tịch Hồ Chí Minh đọc Tuyên ngôn Độc lập tại Quảng trường Ba Đình",
         "Bài viết, phim tài liệu, bức ảnh, bài giảng về sự kiện ngày 2/9/1945"],
    ], [1.3, 2.5, 2.7], bold_first_col=True)

    f += H3("Mối quan hệ giữa hai khái niệm")
    f += bullets([
        "Hiện thực lịch sử là <b>đối tượng, cơ sở</b> của nhận thức lịch sử; có hiện thực lịch sử mới có nhận thức về nó.",
        "Lịch sử được nhận thức <b>luôn cố gắng phản ánh đúng</b> hiện thực lịch sử. Càng có nhiều sử liệu tin cậy, phương pháp "
        "khoa học thì nhận thức càng <b>tiệm cận</b> hiện thực.",
    ])
    f += H3("Đặc điểm của lịch sử được con người nhận thức")
    f += bullets([
        "<b>Đa dạng</b> về hình thức trình bày: truyền miệng, chữ viết, hình ảnh, phim, sách báo, bảo tàng số…",
        "<b>Mang tính chủ quan</b>: phụ thuộc vào quan điểm, mục đích, trình độ, phương pháp của người nhận thức.",
        "<b>Có thể khác nhau</b> giữa các cá nhân, các thời kì; <b>không phải lúc nào cũng đầy đủ, chính xác</b>.",
        "<b>Luôn được bổ sung, điều chỉnh</b> khi phát hiện sử liệu mới, có cách tiếp cận mới.",
    ])
    f += box("Vì sao cùng một sự kiện lại có những nhận thức khác nhau?", [
        *bullets([
            "<b>Nguồn sử liệu</b> mỗi người tiếp cận khác nhau (nhiều/ít, đầy đủ/thiếu, tin cậy/không).",
            "<b>Quan điểm, lập trường, mục đích</b> nghiên cứu khác nhau.",
            "<b>Trình độ, phương pháp</b> nghiên cứu và <b>bối cảnh thời đại</b> khác nhau.",
        ]),
        P("→ Vì vậy nhận thức lịch sử cần dựa trên sử liệu đáng tin cậy và tuân thủ nguyên tắc <b>khách quan, trung thực</b>."),
    ], color=AMBER, bg=CREAM, icon="✦")

    f += H2("3. Sử học")
    f += box("Khái niệm Sử học", [
        P("<b>Sử học là khoa học nghiên cứu về quá khứ của con người và xã hội loài người.</b>"),
        P("<i>Giải thích (mức Hiểu):</i> Sử học là một <b>khoa học</b> vì có <b>đối tượng nghiên cứu</b> riêng, "
          "có <b>nguyên tắc</b> và <b>phương pháp</b> khoa học, dựa trên <b>sử liệu</b> được kiểm chứng để khôi phục "
          "quá khứ một cách khách quan, chính xác và rút ra quy luật, bài học."),
    ], color=RED, bg=ROSE, icon="✎")

    f += H3("a) Đối tượng nghiên cứu")
    f += bullets([
        "Là <b>quá khứ của con người và xã hội loài người</b> – toàn bộ hoạt động của con người trên <b>mọi lĩnh vực</b>: "
        "chính trị, kinh tế, văn hóa, xã hội, quân sự, ngoại giao, tư tưởng…",
        ("Có thể nghiên cứu theo nhiều phạm vi:", [
            "<b>Không gian</b>: lịch sử thế giới, khu vực, quốc gia, địa phương.",
            "<b>Thời gian</b>: cổ đại, trung đại, cận đại, hiện đại.",
            "<b>Lĩnh vực</b>: lịch sử chính trị, kinh tế, văn hóa, quân sự…; <b>nhân vật, sự kiện</b> cụ thể.",
        ]),
    ])
    f += H3("b) Chức năng (2 chức năng)")
    f += table([
        ["Chức năng", "Nội dung"],
        ["Chức năng khoa học", "<b>Khôi phục lại hiện thực lịch sử</b> một cách <b>chính xác, khách quan</b>; tìm hiểu bản chất, "
                               "<b>rút ra quy luật</b> vận động, phát triển của lịch sử."],
        ["Chức năng xã hội", "<b>Phục vụ cuộc sống</b>: cung cấp tri thức, giáo dục, nêu gương, rút ra bài học kinh nghiệm, "
                             "góp phần dự báo tương lai."],
    ], [1.4, 5], bold_first_col=True)
    f += H3("c) Nhiệm vụ (3 nhiệm vụ)")
    f += table([
        ["Nhiệm vụ", "Nội dung"],
        ["Nhận thức", "Cung cấp tri thức khoa học về quá khứ; khôi phục, mô tả, giải thích các sự kiện, quá trình lịch sử."],
        ["Giáo dục", "Giáo dục tư tưởng, tình cảm, đạo đức, lòng yêu nước, tinh thần dân tộc, tinh thần quốc tế, tính nhân văn; "
                     "nêu gương những tấm gương tiêu biểu."],
        ["Dự báo", "Từ quy luật và bài học của quá khứ, <b>dự báo xu hướng phát triển</b> trong tương lai."],
    ], [1.4, 5], bold_first_col=True)
    f += H3("d) Nguyên tắc cơ bản – Nguồn sử liệu – Phương pháp")
    f += bullets([
        "<b>Nguyên tắc cơ bản</b>: <b>khách quan</b> (phản ánh đúng hiện thực, không áp đặt ý chủ quan), "
        "<b>trung thực</b> (không bóp méo, xuyên tạc, tô hồng), <b>tiến bộ</b> (vì sự tiến bộ của con người và xã hội).",
        ("<b>Nguồn sử liệu theo dạng thức</b>:", [
            "<b>Chữ viết</b>: sách sử, văn bia, gia phả, văn bản hành chính, báo chí, nhật kí…",
            "<b>Hiện vật</b>: công cụ, trống đồng, đồ gốm, di chỉ khảo cổ, công trình kiến trúc…",
            "<b>Truyền miệng</b>: truyền thuyết, thần thoại, ca dao, tục ngữ, lời kể của nhân chứng…",
            "<b>Hình ảnh, âm thanh</b>: tranh, ảnh, phim, băng ghi âm, ghi hình…",
        ]),
        ("<b>Nguồn sử liệu theo nguồn gốc</b>:", [
            "<b>Sử liệu gốc (sơ cấp)</b>: ra đời cùng thời, gắn trực tiếp với sự kiện → <b>độ tin cậy cao</b> "
            "(VD: bản Tuyên ngôn Độc lập 1945, hiện vật khai quật).",
            "<b>Sử liệu phái sinh (thứ cấp)</b>: được tạo ra sau, dựa trên sử liệu gốc (VD: sách giáo khoa, sách nghiên cứu, bài báo).",
        ]),
        "<b>Phương pháp cơ bản</b>: <b>phương pháp lịch sử</b> (tái hiện quá trình theo trình tự thời gian, cụ thể, sinh động) "
        "và <b>phương pháp logic</b> (khái quát bản chất, quy luật); ngoài ra là phương pháp <b>liên ngành</b>.",
    ])
    f += box("Mẹo nhớ Bài 1", [
        *bullets([
            "<b>2 chức năng</b>: “<b>KHOA – XÃ</b>” (Khoa học – Xã hội).",
            "<b>3 nhiệm vụ</b>: “<b>NHÀ GIÁO DẠY</b>” → <b>Nh</b>ận thức – <b>Giáo</b> dục – <b>D</b>ự báo.",
            "<b>3 nguyên tắc</b>: “<b>K – T – T</b>” giống tên sách <b>K</b>ết nối <b>T</b>ri <b>T</b>hức → <b>K</b>hách quan – "
            "<b>T</b>rung thực – <b>T</b>iến bộ.",
            "<b>4 dạng sử liệu</b>: “<b>CHỮ – VẬT – MIỆNG – HÌNH</b>”.",
            "Phân biệt nhanh: <b>“xảy ra”</b> → hiện thực lịch sử; <b>“ghi chép, kể, viết, phim, bài giảng, đánh giá”</b> → lịch sử được nhận thức.",
        ]),
    ], color=PURPLE, bg=LILAC, icon="❖")
    return f


def bai_2():
    f = []
    f += H1("B. BÀI 2 – TRI THỨC LỊCH SỬ VÀ CUỘC SỐNG",
            sub="Chủ đề 1: Lịch sử và Sử học • Đề thi: câu I.7 → I.13 và câu II.1 (a–d) – 2,75 điểm")

    f += H2("1. Vai trò của tri thức lịch sử")
    f += bullets([
        "Giúp con người hiểu biết về <b>cội nguồn</b>, quá khứ của bản thân, gia đình, quê hương, dân tộc và nhân loại; "
        "hiểu <b>bản sắc văn hóa</b> dân tộc → bồi đắp lòng tự hào, ý thức trách nhiệm.",
        "<b>Đúc kết bài học kinh nghiệm</b> từ quá khứ cho hiện tại và tương lai (“ôn cố tri tân” – ôn cũ biết mới).",
        "Giúp <b>giải thích</b> các vấn đề, hiện tượng của hiện tại và <b>định hướng</b> tương lai.",
        "Góp phần hình thành <b>phẩm chất, năng lực</b>; hỗ trợ định hướng nghề nghiệp.",
    ])
    f += box("Câu nói cần nhớ", [
        P("“<b>Dân ta phải biết sử ta / Cho tường gốc tích nước nhà Việt Nam.</b>” – <i>Hồ Chí Minh, “Lịch sử nước ta” (1942)</i>."),
    ], color=BLUE, bg=SKY, icon="❝")

    f += H2("2. Sự cần thiết phải học tập, khám phá lịch sử suốt đời (mức Hiểu)")
    f += table([
        ["Lí do", "Giải thích"],
        ["① Tri thức lịch sử rộng lớn, đa dạng", "Kho tàng lịch sử loài người vô cùng phong phú; kiến thức ở nhà trường chỉ là "
                                                 "<b>cơ bản, phổ thông</b>, có giới hạn."],
        ["② Tri thức lịch sử luôn được bổ sung, đổi mới", "Liên tục có <b>phát hiện khảo cổ, tư liệu mới</b>, cách tiếp cận mới "
                                                          "→ nhận thức lịch sử thay đổi, cần cập nhật."],
        ["③ Đáp ứng nhu cầu hiểu biết, hoàn thiện bản thân", "Học lịch sử giúp mở rộng hiểu biết, nâng cao văn hóa, "
                                                            "hình thành nhân cách."],
        ["④ Phục vụ cuộc sống, nghề nghiệp", "Tri thức lịch sử cần cho nhiều nghề: du lịch, báo chí, ngoại giao, luật, "
                                             "bảo tàng, quản lí văn hóa, nghiên cứu…"],
        ["⑤ Thích ứng với thế giới thay đổi", "Hiểu quá khứ giúp lí giải vấn đề hiện tại, ứng xử đúng đắn trong hội nhập."],
    ], [2.2, 4.2], bold_first_col=True)
    f.append(P("<b>Học ở đâu?</b> Không chỉ trên lớp mà còn qua <b>sách báo, thư viện, bảo tàng, di tích, lễ hội, phim ảnh, "
           "Internet, cuộc thi, câu lạc bộ, hoạt động trải nghiệm, lời kể của nhân chứng</b>…"))

    f += H2("3. Thu thập, xử lí thông tin và sử liệu")
    f += H3("Nơi tìm kiếm sử liệu")
    f.append(P("Thư viện, bảo tàng, trung tâm lưu trữ, di tích lịch sử, nhân chứng lịch sử, gia đình – dòng họ (gia phả), "
           "Internet (ưu tiên trang chính thống: cơ quan nhà nước, bảo tàng, viện nghiên cứu…)."))
    f += H3("Các bước thu thập – xử lí (bảng đặc tả yêu cầu “Nêu được các bước”)")
    f += table([
        ["Bước", "Việc làm", "Gợi ý cụ thể"],
        ["1. Lập thư mục", "Xác định mục đích, vấn đề cần tìm hiểu; <b>lập thư mục (danh mục) sử liệu</b> cần sưu tầm",
         "Liệt kê sách, tài liệu, hiện vật, nhân chứng… và nơi có thể tìm"],
        ["2. Sưu tầm, thu thập", "<b>Tiến hành sưu tầm, thu thập</b> sử liệu", "Đọc, ghi chép, sao chụp, phỏng vấn, "
                                                                              "tham quan, tra cứu; <b>ghi rõ nguồn</b>"],
        ["3. Chọn lọc, phân loại", "<b>Chọn lọc, phân loại</b> sử liệu", "Theo dạng thức (chữ viết, hiện vật…), "
                                                                       "theo nội dung, theo sơ cấp – thứ cấp"],
        ["4. Xử lí (xác minh, đánh giá)", "<b>Phân tích, so sánh, đối chiếu</b>; <b>xác minh độ tin cậy và giá trị</b> của sử liệu",
         "Đối chiếu nhiều nguồn; loại bỏ thông tin sai lệch; rút ra thông tin cần thiết để học tập, trình bày"],
    ], [1.5, 2.5, 2.6], bold_first_col=True)
    f += box("Vì sao phải xác minh, đối chiếu sử liệu?", [
        P("Vì sử liệu có thể <b>không đầy đủ, sai lệch, mang tính chủ quan</b>, thậm chí bị <b>xuyên tạc</b> (nhất là trên mạng xã hội). "
          "Xác minh giúp bảo đảm thông tin <b>chính xác, khách quan</b>, đúng nguyên tắc của Sử học."),
    ], color=AMBER, bg=CREAM, icon="✦")

    f += H2("4. Vận dụng tri thức, bài học lịch sử vào cuộc sống")
    f += bullets([
        "<b>Bản chất</b>: <b>kết nối quá khứ với hiện tại</b> – dùng hiểu biết và bài học lịch sử để <b>giải thích, đánh giá, "
        "giải quyết</b> những vấn đề thời sự, thực tiễn và <b>định hướng hành động</b> cho tương lai.",
        ("Một số bài học lịch sử lớn của dân tộc:", [
            "“Lấy dân làm gốc”; “Khoan thư sức dân”; khối <b>đại đoàn kết dân tộc</b>.",
            "<b>Dựng nước đi đôi với giữ nước</b>; kết hợp sức mạnh dân tộc với sức mạnh thời đại.",
            "Ngoại giao <b>mềm dẻo, hòa hiếu</b> nhưng <b>kiên quyết bảo vệ chủ quyền</b>.",
        ]),
        ("Ví dụ vận dụng giải thích vấn đề thời sự:", [
            "Chủ quyền của Việt Nam đối với quần đảo <b>Hoàng Sa, Trường Sa</b> có cơ sở lịch sử vững chắc "
            "(hoạt động của đội Hoàng Sa thời chúa Nguyễn, các văn bản Châu bản triều Nguyễn…).",
            "Bài học đoàn kết, “tương thân tương ái” được vận dụng khi cả nước chung tay phòng chống thiên tai, dịch bệnh.",
        ]),
        "<b>Thái độ cần có</b>: quan tâm, yêu thích, chủ động tham gia các hoạt động tìm hiểu lịch sử, văn hóa của "
        "dân tộc Việt Nam và thế giới.",
    ])
    f += box("Mẹo nhớ Bài 2", [
        *bullets([
            "<b>4 bước thu thập – xử lí</b>: “<b>LẬP – SƯU – LỌC – XÉT</b>” (Lập thư mục → Sưu tầm → Chọn lọc, phân loại → Xét/xác minh, đánh giá).",
            "<b>Học suốt đời vì</b>: “<b>RỘNG – MỚI – CẦN</b>” (tri thức rộng lớn – luôn đổi mới – cần cho cuộc sống, nghề nghiệp).",
            "Bẫy Đúng/Sai hay gặp: “học lịch sử <b>chỉ</b> ở trường”, “thông tin trên mạng <b>đều</b> chính xác”, "
            "“lịch sử <b>không</b> giúp ích cho hiện tại” → đều <b>SAI</b>.",
        ]),
    ], color=PURPLE, bg=LILAC, icon="❖")
    return f


def bai_3():
    f = []
    f += H1("C. BÀI 3 – VAI TRÒ CỦA SỬ HỌC  (★ trọng tâm – 5,75 điểm)", color=RED,
            sub="Chủ đề 2: Vai trò của Sử học • Đề thi: câu I.14 → I.20, câu II.2 (a–d) và TOÀN BỘ câu tự luận")

    f += H2("1. Di sản và các loại hình di sản")
    f += box("Khái niệm", [
        P("<b>Di sản văn hóa</b> là những sản phẩm <b>tinh thần, vật chất</b> có <b>giá trị lịch sử, văn hóa, khoa học</b>, "
          "được <b>lưu truyền từ thế hệ này qua thế hệ khác</b>."),
        P("<b>Di sản thiên nhiên</b> là các cảnh quan, địa hình, địa chất, hệ sinh thái… có giá trị nổi bật về <b>thẩm mĩ, khoa học, môi trường</b>."),
    ], color=RED, bg=ROSE, icon="✎")
    f += table([
        ["Loại hình", "Gồm những gì?", "Ví dụ"],
        ["Di sản văn hóa <b>vật thể</b>",
         "<b>Di tích lịch sử – văn hóa</b>; <b>danh lam thắng cảnh</b>; <b>di vật</b>; <b>cổ vật</b>; <b>bảo vật quốc gia</b>",
         "Hoàng thành Thăng Long, Văn Miếu – Quốc Tử Giám, trống đồng Ngọc Lũ, Khu di tích Kim Liên"],
        ["Di sản văn hóa <b>phi vật thể</b>",
         "Tiếng nói, chữ viết; ngữ văn dân gian; nghệ thuật trình diễn dân gian; tập quán xã hội, tín ngưỡng; "
         "lễ hội truyền thống; nghề thủ công truyền thống; tri thức dân gian",
         "Dân ca Ví, Giặm Nghệ Tĩnh; Nhã nhạc cung đình Huế; Quan họ Bắc Ninh; Hội Gióng"],
        ["Di sản <b>thiên nhiên</b>", "Cảnh quan, địa chất – địa mạo, hệ sinh thái, đa dạng sinh học tiêu biểu",
         "Vịnh Hạ Long; Vườn quốc gia Phong Nha – Kẻ Bàng"],
        ["Di sản <b>hỗn hợp</b> (UNESCO)", "Vừa có giá trị văn hóa, vừa có giá trị thiên nhiên nổi bật",
         "Quần thể danh thắng Tràng An (duy nhất ở Việt Nam)"],
    ], [1.6, 2.9, 2.4], bold_first_col=False, valign="TOP")
    f += box("Cập nhật pháp luật (đọc thêm)", [
        P("Sách giáo khoa KNTT trình bày theo Luật Di sản văn hóa trước đây: di sản văn hóa gồm <b>2 loại chính</b> – "
          "<b>vật thể</b> và <b>phi vật thể</b>. <b>Luật Di sản văn hóa năm 2024</b> (hiệu lực từ 01/7/2025) phân thành 3 loại: "
          "<b>di sản văn hóa phi vật thể, di sản văn hóa vật thể và di sản tư liệu</b>. Khi làm bài, nêu 2 loại chính theo SGK; "
          "có thể bổ sung di sản tư liệu (VD: Mộc bản triều Nguyễn, Châu bản triều Nguyễn, bia Tiến sĩ Văn Miếu – Quốc Tử Giám) để bài làm phong phú."),
    ], color=GREEN, bg=MINT, icon="✚")

    f += H2("2. Sử học với công tác bảo tồn và phát huy giá trị di sản văn hóa, di sản thiên nhiên")
    f += H3("a) Mối quan hệ hai chiều (mức Biết – rất hay hỏi)")
    f += table([
        ["Di sản → Sử học", "Sử học → Di sản"],
        ["Di sản là <b>nguồn sử liệu quan trọng, phong phú, xác thực</b> giúp các nhà sử học nghiên cứu, khôi phục và hiểu rõ quá khứ.",
         "Sử học cung cấp <b>cơ sở khoa học</b> để <b>nhận diện, xác định giá trị, bảo tồn và phát huy</b> giá trị di sản."],
    ], [1, 1], center_cols=())
    f += H3("b) Vai trò cụ thể của Sử học (mức Hiểu)")
    f += table([
        ["Khâu", "Sử học làm gì?"],
        ["① Nhận diện, xác định giá trị",
         "Nghiên cứu, khảo sát để làm rõ <b>nguồn gốc, niên đại, chủ nhân, quá trình hình thành – biến đổi</b>; đánh giá "
         "<b>giá trị lịch sử, văn hóa, khoa học</b> của di sản → cơ sở để <b>xếp hạng, lập hồ sơ</b> (kể cả hồ sơ trình UNESCO)."],
        ["② Bảo tồn",
         "Cung cấp thông tin, cứ liệu khoa học để <b>trùng tu, tôn tạo đúng nguyên gốc</b>, giữ <b>tính xác thực, toàn vẹn</b>; "
         "tư vấn giải pháp bảo tồn phù hợp với từng loại di sản."],
        ["③ Phát huy giá trị",
         "<b>Tuyên truyền, quảng bá, giáo dục</b>; xây dựng nội dung trưng bày, thuyết minh; gắn di sản với <b>du lịch</b> "
         "và đời sống cộng đồng."],
    ], [1.6, 5], bold_first_col=True)
    f += bullets([
        "<b>Nguyên tắc bảo tồn</b>: giữ gìn tối đa <b>yếu tố gốc</b>, bảo đảm <b>tính nguyên vẹn, tính xác thực</b>, phát triển "
        "<b>bền vững</b>, tôn trọng và phát huy vai trò <b>cộng đồng</b>.",
        "<b>Trách nhiệm</b>: Nhà nước, các tổ chức xã hội, cộng đồng và <b>mỗi cá nhân</b> (trong đó có học sinh).",
    ])

    f += H2("3. Sử học với sự phát triển du lịch")
    f += H3("a) Vai trò của lịch sử – văn hóa đối với sự phát triển du lịch")
    f += numbered([
        "Các giá trị lịch sử, văn hóa (di tích, lễ hội, làng nghề, ẩm thực, nghệ thuật…) là <b>nguồn tài nguyên du lịch quan trọng</b> "
        "(tài nguyên du lịch nhân văn) – cơ sở hình thành du lịch văn hóa, lịch sử, tâm linh, lễ hội…",
        "Tạo nên <b>sản phẩm du lịch đặc sắc, hấp dẫn</b>, mang <b>bản sắc riêng</b>, tăng sức cạnh tranh của điểm đến.",
        "Góp phần <b>quảng bá hình ảnh</b> đất nước, con người Việt Nam; thúc đẩy giao lưu văn hóa và phát triển kinh tế.",
    ])
    f += H3("b) Sử học giúp gì cho du lịch?")
    f.append(P("Cung cấp <b>thông tin, tri thức chính xác</b> về lịch sử – văn hóa để <b>xây dựng sản phẩm, tuyến du lịch</b>, "
           "<b>nội dung thuyết minh</b>, đào tạo hướng dẫn viên và quảng bá điểm đến một cách khoa học, hấp dẫn."))
    f += H3("c) Tác động của du lịch đối với công tác bảo tồn di tích (mức Hiểu – phân tích)")
    f += table([
        ["⊕ Tích cực", "⊖ Tiêu cực"],
        ["• Tạo <b>nguồn thu</b> để <b>tái đầu tư</b> cho bảo tồn, trùng tu di tích.<br/>"
         "• <b>Quảng bá</b> giá trị di sản trong nước và quốc tế.<br/>"
         "• <b>Nâng cao nhận thức</b>, ý thức bảo vệ di sản của cộng đồng.<br/>"
         "• Tạo <b>việc làm, sinh kế</b> → người dân gắn bó, chung tay giữ gìn di sản.<br/>"
         "• Thúc đẩy giao lưu, phục hồi lễ hội, nghề truyền thống.",
         "• <b>Quá tải</b> khách → di tích <b>xuống cấp, hư hại</b>.<br/>"
         "• <b>Ô nhiễm môi trường</b>, rác thải, xâm hại cảnh quan.<br/>"
         "• <b>Thương mại hóa</b>, “sân khấu hóa” làm <b>biến dạng giá trị</b> di sản.<br/>"
         "• Xây dựng tràn lan, trùng tu sai lệch yếu tố gốc.<br/>"
         "• Hành vi thiếu ý thức: viết, vẽ bậy, xả rác, lấy cắp hiện vật."],
    ], [1, 1], head_bg=GREEN, valign="TOP")
    f.append(P("→ <b>Kết luận</b>: cần phát triển <b>du lịch bền vững</b>, hài hòa giữa <b>khai thác và bảo tồn</b>."))

    f += H2("4. Địa danh là tài nguyên du lịch của nước ta (bảng đặc tả: “Kể tên được”)")
    f += table([
        ["Nhóm", "Di sản / Địa danh tiêu biểu (năm UNESCO ghi danh)"],
        ["Di sản văn hóa thế giới",
         "Quần thể di tích Cố đô Huế (1993); Đô thị cổ Hội An (1999); Khu đền tháp Mỹ Sơn (1999); "
         "Khu trung tâm Hoàng thành Thăng Long – Hà Nội (2010); Thành nhà Hồ (2011); "
         "Quần thể di tích và danh thắng Yên Tử – Vĩnh Nghiêm – Côn Sơn, Kiếp Bạc (2025)"],
        ["Di sản thiên nhiên thế giới",
         "Vịnh Hạ Long (1994, 2000; mở rộng thành Vịnh Hạ Long – quần đảo Cát Bà năm 2023); "
         "Vườn quốc gia Phong Nha – Kẻ Bàng (2003, 2015)"],
        ["Di sản hỗn hợp thế giới", "Quần thể danh thắng Tràng An – Ninh Bình (2014) – <b>duy nhất ở Việt Nam</b>"],
        ["Di sản phi vật thể (UNESCO)",
         "Nhã nhạc cung đình Huế (2003); Không gian văn hóa Cồng chiêng Tây Nguyên (2005); Dân ca Quan họ Bắc Ninh (2009); "
         "Ca trù (2009); Hội Gióng ở đền Phù Đổng và đền Sóc (2010); Hát Xoan Phú Thọ (2011); "
         "Tín ngưỡng thờ cúng Hùng Vương (2012); Đờn ca tài tử Nam Bộ (2013); <b>Dân ca Ví, Giặm Nghệ Tĩnh (2014)</b>; "
         "Nghi lễ và trò chơi kéo co (2015); Thực hành Tín ngưỡng thờ Mẫu Tam phủ (2016); Nghệ thuật Bài Chòi Trung Bộ (2017); "
         "Thực hành Then (2019); Nghệ thuật Xòe Thái (2021); Nghệ thuật làm gốm của người Chăm (2022); "
         "Lễ hội vía Bà Chúa Xứ núi Sam (2024)"],
        ["Di tích, danh thắng nổi tiếng khác",
         "Văn Miếu – Quốc Tử Giám; Đền Hùng; Chùa Hương; Côn Đảo; Địa đạo Củ Chi; Điện Biên Phủ; Sa Pa; Đà Lạt; Phú Quốc…"],
        ["Ở Nghệ An (liên hệ địa phương)",
         "Khu di tích Kim Liên (quê hương Chủ tịch Hồ Chí Minh); Đền Cuông (thờ An Dương Vương); Thành cổ Vinh; "
         "Khu di tích Truông Bồn; Bảo tàng Xô viết Nghệ Tĩnh; Vườn quốc gia Pù Mát; Khu dự trữ sinh quyển thế giới "
         "miền Tây Nghệ An; biển Cửa Lò; Dân ca Ví, Giặm"],
    ], [1.5, 5], bold_first_col=True, valign="TOP", font_size=8.9)
    f.append(P("<i>Ghi chú: tên di sản ghi theo tên gọi quen thuộc/được UNESCO công nhận; một số địa giới hành chính đã thay đổi "
           "sau sắp xếp năm 2025.</i>", "small"))

    f += H2("5. Biện pháp bảo tồn, phát huy giá trị di sản (phần Vận dụng – 2 điểm tự luận)")
    f += table([
        ["Chủ thể", "Biện pháp"],
        ["Nhà nước", "Hoàn thiện pháp luật về di sản; quy hoạch, đầu tư kinh phí; xếp hạng, lập hồ sơ; "
                     "kiểm tra, <b>xử lí nghiêm</b> hành vi xâm hại di sản."],
        ["Nhà khoa học (Sử học…)", "Nghiên cứu, lập hồ sơ khoa học; <b>số hóa di sản</b> (3D, thực tế ảo, mã QR); "
                                   "tư vấn trùng tu đúng nguyên gốc."],
        ["Ngành du lịch, địa phương", "Phát triển <b>du lịch bền vững</b>: kiểm soát, phân luồng lượng khách; quy định ứng xử văn minh; "
                                      "dùng nguồn thu tái đầu tư bảo tồn; để <b>cộng đồng</b> tham gia và hưởng lợi."],
        ["Cộng đồng", "Giữ gìn, thực hành, truyền dạy di sản phi vật thể (hát Ví, Giặm, lễ hội, nghề truyền thống); giám sát, phát hiện vi phạm."],
        ["<b>Học sinh</b>", "Tìm hiểu, tham quan di tích <b>có văn hóa</b> (không xả rác, viết vẽ bậy, sờ chạm hiện vật); "
                            "<b>tuyên truyền</b> trên mạng xã hội, làm video, poster giới thiệu di sản; tham gia CLB, tình nguyện "
                            "dọn vệ sinh di tích, làm hướng dẫn viên nhí; học và biểu diễn dân ca; <b>vận động</b> người thân, bạn bè "
                            "cùng bảo vệ; lên án, báo cáo hành vi xâm hại di sản."],
    ], [1.4, 5], bold_first_col=True, valign="TOP")

    f += box("Mẹo nhớ Bài 3", [
        *bullets([
            "<b>5 loại di sản vật thể</b>: “<b>TÍCH – THẮNG – VẬT – CỔ – BẢO</b>” (Di <b>tích</b> – Danh <b>thắng</b> – Di <b>vật</b> – "
            "<b>Cổ</b> vật – <b>Bảo</b> vật quốc gia).",
            "<b>Vai trò Sử học với di sản</b>: “<b>XÁC – BẢO – PHÁT</b>” (Xác định giá trị – Bảo tồn – Phát huy).",
            "<b>Tác động của du lịch</b>: <b>3 T tích cực</b> = <b>T</b>iền (nguồn thu) – <b>T</b>iếng (quảng bá) – <b>T</b>hức (nâng cao ý thức); "
            "<b>3 T tiêu cực</b> = <b>T</b>ải (quá tải) – <b>T</b>àn (xuống cấp, ô nhiễm) – <b>T</b>hương (thương mại hóa).",
            "<b>Di sản ở Nghệ An</b>: “<b>Ví, Giặm 2014</b>” – di sản phi vật thể đại diện của nhân loại.",
            "<b>Tràng An</b> = di sản <b>hỗn hợp</b> duy nhất; <b>Hạ Long, Phong Nha</b> = <b>thiên nhiên</b>; "
            "<b>Huế, Hội An, Mỹ Sơn, Hoàng thành, Thành nhà Hồ, Yên Tử</b> = <b>văn hóa</b>.",
        ]),
    ], color=PURPLE, bg=LILAC, icon="❖")
    f.append(PageBreak())
    return f


def so_do_tong_hop():
    """Sơ đồ tóm tắt 1 trang để học thuộc nhanh."""
    f = []
    f += H1("TÓM TẮT 1 TRANG – HỌC THUỘC TRƯỚC GIỜ KIỂM TRA", color=PURPLE)
    f += table([
        ["Bài", "Từ khóa phải thuộc"],
        ["Bài 1",
         "<b>Hiện thực LS</b>: đã diễn ra – khách quan – duy nhất – không đổi.<br/>"
         "<b>LS được nhận thức</b>: hiểu biết của con người – chủ quan – đa dạng – có thể thay đổi, chưa đầy đủ.<br/>"
         "<b>Sử học</b>: khoa học nghiên cứu quá khứ của con người và xã hội loài người.<br/>"
         "<b>Đối tượng</b>: quá khứ loài người trên mọi lĩnh vực. <b>Chức năng</b>: khoa học + xã hội. "
         "<b>Nhiệm vụ</b>: nhận thức – giáo dục – dự báo.<br/>"
         "<b>Nguyên tắc</b>: khách quan – trung thực – tiến bộ. <b>Sử liệu</b>: chữ viết – hiện vật – truyền miệng – hình ảnh; "
         "gốc (sơ cấp) / phái sinh (thứ cấp). <b>Phương pháp</b>: lịch sử + logic."],
        ["Bài 2",
         "<b>Vai trò tri thức LS</b>: hiểu cội nguồn, bản sắc; rút bài học; giải thích hiện tại, định hướng tương lai.<br/>"
         "<b>Học suốt đời vì</b>: tri thức rộng lớn – luôn bổ sung, đổi mới – cần cho cuộc sống, nghề nghiệp.<br/>"
         "<b>4 bước</b>: lập thư mục → sưu tầm, thu thập → chọn lọc, phân loại → xử lí (xác minh, đánh giá).<br/>"
         "<b>Vận dụng</b>: kết nối quá khứ – hiện tại để giải thích, giải quyết vấn đề thực tiễn."],
        ["Bài 3",
         "<b>Di sản vật thể</b>: di tích, danh thắng, di vật, cổ vật, bảo vật quốc gia. <b>Phi vật thể</b>: tiếng nói, chữ viết, "
         "ngữ văn dân gian, nghệ thuật trình diễn, tập quán, tín ngưỡng, lễ hội, nghề thủ công, tri thức dân gian.<br/>"
         "<b>Quan hệ 2 chiều</b>: di sản là nguồn sử liệu ↔ Sử học là cơ sở khoa học để xác định – bảo tồn – phát huy.<br/>"
         "<b>LS – VH với du lịch</b>: tài nguyên quan trọng; tạo sản phẩm đặc sắc; quảng bá hình ảnh.<br/>"
         "<b>Du lịch với bảo tồn</b>: (+) nguồn thu, quảng bá, nâng ý thức, sinh kế; (–) quá tải, xuống cấp, ô nhiễm, thương mại hóa.<br/>"
         "<b>Biện pháp</b>: pháp luật – đầu tư – nghiên cứu, số hóa – du lịch bền vững – cộng đồng – tuyên truyền, giáo dục – HS hành động."],
    ], [0.7, 6], bold_first_col=True, valign="TOP")
    f += H2("Lộ trình ôn tập 7 ngày")
    f += table([
        ["Ngày", "Nội dung", "Sản phẩm tự kiểm tra"],
        ["1", "Phần I (ma trận) + Bài 1 mục 1–2", "Tự vẽ bảng so sánh hiện thực LS / LS được nhận thức"],
        ["2", "Bài 1 mục 3 (Sử học)", "Đọc thuộc 3 nhiệm vụ, 2 chức năng, 3 nguyên tắc, 4 dạng sử liệu"],
        ["3", "Bài 2", "Nói lại 4 bước thu thập – xử lí sử liệu, 5 lí do học suốt đời"],
        ["4", "Bài 3 mục 1–2", "Kể tên 5 loại di sản vật thể, các nhóm phi vật thể; quan hệ Sử học – di sản"],
        ["5", "Bài 3 mục 3–5 + bảng di sản UNESCO", "Viết dàn ý câu tự luận (biện pháp bảo tồn một di sản ở Nghệ An)"],
        ["6", "Làm Đề minh họa số 1 (45 phút) → chấm theo đáp án", "Ghi lại câu sai, xem lại mục kiến thức tương ứng"],
        ["7", "Làm Đề số 2 + Ngân hàng câu hỏi + Hỏi – đáp nhanh", "Đạt ≥ 90% câu trắc nghiệm đúng"],
    ], [0.5, 3, 3.2], center_cols=(0,))
    f.append(PageBreak())
    return f


def ky_nang():
    f = []
    f += H1("PHẦN III. KĨ NĂNG LÀM BÀI – LẤY TRỌN ĐIỂM", color=GREEN)
    f += H3("1. Trắc nghiệm nhiều lựa chọn (I.1 – I.20)")
    f += bullets([
        "Gạch chân <b>từ khóa</b> trong câu dẫn: “khái niệm”, “đối tượng”, “chức năng”, “nhiệm vụ”, “KHÔNG”, “chủ yếu”, “cơ bản”.",
        "Câu hỏi “<b>KHÔNG</b> phải” → tìm phương án <b>sai</b> hoặc không thuộc nhóm.",
        "Phương án chứa từ <b>tuyệt đối</b> (chỉ, duy nhất, tất cả, luôn luôn, hoàn toàn) thường sai – trừ kiến thức đặc biệt "
        "(VD: Tràng An là di sản hỗn hợp <b>duy nhất</b> của Việt Nam).",
        "Không bỏ trống: mỗi câu 0,25 điểm, không trừ điểm khi sai.",
    ])
    f += H3("2. Trắc nghiệm Đúng/Sai (II.1, II.2)")
    f += bullets([
        "<b>Đọc kĩ đoạn tư liệu</b>: ý a, b thường hỏi thông tin trong tư liệu hoặc kiến thức cơ bản; ý c, d yêu cầu suy luận, vận dụng.",
        "Mỗi ý xét <b>độc lập</b>; một ý chỉ cần <b>một chi tiết sai</b> là cả ý <b>Sai</b>.",
        "Cảnh giác các cụm: “chỉ”, “duy nhất”, “hoàn toàn”, “không cần”, “quyết định”, “đầu tiên” – kiểm tra kĩ.",
    ])
    f += H3("3. Tự luận (3,0 điểm = ½ Biết 1,0 đ + ½ Vận dụng 2,0 đ)")
    f += table([
        ["Phần", "Cách viết"],
        ["Ý Biết (1,0 đ)", "Trình bày <b>ngắn gọn, đủ ý, đúng thuật ngữ</b> SGK (VD: kể tên loại hình di sản; nêu quan hệ Sử học – di sản). "
                           "Mỗi ý nhỏ 0,25 đ → viết thành <b>4 gạch đầu dòng</b>."],
        ["Ý Vận dụng (2,0 đ)", "<b>Mở</b>: giới thiệu di sản cụ thể (tên, loại hình, giá trị) → <b>Thân</b>: 4–5 biện pháp, mỗi biện pháp "
                               "có <b>chủ thể + việc làm + mục đích</b> → <b>Kết</b>: liên hệ trách nhiệm của bản thân, vận động mọi người."],
        ["Lỗi mất điểm", "Liệt kê chung chung, không gắn di sản cụ thể; quên phần trách nhiệm của học sinh; nhầm vật thể/phi vật thể."],
    ], [1.4, 5.3], bold_first_col=True, valign="TOP")
    f.append(PageBreak())
    return f
