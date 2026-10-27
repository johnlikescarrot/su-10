#import "style.typ": *

// ============================================================================
// PART III: COMPREHENSIVE, MEMORY-OPTIMIZED LESSON THEORY (LESSONS 1, 2, 3)
// ============================================================================

#part-banner(
  "Phần III • Lý thuyết trọng tâm chuẩn SGK Kết nối tri thức",
  "HỆ THỐNG KIẾN THỨC CHUYÊN SÂU — SƠ ĐỒ HÓA — CHỐNG BẪY ĐỀ THI",
  "Bao phủ 100% chỉ báo Nhận biết – Thông hiểu – Vận dụng của Bài 1, Bài 2 và Bài 3 theo Bảng đặc tả 2026–2027",
)

// ============================================================================
// BÀI 1
// ============================================================================
#sec-heading("BÀI 1. HIỆN THỰC LỊCH SỬ VÀ LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC", badge: pill("1,50 điểm • Câu I.1 → I.6", c-navy-lt, c-navy, bd: c-navy-bd))

#image("assets/bai1_hienthuc_nhanthuc.svg", width: 100%)

#sub-heading("1. Lịch sử là gì? Phân biệt Hiện thực lịch sử và Nhận thức lịch sử")

- *Khái niệm Lịch sử:* #kw[Lịch sử] là tất cả những gì *đã diễn ra trong quá khứ*. #kwb[Lịch sử loài người] là toàn bộ những hoạt động của con người từ khi xuất hiện đến ngày nay (bao gồm cả quá trình con người tương tác với tự nhiên và tương tác với nhau trong xã hội).
- *Hai nghĩa của thuật ngữ “Lịch sử”:* Trong khoa học lịch sử, khái niệm “lịch sử” luôn được hiểu theo hai nghĩa gắn bó chặt chẽ nhưng *không đồng nhất* là *hiện thực lịch sử* và *lịch sử được con người nhận thức* (nhận thức lịch sử).

#block(breakable: false, above: 6pt, below: 6pt)[
  #set text(size: 8.4pt)
  #table(
    columns: (0.95fr, 1.65fr, 1.85fr),
    align: (left + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 6pt, y: 5pt),
    fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { c-subtle } else { white },

    [#text(fill: white, weight: "bold")[Tiêu chí so sánh]],
    [#text(fill: white, weight: "bold")[Hiện thực lịch sử (`1 – K – B`)]],
    [#text(fill: white, weight: "bold")[Lịch sử được con người nhận thức (`N – K/C – Đ`)]],

    [*Bản chất*],
    [Là tất cả những gì *đã diễn ra trong quá khứ* đúng như nó vốn có.],
    [Là những *hiểu biết, hình dung* của con người về hiện thực lịch sử, được trình bày, tái hiện theo những cách khác nhau.],

    [*Tính chất tồn tại*],
    [Tồn tại hoàn toàn *khách quan*, độc lập, không phụ thuộc vào ý muốn chủ quan của người nhận thức.],
    [Vừa mang *tính khách quan* (phản ánh sự thật gốc), vừa mang *tính chủ quan* (in dấu ấn của người tìm hiểu, biên soạn).],

    [*Số lượng & Biến đổi*],
    [*Chỉ có một (duy nhất)* và *không thể thay đổi* theo thời gian.],
    [*Đa dạng, phong phú*; có thể được *bổ sung, điều chỉnh, viết lại* khi phát hiện sử liệu mới hoặc phương pháp mới.],

    [*Vị trí & Quan hệ*],
    [*Có trước*; không có hiện thực lịch sử thì không thể có nhận thức lịch sử.],
    [*Có sau*, phái sinh từ hiện thực; luôn có một *khoảng cách nhất định* so với hiện thực (không thể tái hiện trọn vẹn 100%).],

    [*Hình thức biểu hiện*],
    [Bản thân biến cố, sự kiện, quá trình đã khép lại trong quá khứ.],
    [Câu chuyện kể, công trình sử học, sách giáo khoa, bia kí, tiểu thuyết lịch sử, phim tài liệu, vở kịch, tranh vẽ...],

    [*Ví dụ chuẩn SGK KNTT*],
    [- Chủ tịch Hồ Chí Minh đọc *Tuyên ngôn Độc lập* ngày 2/9/1945 tại Quảng trường Ba Đình. \ - Trận Ngọc Hồi – Đống Đa mùa xuân 1789. \ - Chuyến hải hành của Ph. Ma-gien-lăng đến đảo Mác-tan (Phi-líp-pin) năm 1521.],
    [- Các bộ sách, phim tài liệu, bài giảng viết về Cách mạng tháng Tám và ngày Quốc khánh 2/9. \ - Tiểu thuyết *Hoàng Lê nhất thống chí* (Ngô gia văn phái) hoặc sách nghiên cứu về Tây Sơn của G. Dutton. \ - Nội dung khắc trên *hai tấm bia* tại đảo Mác-tan.],
  )
]

- *Giải mã ví dụ kinh điển SGK KNTT (Tư liệu 2, tr. 8 — Hai tấm bia ở đảo Mác-tan, Phi-líp-pin):*
  - *Điểm giống (cùng phản ánh 1 hiện thực lịch sử):* Cuộc đụng độ ngày 27/4/1521 trên đảo Mác-tan giữa đoàn thám hiểm của *Ph. Ma-gien-lăng* và dân bản địa do thủ lĩnh *La-pu-la-pu* chỉ huy khiến Ma-gien-lăng tử trận.
  - *Điểm khác (2 nhận thức lịch sử trái ngược):* Tấm bia năm 1941 (do người Phi-líp-pin dựng) tôn vinh La-pu-la-pu là người anh hùng đầu tiên *đánh đuổi quân xâm lược châu Âu*; trong khi tấm bia năm 1951 nhìn từ góc độ hàng hải thế giới lại ca ngợi Ph. Ma-gien-lăng thực hiện *cuộc phát kiến địa lí vĩ đại vòng quanh Trái Đất*.
  - *Nguyên nhân cốt lõi:* Do *mục đích, lập trường, góc nhìn và bối cảnh lịch sử* của chủ thể nhận thức khác nhau!
- *04 yếu tố quy định sự khác nhau của nhận thức lịch sử (`N – P – S – T`):*
  1. *Nhu cầu và năng lực* của người tìm hiểu, nghiên cứu lịch sử.
  2. *Điều kiện và phương pháp* tìm hiểu, tiếp cận lịch sử.
  3. *Mức độ phong phú và xác thực* của nguồn thông tin, sử liệu thu thập được.
  4. *Mục đích, thái độ, đạo đức và thế giới quan* của người tìm hiểu, nghiên cứu lịch sử.

#quote-box(
  "Lịch sử chỉ xảy ra duy nhất có một lần, nhưng do nhiều người viết và viết lại nhiều lần. Dù ở thời điểm nào, nhà sử học cũng phải thật trung thực, khách quan.",
  "Đại tướng Võ Nguyên Giáp (Phát biểu tại Đại hội toàn quốc lần thứ II Hội Sử học Việt Nam, 1988)",
)

