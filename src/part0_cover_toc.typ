#import "style.typ": *

// ============================================================================
// COVER PAGE + TABLE OF CONTENTS + SOURCE VERIFICATION NOTE
// ============================================================================

#page(header: none, footer: none, margin: (x: 1.8cm, y: 1.6cm))[
  // Top Hero Card
  #block(
    width: 100%,
    fill: gradient.linear(c-primary, rgb("#4A0E15"), angle: 18deg),
    radius: 12pt,
    inset: (x: 24pt, y: 24pt),
    stroke: 1.5pt + c-amber,
  )[
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      text(size: 8.8pt, weight: "bold", tracking: 1.4pt, fill: rgb("#FDE68A"))[
        CHƯƠNG TRÌNH GDPT 2018 • BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
      ],
      pill("NĂM HỌC 2026 – 2027", rgb("#FDE68A"), rgb("#451A03")),
    )
    #v(12pt)
    #text(size: 23pt, weight: "extrabold", fill: white)[
      ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I
    ]
    #v(4pt)
    #text(size: 18pt, weight: "bold", fill: rgb("#FDE68A"))[
      MÔN LỊCH SỬ LỚP 10 — TỐI ƯU HÓA TRÍ NHỚ & ĐIỂM SỐ
    ]
    #v(10pt)
    #line(length: 100%, stroke: 0.8pt + rgb("#FCA5A5"))
    #v(8pt)
    #text(size: 9.8pt, fill: rgb("#FEE2E2"))[
      Phân tích chuyên sâu từ tệp gốc *`LS10- MTGK1-26-27-HHT.docx`* (Trường THPT Hà Huy Tập) • Tích hợp Sơ đồ tư duy vector, Tờ tóm tắt 1 trang, 12 Khẩu quyết Siêu trí nhớ, Ngân hàng câu hỏi phân tầng & Bộ 03 Đề kiểm tra giữa kì chuẩn 100% Ma trận kèm Đáp án giải chi tiết.
    ]
  ]

  #v(12pt)

  // 4 Key Metric Cards
  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    column-gutter: 8pt,
    block(width: 100%, fill: c-navy-lt, stroke: 0.9pt + c-navy-bd, radius: 8pt, inset: 10pt)[
      #align(center)[
        #text(size: 16pt, weight: "extrabold", fill: c-navy)[45 phút] \
        #v(2pt)
        #text(size: 8.3pt, weight: "bold", fill: c-ink)[Cấu trúc chuẩn 10,0đ] \
        #text(size: 7.7pt, fill: c-muted)[20 TN + 2 Đ/S + 1 TL]
      ]
    ],
    block(width: 100%, fill: c-teal-lt, stroke: 0.9pt + c-teal-bd, radius: 8pt, inset: 10pt)[
      #align(center)[
        #text(size: 16pt, weight: "extrabold", fill: c-teal)[03 Bài] \
        #v(2pt)
        #text(size: 8.3pt, weight: "bold", fill: c-ink)[Chủ đề 1 & Chủ đề 2] \
        #text(size: 7.7pt, fill: c-muted)[Bài 3 chiếm 57,5% điểm!]
      ]
    ],
    block(width: 100%, fill: c-amber-lt, stroke: 0.9pt + c-amber-bd, radius: 8pt, inset: 10pt)[
      #align(center)[
        #text(size: 16pt, weight: "extrabold", fill: c-amber)[12 Mẹo] \
        #v(2pt)
        #text(size: 8.3pt, weight: "bold", fill: c-ink)[Khẩu quyết & 6 Sơ đồ] \
        #text(size: 7.7pt, fill: c-muted)[Mã hóa kép – Nhớ 3 giây]
      ]
    ],
    block(width: 100%, fill: c-primary-lt, stroke: 0.9pt + c-primary-bd, radius: 8pt, inset: 10pt)[
      #align(center)[
        #text(size: 16pt, weight: "extrabold", fill: c-primary)[160 Lệnh] \
        #v(2pt)
        #text(size: 8.3pt, weight: "bold", fill: c-ink)[Ngân hàng & 03 Đề thi] \
        #text(size: 7.7pt, fill: c-muted)[100% có đáp án & rubric]
      ]
    ],
  )

  #v(10pt)

  // Visual Weight Chart right on Cover!
  #image("assets/matrix_weight_chart.svg", width: 100%)

  #v(8pt)

  // Method & Source Box
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 10pt,
    info-box("PHƯƠNG PHÁP GHI NHỚ TỐI ƯU TRONG TÀI LIỆU", accent: c-teal, bg: c-teal-lt, bd: c-teal-bd)[
      - *Mã hóa kép (Dual-Coding):* Kết hợp từ khóa màu sắc và 06 sơ đồ tư duy vector trực quan.
      - *Khẩu quyết chữ cái đầu (Acronyms):* Nén kiến thức dài thành công thức ngắn (`1–K–B`, `2 Chức – 3 Nhiệm`, `L–S–C–X`, `K–V–A–T`, `3G`, `4T`).
      - *Chống bẫy phản xạ:* Chỉ rõ các từ tuyệt đối hóa hay gài ở Phần I và Phần II Đúng/Sai.
      - *Truy hồi chủ động (Active Recall):* Thẻ hỏi nhanh cuối mỗi bài + thực chiến 03 đề 45 phút.
    ],
    info-box("THÔNG BÁO MINH BẠCH VỀ NGUỒN DỮ LIỆU GỐC", accent: c-navy, bg: c-navy-lt, bd: c-navy-bd)[
      Tệp gốc *`LS10- MTGK1-26-27-HHT.docx`* cung cấp chính thức *Ma trận & Bảng đặc tả đề kiểm tra định kì giữa HK1* (gồm đủ tọa độ `I.1→I.20`, `II.1a–d`, `II.2a–d` và `TL 2 vế`), không đính kèm văn bản đề thi có sẵn. Đề cương này ánh xạ *100% từng ô lệnh hỏi* của ma trận thành Ngân hàng câu hỏi chuyên sâu và *03 Đề kiểm tra hoàn chỉnh* kèm đáp án, giải thích và thang điểm chi tiết.
    ],
  )

  #v(1fr)
  #align(center)[
    #line(length: 60%, stroke: 0.5pt + c-border)
    #v(4pt)
    #text(size: 8.3pt, fill: c-muted)[
      Tài liệu học tập chuẩn hóa theo SGK *Lịch sử 10 – Kết nối tri thức với cuộc sống* (Bản chỉnh lí bắt buộc hiện hành) • Cập nhật danh mục Di sản UNESCO Việt Nam đến năm 2026
    ]
  ]
]

