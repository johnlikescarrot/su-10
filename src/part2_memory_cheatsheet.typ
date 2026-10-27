#import "style.typ": *

// ============================================================================
// PART II: 1-PAGE GOLDEN CHEAT SHEET + 12 MEMORY HOOKS & CONFUSION PAIRS
// ============================================================================

#part-banner(
  "Phần II • Tối ưu hóa trí nhớ siêu tốc (In 2 mặt làm tờ cầm tay)",
  "TỜ TÓM TẮT VÀNG 1 TRANG & 12 KHẨU QUYẾT SIÊU TRÍ NHỚ",
  "Nén trọn 100% cốt lõi Bài 1 – Bài 2 – Bài 3 thành từ khóa phản xạ 3 giây để không bao giờ quên trong phòng thi",
)

#sec-heading("2.1. Bản đồ cốt lõi 03 bài học gói gọn trên 1 mặt trang (Ôn lướt 5 phút)", badge: pill("Cheat-Sheet Vàng", c-amber-lt, c-amber, bd: c-amber-bd))

#grid(
  columns: (1fr, 1fr),
  column-gutter: 8pt,
  row-gutter: 7pt,

  // Card 1: Bai 1
  block(width: 100%, fill: c-navy-lt, stroke: 0.9pt + c-navy-bd, radius: 6pt, inset: 8.5pt)[
    #text(size: 9.6pt, weight: "extrabold", fill: c-navy)[BÀI 1. HIỆN THỰC LS & NHẬN THỨC LS (1,50đ)]
    #v(3pt)
    #set text(size: 8.3pt)
    - *Lịch sử:* Những gì *đã diễn ra trong quá khứ*. Lịch sử loài người = toàn bộ hoạt động con người từ khi xuất hiện đến nay.
    - *Hiện thực lịch sử (`1–K–B`):* Tất cả những gì đã diễn ra; *chỉ có 1 (duy nhất)*, tồn tại *khách quan*, *bất biến* (không đổi).
    - *Nhận thức lịch sử (`N–K/C–Đ`):* *Hiểu biết* của con người về hiện thực LS; trình bày bằng *nhiều cách*; vừa *khách quan* vừa *chủ quan*; *thay đổi/bổ sung* được.
    - *4 yếu tố chi phối nhận thức:* (1) Nhu cầu, năng lực; (2) Điều kiện, phương pháp; (3) Độ phong phú, xác thực sử liệu; (4) Mục đích, thái độ, đạo đức, thế giới quan.
    - *Sử học:* Khoa học nghiên cứu *quá khứ của loài người* (đối tượng toàn diện: cá nhân → cộng đồng → quốc gia → nhân loại).
    - *2 Chức năng:* *Khoa học* (khôi phục sự kiện + tìm quy luật) & *Xã hội* (giáo dục tư tưởng, đạo đức + rút bài học hiện tại).
    - *3 Nhiệm vụ (`N–G–D`):* *Nhận thức* • *Giáo dục* • *Dự báo*.
  ],

  // Card 2: Bai 2
  block(width: 100%, fill: c-teal-lt, stroke: 0.9pt + c-teal-bd, radius: 6pt, inset: 8.5pt)[
    #text(size: 9.6pt, weight: "extrabold", fill: c-teal)[BÀI 2. TRI THỨC LỊCH SỬ & CUỘC SỐNG (2,75đ)]
    #v(3pt)
    #set text(size: 8.3pt)
    - *Ý nghĩa tri thức LS:* Hiểu *cội nguồn, bản sắc*; đúc kết *bài học kinh nghiệm*; gắn kết *quá khứ – hiện tại – tương lai*.
    - *4 lí do học suốt đời (`V–B–H–N`):* (1) #kw[V]ận dụng kinh nghiệm sống; (2) #kw[B]í ẩn, khoảng trống & sử liệu mới; (3) #kw[H]ội nhập thế giới, giữ bản sắc; (4) #kw[N]ghề nghiệp mới (du lịch, công nghiệp VH).
    - *Kết nối LS ↔ Cuộc sống:* Hiện tại bắt nguồn từ quá khứ; học qua lớp học, bảo tàng, di tích, sách báo, phim ảnh, lễ hội...
    - *4 loại hình sử liệu (`K–V–A–T`):* Truyền #kw[K]hẩu • Hiện #kw[V]ật • Hình #kw[Ả]nh • #kw[T]hành văn. *(Sơ cấp = gốc đương thời; Thứ cấp = biên soạn sau)*.
    - *3 bước khám phá LS:* Xác định vấn đề → Chuẩn bị sử liệu → Giải quyết vấn đề.
    - *Quy trình 4 bước sử liệu (`L–S–C–X`):*
      *B1:* #kw[L]ập danh mục → *B2:* #kw[S]ưu tầm, đọc, ghi chép *(Thu thập)* → *B3:* #kw[C]họn lọc, phân loại → *B4:* #kw[X]ác minh, đánh giá, thẩm định *(Xử lí)*.
  ],
)