#sub-heading("2. Sử học là gì? Đối tượng, chức năng và nhiệm vụ của Sử học")

- *Khái niệm Sử học:* #kw[Sử học] là *khoa học nghiên cứu về quá khứ của loài người*. (Xét trong hai nghĩa của lịch sử, nghiên cứu Sử học thuộc về phạm trù *nhận thức lịch sử* mang tính khoa học, chuyên sâu).
- *Đối tượng nghiên cứu của Sử học:* Là *toàn bộ quá khứ của loài người* — bao gồm quá khứ của một cá nhân, một nhóm người, một cộng đồng, một quốc gia, một khu vực hoặc toàn thể nhân loại trên *tất cả các lĩnh vực* (chính trị, kinh tế, xã hội, văn hóa, quân sự, ngoại giao...). → Đặc trưng nổi bật: mang tính *toàn diện và đa dạng*.
- *Chức năng và nhiệm vụ của Sử học (Cực kì hay hỏi ở câu I.2 – I.4!):*

#grid(
  columns: (1fr, 1fr),
  column-gutter: 9pt,
  info-box("02 CHỨC NĂNG CỦA SỬ HỌC (Khoa Khôi – Xã Giáo)", accent: c-navy, bg: c-navy-lt, bd: c-navy-bd)[
    1. *Chức năng khoa học:*
       - *Khôi phục* các sự kiện lịch sử diễn ra trong quá khứ một cách chân thực, chính xác.
       - *Rút ra bản chất* của các quá trình lịch sử để *phát hiện quy luật* vận động và phát triển của lịch sử.
    2. *Chức năng xã hội:*
       - *Giáo dục* tư tưởng, tình cảm, đạo đức cách mạng.
       - *Rút ra bài học kinh nghiệm* phục vụ cuộc sống hiện tại.
  ],
  info-box("03 NHIỆM VỤ CỦA SỬ HỌC (Khẩu quyết N – G – D)", accent: c-teal, bg: c-teal-lt, bd: c-teal-bd)[
    1. *Nhiệm vụ nhận thức:* Cung cấp tri thức khoa học, giúp con người tìm hiểu, khám phá hiện thực lịch sử khách quan, chân thực.
    2. *Nhiệm vụ giáo dục:* Truyền bá truyền thống tốt đẹp; bồi dưỡng đạo đức, tinh thần dân tộc, tình yêu quê hương đất nước, lòng khoan dung, nhân ái.
    3. *Nhiệm vụ dự báo:* Qua tổng kết thực tiễn và quy luật, góp phần *dự báo xu hướng vận động tương lai* của đất nước, nhân loại.
  ],
)

