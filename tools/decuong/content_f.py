# -*- coding: utf-8 -*-
"""Phần F – Đề mẫu bám ma trận + đáp án."""
from style import *
from reportlab.platypus import PageBreak
from qbank import balance

EXAM = [
    ("1", "Lịch sử được hiểu là",
     ["những gì đã diễn ra trong quá khứ",
      "những gì sẽ diễn ra trong tương lai",
      "những câu chuyện hư cấu do con người tưởng tượng",
      "những dự báo của các nhà khoa học"]),
    ("2", "Hiện thực lịch sử tồn tại",
     ["phụ thuộc vào ý muốn của con người",
      "khách quan, không phụ thuộc vào ý muốn chủ quan của con người",
      "theo nhận thức của mỗi thời đại",
      "do nhà sử học tạo ra khi nghiên cứu"]),
    ("3", "Đặc điểm nào sau đây đúng với lịch sử được con người nhận thức?",
     ["Chỉ có một và không thể thay đổi",
      "Luôn đầy đủ và chính xác như hiện thực",
      "Đa dạng, có thể thay đổi và không bao giờ tái hiện đầy đủ hiện thực lịch sử",
      "Tồn tại hoàn toàn độc lập với con người"]),
    ("4", "Vì sao nhận thức về cùng một sự kiện lịch sử lại có thể khác nhau giữa các thời đại?",
     ["Vì hiện thực lịch sử bị thay đổi theo thời gian",
      "Vì mỗi thời đại có nguồn sử liệu, lập trường và nhu cầu nhận thức khác nhau",
      "Vì mọi nguồn sử liệu đều sai lệch",
      "Vì con người không có khả năng nhận thức quá khứ"]),
    ("5", "Đối tượng nghiên cứu của Sử học là",
     ["toàn bộ quá khứ của loài người",
      "các hiện tượng tự nhiên ngoài tác động của con người",
      "tương lai của nhân loại",
      "các tác phẩm văn học dân gian"]),
    ("6", "Nội dung nào sau đây là biểu hiện của <b>chức năng xã hội</b> của Sử học?",
     ["Xác định niên đại của một di vật khảo cổ",
      "Khôi phục diễn biến của một trận đánh",
      "Giáo dục lòng yêu nước và rút ra bài học kinh nghiệm cho hiện tại",
      "Phát hiện quy luật vận động của kinh tế"]),
    ("7", "Tri thức lịch sử được con người hình thành chủ yếu thông qua",
     ["quá trình học tập, khám phá, nghiên cứu và trải nghiệm",
      "trí nhớ bẩm sinh",
      "những giấc mơ về quá khứ",
      "những lời truyền miệng không kiểm chứng"]),
    ("8", "Bước thứ hai của quy trình thu thập, xử lí thông tin và sử liệu là",
     ["lập thư mục và danh mục các nguồn sử liệu",
      "sưu tầm, đọc và ghi chép thông tin sử liệu",
      "xác minh, đánh giá nguồn sử liệu",
      "tổng hợp dữ liệu để rút ra kết luận"]),
    ("9", "Sử liệu thành văn là",
     ["hiện vật khảo cổ được khai quật",
      "sử liệu được ghi lại bằng chữ viết",
      "lời kể truyền miệng của nhân chứng",
      "ảnh chụp hiện trường sự kiện"]),
    ("10", "Vì sao khi thu thập sử liệu cần phải kiểm chứng thông tin?",
     ["Vì sử liệu có thể sai lệch, cần xác định tính xác thực và độ tin cậy",
      "Vì muốn thu thập được nhiều thông tin hơn",
      "Vì yêu cầu bắt buộc của giáo viên",
      "Vì mọi sử liệu đều không đáng tin cậy"]),
    ("11", "Việc “phân tích tài liệu, đánh giá – thẩm định, so sánh và tổng hợp dữ liệu” thuộc khâu",
     ["sưu tầm, thu thập sử liệu",
      "xử lí thông tin sử liệu",
      "lập thư mục sử liệu",
      "phỏng vấn nhân chứng lịch sử"]),
    ("12", "Nhận định nào sau đây đúng về tri thức lịch sử?",
     ["Chỉ cần thiết đối với người làm nghề sử",
      "Giúp con người hiểu cội nguồn, hình thành nhân cách và năng lực ứng xử trong cuộc sống",
      "Chỉ là tập hợp những con số vô nghĩa",
      "Không có liên quan gì đến cuộc sống hiện tại"]),
    ("13", "Việc học tập và khám phá lịch sử suốt đời là cần thiết vì",
     ["tri thức lịch sử là vô hạn và nhận thức lịch sử luôn được bổ sung, điều chỉnh",
      "để đạt điểm cao ở trường phổ thông",
      "nhà nước bắt buộc mọi công dân phải học",
      "ai cũng yêu thích môn lịch sử"]),
    ("14", "Di sản nào sau đây của Việt Nam được UNESCO ghi danh là di sản văn hoá phi vật thể "
           "đại diện của nhân loại?",
     ["Dân ca Ví, Giặm Nghệ Tĩnh", "Chèo", "Cải lương", "Hát ru"]),
    ("15", "Di sản văn hoá vật thể bao gồm",
     ["lễ hội, dân ca, nghề thủ công truyền thống",
      "di tích lịch sử – văn hoá, danh lam thắng cảnh, di vật, cổ vật",
      "tri thức dân gian về y học cổ truyền",
      "các nghi lễ, phong tục của cộng đồng"]),
    ("16", "Công tác bảo tồn di sản văn hoá phi vật thể được thực hiện chủ yếu thông qua",
     ["sưu tầm, lưu giữ, truyền nghề, trình diễn",
      "xây dựng thêm nhà máy, xí nghiệp",
      "mở rộng đô thị và hạ tầng giao thông",
      "khai thác tối đa để thu vé tham quan"]),
    ("17", "Giá trị của một di sản được khẳng định chủ yếu nhờ",
     ["phương pháp nghiên cứu của Sử học",
      "các hoạt động quảng cáo trên truyền hình",
      "doanh thu từ du lịch",
      "số lượng khách tham quan hằng năm"]),
    ("18", "Nguồn tài nguyên quý báu của du lịch, đặc biệt là du lịch văn hoá, là",
     ["những giá trị lịch sử và văn hoá của mỗi dân tộc, của toàn nhân loại",
      "nguồn nhiên liệu hoá thạch",
      "trình độ công nghệ thông tin",
      "nguồn lao động giá rẻ"]),
    ("19", "Việc một phần doanh thu du lịch được tái đầu tư vào bảo tồn, tôn tạo di tích thể hiện",
     ["vai trò của du lịch đối với công tác bảo tồn",
      "vai trò của bảo tồn đối với sự phát triển du lịch",
      "tác động tiêu cực của du lịch đối với di sản",
      "sự xuống cấp không thể cứu vãn của di tích"]),
    ("20", "Biện pháp nào sau đây góp phần phát triển du lịch bền vững?",
     ["Tăng tối đa lượng khách để tối đa hoá doanh thu",
      "Kiểm soát sức chứa, gắn du lịch với bảo tồn và chia sẻ lợi ích cho cộng đồng",
      "Xây dựng nhiều khách sạn ngay trong khu vực di tích",
      "Cho phép mọi hoạt động khai thác nhằm thu hút đầu tư"]),
]
_ORIG_EXAM = EXAM
_RAW_ANS = ["A", "B", "C", "B", "A", "C", "A", "B", "B", "A",
            "B", "B", "A", "A", "B", "A", "A", "A", "A", "B"]