// Full-width Card 3: Bai 3 (5,75 points!)
#block(width: 100%, above: 7pt, below: 6pt, fill: c-primary-lt, stroke: 1.1pt + c-primary-bd, radius: 6pt, inset: 9pt)[
  #grid(
    columns: (1fr, auto),
    align: (left + horizon, right + horizon),
    text(size: 9.8pt, weight: "extrabold", fill: c-primary)[BÀI 3. VAI TRÒ CỦA SỬ HỌC — TRỌNG TÂM SỐ 1 (5,75 ĐIỂM = 57,5% TOÀN ĐỀ!)],
    pill("Có câu Tự luận 3,0đ!", c-primary, white),
  )
  #v(4pt)
  #set text(size: 8.3pt)
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 10pt,
    [
      *1. Sử học với bảo tồn & phát huy di sản:*
      - *Quan hệ cốt lõi:* Sử học (khoa học *liên ngành*) khẳng định giá trị nhiều mặt của di sản và cung cấp *cơ sở khoa học vững chắc* để bảo tồn đúng *3 nguyên tắc vàng (`3G`)*: giữ *yếu tố Gốc (nguyên trạng)*, tính *Xác thực*, tính *Toàn vẹn*.
      - *Các loại hình di sản:*
        - *DSVH vật thể:* thành quách, lăng tẩm, đình, đền, chùa, tháp, nhà cổ, cổ vật, bảo vật quốc gia... → Bảo tồn giúp *chống xuống cấp, hư hỏng*, kéo dài tuổi thọ.
        - *DSVH phi vật thể:* dân ca, lễ hội, tín ngưỡng, nghệ thuật trình diễn, nghề truyền thống, tri thức dân gian... → Bảo tồn qua *sưu tầm, truyền nghề, trình diễn* giúp chống mai một, lưu truyền thế hệ.
        - *DS thiên nhiên:* vịnh, vườn quốc gia, hang động... → Bảo vệ *đa dạng sinh học* & tăng giá trị khoa học.
        - *DS hỗn hợp:* hội tụ cả VH & TN (*Tràng An* — duy nhất ở VN!).
    ],
    [
      *2. Mối quan hệ tương tác hai chiều Lịch sử – Văn hóa ↔ Du lịch:*
      - *Chiều 1 (LS – VH → Du lịch):* Là *nguồn tài nguyên du lịch quý báu* (đặc biệt du lịch văn hóa); cung cấp tri thức thuyết minh, quảng bá hình ảnh quốc gia, ý tưởng xây dựng chiến lược du lịch bền vững.
      - *Chiều 2 (Du lịch → Bảo tồn di tích, di sản):*
        1. Thúc đẩy bảo vệ di sản văn hóa, di tích lịch sử quốc gia.
        2. Nhu cầu du khách thôi thúc chính quyền & nhân dân giữ gìn, tôn tạo.
        3. *Trích một phần doanh thu du lịch tái đầu tư* bảo tồn, quản lí di sản.
        4. Thúc đẩy sưu tầm, phục dựng, truyền dạy di sản phi vật thể.
      - *Công thức 4T viết Tự luận Vận dụng (2,0đ):*
        *(1) Tuyên truyền* nâng cao nhận thức cộng đồng • *(2) Tôn tạo* khoa học giữ yếu tố gốc • *(3) Thích ứng* du lịch bền vững, ứng dụng số hóa 3D/QR • *(4) Thanh tra* xử lí xâm hại & hành động thiết thực của học sinh.
    ],
  )
]

#pagebreak()

#sec-heading("2.2. Bộ 12 Khẩu quyết Siêu trí nhớ & Bảng phân biệt 10 cặp khái niệm dễ nhầm", badge: pill("Phản xạ 3 giây", c-teal-lt, c-teal, bd: c-teal-bd))