#trap-box("BẪY ĐỀ THI BÀI 1 — ĐỌC KỸ ĐỂ KHÔNG MẤT OAN 0,25 ĐIỂM")[
  - *Bẫy 1:* “Đối tượng nghiên cứu của Sử học là mọi biến đổi của Trái Đất từ khi hình thành 4,6 tỉ năm trước” → *SAI!* Sự hình thành Trái Đất trước khi có con người thuộc Địa chất học/Tự nhiên học; Sử học chỉ nghiên cứu quá khứ *từ khi xuất hiện con người* và *gắn với hoạt động của con người*.
  - *Bẫy 2:* “Nhờ khoa học hiện đại, nhận thức lịch sử có thể tái hiện hoàn toàn nguyên vẹn 100% hiện thực lịch sử” → *SAI!* Nhận thức lịch sử ngày càng *tiệm cận* chân lí khách quan nhưng luôn tồn tại khoảng cách nhất định so với hiện thực đã qua.
]

// ============================================================================
// BÀI 2
// ============================================================================
#sec-heading("BÀI 2. TRI THỨC LỊCH SỬ VÀ CUỘC SỐNG", badge: pill("2,75 điểm • Câu I.7 → I.13 & Câu II.1", c-teal-lt, c-teal, bd: c-teal-bd))

#image("assets/bai2_quytrinh_sulieu.svg", width: 100%)

#sub-heading("1. Vai trò của tri thức lịch sử & Sự cần thiết phải học tập, khám phá lịch sử suốt đời")

- *Vai trò, ý nghĩa cốt lõi của tri thức lịch sử:*
  - Giúp mỗi cá nhân và cộng đồng biết rõ *nguồn gốc, tổ tiên, cội nguồn* của bản thân, gia đình, dòng họ, quê hương, dân tộc và nhân loại (*“Dân ta phải biết sử ta / Cho tường gốc tích nước nhà Việt Nam”* — Hồ Chí Minh).
  - Tạo lập sợi dây liên kết bền chặt giữa *quá khứ – hiện tại – tương lai*, hun đúc *ý thức dân tộc và bản sắc văn hóa* để không bị hòa tan trong toàn cầu hóa.
  - Như nhà sử học Ngô Sĩ Liên đúc kết trong *Đại Việt sử ký toàn thư*: lịch sử là *“tấm gương phản chiếu”* việc hay dở của người xưa để đời sau đúc kết bài học thành công và tránh lặp lại sai lầm.
- *Giải thích 04 lí do cần học tập và khám phá lịch sử suốt đời (Khẩu quyết `V – B – H – N` — Chuẩn câu I.11 & II.1b):*
  1. *(V) Vận dụng kinh nghiệm sống:* Trong cuộc sống hằng ngày, con người luôn cần vận dụng tri thức, kinh nghiệm từ quá khứ để giải quyết vấn đề hiện tại và định hướng cho tương lai.
  2. *(B) Bí ẩn lịch sử & sử liệu mới:* Kho tàng tri thức lịch sử nhân loại mênh mông và biến đổi không ngừng; nhiều sự kiện trong quá khứ vẫn còn khoảng trống, bí ẩn. Khi phát hiện sử liệu mới hoặc thành tựu khảo cổ mới, nhận thức lịch sử cần được cập nhật, bổ sung suốt đời.
  3. *(H) Hội nhập quốc tế & giữ bản sắc:* Giúp con người tự tin hội nhập thế giới, biết tôn trọng sự đa dạng, khác biệt văn hóa của các dân tộc, tiếp thu tinh hoa nhân loại đồng thời tôn vinh, giữ gìn bản sắc Việt Nam.
  4. *(N) Nghề nghiệp & sáng tạo mới:* Tri thức lịch sử mang lại nguồn cảm hứng sáng tạo dồi dào cho công nghiệp văn hóa (điện ảnh, văn học, thiết kế, game lịch sử...), du lịch di sản, mở ra nhiều cơ hội nghề nghiệp hấp dẫn trong kỉ nguyên mới.

#sub-heading("2. Kết nối lịch sử với cuộc sống & Vận dụng giải thích vấn đề thời sự")