# Cân bằng đáp án A/B/C/D (5 câu mỗi loại) để không “đoán mò” theo thói quen
_balanced = balance([(stem, opts, ans) for (num, stem, opts), ans in zip(EXAM, _RAW_ANS)],
                    {"A": 5, "B": 5, "C": 5, "D": 5})
EXAM = [(num, b[0], b[1]) for num, b in zip([e[0] for e in _ORIG_EXAM], _balanced)]
EXAM_ANS = [b[2] for b in _balanced]


def build():
    s = []
    s += h1("F", "ĐỀ MẪU BÁM SÁT MA TRẬN VÀ ĐÁP ÁN", "F")
    s += [P("Đề dưới đây được dựng <b>đúng theo ma trận</b> ở Phần A: 20 câu trắc nghiệm nhiều lựa chọn "
            "(mã I.1 → I.20), 2 câu trắc nghiệm Đúng/Sai (mã II.1, II.2 – mỗi câu 4 ý), 1 câu tự luận gồm 2 vế. "
            "Đề <b>không trùng câu</b> với ngân hàng ở Phần E, nên có thể dùng làm bài kiểm tra thử.")]

    # ------------------------------------------------------------- header
    hdr = Table([[Paragraph("ĐỀ KIỂM TRA ĐỊNH KÌ GIỮA HỌC KÌ 1 – NĂM HỌC 2026 – 2027",
                            ParagraphStyle("eh1", fontName="Head-B", fontSize=12.5,
                                           leading=16, textColor=WHITE, alignment=TA_CENTER))],
                 [Paragraph("MÔN: LỊCH SỬ 10 – Bộ sách Kết nối tri thức với cuộc sống",
                            ParagraphStyle("eh2", fontName="Head", fontSize=8.8,
                                           leading=12, textColor=colors.HexColor("#D8E4F5"),
                                           alignment=TA_CENTER))],
                 [Paragraph("Thời gian làm bài: 45 phút  •  Không kể thời gian phát đề  •  "
                            "Đề gồm 2 trang, 20 câu TN + 2 câu Đ/S + 1 câu TL",
                            ParagraphStyle("eh3", fontName="Head", fontSize=8,
                                           leading=11, textColor=colors.HexColor("#D8E4F5"),
                                           alignment=TA_CENTER))]],
                colWidths=[CONTENT_W])
    hdr.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY),
                             ("TOPPADDING", (0, 0), (-1, -1), 6),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                             ("LINEBELOW", (0, -1), (-1, -1), 3, GOLD)]))
    s += [Spacer(1, 4), hdr, Spacer(1, 8)]

    # ------------------------------------------------------------- phần I
    s += [Paragraph("<b>PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (5,0 điểm)</b> – "
                    "<font size=8.4>Chọn một phương án đúng nhất trong mỗi câu (mỗi câu 0,25 điểm).</font>",
                    ParagraphStyle("pi", parent=S["body"], fontSize=9.6, leading=13,
                                   textColor=NAVY, spaceAfter=4))]
    for num, stem, opts in EXAM:
        s += [mcq(num, stem, opts)]

    # ------------------------------------------------------------- phần II
    s += [Spacer(1, 6)]
    s += [Paragraph("<b>PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2,0 điểm)</b> – "
                    "<font size=8.4>Mỗi câu gồm 4 ý. Xác định mỗi ý Đúng (Đ) hay Sai (S).</font>",
                    ParagraphStyle("pii", parent=S["body"], fontSize=9.6, leading=13,
                                   textColor=NAVY, spaceAfter=4))]
    s += [tf_item("1",
                  "<i>Đọc đoạn tư liệu sau:</i> “Sứ mệnh của Sử học là tái hiện lại hiện thực lịch sử, "
                  "đưa ra nhận thức đầy đủ nhất về quá khứ của con người dựa trên những thông tin đáng tin cậy. "
                  "Do đó, khách quan là nguyên tắc quan trọng nhất của Sử học.”",
                  ["Sử học có sứ mệnh tái hiện lại hiện thực lịch sử.",
                   "Khách quan là nguyên tắc quan trọng nhất của Sử học.",
                   "Nguyên tắc khách quan cho phép nhà sử học bỏ qua sử liệu nếu đã có kết luận trước đó.",
                   "Để tái hiện chính xác, nhà sử học cần trung thực và dựa trên những sử liệu đáng tin cậy."])]
    s += [tf_item("2",
                  "<i>Đọc đoạn tư liệu sau:</i> “Trong bối cảnh hội nhập và toàn cầu hoá, du lịch đóng vai trò "
                  "quan trọng trong phát triển kinh tế – xã hội. Giá trị văn hoá, lịch sử là tài nguyên quý báu "
                  "của du lịch, đặc biệt là du lịch văn hoá.”",
                  ["Du lịch chỉ dựa vào cảnh quan thiên nhiên, không liên quan đến lịch sử – văn hoá.",
                   "Di sản văn hoá là tài nguyên quan trọng cho sự phát triển du lịch.",
                   "Du lịch văn hoá không đóng góp gì cho sự phát triển kinh tế – xã hội.",
                   "Hội nhập và toàn cầu hoá làm tăng vai trò của du lịch trong phát triển."])]

    # ------------------------------------------------------------- phần III
    s += [Spacer(1, 6)]
    s += [Paragraph("<b>PHẦN III. TỰ LUẬN (3,0 điểm)</b>",
                    ParagraphStyle("piii", parent=S["body"], fontSize=9.6, leading=13,
                                   textColor=NAVY, spaceAfter=3))]
    s += box(None, [
        "<b>Câu 1 (1,0 điểm).</b> Trình bày vai trò của Sử học đối với công tác bảo tồn và phát huy giá trị "
        "di sản văn hoá, di sản thiên nhiên.",
        "<b>Câu 2 (2,0 điểm).</b> Từ thực tiễn địa phương, em hãy đề xuất các biện pháp bảo tồn và phát huy "
        "giá trị di sản văn hoá, di sản thiên nhiên. Liên hệ trách nhiệm của học sinh.",
    ], "note")

    # ------------------------------------------------------------- đáp án
    s += [PageBreak()]
    s += h2("F1. Đáp án – thang điểm chi tiết", "F1")

    s += h3("F1.1. Phần I – Trắc nghiệm nhiều lựa chọn (5,0 điểm)")
    pairs = [(str(i + 1), a) for i, a in enumerate(EXAM_ANS)]
    s += [answer_grid(pairs, per_row=10), Spacer(1, 6)]
    s += [P("Mỗi câu đúng được <b>0,25 điểm</b>. Tổng 20 câu = <b>5,0 điểm</b>.")]

    s += h3("F1.2. Phần II – Trắc nghiệm Đúng/Sai (2,0 điểm)")
    s += tb([
        ["Câu", "a", "b", "c", "d", "Căn cứ"],
        ["<b>II.1</b>", "<b>Đ</b>", "<b>Đ</b>", "<b>S</b>", "<b>Đ</b>",
         "Ý c sai: nguyên tắc khách quan <b>đòi hỏi dựa trên sử liệu</b>, không cho phép bỏ qua sử liệu."],
        ["<b>II.2</b>", "<b>S</b>", "<b>Đ</b>", "<b>S</b>", "<b>Đ</b>",
         "Ý a sai vì du lịch văn hoá dựa trên di sản; ý c sai vì du lịch văn hoá tạo việc làm, thu nhập."],
    ], widths=[0.55, 0.5, 0.5, 0.5, 0.5, 3.95], align_center=[0, 1, 2, 3, 4], sp_after=6)
    s += [P("<b>Cách chấm tham khảo:</b> mỗi câu 1,0 điểm, chia theo bậc: đúng <b>1 ý = 0,1</b>; "
            "<b>2 ý = 0,25</b>; <b>3 ý = 0,5</b>; <b>4 ý = 1,0</b>. "
            "Tổng 2 câu = <b>2,0 điểm</b>.")]

    s += h3("F1.3. Phần III – Tự luận (3,0 điểm)")
    s += [caption("Câu 1 (1,0 điểm) – Vai trò của Sử học với công tác bảo tồn và phát huy giá trị di sản")]
    s += tb([
        ["Ý", "Nội dung cần đạt", "Điểm"],
        ["1", "Sử học <b>xác định giá trị</b> của di sản (niên đại, nguồn gốc, giá trị lịch sử – văn hoá – "
              "kiến trúc – khoa học), nhờ đó di sản được nhìn nhận, đánh giá đúng.", "0,25"],
        ["2", "Kết quả nghiên cứu Sử học là <b>cơ sở khoa học vững chắc</b> cho công tác bảo tồn: "
              "tu bổ, tôn tạo, phục dựng đúng nguyên tắc giữ tối đa giá trị gốc.", "0,25"],
        ["3", "Sử học giúp <b>phân loại di sản</b> và <b>đề xuất phương án bảo tồn</b> phù hợp với từng loại hình: "
              "vật thể (chống xuống cấp), phi vật thể (sưu tầm, truyền dạy), thiên nhiên (bảo vệ đa dạng sinh học).", "0,25"],
        ["4", "Sử học cung cấp nội dung để <b>phát huy giá trị</b> di sản: trưng bày, thuyết minh, giáo dục, "
              "quảng bá, phát triển du lịch; góp phần phát triển kinh tế – xã hội địa phương.", "0,25"],
    ], widths=[0.35, 5.75, 0.6], align_center=[0, 2], sp_after=6)

    s += [caption("Câu 2 (2,0 điểm) – Đề xuất biện pháp bảo tồn, phát huy di sản và liên hệ bản thân")]
    s += tb([
        ["Ý", "Nội dung cần đạt", "Điểm"],
        ["1", "<b>Nêu thực trạng ngắn</b> về di sản ở địa phương (thuận lợi, khó khăn) – "
              "có thể dùng ví dụ Nghệ An: Dân ca Ví, Giặm, Khu di tích Kim Liên, Đền Cuông…", "0,25"],
        ["2", "<b>Nhóm giải pháp nhận thức – giáo dục:</b> tuyên truyền, đưa di sản vào nhà trường, "
              "tổ chức tham quan, trải nghiệm.", "0,25"],
        ["3", "<b>Nhóm giải pháp thể chế – pháp luật:</b> thực hiện Luật Di sản văn hoá, quy hoạch khoanh vùng, "
              "xử lí nghiêm vi phạm.", "0,25"],
        ["4", "<b>Nhóm giải pháp khoa học – kĩ thuật:</b> tu bổ giữ giá trị gốc; số hoá, bảo tàng ảo, công nghệ 3D.", "0,25"],
        ["5", "<b>Nhóm giải pháp kinh tế – du lịch:</b> du lịch bền vững, kiểm soát sức chứa, "
              "tái đầu tư doanh thu, gắn di sản với sinh kế.", "0,25"],
        ["6", "<b>Nhóm giải pháp cộng đồng:</b> trao quyền, chia sẻ lợi ích, tôn vinh nghệ nhân, "
              "khuyến khích người trẻ tham gia.", "0,25"],
        ["7", "<b>Liên hệ trách nhiệm học sinh:</b> tìm hiểu di sản quê hương; tham gia lễ hội, hoạt động tình nguyện; "
              "không xả rác, không khắc vẽ lên di tích; tuyên truyền cho bạn bè, gia đình; "
              "chia sẻ thông tin trung thực, có trách nhiệm.", "0,5"],
        ["", "<b>Tổng điểm câu 2</b>", "<b>2,0</b>"],
    ], widths=[0.35, 5.75, 0.6], align_center=[0, 2], sp_after=6)

    s += box("LƯU Ý KHI CHẤM VÀ KHI LÀM BÀI TỰ LUẬN", [
        "Giám khảo <b>linh hoạt</b>: học sinh có thể trình bày theo cách khác, miễn đủ ý và lập luận hợp lí vẫn cho điểm tối đa.",
        "Học sinh nên <b>viết thành đoạn văn</b>, không gạch đầu dòng thuần tuý; mỗi ý 2–3 câu, "
        "có dẫn chứng cụ thể.",
        "Tuyệt đối tránh: nêu lí thuyết chung chung mà <b>không có ví dụ</b>; hoặc chỉ kể tên di sản mà "
        "<b>không phân tích vai trò</b>.",
    ], "warn")

    # ------------------------------------------------------------- bảng quy đổi
    s += h3("F1.4. Bảng quy đổi điểm và mục tiêu phấn đấu")
    s += tb([
        ["Mức điểm", "Số câu TN đúng (ước tính)", "Đặc điểm", "Việc cần làm để nâng điểm"],
        ["<b>9 – 10</b>", "18 – 20/20 + Đ/S ≥ 7/8 ý + TL 2,5 – 3,0",
         "Nắm chắc toàn bộ, biết vận dụng", "Luyện thêm câu vận dụng cao, viết tự luận có dẫn chứng"],
        ["<b>7 – 8,5</b>", "15 – 17/20 + Đ/S 5 – 6/8 ý + TL 2,0 – 2,5",
         "Chắc kiến thức cơ bản, còn nhầm vài bẫy", "Ôn kĩ bảng D.1 (cặp dễ nhầm), luyện câu “KHÔNG đúng”"],
        ["<b>5 – 6,5</b>", "11 – 14/20 + Đ/S 3 – 4/8 ý + TL 1,5",
         "Nhớ định nghĩa nhưng chưa hiểu bản chất", "Học lại bảng so sánh và sơ đồ; làm lại 50 câu ở Phần E"],
        ["<b>Dưới 5</b>", "≤ 10/20", "Chưa nắm khái niệm gốc", "Quay lại mục B2, B3, C1 – C2; học mẹo nhớ ở mục D2"],
    ], widths=[0.9, 2.1, 1.75, 1.95], align_center=[0], sp_after=6)

    return s
