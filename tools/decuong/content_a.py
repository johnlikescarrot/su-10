# -*- coding: utf-8 -*-
"""Phần A – Phân tích đề và chiến lược ôn tập."""
from style import *
from reportlab.platypus import PageBreak


def build():
    s = []
    s += h1("A", "PHÂN TÍCH ĐỀ VÀ CHIẾN LƯỢC ÔN TẬP", "A")

    s += [P("Trước khi học thuộc bất cứ nội dung nào, việc đầu tiên là <b>hiểu rõ “luật chơi” của đề</b>. "
            "Phần này bóc tách toàn bộ thông tin trong <i>Ma trận kiểm tra định kì giữa học kì 1 – Khối 10, "
            "năm học 2026 – 2027</i> để bạn biết chính xác: học bài nào, học đến đâu, dạng câu nào chiếm bao nhiêu điểm "
            "và nên phân bổ thời gian ra sao. Học đúng trọng số sẽ tiết kiệm cho bạn rất nhiều thời gian.")]

    # ---------------------------------------------------------------- A1
    s += h2("A1. Cấu trúc đề kiểm tra", "A1")
    s += [P("Đề gồm <b>ba phần</b> với tổng cộng <b>28 lệnh hỏi trắc nghiệm và 01 câu tự luận</b>, "
            "thời gian làm bài <b>45 phút</b>, thang điểm <b>10</b>.")]
    s += tb([
        ["Phần", "Dạng câu hỏi", "Số lệnh hỏi", "Số điểm", "Cách tính điểm"],
        ["<b>I</b>", "Trắc nghiệm nhiều lựa chọn (A, B, C, D)", "20 câu", "5,0",
         "Mỗi câu đúng = 0,25 điểm"],
        ["<b>II</b>", "Trắc nghiệm Đúng / Sai", "2 câu, mỗi câu 4 ý → 8 ý", "2,0",
         "Chấm theo số ý đúng của từng câu"],
        ["<b>III</b>", "Tự luận", "1 câu gồm 2 vế", "3,0",
         "Vế 1 (Bài 3 – nhận biết) ≈ 1,0 đ; Vế 2 (Bài 3 – vận dụng) ≈ 2,0 đ"],
        ["", "<b>TỔNG</b>", "<b>28 lệnh hỏi + 1 TL</b>", "<b>10,0</b>", "<b>45 phút</b>"],
    ], widths=[0.55, 2.35, 1.5, 0.85, 2.75], align_center=[0, 2, 3], sp_after=8)

    s += box("ĐIỂM MẤU CHỐT CẦN NHỚ NGAY", [
        "<b>Trắc nghiệm chiếm 7/10 điểm</b> (5,0 + 2,0) → đây là “mỏ điểm” lớn nhất, quyết định bạn ở mức 7–8 điểm.",
        "<b>Tự luận 3 điểm nhưng chỉ nằm trong Bài 3</b> → Bài 3 là bài “đắt” nhất: 7 câu TN (I.14 – I.20) + 1 câu Đ/S (II.2) + cả câu tự luận = <b>5,75 điểm</b>.",
        "<b>Bài 1 và Bài 2 không có tự luận</b> nhưng chiếm tới <b>13 câu TN</b> → đừng học lệch.",
    ], "tip")

    # ---------------------------------------------------------------- A2
    s += h2("A2. Ma trận đề – phân bổ câu hỏi theo bài và cấp độ tư duy", "A2")
    s += [P("Bảng dưới đây tái hiện <b>ma trận kiểm tra</b> trong tệp gốc, được sắp xếp lại theo hàng dọc để dễ đọc. "
            "Ký hiệu: <b>I.x</b> = câu trắc nghiệm nhiều lựa chọn số x; <b>II.y</b> = câu Đúng/Sai số y; "
            "<b>TL</b> = tự luận. Các ô ghi <b>½ TL</b> nghĩa là một nửa câu tự luận được tính cho cấp độ đó.")]

    s += [caption("Bảng A.1 – Ma trận phân bổ lệnh hỏi (số câu) theo năng lực và cấp độ tư duy")]
    s += tb([
        ["Chủ đề / Bài", "NL1<br/>Biết", "NL1<br/>Hiểu", "NL2<br/>Biết", "NL2<br/>Hiểu",
         "NL3<br/>Biết", "NL3<br/>Vận dụng", "Điểm"],
        ["<b>Bài 1.</b> Hiện thực lịch sử và lịch sử được con người nhận thức",
         "I.1, 2, 3", "I.4", "—", "I.5, 6", "—", "—", "1,50"],
        ["<b>Bài 2.</b> Tri thức lịch sử và cuộc sống",
         "I.7, 8, 9", "I.10, 11", "I.12, 13<br/>II.1a", "II.1b", "II.1c", "II.1d", "2,75"],
        ["<b>Bài 3.</b> Vai trò của Sử học",
         "I.14, 15<br/>½ TL", "I.16", "I.17, 18<br/>II.2a", "I.19, 20<br/>II.2b",
         "II.2c", "II.2d<br/>½ TL", "5,75"],
        ["<b>Tổng số lệnh</b>", "8 + ½ TL", "4", "6", "6", "2", "2 + ½ TL", "<b>28 + 1 TL</b>"],
        ["<b>Tổng số điểm</b>", "3,0", "1,0", "1,5", "1,5", "0,5", "2,5", "<b>10,0</b>"],
        ["<b>Tỉ lệ</b>", "30%", "10%", "15%", "15%", "5%", "25%", "<b>100%</b>"],
    ], widths=[2.5, 0.75, 0.62, 0.75, 0.72, 0.65, 0.85, 0.6],
        align_center=[1, 2, 3, 4, 5, 6, 7], sp_after=4)

    s += [P("<font size=7.6 color='#6B6B6B'>Ghi chú kiểm chứng: bản gốc ghi dòng tỉ lệ ở hai bảng lần lượt là "
            "“0,5%” và “2,5%” ở vị trí NL3 – Biết / NL3 – Vận dụng. Đối chiếu với tổng điểm (0,5 điểm = 5% và "
            "2,5 điểm = 25%) cùng yêu cầu tổng bằng 100%, bảng trên đã chuẩn hoá thành 5% và 25%. "
            "Điểm từng bài được tính từ số lệnh hỏi tương ứng.</font>", "small")]

    s += [P("Nhìn vào bảng, có thể thấy ngay <b>ba quy luật phân bổ</b> rất đáng lưu ý:")]
    s += bullets([
        "<b>Bài 3 nặng nhất</b>: 7 câu TN + 1 câu Đ/S + cả câu tự luận = <b>5,75 điểm</b> – hơn một nửa số điểm của đề.",
        "<b>Câu hỏi “Biết” chiếm 8/28 lệnh hỏi TN</b> – tức gần 1/3 số câu chỉ cần học thuộc định nghĩa, khái niệm. Đây là phần “điểm cho không”, tuyệt đối không được mất.",
        "<b>Nhóm “Vận dụng” (NL3) chỉ có 4 lệnh nhưng chiếm tới 2,5 điểm</b> vì nằm ở câu Đ/S và câu tự luận – tức là phần phân loại học sinh. Muốn đạt 8–10 điểm, buộc phải luyện phần này.",
    ])

    # ---------------------------------------------------------------- A3
    s += h2("A3. Bảng đặc tả – yêu cầu cần đạt của từng bài", "A3")
    s += [P("Bảng đặc tả cho biết <b>mức độ yêu cầu cụ thể</b> của từng bài. Hãy dùng nó như danh sách "
            "“phải làm được những gì” để tự kiểm tra. Nếu một gạch đầu dòng nào bạn chưa nói lại được bằng lời của mình, "
            "hãy đánh dấu và quay lại phần kiến thức tương ứng ở các mục B, C.")]

    spec = [
        ("Bài 1 – Hiện thực lịch sử và lịch sử được con người nhận thức", [
            ("Nhận biết",
             ["Trình bày được khái niệm <b>lịch sử</b>, khái niệm <b>sử học</b>.",
              "Nêu được <b>đối tượng, chức năng và nhiệm vụ</b> của Sử học.",
              "Nhận diện được <b>hiện thực lịch sử</b> và <b>lịch sử được con người nhận thức</b> qua một sự kiện cụ thể.",
              "Chỉ ra được <b>đặc điểm</b> của lịch sử được con người nhận thức."]),
            ("Thông hiểu",
             ["Giải thích được khái niệm sử học.",
              "Phân biệt được hiện thực lịch sử và lịch sử được con người nhận thức qua một tình huống cụ thể."]),
        ]),
        ("Bài 2 – Tri thức lịch sử và cuộc sống", [
            ("Nhận biết",
             ["Nêu được <b>các bước</b> trong việc thu thập, xử lí thông tin và sử liệu.",
              "Biết cách <b>sưu tầm, thu thập, xử lí</b> thông tin, sử liệu để học tập, khám phá lịch sử."]),
            ("Thông hiểu",
             ["Giải thích được sự cần thiết phải <b>học tập và khám phá lịch sử suốt đời</b>.",
              "Hiểu được <b>bản chất của việc kết nối</b> tri thức, bài học lịch sử vào cuộc sống."]),
            ("Vận dụng",
             ["Vận dụng được kiến thức, bài học lịch sử để <b>giải thích những vấn đề thời sự</b> trong nước và thế giới, "
              "những vấn đề trong thực tiễn cuộc sống (ở mức độ đơn giản).",
              "Quan tâm, yêu thích và tham gia các hoạt động <b>tìm hiểu lịch sử, văn hoá</b> của dân tộc Việt Nam và thế giới."]),
        ]),
        ("Bài 3 – Vai trò của Sử học", [
            ("Nhận biết",
             ["Nêu được <b>mối quan hệ</b> giữa Sử học với công tác bảo tồn và phát huy giá trị di sản văn hoá, di sản thiên nhiên.",
              "Kể tên được một số <b>địa danh là tài nguyên du lịch</b> của nước ta.",
              "Kể tên được <b>các loại hình di sản văn hoá</b>."]),
            ("Thông hiểu",
             ["Hiểu rõ <b>vai trò của Sử học</b> với công tác bảo tồn và phát huy giá trị di sản văn hoá, di sản thiên nhiên.",
              "Giải thích được vai trò của <b>lịch sử – văn hoá đối với sự phát triển du lịch</b> qua một số tình huống cụ thể.",
              "<b>Phân tích tác động của du lịch</b> đối với công tác bảo tồn di tích lịch sử, di tích văn hoá."]),
            ("Vận dụng",
             ["<b>Đề xuất biện pháp</b> bảo tồn, phát huy các giá trị của di sản.",
              "Có ý thức <b>vận động mọi người</b> xung quanh cùng tham gia bảo vệ di sản văn hoá, di sản thiên nhiên ở nhiều địa phương."]),
        ]),
    ]
    for name, groups in spec:
        s += [Spacer(1, 3)]
        s += h3(name)
        rows = []
        for lvl, items in groups:
            cell = [Paragraph("• " + it, ParagraphStyle("sp", parent=S["cell"], fontSize=8.2,
                                                       leading=11.4, leftIndent=8,
                                                       bulletIndent=0)) for it in items]
            rows.append([Paragraph("<b>%s</b>" % lvl, S["cellc"]), cell])
        t = Table(rows, colWidths=[62, CONTENT_W - 62])
        st = [("GRID", (0, 0), (-1, -1), 0.4, BORDER),
              ("VALIGN", (0, 0), (-1, -1), "TOP"),
              ("BACKGROUND", (0, 0), (0, -1), BLUE_PALE),
              ("LEFTPADDING", (0, 0), (-1, -1), 5),
              ("RIGHTPADDING", (0, 0), (-1, -1), 5),
              ("TOPPADDING", (0, 0), (-1, -1), 4),
              ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
        t.setStyle(TableStyle(st))
        s += [t, Spacer(1, 5)]

    # ---------------------------------------------------------------- A4
    s += h2("A4. Nội dung nào học trước, nội dung nào học sau?", "A4")
    s += [P("Với 45 phút làm bài và cấu trúc như trên, thứ tự ưu tiên ôn tập tối ưu là:")]
    s += tb([
        ["Ưu tiên", "Nội dung", "Vì sao", "Thời lượng gợi ý"],
        ["<b>1</b>", "Ba bảng “khái niệm – đối tượng – chức năng – nhiệm vụ – nguyên tắc” của Bài 1",
         "Xuất hiện ở 6 câu TN (1,5 điểm), là nền để hiểu Bài 2 và Bài 3", "60 – 90 phút"],
        ["<b>2</b>", "Bài 3: quan hệ Sử học – di sản; tác động hai chiều Sử học ↔ du lịch",
         "Chiếm 5,75 điểm, có cả tự luận", "120 phút"],
        ["<b>3</b>", "Bài 2: quy trình 4 bước thu thập – xử lí sử liệu; học tập suốt đời",
         "4 câu TN + 1 câu Đ/S, dễ mất điểm vì dễ nhầm thứ tự", "90 phút"],
        ["<b>4</b>", "Luyện đề mẫu + chữa lỗi sai", "Chuyển kiến thức thành kĩ năng làm bài", "90 phút"],
        ["<b>5</b>", "Ôn lại mẹo nhớ, sơ đồ, checklist", "Chống quên trước giờ thi", "30 phút"],
    ], widths=[0.55, 2.6, 2.45, 1.0], align_center=[0, 3], sp_after=8)

    # ---------------------------------------------------------------- A5
    s += h2("A5. Chiến thuật phòng thi 45 phút", "A5")
    s += [P("Điểm số không chỉ phụ thuộc vào việc bạn thuộc bài, mà còn vào cách bạn phân bổ 45 phút. "
            "Dưới đây là cách chia thời gian đã được kiểm nghiệm với đúng cấu trúc đề này:")]
    s += tb([
        ["Chặng", "Thời gian", "Việc cần làm", "Mẹo"],
        ["<b>1</b>", "0 – 3 phút", "Đọc lướt toàn đề, đánh dấu câu dễ / câu khó",
         "Không sa đà vào câu khó đầu tiên"],
        ["<b>2</b>", "3 – 18 phút", "Làm 20 câu trắc nghiệm nhiều lựa chọn",
         "Câu nào quá 40 giây chưa ra đáp án thì bỏ qua, đánh dấu"],
        ["<b>3</b>", "18 – 27 phút", "Làm 2 câu Đúng/Sai (mỗi câu 4 ý)",
         "Đọc kỹ từng ý; mỗi ý chỉ cần xác định đúng/sai, không cần giải thích"],
        ["<b>4</b>", "27 – 40 phút", "Làm câu tự luận",
         "Mở bài 1 câu, thân bài gạch ý, kết bài 1 câu – viết theo dàn ý"],
        ["<b>5</b>", "40 – 45 phút", "Rà soát toàn bộ", "Kiểm tra phiếu trả lời, không bỏ trống câu nào"],
    ], widths=[0.55, 1.0, 2.55, 2.15], align_center=[0, 1], sp_after=6)

    s += box("NGUYÊN TẮC “3 KHÔNG” KHI LÀM BÀI TRẮC NGHIỆM", [
        "<b>Không bỏ trống</b>: câu nào cũng phải tô, kể cả khi phải đoán – xác suất đúng vẫn là 25%.",
        "<b>Không chọn theo cảm giác</b> khi gặp phương án “tất cả các đáp án trên”: hãy kiểm tra từng phương án một.",
        "<b>Không đổi đáp án</b> nếu không có căn cứ rõ ràng – lần đổi theo cảm tính thường làm mất điểm.",
    ], "warn")

    return s
