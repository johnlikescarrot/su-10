#import "style.typ": *

// ============================================================================
// PART I: FORENSIC MATRIX ANALYSIS & 45-MINUTE EXAM STRATEGY
// ============================================================================

#part-banner(
  "Phần I • Giải mã cấu trúc đề kiểm tra",
  "PHÂN TÍCH MA TRẬN, ĐẶC TẢ & CHIẾN THUẬT CHINH PHỤC ĐIỂM 10",
  "Bóc tách chính xác từng ô câu hỏi trong tệp LS10- MTGK1-26-27-HHT.docx và thiết lập lộ trình ôn tập tối ưu",
)

#sec-heading("1.1. Bảng Ma trận đề kiểm tra giữa học kì I (Đã chuẩn hóa từ tệp gốc)", badge: pill("45 phút • 10,0 điểm", c-primary-lt, c-primary, bd: c-primary-bd))

Dưới đây là bảng ma trận đã được đối chiếu chéo giữa *Bảng Ma trận* và *Bảng Đặc tả* trong tệp gốc `LS10- MTGK1-26-27-HHT.docx`, bổ sung cột quy đổi điểm thành phần của từng bài học để học sinh nhìn rõ trọng tâm ôn tập:

#block(breakable: false, above: 6pt, below: 8pt)[
  #set text(size: 8.1pt)
  #table(
    columns: (1.05fr, 1.55fr, 0.72fr, 0.55fr, 0.68fr, 0.68fr, 0.52fr, 0.75fr, 0.85fr),
    align: (left + horizon, left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 4.5pt, y: 5pt),
    fill: (_, row) => if row == 0 or row == 1 { c-navy } else if row >= 5 { c-warm-bg } else if calc.odd(row) { c-subtle } else { white },

    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Chủ đề]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Đơn vị kiến thức (SGK KNTT)]],
    table.cell(colspan: 2)[#text(fill: white, weight: "bold")[NL1: Tìm hiểu LS]],
    table.cell(colspan: 2)[#text(fill: white, weight: "bold")[NL2: Nhận thức & TD]],
    table.cell(colspan: 2)[#text(fill: white, weight: "bold")[NL3: Vận dụng KT]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Tổng điểm bài]],

    [#text(fill: rgb("#FDE68A"), weight: "bold")[Biết]],
    [#text(fill: rgb("#FDE68A"), weight: "bold")[Hiểu]],
    [#text(fill: rgb("#FDE68A"), weight: "bold")[Biết]],
    [#text(fill: rgb("#FDE68A"), weight: "bold")[Hiểu]],
    [#text(fill: rgb("#FDE68A"), weight: "bold")[Biết]],
    [#text(fill: rgb("#FDE68A"), weight: "bold")[Vận dụng]],

    table.cell(rowspan: 2)[*Chủ đề 1.* Lịch sử và Sử học *(4,25đ)*],
    [*Bài 1.* Hiện thực lịch sử và lịch sử được con người nhận thức],
    [`I.1, 2, 3`], [`I.4`], [—], [`I.5, 6`], [—], [—],
    [*1,50 điểm* \ *(15,0%)*],

    [*Bài 2.* Tri thức lịch sử và cuộc sống],
    [`I.7, 8, 9`], [`I.10, 11`], [`I.12, 13` \ `II.1a`], [`II.1b`], [`II.1c`], [`II.1d`],
    [*2,75 điểm* \ *(27,5%)*],

    [*Chủ đề 2.* Vai trò của Sử học *(5,75đ)*],
    [*Bài 3.* Vai trò của Sử học ★],
    [`I.14, 15` \ `1/2 TL`], [`I.16`], [`I.17, 18` \ `II.2a`], [`I.19, 20` \ `II.2b`], [`II.2c`], [`II.2d` \ `1/2 TL`],
    [#text(fill: c-primary, weight: "extrabold")[5,75 điểm] \ *#text(fill: c-primary)[(57,5%)]*],

    table.cell(colspan: 2)[*Tổng số lệnh hỏi* *(Các cột NL1-VD, NL2-VD, NL3-Hiểu = 0)*],
    [*8 + 1/2 TL*], [*4*], [*6*], [*6*], [*2*], [*2 + 1/2 TL*],
    [*28 lệnh TN* \ *+ 1 câu TL*],

    table.cell(colspan: 2)[*Tổng số điểm từng cột năng lực*],
    [*3,0đ*], [*1,0đ*], [*1,5đ*], [*1,5đ*], [*0,5đ*], [*2,5đ*],
    [*10,0 điểm*],

    table.cell(colspan: 2)[*Tỷ lệ phần trăm chuẩn hóa*],
    [*30%*], [*10%*], [*15%*], [*15%*], [*5%*], [*25%*],
    [*100%*],
  )
]

#info-box("PHÁT HIỆN & CHUẨN HÓA 04 ĐIỂM SAI SỐ ĐÁNH MÁY TRONG TỆP .DOCX GỐC")[
  Khi đối chiếu từng ô giữa *Bảng 1 (Ma trận)* và *Bảng 2 (Bảng đặc tả)* trong tệp `LS10- MTGK1-26-27-HHT.docx`, có *04 lỗi gõ máy nhỏ* đã được chuẩn hóa ở bảng trên để đảm bảo tính chính xác toán học tuyệt đối:
  1. *Hàng Tỷ lệ %, cột `NL3 – Biết` (Bảng 1):* Tệp gốc ghi `0,5%` (nhầm từ `0,5 điểm`); giá trị đúng là *`5%`* (đã được sửa đúng ở Bảng 2).
  2. *Hàng Tỷ lệ %, cột `NL3 – Vận dụng` (Bảng 2):* Tệp gốc gõ nhầm `2,5%` (nhầm từ `2,5 điểm`); giá trị đúng là *`25%`* (như đã ghi đúng ở Bảng 1).
  3. *Ô Tổng số lệnh cuối hàng (Bảng 2, cột Tổng):* Tệp gốc lặp lại `2+1/2 TL` do sao chép ô liền trước; giá trị đúng là *`28 lệnh hỏi TN + 1 TL`*.
  4. *Ký hiệu câu hỏi & tiêu đề phụ:* Ký hiệu `I. 5.6` ở Bảng 1 chuẩn hóa thành `I.5, 6` như Bảng 2; hai cột trống nhãn đầu Bảng 2 tương ứng là *Đơn vị kiến thức* và *Yêu cầu cần đạt theo mức độ đánh giá*.
]

#sec-heading("1.2. Giải mã quy tắc tính điểm & 03 phát hiện chiến lược quyết định điểm 9 – 10")

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  trap-box("CẢNH BÁO QUY TẮC ĐIỂM LŨY TIẾN PHẦN II (ĐÚNG/SAI)")[
    Trong ma trận thiết kế, 8 ý Đúng/Sai (`II.1a–d`, `II.2a–d`) có trọng số trung bình `0,25đ/ý` (`1,0đ/câu`). Tuy nhiên, theo quy chế chấm thi định kì THPT hiện hành của Bộ GD&ĐT cho mỗi câu Đúng/Sai (`1,0 điểm`):
    - Chỉ đúng *1/4 ý*: đạt *0,10 điểm*
    - Đúng *2/4 ý*: đạt *0,25 điểm*
    - Đúng *3/4 ý*: đạt *0,50 điểm*
    - Đúng trọn vẹn *4/4 ý*: đạt *1,00 điểm*!
    *Hệ quả sống còn:* Sai 1 ý duy nhất ở câu Đúng/Sai làm bạn mất ngay *0,50 điểm* (bằng 2 câu Phần I cộng lại)!
  ],
  memory-box("03 PHÁT HIỆN VÀNG TỪ MA TRẬN HHT")[
    1. *Bài 3 là “Mỏ vàng 5,75 điểm”:* Một mình *Bài 3 (Vai trò của Sử học)* chiếm *57,5%* toàn đề, ôm trọn câu Tự luận *3,0 điểm* + câu Đúng/Sai số 2 (*1,0đ*) + 7 câu Phần I (*1,75đ*).
    2. *Bài 1 chỉ thi nhẹ ở 6 câu đầu Phần I (1,50đ):* Không có Vận dụng, không có Đúng/Sai, không có Tự luận — chỉ cần nắm chắc khái niệm và phân biệt *Hiện thực vs Nhận thức*.
    3. *Câu Tự luận 3,0đ chia 2 vế rõ rệt:* *Ý 1 (1,0đ – NL1 Biết)* chép chuẩn kiến thức SGK Bài 3; *Ý 2 (2,0đ – NL3 Vận dụng)* đề xuất giải pháp bảo tồn & liên hệ trách nhiệm học sinh.
  ],
)

#sec-heading("1.3. Bảng ánh xạ 1-đối-1 toàn bộ 28 lệnh hỏi TN + 1 câu TL trong đề kiểm tra")

Mỗi câu hỏi trong bài kiểm tra giữa kì đều có vị trí cố định theo Bảng đặc tả. Khi ôn luyện theo bảng ánh xạ này, học sinh biết chính xác câu số mấy sẽ hỏi đơn vị kiến thức nào:

#block(above: 5pt, below: 8pt)[
  #set text(size: 8.2pt)
  #table(
    columns: (0.9fr, 0.85fr, 0.85fr, 2.6fr),
    align: (center + horizon, center + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 5pt, y: 4.3pt),
    fill: (_, row) => if row == 0 { c-primary } else if calc.odd(row) { c-subtle } else { white },

    [#text(fill: white, weight: "bold")[Vị trí câu]],
    [#text(fill: white, weight: "bold")[Năng lực / Cấp độ]],
    [#text(fill: white, weight: "bold")[Bài học SGK]],
    [#text(fill: white, weight: "bold")[Yêu cầu cần đạt cụ thể sẽ hỏi trong bài kiểm tra]],

    [`I.1 → I.3` \ *(0,75 điểm)*], [#nl1 #nb], [Bài 1],
    [Trình bày khái niệm lịch sử, Sử học; nêu đối tượng, chức năng (khoa học, xã hội), nhiệm vụ (nhận thức, giáo dục, dự báo) của Sử học; chỉ ra đặc điểm nhận thức lịch sử.],

    [`I.4` \ *(0,25 điểm)*], [#nl1 #th], [Bài 1],
    [Giải thích khái niệm Sử học, tính toàn diện của đối tượng nghiên cứu và vai trò khôi phục quá khứ.],

    [`I.5 → I.6` \ *(0,50 điểm)*], [#nl2 #th], [Bài 1],
    [Phân biệt *hiện thực lịch sử* và *lịch sử được con người nhận thức* qua tình huống/sự kiện cụ thể; lí giải nguyên nhân có nhận thức khác nhau.],

    [`I.7 → I.9` \ *(0,75 điểm)*], [#nl1 #nb], [Bài 2],
    [Khái niệm sử liệu, các loại hình sử liệu; nêu đúng các bước sưu tầm, thu thập và xử lí thông tin, sử liệu (`Lập danh mục → Sưu tầm → Chọn lọc → Xác minh`).],

    [`I.10 → I.11` \ *(0,50 điểm)*], [#nl1 #th], [Bài 2],
    [Giải thích cách sưu tầm, xử lí sử liệu trong học tập; giải thích *4 lí do* cần học tập và khám phá lịch sử suốt đời.],

    [`I.12 → I.13` \ *(0,50 điểm)*], [#nl2 #nb], [Bài 2],
    [Nhận diện vai trò tri thức lịch sử, các hình thức học tập lịch sử và biểu hiện kết nối tri thức lịch sử với cuộc sống.],

    [`I.14 → I.15` \ *(0,50 điểm)*], [#nl1 #nb], [Bài 3],
    [Nêu mối quan hệ giữa Sử học với bảo tồn di sản; kể tên các loại hình di sản văn hóa (vật thể, phi vật thể) và di sản thiên nhiên.],

    [`I.16` \ *(0,25 điểm)*], [#nl1 #th], [Bài 3],
    [Hiểu rõ vai trò của Sử học (cơ sở khoa học, giữ yếu tố gốc) và vai trò công tác bảo tồn đối với từng loại hình di sản.],

    [`I.17 → I.18` \ *(0,50 điểm)*], [#nl2 #nb], [Bài 3],
    [Kể tên/nhận diện địa danh là tài nguyên du lịch của Việt Nam (UNESCO, di tích quốc gia đặc biệt); nhận diện vai trò cơ bản của du lịch – di sản.],

    [`I.19 → I.20` \ *(0,50 điểm)*], [#nl2 #th], [Bài 3],
    [Giải thích vai trò của lịch sử – văn hóa đối với sự phát triển du lịch và phân tích tác động hai chiều của du lịch đối với bảo tồn di tích qua tình huống cụ thể.],

    [`Câu II.1` \ (`a, b, c, d`) \ *(1,00 điểm)*], [#nl2 #nb/#th \ #nl3 #nb/#vd], [Bài 2],
    [*Tư liệu Bài 2:* `a)` Nhận biết thông tin tư liệu (#nl2 #nb); `b)` Giải thích học tập suốt đời / bản chất kết nối lịch sử với cuộc sống (#nl2 #th); `c)` Hoạt động tìm hiểu lịch sử – văn hóa (#nl3 #nb); `d)` Vận dụng bài học lịch sử giải thích vấn đề thời sự thực tiễn (#nl3 #vd).],

    [`Câu II.2` \ (`a, b, c, d`) \ *(1,00 điểm)*], [#nl2 #nb/#th \ #nl3 #nb/#vd], [Bài 3],
    [*Tư liệu Bài 3:* `a)` Nhận biết di sản / địa danh du lịch (#nl2 #nb); `b)` Phân tích vai trò Sử học – du lịch – di sản (#nl2 #th); `c)` Hành động tham gia bảo vệ di sản địa phương (#nl3 #nb); `d)` Đề xuất/đánh giá giải pháp bảo tồn bền vững hài hòa kinh tế – văn hóa (#nl3 #vd).],

    [`Câu III.1` \ (`Ý 1 + Ý 2`) \ *(3,00 điểm)*], [#nl1 #nb *(1,0đ)* \ #nl3 #vd *(2,0đ)*], [Bài 3],
    [*Tự luận 2 vế:* *Ý 1 (1,0đ):* Nêu mối quan hệ Sử học – bảo tồn di sản / các loại hình di sản / địa danh du lịch tiêu biểu. *Ý 2 (2,0đ):* Đề xuất biện pháp bảo tồn, phát huy giá trị di sản cụ thể & ý thức vận động cộng đồng bảo vệ di sản ở địa phương.],
  )
]

#sec-heading("1.4. Chiến thuật phân bổ 45 phút & Lộ trình ôn tập 7 ngày (Spaced Repetition)")

#image("assets/timeline_45min_strategy.svg", width: 100%)

#v(4pt)
#block(breakable: false)[
  #set text(size: 8.4pt)
  #table(
    columns: (0.85fr, 1.45fr, 2.3fr),
    align: (center + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 6pt, y: 4.5pt),
    fill: (_, row) => if row == 0 { c-teal } else if calc.odd(row) { c-teal-lt } else { white },

    [#text(fill: white, weight: "bold")[Ngày ôn]],
    [#text(fill: white, weight: "bold")[Trọng tâm kiến thức]],
    [#text(fill: white, weight: "bold")[Hoạt động Truy hồi chủ động (Active Recall — 35 phút/ngày)]],

    [*Ngày 1*], [Bài 3 – Mục 1 *(Bảo tồn di sản)*],
    [Thuộc khẩu quyết `3G (Gốc – Xác thực – Toàn vẹn)` + phân loại 9 Di sản UNESCO VN; làm câu 41–50 Ngân hàng TN.],

    [*Ngày 2*], [Bài 3 – Mục 2 *(Du lịch & Tự luận)*],
    [Vẽ lại mũi tên 2 chiều *Di sản ↔ Du lịch*; thuộc lòng *Công thức 4T* và viết tay nháp 2 bài Tự luận mẫu (ăn chắc 5,75đ!).],

    [*Ngày 3*], [Bài 2 *(Sử liệu & Học suốt đời)*],
    [Thuộc khẩu quyết `L–S–C–X` (4 bước sử liệu), `K–V–A–T` (4 nguồn sử liệu), `V–B–H–N` (4 lí do học suốt đời); làm câu 21–40 TN + 3 câu Đ/S Bài 2.],

    [*Ngày 4*], [Bài 1 *(Hiện thực & Nhận thức)*],
    [Thuộc khẩu quyết `1–K–B` vs `N–K/C–Đ` và `2 Chức – 3 Nhiệm`; làm câu 1–20 TN Bài 1 (khóa sổ trọn vẹn 3 bài!).],

    [*Ngày 5*], [Thực chiến *Đề số 01* (45 phút)],
    [Bấm đồng hồ đúng 45 phút không mở tài liệu; tự chấm theo rubric 0,25đ, ghi lại các câu sai vào sổ tay chống bẫy.],

    [*Ngày 6*], [Thực chiến *Đề số 02 & 03*],
    [Làm tiếp Đề số 02 & 03; rà kỹ các mệnh đề Đúng/Sai chứa từ khóa giới hạn (*chỉ, mọi, duy nhất, hoàn toàn, thay thế*).],

    [*Ngày 7*], [Tổng duyệt Siêu tốc 20 phút],
    [Đọc lại duy nhất *Phần II (Tờ Tóm Tắt Vàng 1 Trang & 12 Khẩu Quyết)* + ngủ sớm để não bộ củng cố trí nhớ dài hạn.],
  )
]

#pagebreak()
