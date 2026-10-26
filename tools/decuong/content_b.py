# -*- coding: utf-8 -*-
"""Phần B – Chủ đề 1: Lịch sử và Sử học (Bài 1, Bài 2)."""
from style import *
from reportlab.platypus import PageBreak


def bai1():
    s = []
    s += h2("B2. Bài 1 – Hiện thực lịch sử và lịch sử được con người nhận thức", "B2")

    s += box("VỊ TRÍ CỦA BÀI TRONG ĐỀ", [
        "<b>6 câu trắc nghiệm nhiều lựa chọn</b> (I.1 → I.6), chiếm <b>1,5 điểm</b>.",
        "Nội dung chính: khái niệm lịch sử; hiện thực lịch sử; lịch sử được con người nhận thức; "
        "khái niệm, đối tượng, chức năng, nhiệm vụ của Sử học.",
    ], "note")

    # ---------------------------------------------------------- B2.1
    s += h3("B2.1. Lịch sử là gì?")
    s += [P("<b>Lịch sử</b> là những gì đã diễn ra trong quá khứ. <b>Lịch sử loài người</b> là toàn bộ "
            "những hoạt động của con người từ khi xuất hiện đến ngày nay, bao gồm cả quá trình con người "
            "tương tác với tự nhiên và quá trình con người tương tác với nhau.")]
    s += [P("Tuỳ theo cách tiếp cận, “lịch sử” được hiểu theo <b>hai nghĩa</b> cơ bản mà các em phải phân biệt "
            "thật chắc, vì đây là nguồn gốc của gần như toàn bộ câu hỏi của Bài 1:")]
    s += tb([
        ["Cách hiểu", "Nội dung", "Ví dụ"],
        ["<b>Hiện thực lịch sử</b>",
         "Toàn bộ những gì đã diễn ra trong quá khứ, tồn tại một cách khách quan, "
         "không phụ thuộc vào ý muốn chủ quan của con người.",
         "Ngày 2/9/1945, tại Quảng trường Ba Đình, Chủ tịch Hồ Chí Minh đọc Tuyên ngôn Độc lập – "
         "việc này <b>đã xảy ra</b>, không ai thay đổi được."],
        ["<b>Lịch sử được con người nhận thức</b>",
         "Những hiểu biết của con người về hiện thực lịch sử, được trình bày, tái hiện theo những cách khác nhau.",
         "Cùng sự kiện đó, mỗi cuốn sách, bộ phim, bài giảng, bảo tàng lại kể một cách khác nhau."],
    ], widths=[1.15, 2.6, 2.55], sp_after=8)

    # ---------------------------------------------------------- B2.2
    s += h3("B2.2. Hiện thực lịch sử – “cái đã xảy ra”")
    s += [P("<b>Hiện thực lịch sử</b> là toàn bộ những gì đã diễn ra trong quá khứ, tồn tại một cách khách quan, "
            "không phụ thuộc vào ý muốn chủ quan của con người. Đây là đối tượng nghiên cứu của Sử học.")]
    s += [P("Ba đặc điểm bắt buộc phải nhớ:")]
    s += numlist([
        "<b>Chỉ có một và không thể thay đổi.</b> Một sự kiện đã xảy ra thì mãi mãi là như vậy, "
        "không thể “sửa lại” hay “làm lại”.",
        "<b>Tồn tại khách quan, độc lập</b> với ý muốn, nhận thức của con người. Dù không ai biết đến, "
        "sự kiện đó vẫn đã diễn ra.",
        "<b>Không thể quan sát trực tiếp</b> vì đã lùi vào quá khứ; con người chỉ có thể tiếp cận gián tiếp "
        "thông qua <b>sử liệu</b> và các dấu vết còn lại.",
    ])
    s += box("PHÂN BIỆT NHANH BẰNG MỘT CÂU", [
        "Nếu sự việc <b>đã xảy ra ngoài kia</b>, dù có người biết hay không → đó là <b>hiện thực lịch sử</b>.",
        "Nếu sự việc <b>nằm trong đầu, trong sách, trong phim</b> của ai đó → đó là <b>nhận thức lịch sử</b>.",
    ], "tip")

    # ---------------------------------------------------------- B2.3
    s += h3("B2.3. Lịch sử được con người nhận thức – “cái ta hiểu về quá khứ”")
    s += [P("<b>Lịch sử được con người nhận thức</b> (còn gọi là <b>nhận thức lịch sử</b>) là những hiểu biết "
            "của con người về hiện thực lịch sử, được <b>trình bày, tái hiện theo những cách khác nhau</b>: "
            "kể chuyện, ghi chép, nghiên cứu, trình diễn, lập đài tưởng niệm, thực hành các nghi lễ, phong tục…")]
    s += [P("Nhận thức lịch sử có <b>bốn đặc điểm</b> mà đề thi rất hay hỏi:")]
    s += tb([
        ["#", "Đặc điểm", "Diễn giải", "Hệ quả"],
        ["1", "<b>Mang tính chủ quan</b>",
         "Phụ thuộc vào lập trường, mục đích, trình độ, kinh nghiệm và nguồn tư liệu mà người nhận thức tiếp cận.",
         "Cùng một sự kiện có thể có nhiều cách hiểu khác nhau"],
        ["2", "<b>Đa dạng, không đồng nhất</b>",
         "Mỗi cá nhân, cộng đồng, thời đại nhận thức khác nhau; thể hiện qua nhiều hình thức khác nhau.",
         "Không có “một” bản kể duy nhất"],
        ["3", "<b>Có thể thay đổi theo thời gian</b>",
         "Khi phát hiện thêm sử liệu mới, nhận thức cũ được bổ sung, điều chỉnh, thậm chí bị bác bỏ.",
         "Nhận thức lịch sử là một quá trình, không phải kết quả cố định"],
        ["4", "<b>Không bao giờ tái hiện đầy đủ</b> hiện thực lịch sử",
         "Luôn tồn tại “khoảng cách” giữa quá khứ và nhận thức về quá khứ.",
         "Vì vậy nhà sử học phải không ngừng tìm tòi, kiểm chứng"],
    ], widths=[0.35, 1.5, 3.0, 1.8], align_center=[0], sp_after=8)

    s += h4("Vì sao cùng một sự kiện lại có nhiều cách nhận thức khác nhau?")
    s += bullets([
        "<b>Khoảng cách thời gian</b>: người nghiên cứu ở hiện tại, sự kiện ở quá khứ, không thể quan sát trực tiếp.",
        "<b>Nguồn sử liệu khác nhau</b>: mỗi người tiếp cận một số nguồn tài liệu khác nhau, độ tin cậy khác nhau.",
        "<b>Lập trường, mục đích, trình độ</b> của người nghiên cứu khác nhau.",
        "<b>Nhu cầu của thời đại</b>: mỗi thời kì đặt ra những câu hỏi khác nhau với quá khứ.",
    ])

    # ---------------------------------------------------------- B2.4
    s += h3("B2.4. Bảng so sánh “kinh điển” – chắc chắn phải thuộc")
    s += [P("Đây là bảng so sánh xuất hiện nhiều nhất trong các đề kiểm tra. Hãy học theo <b>cặp đối lập</b>: "
            "một bên là “có thật, duy nhất, bất biến”, một bên là “trong đầu, đa dạng, biến đổi”.")]
    s += compare("Hiện thực lịch sử", "Lịch sử được con người nhận thức", [
        ("Bản chất", "Là <b>cái đã xảy ra</b> trong quá khứ", "Là <b>cái con người hiểu</b> về cái đã xảy ra"),
        ("Tính chất", "Khách quan, độc lập với ý muốn con người", "Vừa khách quan (dựa trên sự thật), vừa <b>chủ quan</b> (qua lăng kính người nhận thức)"),
        ("Số lượng", "<b>Chỉ có một</b>, duy nhất", "<b>Nhiều</b>, đa dạng, phong phú"),
        ("Khả năng thay đổi", "<b>Không thể thay đổi</b>", "<b>Có thể thay đổi</b>, bổ sung khi có sử liệu mới"),
        ("Thời điểm", "Có <b>trước</b>", "Có <b>sau</b>, hình thành khi con người tìm hiểu quá khứ"),
        ("Quan sát trực tiếp", "Không thể", "Được thể hiện ra bằng sách, phim, bảo tàng, lễ hội…"),
        ("Vai trò", "Là <b>đối tượng</b> nghiên cứu của Sử học", "Là <b>kết quả</b> nghiên cứu của Sử học"),
        ("Mối quan hệ", "Không có hiện thực lịch sử thì <b>không có</b> nhận thức lịch sử", "Không có nhận thức lịch sử thì hiện thực lịch sử <b>không được biết đến</b>"),
    ], wl=1.35, wr=1.35, wc=0.95)

    s += box("MẸO NHỚ: “MỘT THẬT – NHIỀU HIỂU”", [
        "<b>Hiện thực</b> = <b>1</b> (một sự thật, một lần xảy ra, không đổi) → nhớ số <b>1</b>.",
        "<b>Nhận thức</b> = <b>N</b> (nhiều người, nhiều cách kể, nhiều thời điểm) → nhớ chữ <b>N</b>.",
        "Câu chốt: <i>“Hiện thực lịch sử chỉ có một, nhưng lịch sử được con người nhận thức thì có rất nhiều.”</i>",
    ], "tip")

    # ---------------------------------------------------------- B2.5
    s += h3("B2.5. Sử học – khái niệm, đối tượng, chức năng, nhiệm vụ")
    s += [P("<b>Sử học</b> (khoa học lịch sử) là <b>khoa học nghiên cứu về quá khứ của loài người</b>. "
            "Sử học nghiên cứu các sự kiện, hiện tượng đã diễn ra trong xã hội loài người, "
            "khôi phục lại hiện thực lịch sử và phát hiện ra quy luật phát sinh, phát triển của nó.")]
    s += box("VÌ SAO GỌI SỬ HỌC LÀ MỘT KHOA HỌC?", [
        "Sử học có <b>đối tượng nghiên cứu riêng</b> (quá khứ loài người), có <b>phương pháp nghiên cứu riêng</b> "
        "(phương pháp lịch sử, phương pháp logic, phương pháp liên ngành…), có <b>nguyên tắc</b> và "
        "<b>chức năng, nhiệm vụ</b> rõ ràng. Đó là các tiêu chí của một ngành khoa học.",
    ], "note")

    s += mindmap("SỬ HỌC", [
        ("KHÁI NIỆM", ["Khoa học nghiên cứu về <b>quá khứ của loài người</b>",
                       "Khôi phục hiện thực lịch sử",
                       "Phát hiện quy luật phát sinh, phát triển"]),
        ("ĐỐI TƯỢNG", ["Toàn bộ quá khứ của loài người",
                       "Cá nhân, nhóm, cộng đồng, quốc gia, khu vực, nhân loại",
                       "Mọi lĩnh vực: chính trị, kinh tế, xã hội, văn hoá, quân sự, ngoại giao…"]),
        ("CHỨC NĂNG", ["<b>Khoa học:</b> khôi phục hiện thực lịch sử chính xác, khách quan",
                       "<b>Xã hội:</b> giáo dục tư tưởng, đạo đức; rút ra bài học kinh nghiệm"]),
        ("NHIỆM VỤ", ["<b>Nhận thức:</b> cung cấp tri thức khoa học",
                      "<b>Giáo dục – nêu gương</b>",
                      "<b>Dự báo:</b> tổng kết thực tiễn, góp phần dự báo tương lai"]),
    ], sub="Sơ đồ B.1 – Bốn trụ cột của Sử học (khái niệm · đối tượng · chức năng · nhiệm vụ)")

    s += h4("Đối tượng nghiên cứu")
    s += [P("Đối tượng nghiên cứu của Sử học là <b>toàn bộ quá khứ của loài người</b> – có thể là quá khứ của "
            "<b>một cá nhân, một nhóm người, một cộng đồng</b>, hay của <b>một quốc gia, một khu vực</b> "
            "hoặc <b>toàn thể nhân loại</b>, diễn ra trên mọi lĩnh vực của đời sống.")]
    s += [P("<b>Lưu ý bẫy:</b> “những hiện tượng tự nhiên xảy ra trong quá khứ” <b>không phải</b> đối tượng "
            "trực tiếp của Sử học – Sử học nghiên cứu <b>hoạt động của con người</b> và sự tương tác của con người "
            "với tự nhiên. Đây là phương án gây nhiễu rất quen thuộc.")]

    s += h4("Chức năng")
    s += tb([
        ["Chức năng", "Nội dung cụ thể", "Ví dụ"],
        ["<b>Chức năng khoa học</b><br/>(nhận thức)",
         "– Khôi phục các sự kiện lịch sử đã diễn ra trong quá khứ.<br/>"
         "– Rút ra <b>bản chất</b> của các quá trình lịch sử để phát hiện <b>quy luật</b> vận động và phát triển của lịch sử.",
         "Nghiên cứu để xác định chính xác thời điểm, diễn biến, nguyên nhân của một sự kiện"],
        ["<b>Chức năng xã hội</b><br/>(giáo dục)",
         "– <b>Giáo dục tư tưởng, đạo đức</b>, lòng yêu nước, tinh thần trách nhiệm.<br/>"
         "– <b>Rút ra bài học kinh nghiệm</b> cho cuộc sống hiện tại.",
         "Dùng bài học giữ nước, ngoại giao thời Lý – Trần để vận dụng hôm nay"],
    ], widths=[1.35, 3.15, 2.0], sp_after=8)

    s += h4("Nhiệm vụ")
    s += bullets([
        "<b>Nhiệm vụ nhận thức</b> – cung cấp những <b>tri thức khoa học</b>, giúp con người tìm hiểu, khám phá "
        "hiện thực lịch sử một cách <b>khách quan, khoa học, chân thực</b>.",
        "<b>Nhiệm vụ giáo dục, nêu gương</b> – hướng con người tới những phẩm chất, giá trị tốt đẹp, "
        "tiến bộ và nhân văn.",
        "<b>Nhiệm vụ dự báo</b> – thông qua việc tổng kết thực tiễn, rút ra các bài học kinh nghiệm, "
        "góp phần <b>dự báo tương lai</b> của đất nước, của nhân loại.",
    ])
    s += box("MẸO NHỚ 3 NHIỆM VỤ: “NHẬN – GIÁO – DỰ”", [
        "<b>NHẬN</b> thức → <b>GIÁO</b> dục, nêu gương → <b>DỰ</b> báo.",
        "Đọc xuôi: Nhận – Giáo – Dự; đọc ngược: Dự – Giáo – Nhận. Cùng một bộ ba, chỉ khác chiều.",
    ], "tip")

    # ---------------------------------------------------------- B2.6
    s += h3("B2.6. Nguyên tắc cơ bản của Sử học")
    s += [P("Nguyên tắc là “điều luật nghề nghiệp” của nhà sử học: nó định hướng việc nghiên cứu, "
            "giúp nhà sử học hiểu rõ sứ mệnh, trách nhiệm, đạo đức của người viết lịch sử, "
            "đồng thời phê phán các quan điểm sai trái, bảo vệ lẽ phải.")]
    s += tb([
        ["Nguyên tắc", "Nội dung", "Nếu vi phạm sẽ dẫn tới"],
        ["<b>Khách quan</b><br/><font size=7.6>(quan trọng nhất)</font>",
         "Dựa trên các nguồn <b>sử liệu</b> để khôi phục hiện thực lịch sử, "
         "<b>không nhận thức phiến diện, một chiều</b>, không theo ý kiến chủ quan. "
         "Sứ mệnh của Sử học là tái hiện lại hiện thực lịch sử, đưa ra nhận thức đầy đủ nhất về quá khứ "
         "dựa trên những thông tin đáng tin cậy.",
         "Lịch sử bị bóp méo, mất tính khoa học"],
        ["<b>Trung thực</b>",
         "Tôn trọng sự thật lịch sử, tái hiện nó một cách chân thực; "
         "không <b>xuyên tạc, thêm bớt hoặc làm sai lệch</b> sự thật lịch sử.",
         "Sử liệu bị làm giả, thế hệ sau hiểu sai quá khứ"],
        ["<b>Tiến bộ</b>",
         "Từ thấu hiểu quá khứ, Sử học hướng đến <b>phục vụ cuộc sống con người</b>, "
         "góp phần xây dựng xã hội văn minh, tiến bộ.",
         "Lịch sử trở thành công cụ kéo lùi xã hội"],
        ["<b>Nhân văn</b><br/><font size=7.6>(nhiều tài liệu bổ sung)</font>",
         "Hướng tới con người, tôn trọng con người, bảo vệ các giá trị chân – thiện – mỹ.",
         "Lịch sử trở nên lạnh lùng, phi nhân tính"],
    ], widths=[1.25, 3.55, 1.7], sp_after=6)
    s += [P("<font size=7.8 color='#6B6B6B'>Sách Kết nối tri thức nêu ba nguyên tắc <b>khách quan – trung thực – tiến bộ</b>, "
            "đồng thời yêu cầu việc nghiên cứu và trình bày lịch sử phải bảo đảm thêm "
            "<b>tính toàn diện và tính cụ thể</b>. Trong đề thi, bộ bốn nguyên tắc "
            "<b>khách quan – trung thực – nhân văn – tiến bộ</b> cũng rất thường xuất hiện, "
            "nên hãy nhớ cả bốn để không bị mất điểm.</font>", "small")]

    s += box("MẸO NHỚ 4 NGUYÊN TẮC: “K-T-N-T”", [
        "<b>K</b>hách quan – <b>T</b>rung thực – <b>N</b>hân văn – <b>T</b>iến bộ.",
        "Đọc thành câu: <i>“Khách Trung Nhân Tiến”</i> – một người khách trung thành với con người và sự tiến bộ.",
        "Nhớ thêm: <b>Khách quan là nguyên tắc QUAN TRỌNG NHẤT</b> – câu hỏi “nguyên tắc quan trọng nhất của Sử học là gì?” "
        "luôn có đáp án là <b>khách quan</b>.",
    ], "tip")

    # ---------------------------------------------------------- B2.7
    s += h3("B2.7. Ý nghĩa của việc nắm vững các nguyên tắc")
    s += numlist([
        "<b>Định hướng việc nghiên cứu</b> cho nhà sử học: bám sát mục tiêu, nhiệm vụ, phương pháp nghiên cứu.",
        "Giúp nhà sử học hiểu rõ <b>sứ mệnh, trách nhiệm, đạo đức</b> của người viết lịch sử.",
        "<b>Phê phán các quan điểm sai trái</b>, bảo vệ lẽ phải, ủng hộ quan điểm khoa học, tiến bộ và nhân văn.",
    ])

    s += box("TỰ KIỂM TRA NHANH BÀI 1 – TRẢ LỜI TRONG 60 GIÂY", [
        "1. Lịch sử được hiểu theo mấy nghĩa? → <b>2 nghĩa</b>: hiện thực lịch sử và lịch sử được con người nhận thức.",
        "2. Hiện thực lịch sử có thay đổi không? → <b>Không</b>, chỉ có một và bất biến.",
        "3. Sử học nghiên cứu cái gì? → <b>Toàn bộ quá khứ của loài người</b>.",
        "4. Sử học có mấy chức năng? → <b>2</b>: khoa học (nhận thức) và xã hội (giáo dục).",
        "5. Sử học có mấy nhiệm vụ? → <b>3</b>: nhận thức, giáo dục – nêu gương, dự báo.",
        "6. Nguyên tắc quan trọng nhất của Sử học? → <b>Khách quan</b>.",
    ], "ok")
    return s


