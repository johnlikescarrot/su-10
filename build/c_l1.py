# -*- coding: utf-8 -*-
"""c_l1.py — BÀI 1: Hiện thực lịch sử và lịch sử được con người nhận thức."""
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer, KeepTogether
from layout import (S, CW, h2, h3, h4, p, bullets, numbered, card, data_table, quote,
                    band, CHECK, CROSS, ARROW, STAR, WARN)


def story():
    st = []
    st += band("1", "HIỆN THỰC LỊCH SỬ VÀ LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC",
               "Bài 1 · Chủ đề 1: Lịch sử và Sử học · 6 câu trắc nghiệm (Câu 1–6)")

    # ---------------------------------------------------------------- khung
    st.append(h2("A. Khung xương: bài này có đúng 3 trục"))
    rows = [
        ["Trục", "Câu hỏi cốt lõi phải trả lời được", "Từ khoá nhớ"],
        ["<b>1. Lịch sử là gì?</b>", "Cái gì đã xảy ra, và nó tồn tại thế nào?", "đã diễn ra · khách quan"],
        ["<b>2. Sử học là gì?</b>",
         "Khoa học nào nghiên cứu cái đã xảy ra, nghiên cứu cái gì, để làm gì, theo nguyên tắc nào?",
         "đối tượng · chức năng · nhiệm vụ · nguyên tắc"],
        ["<b>3. Nhận thức lịch sử là gì?</b>",
         "Con người hiểu biết về quá khứ ra sao, và vì sao hiểu biết ấy không bao giờ giống hệt quá khứ?",
         "chủ quan · khoảng cách · bổ sung"],
    ]
    st.append(data_table(rows, [40 * mm, 92 * mm, CW - 132 * mm]))
    st.append(Spacer(1, 3))
    st.append(p("Nếu chỉ nhớ 3 dòng trên, bạn đã có thể trả lời đúng khoảng 4/6 câu của bài này. "
                "Ba mục B, C, D dưới đây chỉ là “giãn” ba dòng ấy ra cho đủ chi tiết.", S["small"]))

    # ---------------------------------------------------------------- lịch sử
    st.append(h2("B. Lịch sử là gì?"))
    st.append(h3("1. Hai nghĩa của từ “lịch sử”"))
    st += bullets([
        "<b>Nghĩa rộng:</b> lịch sử là <b>toàn bộ những gì đã diễn ra trong quá khứ</b> — của giới tự nhiên "
        "và của xã hội loài người.",
        "<b>Nghĩa hẹp (dùng trong nhà trường, trong đời sống):</b> lịch sử là <b>quá trình phát sinh, phát triển "
        "của xã hội loài người</b> nói chung, hoặc của một cộng đồng người, một quốc gia – dân tộc nói riêng.",
    ])
    st.append(h3("2. Hai tính chất không thể bỏ sót"))
    st += bullets([
        "<b>Tồn tại khách quan:</b> sự việc đã xảy ra thì nằm ngoài ý muốn, ngoài sự lựa chọn của con người.",
        "<b>Không thể thay đổi, không thể xoá bỏ:</b> con người chỉ có thể <i>nhận thức</i> và <i>đánh giá</i> "
        "khác đi, chứ không làm cho quá khứ khác đi.",
    ])

    st.append(h3("3. Phân biệt ba tầng khái niệm rất dễ lẫn"))
    rows = [
        ["Tầng khái niệm", "Nội dung", "Ví dụ (khởi nghĩa Lam Sơn)"],
        ["<b>Hiện thực lịch sử</b><br/><i>(quá khứ)</i>",
         "Những gì đã thực sự diễn ra; khách quan; duy nhất.",
         "Năm 1418–1427, nghĩa quân Lam Sơn đánh đuổi quân Minh, giành lại độc lập; năm 1428 Lê Lợi lên ngôi."],
        ["<b>Lịch sử được con người nhận thức</b>",
         "Những hiểu biết của con người về quá khứ ấy; chủ quan; nhiều cách; có thể bổ sung.",
         "Sự tích Hồ Gươm (truyền thuyết), <i>Bình Ngô đại cáo</i>, phim tài liệu, bài giảng — mỗi cách kể một khác."],
        ["<b>Sử học</b>",
         "Khoa học nghiên cứu quá khứ bằng sử liệu và phương pháp khoa học để đi đến nhận thức chân thực nhất.",
         "Nhà sử học so sánh bia Vĩnh Lăng (1433) với <i>Đại Việt sử ký toàn thư</i> để xác định niên đại, sự kiện."],
    ]
    st.append(data_table(rows, [36 * mm, 66 * mm, CW - 102 * mm]))

    # ---------------------------------------------------------------- sử học
    st.append(h2("C. Sử học là gì? (phần “nặng” nhất của bài)"))
    st.append(h3("1. Khái niệm"))
    st.append(p("<b>Sử học là khoa học nghiên cứu về lịch sử</b> — tức là nghiên cứu <b>quá trình phát sinh, "
                "phát triển của xã hội loài người</b> trên mọi lĩnh vực: kinh tế, chính trị, quân sự, văn hoá, "
                "tư tưởng, tôn giáo, xã hội… Nói cách khác, Sử học nghiên cứu <b>con người trong quá khứ</b>, "
                "cả đời sống vật chất lẫn đời sống tinh thần."))
    st.append(card("bay", [
        Paragraph("Câu hỏi “Sử học là gì?” rất dễ chọn nhầm phương án <i>“toàn bộ những gì đã diễn ra "
                  "trong quá khứ”</i>. Đó là <b>lịch sử</b> (đối tượng), không phải <b>Sử học</b> (khoa học). "
                  "Dấu hiệu nhận diện: trong phương án đúng của “Sử học” luôn có chữ <b>“khoa học”</b> "
                  "hoặc <b>“nghiên cứu”</b>.", S["small"])]))

    st.append(h3("2. Đối tượng nghiên cứu"))
    st.append(p("<b>Toàn bộ quá trình phát triển của xã hội loài người</b> và của các cộng đồng người trong quá khứ "
                "— không chỉ là các sự kiện chính trị, quân sự, không chỉ là “những chuyện của vua chúa”."))

    st.append(h3("3. Ba chức năng"))
    rows = [
        ["Chức năng", "Nội dung", "Biểu hiện dễ nhớ"],
        ["<b>Khoa học</b>",
         "Nhận thức, khám phá, tái hiện quá khứ một cách chân thực, khách quan; phát hiện quy luật vận động.",
         "Trả lời: <i>đã thực sự xảy ra cái gì, vì sao?</i>"],
        ["<b>Giáo dục</b>",
         "Giáo dục truyền thống, lòng yêu nước, tự hào dân tộc; hình thành nhân cách, lý tưởng, kĩ năng sống.",
         "Trả lời: <i>ta học được gì để sống cho đúng?</i>"],
        ["<b>Xã hội</b><br/><i>(dự báo)</i>",
         "Cung cấp bài học kinh nghiệm, luận cứ cho hoạch định chính sách; dự báo xu hướng phát triển.",
         "Trả lời: <i>tương lai nên đi theo hướng nào?</i>"],
    ]
    st.append(data_table(rows, [28 * mm, 88 * mm, CW - 116 * mm]))

    st.append(h3("4. Nhiệm vụ"))
    st += bullets([
        "Nhận thức đúng đắn, đầy đủ, khách quan về quá khứ; tái hiện và phục dựng quá khứ.",
        "Giải thích, đánh giá sự kiện và nhân vật lịch sử một cách khoa học, công bằng.",
        "Phục vụ giáo dục, bảo tồn và phát huy giá trị di sản, nghiên cứu và phát triển đất nước.",
        "Đấu tranh chống lại sự xuyên tạc, bóp méo lịch sử; bảo vệ chân lý lịch sử.",
    ])

    st.append(h3("5. Bốn nguyên tắc (thuộc lòng theo cụm “KQ – TD – CT – PT”)"))
    rows = [
        ["Nguyên tắc", "Nghĩa là", "Phản ví dụ (nếu vi phạm)"],
        ["<b>Khách quan</b>", "Phản ánh sự việc như nó đã diễn ra, không vì thiên vị hay định kiến.",
         "Chỉ ca ngợi, không nêu mặt hạn chế của một triều đại."],
        ["<b>Toàn diện</b>", "Xem xét nhiều mặt, nhiều chiều, nhiều nguồn; không chỉ một góc nhìn.",
         "Chỉ dùng một nguồn duy nhất rồi kết luận."],
        ["<b>Lịch sử – cụ thể</b>", "Đặt sự việc trong bối cảnh, thời gian, không gian cụ thể của nó.",
         "Lấy tiêu chuẩn hôm nay để phán xét người của 500 năm trước."],
        ["<b>Phát triển</b>", "Xem sự việc trong quá trình vận động, biến đổi, không tĩnh tại.",
         "Coi một hiện tượng là bất biến, không thấy sự chuyển hoá."],
    ]
    st.append(data_table(rows, [34 * mm, 82 * mm, CW - 116 * mm]))

    st.append(card("meo", [
        Paragraph("<b>“LỊCH SỬ – SỬ HỌC – SỬ LIỆU”</b> là ba việc khác nhau:", S["small"]),
        Paragraph("• <b>Lịch sử</b> = cái <b>ĐÃ XẢY RA</b>.", S["small"]),
        Paragraph("• <b>Sử học</b> = cái <b>NGHIÊN CỨU</b> cái đã xảy ra.", S["small"]),
        Paragraph("• <b>Sử liệu</b> = cái <b>CÒN LẠI</b> để nghiên cứu (học ở Bài 2).", S["small"]),
        Paragraph("Ba chức năng: <b>K – G – X</b> (Khoa học · Giáo dục · Xã hội). "
                  "Bốn nguyên tắc: <b>KQ – TD – CT – PT</b>. Đọc thành nhịp: <i>“Khách quan, toàn diện, "
                  "cụ thể, phát triển”</i> — đọc 3 lần là thuộc.", S["small"]),
    ], title="Mẹo nhớ 30 giây"))

    # ---------------------------------------------------------------- hiện thực vs nhận thức
    st.append(h2("D. Hiện thực lịch sử và lịch sử được con người nhận thức"))
    st.append(h3("1. Hiện thực lịch sử"))
    st.append(p("Là <b>những gì đã thực sự diễn ra trong quá khứ</b>, tồn tại <b>khách quan</b>, "
                "không phụ thuộc vào ý muốn của con người; đã xảy ra thì <b>không thể thay đổi, "
                "không thể xoá bỏ</b>. Ta chỉ có thể tiếp cận nó <b>gián tiếp</b>, qua dấu vết còn lại (sử liệu)."))

    st.append(h3("2. Lịch sử được con người nhận thức"))
    st.append(p("Là <b>những hiểu biết, sự phản ánh của con người về hiện thực lịch sử</b>, được hình thành "
                "qua học tập, nghiên cứu, trải nghiệm và truyền lại giữa các thế hệ; mang <b>tính chủ quan</b>; "
                "được biểu hiện dưới <b>nhiều hình thức</b>: truyền miệng (truyền thuyết, ca dao), chữ viết "
                "(sách sử, văn bia, nhật ký), hiện vật (bảo tàng), hình ảnh – phim, sản phẩm số (bảo tàng ảo, "
                "phim tài liệu, bài giảng trực tuyến)…"))

    st.append(h3("3. Bảng so sánh “7 tiêu chí” — học đúng bảng này là ăn trọn câu 5, 6"))
    rows = [
        ["Tiêu chí", "Hiện thực lịch sử", "Lịch sử được con người nhận thức"],
        ["<b>1.</b> Bản chất", "Cái đã xảy ra", "Hiểu biết về cái đã xảy ra"],
        ["<b>2.</b> Tính chất", "<b>Khách quan</b>", "<b>Chủ quan</b>"],
        ["<b>3.</b> Số lượng cách thể hiện", "Duy nhất, chỉ một", "Đa dạng, nhiều cách kể"],
        ["<b>4.</b> Khả năng thay đổi", "Không thể thay đổi", "Có thể thay đổi, bổ sung, hoàn thiện"],
        ["<b>5.</b> Phụ thuộc vào ai", "Không phụ thuộc con người", "Phụ thuộc trình độ, nhu cầu, lập trường của người nhận thức"],
        ["<b>6.</b> Hình thức tồn tại", "Trong chính quá khứ (chỉ còn dấu vết)", "Truyền miệng, văn bản, hiện vật, phim ảnh, sản phẩm số"],
        ["<b>7.</b> Cách kiểm chứng", "Không cần kiểm chứng — nó đã xảy ra", "Kiểm chứng được bằng sử liệu và phương pháp khoa học"],
    ]
    st.append(data_table(rows, [34 * mm, 58 * mm, CW - 92 * mm]))

    st.append(h3("4. Năm đặc điểm của lịch sử được con người nhận thức"))
    st += numbered([
        "<b>Mang tính chủ quan.</b> Cùng một sự kiện, nhà sử học, nhà văn, người dân, một bộ phim… có thể hiểu và "
        "trình bày khác nhau, vì mỗi người có trình độ, nhu cầu, lập trường, mục đích riêng.",
        "<b>Luôn có “khoảng cách” với hiện thực lịch sử.</b> Nhận thức không bao giờ trùng khít quá khứ; "
        "nó chỉ tiến gần chân lý hơn mà thôi.",
        "<b>Đa dạng, nhiều chiều.</b> Một sự kiện có thể được nhìn từ góc độ chính trị, kinh tế, văn hoá, "
        "từ phía người thắng và người thua, từ trong nước và ngoài nước.",
        "<b>Không ngừng được bổ sung, hoàn thiện.</b> Khi phát hiện sử liệu mới hoặc có phương pháp mới "
        "(khảo cổ học, phục dựng 3D, phân tích ADN, số hoá tư liệu), nhận thức cũ có thể được sửa lại.",
        "<b>Được biểu hiện qua nhiều loại hình</b> và được truyền từ thế hệ này sang thế hệ khác "
        "(truyền khẩu, văn tự, hiện vật, nghi lễ, phim ảnh, không gian số).",
    ])

    st.append(card("vd", [
        Paragraph("<b>Hiện thực:</b> thế kỉ XV, nghĩa quân Lam Sơn kháng chiến chống quân Minh thắng lợi.", S["small"]),
        Paragraph("<b>Nhận thức (dân gian):</b> <i>Sự tích Hồ Gươm</i> — Lê Lợi nhận gươm thần, trả gươm cho Rùa Vàng. "
                  "Đây không phải bản ghi sự kiện, nhưng phản ánh khát vọng hoà bình, chính nghĩa của nhân dân.", S["small"]),
        Paragraph("<b>Nhận thức (khoa học):</b> so sánh <i>Bình Ngô đại cáo</i>, bia Vĩnh Lăng, "
                  "<i>Đại Việt sử ký toàn thư</i> với các nguồn khảo cổ để xác định niên đại, diễn biến, tính chất "
                  "của cuộc khởi nghĩa.", S["small"]),
    ], title="Cùng một quá khứ, ba cách nhận thức"))

    st.append(card("bay", [
        Paragraph("<b>Bẫy 1.</b> “Hiện thực lịch sử thay đổi theo thời gian” <font name='DJ'>→</font> <b>Sai.</b> "
                  "Chỉ <i>nhận thức</i> thay đổi; hiện thực thì không.", S["small"]),
        Paragraph("<b>Bẫy 2.</b> “Nhận thức lịch sử mang tính chủ quan nên không có giá trị” <font name='DJ'>→</font> <b>Sai.</b> "
                  "Chủ quan là <i>thuộc tính</i>, nhưng nhờ sử liệu và phương pháp khoa học, nhận thức có thể "
                  "ngày càng tiến gần chân lý.", S["small"]),
        Paragraph("<b>Bẫy 3.</b> Đồng nhất “truyền thuyết” với “hiện thực lịch sử” <font name='DJ'>→</font> <b>Sai.</b> "
                  "Truyền thuyết là <i>một hình thức nhận thức</i> (dân gian, truyền miệng).", S["small"]),
        Paragraph("<b>Bẫy 4.</b> “Sử học” = “môn Lịch sử ở trường” <font name='DJ'>→</font> <b>Không đồng nhất.</b> "
                  "Sử học là ngành khoa học; môn Lịch sử là một phần tri thức của Sử học được dạy trong nhà trường.", S["small"]),
    ]))

    st.append(st_chot := card("chot", [
        Paragraph("<b>Một câu để nhớ cả bài:</b> “Quá khứ chỉ có một, cách kể có muôn vàn — "
                  "Sử học là nghề đi tìm cách kể đúng nhất.”", S["small"]),
    ], title="Chốt bài"))

    # ---------------------------------------------------------------- tự kiểm tra
    st.append(h2("E. Tự kiểm tra 6 câu (trả lời miệng trong 3 phút)"))
    rows = [
        ["Câu hỏi", "Trả lời gọn"],
        ["1. Lịch sử là gì?", "Toàn bộ những gì đã diễn ra trong quá khứ (nghĩa hẹp: quá trình phát sinh, phát triển của xã hội loài người)."],
        ["2. Ba chức năng của Sử học?", "Khoa học – Giáo dục – Xã hội."],
        ["3. Đối tượng của Sử học?", "Toàn bộ quá trình phát triển của xã hội loài người."],
        ["4. Hiện thực lịch sử khác nhận thức lịch sử ở đâu?", "Khách quan / chủ quan; một / nhiều; không đổi / có thể bổ sung."],
        ["5. Vì sao nhận thức lịch sử luôn có khoảng cách với quá khứ?", "Vì con người tiếp cận gián tiếp qua sử liệu, bằng trình độ và lập trường riêng."],
        ["6. Nêu 4 nguyên tắc của Sử học.", "Khách quan – Toàn diện – Lịch sử cụ thể – Phát triển."],
    ]
    st.append(data_table(rows, [62 * mm, CW - 62 * mm]))
    return st