- *Bản chất của việc kết nối tri thức lịch sử với cuộc sống:* Hiện tại không xuất hiện ngẫu nhiên mà *luôn kế thừa và khởi nguồn từ quá khứ*; hiểu sâu quá khứ giúp lí giải căn nguyên các vấn đề đương đại và kiến tạo tương lai bền vững.
- *Không gian & hình thức học tập lịch sử đa dạng (ngoài trang sách nhà trường):* Lịch sử hiện diện ở khắp mọi nơi (ngôi nhà, gia phả dòng họ, mái đình, ngôi chùa, tên đường phố, kỉ vật kháng chiến...). Học sinh có thể tìm hiểu qua: giờ học chính khóa, tham quan bảo tàng – di tích lịch sử, đọc sách báo, xem phim tài liệu/nghệ thuật, tham gia lễ hội truyền thống, phỏng vấn nhân chứng, khai thác bảo tàng số trực tuyến...
- *Vận dụng bài học lịch sử giải thích vấn đề thời sự (Trọng tâm câu Đúng/Sai `II.1d` — Mức Vận dụng):*
  + *Bài học đại đoàn kết dân tộc:* Từ truyền thống đoàn kết chống ngoại xâm thời Lý – Trần – Lê và Cách mạng tháng Tám 1945 → Vận dụng vào phát huy sức mạnh toàn dân tộc trong *khắc phục hậu quả thiên tai, bão lũ, dịch bệnh, xóa đói giảm nghèo và phát triển đất nước*.
  + *Bài học bảo vệ chủ quyền lãnh thổ & biển đảo:* Các nguồn sử liệu thành văn và bản đồ cổ (*Phủ biên tạp lục*, *Đại Nam thực lục*, *Châu bản triều Nguyễn*) là bằng chứng lịch sử – pháp lí đanh thép khẳng định chủ quyền của Việt Nam đối với hai quần đảo *Hoàng Sa và Trường Sa*, kết hợp đấu tranh hòa bình theo luật pháp quốc tế (UNCLOS 1982).
  + *Bài học độc lập, tự chủ kết hợp ngoại giao mềm dẻo:* Kế thừa nghệ thuật bang giao hòa hiếu của cha ông → Đường lối đối ngoại độc lập, tự chủ, đa phương hóa, đa dạng hóa (*“ngoại giao cây tre Việt Nam”*: gốc vững, thân chắc, cành uyển chuyển) trong hội nhập quốc tế hiện nay.

#sub-heading("3. Sưu tầm, thu thập và xử lí thông tin, sử liệu trong học tập lịch sử")

- *Khái niệm sử liệu:* #kw[Sử liệu] là toàn bộ những hình thức khác nhau của tư liệu lịch sử chứa đựng thông tin về quá khứ của loài người — đóng vai trò *“cầu nối”* duy nhất giúp con người tiếp cận và khôi phục hiện thực lịch sử.
- *Phân loại các nguồn sử liệu (Cực hay hỏi nhận diện ví dụ!):*
  + *Theo dạng thức tồn tại (4 loại — `K – V – A – T`):*
    1. *Sử liệu lời nói – truyền khẩu:* truyền thuyết, thần thoại, ca dao, dân ca, lời kể của nhân chứng lịch sử.
    2. *Sử liệu hiện vật:* công cụ đá/đồng, trống đồng Đông Sơn, vũ khí, tiền cổ, đồ gốm, phế tích kiến trúc (*VD Hình 6 SGK: Lá đề chim phượng bằng đất nung tại khu khảo cổ 18 Hoàng Diệu – Hoàng thành Thăng Long*; *Hình 8 SGK: Tờ tiền giấy 10.000 đồng phát hành năm 1993*).
    3. *Sử liệu hình ảnh (nghe – nhìn):* ảnh chụp tư liệu, băng ghi âm, thước phim tài liệu quay tại hiện trường.
    4. *Sử liệu thành văn (chữ viết):* bia đá khắc chữ, mộc bản, châu bản, thư tịch cổ (*Đại Việt sử ký toàn thư*), văn kiện chính thức (*VD Hình 7 SGK: Bản Tuyên ngôn Độc lập ngày 2/9/1945*), nhật kí, báo chí. *(Lưu ý: tờ tiền hay tấm bia khắc chữ vừa có giá trị hiện vật vừa chứa thông tin thành văn!)*.
  + *Theo mối liên hệ thời gian & độ trực tiếp:*
    - *Sử liệu sơ cấp (sử liệu gốc):* Ra đời trực tiếp vào thời điểm diễn ra sự kiện hoặc do người trong cuộc tạo ra (hiện vật khảo cổ, văn kiện gốc, ảnh chụp hiện trường) → *Độ tin cậy gốc cao nhất*.
    - *Sử liệu thứ cấp (sử liệu phái sinh):* Được biên soạn, tổng hợp về sau dựa trên các sử liệu sơ cấp (sách chuyên khảo hiện đại, sách giáo khoa, bài báo nghiên cứu).