def bai2():
    s = []
    s += h2("B3. Bài 2 – Tri thức lịch sử và cuộc sống", "B3")

    s += box("VỊ TRÍ CỦA BÀI TRONG ĐỀ", [
        "<b>7 câu trắc nghiệm nhiều lựa chọn</b> (I.7 → I.13) + <b>1 câu Đúng/Sai</b> (II.1, gồm 4 ý a–d) = <b>2,75 điểm</b>.",
        "Đây là bài <b>dễ mất điểm nhất</b> vì nội dung dạng “quy trình”, “thứ tự bước” – nếu không nhớ đúng thứ tự "
        "sẽ mất cả cụm câu.",
    ], "note")

    # ---------------------------------------------------------- B3.1
    s += h3("B3.1. Tri thức lịch sử là gì?")
    s += [P("<b>Tri thức lịch sử</b> là những hiểu biết, kiến thức của con người về lịch sử, "
            "được hình thành thông qua quá trình <b>học tập, khám phá, nghiên cứu và trải nghiệm</b>. "
            "Tri thức lịch sử không chỉ là “những con số, sự kiện đã xảy ra” mà còn là cách con người "
            "<b>hiểu, lí giải và vận dụng</b> quá khứ vào hiện tại.")]
    s += [P("Tri thức lịch sử được lưu giữ và truyền lại qua nhiều kênh: <b>sách, tư liệu, bảo tàng, di tích, "
            "phim ảnh, lễ hội, truyền miệng, gia đình, nhà trường</b>… Nhờ đó, mỗi thế hệ không phải "
            "“làm lại từ đầu” mà được thừa hưởng hiểu biết của các thế hệ trước.")]

    s += h4("Vai trò, ý nghĩa của tri thức lịch sử")
    s += tb([
        ["Phương diện", "Vai trò, ý nghĩa"],
        ["<b>Đối với cá nhân</b>",
         "– Hiểu được <b>cội nguồn</b>, bản sắc của bản thân, gia đình, dân tộc.<br/>"
         "– Hình thành <b>nhân cách</b>, lòng yêu nước, niềm tự hào dân tộc.<br/>"
         "– Rèn <b>tư duy phản biện</b>, khả năng đánh giá nguồn thông tin.<br/>"
         "– Là <b>hành trang</b> cho nghề nghiệp và cuộc sống."],
        ["<b>Đối với cộng đồng, quốc gia</b>",
         "– Giúp mỗi quốc gia, dân tộc <b>tự nhận thức chính mình</b>.<br/>"
         "– Góp phần <b>khám phá, tiếp cận</b> nhiều nền văn hoá, văn minh của nhân loại.<br/>"
         "– Là cơ sở để <b>giáo dục thế hệ trẻ</b>, giữ gìn và phát huy di sản.<br/>"
         "– Là nguồn lực cho <b>phát triển bền vững</b> (văn hoá, du lịch, giáo dục)."],
        ["<b>Đối với nhân loại</b>",
         "– Tạo nên <b>kí ức chung</b> của nhân loại, giúp các dân tộc hiểu và tôn trọng nhau.<br/>"
         "– Cung cấp <b>bài học kinh nghiệm</b> để tránh lặp lại sai lầm trong quá khứ."],
    ], widths=[1.3, 5.2], sp_after=8)

    # ---------------------------------------------------------- B3.2
    s += h3("B3.2. Vì sao phải học tập và khám phá lịch sử suốt đời?")
    s += [P("Đây là câu hỏi “Thông hiểu” được đặc tả rõ ràng và thường xuất hiện dưới dạng câu hỏi "
            "<b>“Vì sao phải học tập lịch sử suốt đời?”</b>. Có <b>bốn lí do</b> cốt lõi:")]
    s += numlist([
        "<b>Tri thức lịch sử là vô hạn, nhận thức lịch sử luôn thay đổi.</b> Sử liệu mới liên tục được phát hiện, "
        "nhận thức cũ có thể bị bổ sung hoặc điều chỉnh. Ngừng học là ngừng cập nhật.",
        "<b>Thực tiễn luôn vận động.</b> Mỗi thời đại đặt ra những câu hỏi mới với quá khứ; câu trả lời của hôm qua "
        "có thể không đủ cho hôm nay.",
        "<b>Phát triển năng lực và phẩm chất cá nhân.</b> Học lịch sử suốt đời rèn tư duy phản biện, kĩ năng "
        "xử lí thông tin, khả năng đánh giá sử liệu – những kĩ năng dùng được trong mọi nghề.",
        "<b>Đáp ứng yêu cầu của xã hội học tập và công dân toàn cầu.</b> Mỗi người phải tự học để thích ứng, "
        "đồng thời hiểu và tôn trọng sự đa dạng văn hoá của nhân loại.",
    ])
    s += box("MẸO NHỚ 4 LÍ DO: “VÔ – ĐỘNG – NĂNG – HỘI”", [
        "<b>VÔ</b>: tri thức <b>vô</b> hạn · <b>ĐỘNG</b>: thực tiễn luôn vận <b>động</b> · "
        "<b>NĂNG</b>: phát triển <b>năng</b> lực bản thân · <b>HỘI</b>: <b>hội</b> nhập, xã hội học tập.",
    ], "tip")

    # ---------------------------------------------------------- B3.3
    s += h3("B3.3. Quy trình thu thập và xử lí thông tin, sử liệu")
    s += [P("Đây là <b>phần “nóng” nhất</b> của Bài 2 trong đề kiểm tra: 4 câu dạng “bước thứ mấy”, "
            "“việc nào thuộc khâu nào”. Hãy học theo bảng hai cột dưới đây – chính là bảng trong SGK Kết nối tri thức.")]

    s += [caption("Bảng B.1 – Hai nhóm nhiệm vụ và các bước thực hiện")]
    s += tb([
        ["Nhiệm vụ", "Các bước thực hiện"],
        ["<b>1. Sưu tầm, thu thập sử liệu</b><br/><font size=7.6>“đi tìm nguyên liệu”</font>",
         "– <b>Tìm kiếm</b> nguồn tài liệu<br/>"
         "– <b>Phân loại</b> nguồn tài liệu<br/>"
         "– <b>Ghi chép lại</b> các thông tin về tài liệu"],
        ["<b>2. Xử lí thông tin sử liệu</b><br/><font size=7.6>“chế biến nguyên liệu”</font>",
         "– <b>Phân tích</b> tài liệu<br/>"
         "– <b>Đánh giá, thẩm định</b> tài liệu<br/>"
         "– <b>So sánh</b> các nguồn sử liệu đã thu thập được<br/>"
         "– <b>Tổng hợp</b> dữ liệu"],
    ], widths=[2.2, 4.3], sp_after=6)

    s += [P("Nhiều đề và sách tham khảo trình bày quy trình này thành <b>bốn bước</b> nối tiếp. "
            "Các em cần nhận ra cả hai cách diễn đạt, vì đề có thể hỏi theo bất kì cách nào:")]
    s += tb([
        ["Bước", "Tên bước", "Nội dung cốt lõi", "Từ khoá nhận diện"],
        ["<b>1</b>", "Lập thư mục, danh mục sử liệu cần thu thập",
         "Xác định vấn đề và lập danh mục các nguồn sử liệu cần tìm, phục vụ học tập, nghiên cứu",
         "“lập thư mục”, “danh mục”, “xác định vấn đề”"],
        ["<b>2</b>", "Sưu tầm, đọc và ghi chép thông tin sử liệu",
         "Tìm kiếm, thu thập tài liệu liên quan; đọc và ghi chép thông tin; ghi rõ nguồn gốc, xuất xứ",
         "“sưu tầm”, “đọc”, “ghi chép”"],
        ["<b>3</b>", "Chọn lọc, phân loại sử liệu",
         "Sắp xếp sử liệu theo nội dung, chủ đề, loại hình để thuận lợi cho việc xác minh, đánh giá",
         "“chọn lọc”, “phân loại”"],
        ["<b>4</b>", "Xác minh, đánh giá sử liệu",
         "Kiểm tra nguồn gốc, thời điểm ra đời, nội dung phản ánh; đánh giá độ tin cậy, tính xác thực, giá trị thông tin",
         "“xác minh”, “đánh giá”, “thẩm định”"],
    ], widths=[0.45, 1.9, 2.85, 1.45], align_center=[0], sp_after=6)

    s += box("MẸO NHỚ 4 BƯỚC: “MỤC – SƯU – LỌC – MINH”", [
        "<b>MỤC</b> (lập thư <b>mục</b>) → <b>SƯU</b> (<b>sưu</b> tầm, ghi chép) → "
        "<b>LỌC</b> (chọn <b>lọc</b>, phân loại) → <b>MINH</b> (xác <b>minh</b>, đánh giá).",
        "Câu chốt: <i>“Mục sưu lọc minh”</i> – nghe như “mục sưu lọc mình”, rất dễ nhớ.",
        "Phân biệt nhanh: <b>bước 1 và 2 là “đi tìm”</b> (thu thập), <b>bước 3 và 4 là “xử lí”</b> (phân tích, đánh giá).",
    ], "tip")

    s += h4("Phân biệt hai khái niệm dễ nhầm")
    s += compare("Sưu tầm, thu thập sử liệu", "Xử lí thông tin sử liệu", [
        ("Định nghĩa", "Là quá trình <b>lập danh mục</b> sử liệu cần sưu tầm; <b>tìm kiếm, thu thập</b> thông tin liên quan đến đối tượng tìm hiểu",
         "Là quá trình <b>phân loại, đánh giá, thẩm định, so sánh</b> nguồn sử liệu đã thu thập được"),
        ("Mục đích", "Có được <b>nguyên liệu</b> – càng nhiều, càng đa dạng càng tốt", "Xác định <b>tính xác thực, độ tin cậy và giá trị</b> của sử liệu"),
        ("Câu hỏi đặc trưng", "“Tìm ở đâu? Thu thập những gì? Ghi chép ra sao?”", "“Nguồn này có đáng tin không? Có mâu thuẫn với nguồn khác không?”"),
        ("Ví dụ", "Vào bảo tàng, thư viện, internet để tìm tư liệu về phố cổ Hội An", "Đối chiếu bản đồ cổ với ảnh chụp hiện nay để kiểm tra niên đại"),
    ], wl=1.4, wr=1.4, wc=0.9)

    # ---------------------------------------------------------- B3.4
    s += h3("B3.4. Các loại nguồn sử liệu cần biết")
    s += [P("Muốn “sưu tầm” và “xử lí” đúng, phải phân biệt được các loại sử liệu. Đây là kiến thức nền "
            "để trả lời các câu hỏi tình huống trong đề.")]
    s += tb([
        ["Tiêu chí", "Sử liệu sơ cấp", "Sử liệu thứ cấp"],
        ["Khái niệm", "Được tạo ra <b>đầu tiên, gần nhất</b> hoặc <b>gắn liền với thời gian xuất hiện</b> của sự kiện",
         "Được tạo ra <b>sau</b> thời điểm xuất hiện của sự vật, hiện tượng được nghiên cứu"],
        ["Dạng thường gặp", "Văn bản gốc, hiện vật, di tích, ảnh chụp tại chỗ, ghi âm lời kể của nhân chứng",
         "Công trình, tác phẩm, bài báo nghiên cứu, sách tham khảo, phim tài liệu tổng hợp"],
        ["Giá trị", "Được coi là <b>bằng chứng quan trọng nhất</b> khi miêu tả, phục dựng quá khứ",
         "Giúp <b>hiểu, lí giải, tổng hợp</b>; cần kiểm chứng lại bằng sơ cấp"],
    ], widths=[1.15, 2.75, 2.6], sp_after=6)

    s += [P("Theo <b>loại hình</b>, sử liệu được chia thành các nhóm sau – đề rất hay hỏi “đâu là sử liệu hiện vật / "
            "thành văn / truyền khẩu”:")]
    s += tb([
        ["Loại hình", "Đặc điểm", "Ví dụ"],
        ["<b>Thành văn</b>", "Sử liệu viết thành chữ", "Bia đá, sắc phong, văn bản, sách, báo"],
        ["<b>Hiện vật</b>", "Vật thể do con người tạo ra hoặc để lại", "Trống đồng, rìu đá, gốm, tiền cổ"],
        ["<b>Hình ảnh</b>", "Ghi lại hình ảnh sự kiện, con người", "Ảnh chụp, tranh vẽ, phim tài liệu"],
        ["<b>Lời nói – truyền khẩu</b>", "Truyền miệng từ đời này sang đời khác", "Truyền thuyết, ca dao, lời kể nhân chứng"],
        ["<b>Đa phương tiện</b>", "Sử liệu số, ghi âm, ghi hình", "Băng ghi âm, video số, cơ sở dữ liệu số hoá"],
    ], widths=[1.5, 2.5, 2.5], sp_after=8)

    # ---------------------------------------------------------- B3.5
    s += h3("B3.5. Kết nối tri thức, bài học lịch sử vào cuộc sống")
    s += [P("<b>Bản chất</b> của việc kết nối là biến tri thức lịch sử thành <b>năng lực và hành động</b> trong hiện tại: "
            "không chỉ “biết quá khứ đã diễn ra thế nào” mà còn “hiểu vì sao” và “vận dụng được gì”.")]
    s += tb([
        ["Cấp độ kết nối", "Biểu hiện cụ thể"],
        ["<b>1. Hiểu</b>", "Giải thích được các sự kiện, hiện tượng, vấn đề của hiện tại bằng bối cảnh lịch sử của nó"],
        ["<b>2. Vận dụng</b>",
         "– Giải thích những <b>vấn đề thời sự</b> trong nước và thế giới (ở mức độ đơn giản).<br/>"
         "– Rút ra <b>bài học kinh nghiệm</b> (giữ nước, ngoại giao, tổ chức cộng đồng, ứng xử với tự nhiên…)."],
        ["<b>3. Hành động</b>",
         "– Tham gia <b>bảo tồn di sản</b>, hoạt động văn hoá ở địa phương.<br/>"
         "– Tuyên truyền, vận động người khác cùng gìn giữ di sản.<br/>"
         "– Học tập suốt đời, chủ động tìm hiểu lịch sử, văn hoá dân tộc và thế giới."],
    ], widths=[1.4, 5.1], sp_after=6)

    s += box("LIÊN HỆ THỰC TIỄN – DẠNG CÂU HỎI “VẬN DỤNG”", [
        "Đề có thể yêu cầu: <i>“Bằng kiến thức đã học, em hãy giải thích vì sao giới trẻ ngày nay cần tìm hiểu lịch sử?”</i> "
        "hoặc <i>“Nêu một việc em có thể làm để góp phần bảo tồn di sản ở địa phương.”</i>",
        "Cách trả lời ăn điểm: nêu <b>1 lí do khái quát</b> → <b>1 ví dụ cụ thể</b> (có thể ở địa phương em) → "
        "<b>1 hành động cụ thể của bản thân</b>. Không lan man, không nói chung chung.",
    ], "warn")
    return s