#block(above: 4pt, below: 7pt)[
  #set text(size: 8.15pt)
  #table(
    columns: (0.42fr, 1.15fr, 2.45fr),
    align: (center + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 5pt, y: 4.2pt),
    fill: (_, row) => if row == 0 { c-amber } else if calc.odd(row) { c-amber-lt } else { white },

    [#text(fill: white, weight: "bold")[Mã]],
    [#text(fill: white, weight: "bold")[Khẩu quyết ghi nhớ]],
    [#text(fill: white, weight: "bold")[Giải mã tức thì khi làm bài (Gặp từ khóa là khoanh ngay!)]],

    [*M01*], [*Hiện thực = `1 – K – B`*], [#kw[1] (chỉ xảy ra 1 lần duy nhất) • #kw[K]hách quan (ngoài ý muốn) • #kw[B]ất biến (không thể thay đổi).],
    [*M02*], [*Nhận thức = `N – K/C – Đ`*], [#kw[N]hiều góc nhìn tái hiện • Vừa #kw[K]hách quan vừa #kw[C]hủ quan • #kw[Đ]ổi mới, bổ sung được.],
    [*M03*], [*Chi phối NT = `N – P – S – T`*], [#kw[N]hu cầu/năng lực • #kw[P]hương pháp/điều kiện • #kw[S]ử liệu (độ xác thực) • #kw[T]hái độ/thế giới quan.],
    [*M04*], [*Đối tượng SH = `Loài người`*], [Sử học *chỉ* nghiên cứu quá khứ *loài người* (mọi cấp độ), không nghiên cứu tự nhiên thuần túy trước khi có người.],
    [*M05*], [*2 Chức = `Khoa Khôi – Xã Giáo`*], [*Khoa học* = *Khôi* phục hiện thực + tìm quy luật; *Xã hội* = *Giáo* dục đạo đức + rút bài học cuộc sống.],
    [*M06*], [*3 Nhiệm = `N – G – D`*], [#kw[N]hận thức (tri thức khoa học) • #kw[G]iáo dục (truyền thống, nhân cách) • #kw[D]ự báo (tương lai).],
    [*M07*], [*Học suốt đời = `V – B – H – N`*], [#kw[V]ận dụng kinh nghiệm • #kw[B]í ẩn/sử liệu mới • #kw[H]ội nhập giữ bản sắc • #kw[N]ghề nghiệp & sáng tạo mới.],
    [*M08*], [*4 Sử liệu = `K – V – A – T`*], [Truyền #kw[K]hẩu (lời kể) • Hiện #kw[V]ật (đồ vật cổ) • Hình #kw[Ả]nh (ảnh/phim) • #kw[T]hành văn (chữ viết).],
    [*M09*], [*4 Bước SL = `L – S – C – X`*], [#kw[L]ập danh mục → #kw[S]ưu tầm, đọc, chép → #kw[C]họn lọc, phân loại → #kw[X]ác minh, thẩm định (*“Lập Sổ Chọn Xác”*).],
    [*M10*], [*Bảo tồn cốt lõi = `3G`*], [Giữ #kw[G]ốc (yếu tố nguyên trạng) • Tính #kw[X]ác thực • Tính #kw[T]oàn vẹn — dựa trên *cơ sở khoa học Sử học*.],
    [*M11*], [*9 UNESCO VN = `6 Văn – 2 Thiên – 1 Hỗn`*], [*6 Văn hóa* (Huế, Hội An, Mỹ Sơn, Thăng Long, Thành nhà Hồ, Yên Tử 2025) + *2 Thiên nhiên* (Hạ Long–Cát Bà, Phong Nha) + *1 Hỗn hợp* (*Tràng An*).],
    [*M12*], [*Tự luận 2,0đ = `Công thức 4T`*], [#kw[T]uyên truyền ý thức • #kw[T]ôn tạo khoa học • #kw[T]hích ứng du lịch xanh & số hóa • #kw[T]hanh tra & tự giác học sinh.],
  )
]

#sub-heading("Bảng đối đầu trực diện 10 cặp khái niệm đề thi hay tráo đổi nhất")

#block(above: 3pt, below: 4pt)[
  #set text(size: 8.05pt)
  #table(
    columns: (0.35fr, 1.55fr, 1.55fr, 1.35fr),
    align: (center + horizon, left + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 4.5pt, y: 3.8pt),
    fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { c-subtle } else { white },

    [#text(fill: white, weight: "bold")[STT]],
    [#text(fill: white, weight: "bold")[Khái niệm A]],
    [#text(fill: white, weight: "bold")[Khái niệm B (Hay bị tráo!) ⚠]],
    [#text(fill: white, weight: "bold")[Mẹo phân biệt trong 2 giây]],

    [1], [*Hiện thực lịch sử:* sự kiện gốc đã xảy ra (VD: Chiến thắng Điện Biên Phủ 7/5/1954).],
    [*Nhận thức lịch sử:* sách viết, phim ảnh, lời kể về sự kiện đó (VD: Hồi kí, phim tài liệu).],
    [Có *tác giả / người kể / tác phẩm* → chắc chắn là *Nhận thức*!],

    [2], [*Lịch sử:* tất cả những gì đã diễn ra trong quá khứ.],
    [*Sử học:* ngành *khoa học* nghiên cứu về quá khứ của loài người.],
    [Có cụm *“khoa học nghiên cứu”* → khoanh *Sử học*!],

    [3], [*Chức năng khoa học:* khôi phục hiện thực, rút bản chất & phát hiện quy luật.],
    [*Chức năng xã hội:* giáo dục tư tưởng, đạo đức, rút bài học phục vụ đời sống.],
    [*Khôi phục/Quy luật* = Khoa học; *Giáo dục/Bài học* = Xã hội.],

    [4], [*Thu thập sử liệu:* lập danh mục, tìm kiếm, sưu tầm, đọc và ghi chép.],
    [*Xử lí sử liệu:* chọn lọc, phân loại, xác minh, đánh giá, thẩm định, so sánh.],
    [*Tìm – Gom – Chép* = Thu thập; *Lọc – Xác minh* = Xử lí.],

    [5], [*Sử liệu sơ cấp (gốc):* ra đời đương thời sự kiện (Bản Tuyên ngôn 2/9/1945, hiện vật khảo cổ).],
    [*Sử liệu thứ cấp (phái sinh):* sách chuyên khảo, SGK biên soạn đời sau.],
    [Ra đời *cùng thời sự kiện* = Sơ cấp (độ tin cậy gốc cao nhất).],

    [6], [*Sử liệu hiện vật:* công cụ, vũ khí, lá đề đất nung, trống đồng (vật chất cụ thể).],
    [*Sử liệu thành văn:* bia đá khắc chữ, châu bản, mộc bản, sách sử, báo chí.],
    [Trọng tâm ở *văn tự/chữ viết* ghi chép → *Thành văn*!],

    [7], [*Di sản VH vật thể:* đình, chùa, thành quách, lăng tẩm, mộc bản, bảo vật...],
    [*Di sản VH phi vật thể:* Nhã nhạc, Quan họ, Ví Giặm, Cồng chiêng, Hội Gióng, Tranh Đông Hồ (nghề)...],
    [*Chạm/nhìn khối vật chất* = Vật thể; *Trình diễn/tập quán/nghề* = Phi vật thể.],

    [8], [*Di sản thiên nhiên:* Vịnh Hạ Long – Cát Bà, VQG Phong Nha – Kẻ Bàng.],
    [*Di sản hỗn hợp:* *Quần thể danh thắng Tràng An* (vừa cố đô Hoa Lư vừa hang động karst).],
    [Đề hỏi *“vừa văn hóa vừa thiên nhiên”* → chỉ có *Tràng An*!],

    [9], [*Bảo tồn nguyên trạng:* giữ yếu tố gốc, xác thực trên cơ sở Sử học.],
    [*“Làm mới” / hiện đại hóa tùy tiện:* đập cũ xây bê tông sơn mới lòe loẹt.],
    [Thấy *“thay mới hoàn toàn / ưu tiên kinh tế trước mắt”* → chọn *SAI*!],

    [10], [*Vai trò LS–VH với Du lịch:* cung cấp *tài nguyên*, tri thức thuyết minh, quảng bá.],
    [*Vai trò Du lịch với Bảo tồn:* tạo *nguồn thu tái đầu tư*, thúc đẩy chính quyền & dân bảo vệ.],
    [Chú ý hướng mũi tên: *Ai tác động lên ai?*],
  )
]

#pagebreak()