- *03 bước lớn tìm hiểu, khám phá lịch sử dựa trên sử liệu (SGK KNTT tr. 14):*
  *(1) Xác định vấn đề cần tìm hiểu* → *(2) Chuẩn bị sử liệu (sưu tầm, thu thập & xử lí sử liệu)* → *(3) Giải quyết vấn đề trên cơ sở khai thác sử liệu*.
- *Quy trình 04 bước chuẩn trong thu thập và xử lí thông tin, sử liệu (Khẩu quyết `L – S – C – X` — Câu I.8, I.9, I.10):*
  + *Bước 1 — Lập danh mục (`L`):* Lập thư mục và danh sách các nguồn sử liệu cần sưu tầm bám sát chủ đề tìm hiểu.
  + *Bước 2 — Sưu tầm, đọc và ghi chép (`S`):* Tìm kiếm, khảo sát, phỏng vấn, đọc và ghi chép thông tin sử liệu *(Bước 1 + Bước 2 thuộc khâu **Sưu tầm, thu thập sử liệu**)*.
  + *Bước 3 — Chọn lọc và phân loại (`C`):* Tách lọc tư liệu liên quan, sắp xếp theo loại hình/niên đại/nội dung để thuận tiện kiểm chứng.
  + *Bước 4 — Xác minh, đánh giá và thẩm định (`X`):* Kiểm tra nguồn gốc xuất xứ, thời điểm ra đời, tác giả, đối chiếu chéo nhiều nguồn để xác định tính xác thực và độ tin cậy *(Bước 3 + Bước 4 thuộc khâu **Xử lí thông tin, sử liệu** — còn gọi là phê phán sử liệu)*.

#pagebreak()

// ============================================================================
// BÀI 3 — TRỌNG TÂM 5,75 ĐIỂM!
// ============================================================================
#sec-heading("BÀI 3. VAI TRÒ CỦA SỬ HỌC (TRỌNG TÂM SỐ 1: 5,75 ĐIỂM!)", badge: pill("5,75 điểm • 7 TN + 1 Đ/S + 1 TL 3,0đ", c-primary-lt, c-primary, bd: c-primary-bd))

#image("assets/bai3_disan_dulich_2chieu.svg", width: 100%)

#sub-heading("1. Sử học với công tác bảo tồn và phát huy giá trị di sản văn hóa, di sản thiên nhiên")

*a) Nhận diện hệ thống các loại hình di sản (Câu I.15, I.17 & Ý 1 câu Tự luận):*
- #kw[Di sản văn hóa] là sản phẩm tinh thần, vật chất có giá trị lịch sử, văn hóa, khoa học, được lưu truyền từ thế hệ này qua thế hệ khác, chia làm *02 loại hình chính*:
  1. *Di sản văn hóa vật thể:* Sản phẩm vật chất có giá trị lịch sử, văn hóa, khoa học — gồm *di tích lịch sử – văn hóa* (thành quách, cung điện, lăng tẩm, đình, đền, chùa, tháp, nhà cổ, địa điểm cách mạng), *danh lam thắng cảnh*, *di vật, cổ vật, bảo vật quốc gia* (trống đồng Ngọc Lũ, ấn vàng, Cửu đỉnh Huế...).
  2. *Di sản văn hóa phi vật thể:* Sản phẩm tinh thần gắn với cộng đồng, được lưu truyền bằng truyền miệng, truyền nghề, trình diễn — gồm: tiếng nói, chữ viết; ngữ văn dân gian; nghệ thuật trình diễn dân gian (*Nhã nhạc cung đình Huế, Quan họ Bắc Ninh, Ca trù, Đờn ca tài tử, Dân ca Ví, Giặm Nghệ Tĩnh, Bài chòi, Xòe Thái...*); tập quán xã hội và tín ngưỡng (*Tín ngưỡng thờ cúng Hùng Vương, thờ Mẫu Tam phủ*); lễ hội truyền thống (*Hội Gióng, Lễ hội Vía Bà Chúa Xứ núi Sam*); nghề thủ công truyền thống (*Nghề làm gốm Chăm, Nghề làm tranh dân gian Đông Hồ – UNESCO ghi danh năm 2025*); tri thức dân gian.
  *(Mở rộng: UNESCO còn ghi danh hạng mục **Di sản tư liệu** thuộc Chương trình Ký ức Thế giới như Mộc bản triều Nguyễn, 82 Bia đá Tiến sĩ Văn Miếu – Quốc Tử Giám, Châu bản triều Nguyễn, Hoàng hoa sứ trình đồ...).*