def build():
    s = []
    s += h1("B", "CHỦ ĐỀ 1 – LỊCH SỬ VÀ SỬ HỌC", "B")
    s += [P("Chủ đề này gồm hai bài: <b>Bài 1</b> (Hiện thực lịch sử và lịch sử được con người nhận thức) và "
            "<b>Bài 2</b> (Tri thức lịch sử và cuộc sống). Đây là phần “nhập môn” của môn Lịch sử 10: "
            "nó dạy bạn <b>cách hiểu lịch sử, cách làm việc với sử liệu</b>, và cũng là nền để hiểu hai chủ đề còn lại. "
            "Trong đề giữa học kì 1, Chủ đề 1 chiếm <b>13 câu trắc nghiệm + 1 câu Đúng/Sai</b> (4,25 điểm).")]

    s += h2("B1. Toàn cảnh Chủ đề 1 – bản đồ kiến thức", "B1")
    s += [caption("Sơ đồ B.0 – Toàn cảnh Chủ đề 1")]
    s += mindmap("CHỦ ĐỀ 1: LỊCH SỬ VÀ SỬ HỌC", [
        ("BÀI 1<br/>“Hiểu lịch sử”", ["Lịch sử là gì",
                                      "Hiện thực lịch sử",
                                      "Nhận thức lịch sử",
                                      "Sử học: khái niệm, đối tượng",
                                      "Chức năng, nhiệm vụ, nguyên tắc"]),
        ("BÀI 2<br/>“Dùng lịch sử”", ["Tri thức lịch sử là gì",
                                      "Vai trò, ý nghĩa",
                                      "Học tập suốt đời",
                                      "Thu thập – xử lí sử liệu",
                                      "Kết nối vào cuộc sống"]),
    ], sub="Từ “hiểu đúng quá khứ” đến “vận dụng quá khứ vào hiện tại”")

    s += bai1()
    s += bai2()
    return s