// Table of Contents Page
#sec-heading("MỤC LỤC TRA CỨU NHANH TOÀN TÀI LIỆU", badge: pill("Định vị thông minh", c-navy-lt, c-navy, bd: c-navy-bd), outlined-sec: false)

#block(
  width: 100%,
  fill: c-warm-bg,
  stroke: 0.7pt + rgb("#D6CFC7"),
  radius: 7pt,
  inset: (x: 14pt, y: 10pt),
)[
  #set text(size: 9.2pt)
  #outline(
    title: none,
    depth: 2,
    indent: 14pt,
  )
]

#v(8pt)
#memory-box("HƯỚNG DẪN SỬ DỤNG ĐỀ CƯƠNG THEO QUỸ THỜI GIAN CỦA BẠN")[
  - *Nếu chỉ còn 30 phút trước giờ kiểm tra:* Mở ngay *Phần II (Tờ Tóm Tắt Vàng 1 Trang & 12 Khẩu Quyết)* + đọc kỹ *Khung công thức 4T làm câu Tự luận 3,0 điểm* ở cuối Bài 3 + lướt *Bảng 10 Cặp Khái Niệm Dễ Nhầm*.
  - *Nếu còn 2 – 3 buổi tối:* Học kỹ *Bài 3 trước tiên* (vì riêng Bài 3 chiếm *5,75/10 điểm* = 57,5% toàn đề!), sau đó học *Bài 2* (2,75 điểm) và *Bài 1* (1,50 điểm), rồi bấm giờ làm *Đề kiểm tra số 01 & số 02* ở Phần V.
  - *Nếu ôn bài bản 7 ngày lấy điểm 9,5 – 10:* Theo sát *Lộ trình Lặp lại ngắt quãng 7 ngày* ở cuối Phần I, hoàn thành toàn bộ Ngân hàng câu hỏi Phần IV và cả *03 Đề kiểm tra thực chiến* Phần V.
]

#pagebreak()