- #kwt[Di sản thiên nhiên]: Các khu vực tự nhiên có giá trị đặc biệt về địa chất, địa mạo, cảnh quan thẩm mĩ, hệ sinh thái và đa dạng sinh học (*Vịnh Hạ Long – Quần đảo Cát Bà, VQG Phong Nha – Kẻ Bàng, VQG Pù Mát, Hồ Ba Bể, Cao nguyên đá Đồng Văn...*).
- #kwb[Di sản hỗn hợp (Văn hóa và Thiên nhiên)]: Hội tụ đồng thời cả tiêu chí văn hóa xuất sắc lẫn tiêu chí thiên nhiên đặc sắc — tiêu biểu duy nhất tại Việt Nam và Đông Nam Á là *Quần thể danh thắng Tràng An (Ninh Bình, 2014)*.

#image("assets/unesco_vietnam_9_disan.svg", width: 100%)

*b) Mối quan hệ giữa Sử học với công tác bảo tồn và phát huy giá trị di sản (Câu I.14, I.16 & Ý 1 Tự luận):*
- Giá trị của một di sản thường kết tinh ở nhiều khía cạnh (lịch sử, văn hóa, kiến trúc, mĩ thuật, khảo cổ, sinh thái...). Do đó, việc vận dụng các phương pháp nghiên cứu của *Sử học với tư cách là một khoa học có tính liên ngành* giữ vai trò *quan trọng nhất trong việc xác định và khẳng định giá trị đích thực của di sản* (lập hồ sơ xếp hạng di tích quốc gia, hồ sơ đệ trình UNESCO).
- Kết quả nghiên cứu của Sử học cung cấp *cơ sở khoa học vững chắc* cho công tác bảo tồn, trùng tu và phát huy giá trị di sản, đảm bảo yêu cầu cốt lõi nhất của bảo tồn là *giữ gìn “yếu tố gốc cấu thành di tích”* — tức đảm bảo *tính nguyên trạng, tính xác thực, tính toàn vẹn* và *giá trị nổi bật* của di sản, vì sự phát triển bền vững và lợi ích chung của toàn xã hội.
- *Hệ quả nếu tách rời Sử học:* Nếu trùng tu, khai thác mà không dựa trên nghiên cứu Sử học sẽ dẫn tới tình trạng *“làm mới” di tích tùy tiện*, bê tông hóa, sai lệch niên đại – kiến trúc, làm biến dạng hoặc hủy hoại vĩnh viễn giá trị gốc không thể khôi phục của di sản.

*c) Vai trò của công tác bảo tồn và phát huy giá trị di sản đối với từng loại hình:*
- *Đối với di sản văn hóa vật thể:* Được tạo dựng bằng nhiều chất liệu (đất, đá, gạch, gỗ, tre, lá...) nên luôn chịu nguy cơ phong hóa, xuống cấp, hư hỏng do thiên nhiên (mưa bão, ẩm mốc) và con người (chiến tranh, đô thị hóa, xâm lấn). Bảo tồn giúp *hạn chế, khắc phục tác động tiêu cực và kéo dài tuổi thọ của di sản*.
- *Đối với di sản văn hóa phi vật thể:* Đứng trước nguy cơ thất truyền, mai một trong đời sống hiện đại. Thông qua các biện pháp *sưu tầm, ghi chép, lưu giữ, truyền nghề, trình diễn, vinh danh nghệ nhân*, di sản được *tái tạo, giữ gìn và lưu truyền qua nhiều thế hệ*.
- *Đối với di sản thiên nhiên:* Góp phần *bảo vệ sự phát triển đa dạng sinh học*, bảo vệ nguồn gen quý hiếm, cân bằng sinh thái và *làm tăng giá trị khoa học* của di sản.
- *Vai trò kinh tế – xã hội chung:* Bảo vệ bản sắc dân tộc, giáo dục lòng yêu nước và trở thành nguồn lực quan trọng *thúc đẩy phát triển kinh tế – xã hội địa phương bền vững*.

#sub-heading("2. Sử học với sự phát triển du lịch — Mối quan hệ tương tác hai chiều")

Giữa lịch sử – văn hóa và ngành du lịch tồn tại *mối quan hệ tương tác hai chiều hữu cơ, gắn bó khăng khít*:

#grid(
  columns: (1fr, 1fr),
  column-gutter: 9pt,
  info-box("CHIỀU 1: VAI TRÒ CỦA LỊCH SỬ – VĂN HÓA ĐỐI VỚI DU LỊCH", accent: c-navy, bg: c-navy-lt, bd: c-navy-bd)[
    1. *Là nguồn tài nguyên du lịch quý báu:* Hệ thống di tích lịch sử – văn hóa, lễ hội, ẩm thực, làng nghề truyền thống tạo sức hút đặc sắc cho ngành du lịch (nhất là *du lịch văn hóa – di sản*).
    2. *Cung cấp tri thức khoa học để quảng bá:* Sử học cung cấp thông tin chính xác để xây dựng bài thuyết minh hấp dẫn, thiết kế tour trải nghiệm có chiều sâu văn hóa (như tour đêm *“Giải mã Hoàng thành Thăng Long”*, Nhã nhạc trên sông Hương).
    3. *Định hướng chiến lược:* Cung cấp bài học kinh nghiệm để quy hoạch, xây dựng chiến lược phát triển du lịch bền vững.
  ],
  info-box("CHIỀU 2: TÁC ĐỘNG CỦA DU LỊCH ĐỐI VỚI BẢO TỒN DI TÍCH", accent: c-teal, bg: c-teal-lt, bd: c-teal-bd)[
    1. *Thúc đẩy trách nhiệm bảo vệ:* Góp phần thúc đẩy việc bảo vệ di tích lịch sử, di sản văn hóa của các quốc gia.
    2. *Khơi dậy động lực cộng đồng:* Nhu cầu tham quan, tìm hiểu, trải nghiệm của du khách thôi thúc chính quyền và người dân địa phương tự giác gìn giữ, tôn tạo di sản.
    3. *Tạo nguồn lực tài chính tái đầu tư:* Một phần doanh thu từ vé tham quan và dịch vụ du lịch được *trích lại tái đầu tư* cho trùng tu, quản lí, bảo vệ di tích và tạo sinh kế cho người dân.
    4. *Nuôi dưỡng phi vật thể:* Thúc đẩy sưu tầm, phục dựng, truyền dạy và trình diễn các di sản phi vật thể, quảng bá văn hóa Việt Nam ra thế giới.
  ],
)

#trap-box("PHÂN TÍCH MẶT TRÁI KHI PHÁT TRIỂN DU LỊCH THIẾU BỀN VỮNG (DÀNH CHO CÂU HIỂU & VẬN DỤNG)")[
  Bên cạnh các tác động tích cực chủ đạo, nếu chạy theo *lợi ích kinh tế trước mắt* và khai thác du lịch ồ ạt thiếu kiểm soát sẽ gây hệ lụy nghiêm trọng cho di sản: *(1)* Quá tải lượng khách gây lún sụt, bào mòn kết cấu di tích và ô nhiễm rác thải; *(2)* Xâm lấn cảnh quan vùng lõi (xây khách sạn, cáp treo trái phép phá vỡ không gian nguyên gốc); *(3)* Thương mại hóa, “sân khấu hóa” dung tục làm biến tướng bản sắc lễ hội và di sản phi vật thể. → *Nguyên tắc bất di bất dịch:* Phát triển hài hòa, lấy *bảo tồn giá trị văn hóa – lịch sử làm nền tảng* cho *lợi ích kinh tế lâu dài, bền vững*!
]

#sub-heading("3. Khung Công thức 4T & Hồ sơ địa danh mẫu ăn trọn 3,0 điểm Tự luận")

#memory-box("DÀN Ý VẠN NĂNG GIẢI QUYẾT MỌI CÂU TỰ LUẬN BÀI 3 (3,0 ĐIỂM)", breakable-box: true)[
  - *VẾ 1 — NHẬN BIẾT (1,0 điểm):* Trình bày gãy gọn 3 gạch đầu dòng chuẩn SGK: *(i)* Nêu khái niệm/phân loại di sản (vật thể, phi vật thể, thiên nhiên, hỗn hợp) kèm 3–5 địa danh tiêu biểu; *(ii)* Khẳng định Sử học là khoa học liên ngành giúp xác định giá trị nhiều mặt của di sản; *(iii)* Kết quả nghiên cứu Sử học là *cơ sở khoa học* bảo đảm giữ gìn *yếu tố gốc, tính xác thực, tính toàn vẹn* để phát triển bền vững.
  - *VẾ 2 — VẬN DỤNG ĐỀ XUẤT BIỆN PHÁP & LIÊN HỆ BẢN THÂN (2,0 điểm — Áp dụng Công thức 4T):*
    + *Bước mở đầu (0,25đ):* Giới thiệu ngắn gọn 01 di sản tiêu biểu của đất nước hoặc địa phương (VD: *Khu di tích Quốc gia đặc biệt Kim Liên – Nam Đàn* hoặc *Dân ca Ví, Giặm Nghệ Tĩnh* tại Nghệ An; hoặc *Hoàng thành Thăng Long / Cố đô Huế / Quần thể Tràng An*).
    + *Nhóm giải pháp 1 — (T) Tuyên truyền & Giáo dục (0,50đ):* Đẩy mạnh tuyên truyền Luật Di sản văn hóa, lồng ghép giáo dục di sản địa phương trong trường học để nâng cao ý thức tự hào, tự giác bảo vệ của người dân và du khách.
    + *Nhóm giải pháp 2 — (T) Tôn tạo dựa trên cơ sở khoa học (0,50đ):* Tu bổ, chống xuống cấp định kì trên cơ sở nghiên cứu nghiêm ngặt của Sử học, tuyệt đối giữ gìn *yếu tố gốc*, không “làm mới” thô bạo; với di sản phi vật thể thì hỗ trợ nghệ nhân mở lớp truyền dạy cho thế hệ trẻ.
    + *Nhóm giải pháp 3 — (T) Thích ứng du lịch bền vững & Chuyển đổi số (0,50đ):* Khai thác du lịch xanh có kiểm soát sức chứa, gắn lợi ích sinh kế cộng đồng với bảo vệ di sản; ứng dụng công nghệ số (mã QR thuyết minh đa ngôn ngữ, số hóa 3D, bảo tàng ảo VR/AR, truyền thông mạng xã hội).
    + *Nhóm giải pháp 4 — (T) Thanh tra bảo vệ & Trách nhiệm học sinh (0,25đ):* Xử lí nghiêm hành vi xâm hại, viết vẽ bậy, buôn bán cổ vật trái phép. *Liên hệ bản thân học sinh:* Tích cực tìm hiểu lịch sử địa phương, ứng xử văn minh khi tham quan (không xả rác, không khắc tên lên di tích), viết bài/làm video ngắn giới thiệu di sản quê hương và vận động gia đình, bạn bè cùng chung tay gìn giữ.
]

#sub-heading("4. Bảng thẻ Flashcard Truy hồi chủ động (Che cột phải để tự kiểm tra trong 3 phút!)")

#block(above: 4pt, below: 6pt)[
  #set text(size: 8.15pt)
  #table(
    columns: (0.4fr, 1.85fr, 2.35fr),
    align: (center + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 5pt, y: 4.2pt),
    fill: (_, row) => if row == 0 { c-teal } else if calc.odd(row) { c-subtle } else { white },

    [#text(fill: white, weight: "bold")[Thẻ]],
    [#text(fill: white, weight: "bold")[Câu hỏi tự truy hồi (Mặt trước)]],
    [#text(fill: white, weight: "bold")[Đáp án từ khóa cốt lõi (Mặt sau)]],

    [F01], [Điểm khác nhau căn bản nhất giữa Hiện thực LS và Nhận thức LS?], [*Hiện thực:* 1 duy nhất, khách quan, bất biến. *Nhận thức:* đa dạng, vừa khách quan vừa chủ quan, bổ sung được.],
    [F02], [Nêu đủ 2 chức năng và 3 nhiệm vụ của Sử học?], [*2 chức năng:* Khoa học & Xã hội. *3 nhiệm vụ:* Nhận thức – Giáo dục – Dự báo (`N–G–D`).],
    [F03], [Nêu đúng thứ tự 4 bước thu thập và xử lí sử liệu?], [*B1:* Lập danh mục → *B2:* Sưu tầm, đọc, ghi chép → *B3:* Chọn lọc, phân loại → *B4:* Xác minh, đánh giá, thẩm định (`L–S–C–X`).],
    [F04], [Bản Tuyên ngôn Độc lập 2/9/1945 thuộc loại sử liệu nào?], [Vừa là *sử liệu thành văn*, vừa là *sử liệu sơ cấp (gốc)* có giá trị xác thực cao nhất.],
    [F05], [Yêu cầu cốt lõi nhất khi bảo tồn, trùng tu di tích lịch sử là gì?], [Phải dựa trên cơ sở khoa học của Sử học để giữ gìn *yếu tố gốc cấu thành di tích* (tính nguyên trạng, xác thực, toàn vẹn).],
    [F06], [Kể tên Di sản Thế giới hỗn hợp duy nhất và Di sản mới nhất (2025) của VN?], [*Hỗn hợp duy nhất:* Quần thể danh thắng Tràng An (2014). *Mới nhất (7/2025):* Yên Tử – Vĩnh Nghiêm – Côn Sơn, Kiếp Bạc.],
    [F07], [Nêu 2 địa danh/di sản tiêu biểu tại Nghệ An để liên hệ câu Tự luận?], [*Di tích quốc gia đặc biệt:* Khu di tích Kim Liên (Nam Đàn), Khu di tích Truông Bồn (Đô Lương). *Phi vật thể UNESCO:* Dân ca Ví, Giặm Nghệ Tĩnh; *Thiên nhiên:* VQG Pù Mát.],
    [F08], [Khi đứng trước bài toán “kinh tế trước mắt hay văn hóa lâu dài”, chọn gì?], [Đặt *bảo tồn giá trị văn hóa – lịch sử làm nền tảng* để phát triển du lịch mang lại *lợi ích kinh tế lâu dài, bền vững*.],
  )
]

#pagebreak()
