# -*- coding: utf-8 -*-
"""
Noi dung de cuong on tap kiem tra giua hoc ki I - Lich su 10
Bo sach: Ket noi tri thuc voi cuoc song. Nam hoc 2026-2027.

Nguon phan tich: LS10- MTGK1-26-27-HHT.docx (ma tran de + bang dac ta).
Day la dang "block" trung gian; src/build_outline.py chiu trach nhiem render ra PDF.

Quy uoc markup noi dong:
  **dam**  //nghien//  {{nhan manh}}  __gach chan__
"""

DOC = []


def add(t, **kw):
    kw['t'] = t
    DOC.append(kw)


# =====================================================================
# TRANG BIA / HUONG DAN
# =====================================================================
add('toc')

add('h1', n='PHẦN 0', title='GIẢI MÃ ĐỀ KIỂM TRA',
    sub='Đọc vị ma trận trước khi bắt đầu học')

add('box', kind='note', title='Tài liệu này được biên soạn từ đâu?',
    items=[
        'Nguồn duy nhất được phân tích là tệp **LS10- MTGK1-26-27-HHT.docx** (32.101 byte) — gồm 2 bảng: **MA TRẬN KIỂM TRA ĐỊNH KÌ GIỮA HỌC KÌ 1 – KHỐI 10** và **BẢNG ĐẶC TẢ MA TRẬN ĐỀ KIỂM TRA GIỮA HỌC KÌ 1 – LỚP 10**.',
        '**Lưu ý quan trọng và trung thực:** tệp gốc là //ma trận đề + bảng đặc tả//, tức là bản thiết kế của đề thi, **không chứa câu hỏi hay đáp án cụ thể nào** (đã kiểm tra toàn bộ các phần XML của tệp, kể cả văn bản ẩn, hộp văn bản, ghi chú, đối tượng nhúng — không có câu hỏi gốc).',
        'Vì vậy, để đáp ứng yêu cầu “bao gồm TẤT CẢ các câu hỏi cùng đáp án tương ứng”, đề cương này **tái tạo trọn vẹn toàn bộ 28 lệnh hỏi trắc nghiệm + 1 câu tự luận** theo đúng **mã câu (I.1–I.20, II.1a–d, II.2a–d, TL)**, đúng **bài**, đúng **năng lực** và đúng **cấp độ tư duy** đã ghi trong ma trận; mỗi câu đều có **đáp án và giải thích chi tiết** ở Phần 4.',
        'Nội dung kiến thức bám sát Chương trình GDPT 2018 và SGK **Lịch sử 10 – Kết nối tri thức với cuộc sống** (Chủ đề 1: Lịch sử và sử học; Chủ đề 2: Vai trò của sử học). Học sinh nên đối chiếu thêm với vở ghi và tài liệu giáo viên bộ môn.',
    ])

add('h2', title='0.1. Thông tin chung về bài kiểm tra')

add('table', caption='Bảng 0.1 – Thông số của đề',
    cols=[110, 389], head=['Thông số', 'Nội dung (trích từ ma trận đề)'], rows=[
        ['Kì kiểm tra', 'Kiểm tra định kì **giữa học kì I**, khối **10**, năm học **2026 – 2027**'],
        ['Thời gian làm bài', '**45 phút**'],
        ['Thang điểm', '**10 điểm**'],
        ['Cấu trúc đề', '**20 câu** trắc nghiệm nhiều lựa chọn + **2 câu** trắc nghiệm Đúng/Sai + **1 câu** tự luận'],
        ['Tổng số lệnh hỏi', '**28 lệnh hỏi trắc nghiệm + 1 câu tự luận** (20 câu TN + 8 ý Đ/S + 1 TL)'],
        ['Phạm vi kiến thức', '**Chủ đề 1.** Lịch sử và sử học (Bài 1, Bài 2); **Chủ đề 2.** Vai trò của sử học (Bài 3)'],
        ['3 năng lực đánh giá', '**NL1** Tìm hiểu lịch sử · **NL2** Nhận thức và tư duy lịch sử · **NL3** Vận dụng kiến thức, kĩ năng'],
        ['3 cấp độ tư duy', '**Biết** (nhận biết) · **Hiểu** (thông hiểu) · **Vận dụng**'],
    ])

add('h2', title='0.2. Ma trận đề — bảng mã câu theo năng lực và cấp độ tư duy')

add('p', text='Đây là “xương sống” của đề thi. Mỗi ô trong bảng dưới đây là một **mã lệnh hỏi** đã được ghi trong tệp DOCX. Nắm được bảng này là biết chính xác mình sẽ bị hỏi gì.')

add('table', caption='Bảng 0.2 – Ma trận đề (rút gọn, giữ nguyên mã câu của tệp gốc)', fontsize=7.2,
    cols=[86, 66, 55, 70, 62, 55, 55, 50],
    head=['Bài / Năng lực', 'NL1 · Biết', 'NL1 · Hiểu', 'NL2 · Biết', 'NL2 · Hiểu', 'NL3 · Biết', 'NL3 · VD', 'Tổng'],
    rows=[
        ['**Bài 1**', 'I.1, I.2, I.3', 'I.4', '—', 'I.5, I.6', '—', '—', '6 lệnh'],
        ['**Bài 2**', 'I.7, I.8, I.9', 'I.10, I.11', 'I.12, I.13; II.1a', 'II.1b', 'II.1c', 'II.1d', '11 lệnh'],
        ['**Bài 3**', 'I.14, I.15; TL(1/2)', 'I.16', 'I.17, I.18; II.2a', 'I.19, I.20; II.2b', 'II.2c', 'II.2d; TL(1/2)', '11 lệnh + TL'],
        ['**Số lệnh**', '8 + 1/2 TL', '4', '6', '6', '2', '2 + 1/2 TL', '28 TN + 1 TL'],
        ['**Số điểm**', '3,0', '1,0', '1,5', '1,5', '0,5', '2,5', '**10,0**'],
        ['**Tỉ lệ (đã hiệu chỉnh)**', '30%', '10%', '15%', '15%', '5%', '25%', '**100%**'],
    ])

add('box', kind='key', title='Đọc ngay 3 con số vàng',
    items=[
        '**50% đề (5,0 điểm) là mức độ BIẾT** → học chắc định nghĩa, khái niệm, tên riêng, địa danh là đã có một nửa điểm.',
        '**25% (2,5 điểm) là VẬN DỤNG**, trong đó riêng nửa câu tự luận vận dụng đáng **2,0 điểm** → đây là “điểm rơi” dễ mất nhất.',
        '**Bài 3 chiếm 57,5% (5,75/10 điểm)** → nếu chỉ có 1 buổi ôn, hãy dành một nửa thời gian cho Bài 3.',
    ])

add('h2', title='0.3. Bảng đặc tả — yêu cầu cần đạt của từng bài')

add('table', caption='Bảng 0.3 – Yêu cầu cần đạt (trích và chuẩn hoá từ bảng đặc tả trong tệp DOCX)',
    cols=[96, 403], head=['Bài', 'Yêu cầu cần đạt'], rows=[
        ['**Bài 1**\nHiện thực lịch sử và lịch sử được con người nhận thức',
         '**Nhận biết:** Trình bày được khái niệm lịch sử, sử học; nêu được đối tượng, chức năng và nhiệm vụ của Sử học; nhận diện được hiện thực lịch sử và lịch sử được con người nhận thức qua sự kiện cụ thể; chỉ ra được đặc điểm của lịch sử được con người nhận thức.\n**Thông hiểu:** Giải thích được khái niệm sử học; phân biệt được hiện thực lịch sử và lịch sử được con người nhận thức qua tình huống cụ thể.'],
        ['**Bài 2**\nTri thức lịch sử và cuộc sống',
         '**Nhận biết:** Nêu được các bước trong việc thu thập, xử lí thông tin và sử liệu; biết cách sưu tầm, thu thập, xử lí thông tin, sử liệu để học tập, khám phá lịch sử.\n**Thông hiểu:** Giải thích được sự cần thiết phải học tập và khám phá lịch sử suốt đời; hiểu được bản chất của việc kết nối tri thức, bài học lịch sử vào cuộc sống.\n**Vận dụng:** Vận dụng kiến thức, bài học lịch sử để giải thích những vấn đề thời sự trong nước và thế giới, những vấn đề trong thực tiễn cuộc sống (mức độ đơn giản); quan tâm, yêu thích và tham gia các hoạt động tìm hiểu lịch sử, văn hoá của dân tộc Việt Nam và thế giới.'],
        ['**Bài 3**\nVai trò của Sử học',
         '**Nhận biết:** Nêu được mối quan hệ giữa Sử học với công tác bảo tồn và phát huy giá trị di sản văn hoá, di sản thiên nhiên; kể tên được một số địa danh là tài nguyên du lịch của nước ta; kể tên được các loại hình di sản văn hoá.\n**Thông hiểu:** Hiểu rõ vai trò của Sử học với công tác bảo tồn và phát huy giá trị di sản; giải thích rõ vai trò của lịch sử – văn hoá đối với sự phát triển du lịch thông qua tình huống cụ thể; phân tích tác động của du lịch đối với công tác bảo tồn di tích lịch sử, di tích văn hoá.\n**Vận dụng:** Đề xuất biện pháp bảo tồn, phát huy các giá trị của di sản; có ý thức vận động mọi người xung quanh cùng tham gia bảo vệ di sản văn hoá, di sản thiên nhiên ở nhiều địa phương.'],
    ])

add('h2', title='0.4. Phân phối điểm — xác định đúng thứ tự ưu tiên ôn tập')

add('table', caption='Bảng 0.4 – Điểm số quy đổi theo từng bài (tự tính từ ma trận)',
    cols=[54, 165, 60, 60, 100],
    head=['Bài', 'Thành phần', 'Số lệnh', 'Điểm', 'Ưu tiên'], rows=[
        ['**Bài 1**', '6 câu TN (I.1 – I.6)', '6', '**1,50** (15,0%)', '★★★'],
        ['**Bài 2**', '7 câu TN (I.7 – I.13) + câu Đ/S II.1 (4 ý)', '7 + 4', '**2,75** (27,5%)', '★★★★'],
        ['**Bài 3**', '7 câu TN (I.14 – I.20) + câu Đ/S II.2 (4 ý) + câu TL', '7 + 4 + 1', '**5,75** (57,5%)', '★★★★★'],
        ['**Tổng**', '20 TN + 8 ý Đ/S + 1 TL', '28 + 1', '**10,00** (100%)', '—'],
    ])

add('p', text='**Cách tính:** mỗi lệnh hỏi trắc nghiệm (kể cả mỗi ý Đ/S) = **0,25 điểm** → 28 × 0,25 = **7,0 điểm**. Câu tự luận = 10 − 7 = **3,0 điểm**, được chia không đều: **1,0 điểm** cho ý NL1–Biết (nêu khái niệm, kể tên) và **2,0 điểm** cho ý NL3–Vận dụng (phân tích + đề xuất). Cách chia này khớp hoàn toàn với dòng “Tổng số điểm” của ma trận: ô NL1–Biết = 2,0 + 1,0 = 3,0; ô NL3–Vận dụng = 0,5 + 2,0 = 2,5.')

add('table', caption='Bảng 0.5 – Điểm theo cấp độ tư duy', fontsize=8,
    cols=[125, 125, 125, 124],
    head=['Mức độ', 'Biết', 'Hiểu', 'Vận dụng'], rows=[
        ['Điểm', '**5,0**', '**2,5**', '**2,5**'],
        ['Tỉ lệ', '**50%**', '**25%**', '**25%**'],
        ['Dạng câu', 'Định nghĩa, kể tên, nhận diện', 'Giải thích, phân biệt, phân tích', 'Tình huống, đề xuất, liên hệ bản thân'],
    ])

add('h2', title='0.5. Phân tích kĩ: 8 điểm bất cập trong tệp gốc (rất dễ gây hiểu nhầm)')

add('num', items=[
    '**Tệp không có đề thi thật.** Toàn bộ 44 phần tử của `word/document.xml` chỉ là 2 bảng; không có câu hỏi, không có đáp án, không có phần phụ lục, không có tệp đính kèm. Mọi “câu hỏi trong đề” ở Phần 3 của tài liệu này là **phiên bản tái tạo theo đúng mã và yêu cầu cần đạt** của ma trận — không phải bản sao của một đề đã có sẵn.',
    '**Lỗi tỉ lệ ở ma trận:** ô NL3–Biết ghi **“0,5%”** trong khi số điểm là **0,5/10** → phải là **5%**.',
    '**Lỗi tỉ lệ ở bảng đặc tả:** ô NL3–Vận dụng ghi **“2,5%”** trong khi số điểm là **2,5/10** → phải là **25%**. Cộng dòng tỉ lệ của bảng đặc tả theo nguyên bản chỉ được **77,5%**, không phải 100%.',
    '**Hai bảng mâu thuẫn nhau:** cùng một ô NL3–Vận dụng, ma trận ghi **25%**, bảng đặc tả ghi **2,5%**. Căn cứ vào dòng “Tổng số điểm” (2,5/10) thì **25% mới là đúng**.',
    '**Dòng “Tổng số lệnh” của bảng đặc tả**, cột “Tổng điểm”, bị ghi nhầm thành **“2+1/2 TL”** (sao chép từ ô bên trái). Đúng ra phải là **“28 lệnh hỏi TN + 1 TL”** như ma trận đã ghi.',
    '**Kí hiệu “TL (1/2)” không có nghĩa là chia đôi điểm.** Phần TL của NL1–Biết = **1,0 điểm**, của NL3–Vận dụng = **2,0 điểm** (xem cách tính ở mục 0.4). Học sinh thường ôn phần “nêu khái niệm” kĩ hơn phần “đề xuất giải pháp” — đây là sai lầm chiến thuật.',
    '**Lỗi nhỏ về chính tả/kí hiệu:** “I. 5.6” phải là “I.5, I.6”; “3, 0” phải là “3,0”; “Bài 2:Tri thức…” thiếu dấu cách; một số ô tỉ lệ ghi “0” thay vì “0%”.',
    '**Cột “Tổng điểm” bị bỏ trống ở cả 3 hàng bài** trong ma trận — điểm từng bài chỉ có thể suy ra bằng cách đếm lệnh hỏi (đã làm ở Bảng 0.4). Đây cũng là lí do nhiều học sinh đánh giá thấp tầm quan trọng của Bài 3.',
])

add('h2', title='0.6. Chiến lược làm bài trong 45 phút')

add('table', caption='Bảng 0.6 – Phân bổ thời gian đề xuất', fontsize=8,
    cols=[86, 96, 317], head=['Thời điểm', 'Việc cần làm', 'Mẹo cụ thể'], rows=[
        ['Phút 0 – 3', 'Đọc lướt toàn bộ đề', 'Gạch chân từ khóa: //khái niệm, không phải, đúng nhất, tình huống, đề xuất//. Đánh dấu ngay câu TL để “ngấm” trong lúc làm câu khác.'],
        ['Phút 3 – 18', '20 câu trắc nghiệm (5,0đ)', '~40 giây/câu. Câu nào quá 60 giây → chọn tạm, vòng tròn mã câu, quay lại sau. Đọc hết 4 phương án rồi mới chọn.'],
        ['Phút 18 – 25', '2 câu Đúng/Sai (2,0đ)', 'Xét **từng ý a, b, c, d độc lập**. Cảnh giác kiểu câu ghép: vế đầu đúng, vế sau sai → cả ý vẫn là Sai.'],
        ['Phút 25 – 38', 'Câu tự luận (3,0đ)', '5 phút lập dàn ý (ý 1: 1,0đ; ý 2: 2,0đ) + 8 phút viết. Phải có **ít nhất 4 biện pháp cụ thể** và lời kêu gọi cộng đồng.'],
        ['Phút 38 – 45', 'Rà soát & nộp bài', 'Kiểm tra thứ tự mã câu khi tô đáp án; rà lại các câu đã đánh dấu; chắc chắn không bỏ trống ô nào.'],
    ])

add('box', kind='warn', title='5 cái bẫy thường gặp nhất',
    items=[
        'Câu có các từ **“tất cả”, “duy nhất”, “luôn luôn”, “hoàn toàn”, “không bao giờ”** → khả năng cao là phương án sai.',
        'Câu phân biệt **hiện thực lịch sử** với **lịch sử được nhận thức** hay đảo ngược chủ thể: cái đã xảy ra là //hiện thực//, cái được kể lại là //nhận thức//.',
        'Câu hỏi “bước đầu tiên” của quy trình xử lí sử liệu: đáp án đúng là **xác định nhiệm vụ/câu hỏi**, không phải “tìm kiếm ngay”.',
        'Câu Đ/S ghép một mệnh đề đúng với một mệnh đề sai bằng “vì”, “nên”, “do đó” → phải đọc trọn câu.',
        'Câu tự luận chỉ **liệt kê biện pháp** mà thiếu **phân tích tác động 2 mặt của du lịch** → mất trọn 2,0 điểm vận dụng.',
    ])

# =====================================================================
# PHAN 1 - KIEN THUC COT LOI
# =====================================================================
add('pb')
add('h1', n='PHẦN 1', title='HỆ THỐNG KIẾN THỨC CỐT LÕI',
    sub='3 bài học · sơ đồ tư duy · bảng đối chiếu · công thức trả lời')

add('box', kind='tip', title='Cách đọc Phần 1 để nhớ lâu',
    items=[
        'Mỗi bài bắt đầu bằng một **bản đồ khái niệm** (các ô màu). Hãy nhìn bản đồ, che lại và tự kể lại trước khi đọc chi tiết.',
        'Những bảng **“SO SÁNH”** là nơi ra đề nhiều nhất (I.5, I.6, I.19, I.20). Đọc theo chiều ngang, không đọc theo chiều dọc.',
        'Mỗi cuối bài có **“CHÌA KHOÁ GHI NHỚ”** — chỉ cần thuộc 1 cụm từ là kéo được cả chuỗi ý.',
    ])

# ---------------------------------------------------------------------
add('h2', title='1.1. BÀI 1 — Hiện thực lịch sử và lịch sử được con người nhận thức')

add('p', text='**Vị trí trong đề:** 6 lệnh hỏi (I.1 – I.6) = **1,50 điểm (15%)**. Toàn bộ ở mức Biết và Hiểu — đây là phần “điểm dễ lấy nhất”, không được phép mất.')

add('h3', title='A. Bản đồ khái niệm (học trong 3 phút)')

add('table', caption='Sơ đồ 1.1 – Bản đồ Bài 1', fontsize=8,
    cols=[112, 193, 194], head=['Nhánh', 'Từ khoá', 'Nội dung cốt lõi'], rows=[
        ['**1. LỊCH SỬ**', 'Quá khứ · xã hội loài người', 'Nghĩa rộng: mọi cái đã xảy ra trong quá khứ của tự nhiên và xã hội. Nghĩa hẹp (đối tượng Sử học): **quá trình phát triển của xã hội loài người**.'],
        ['**2. SỬ HỌC**', 'Khoa học · nhận thức lại quá khứ', '**Sử học là khoa học nghiên cứu về lịch sử**, tức là nhận thức, tái hiện và giải thích quá khứ của con người và xã hội loài người dựa trên sử liệu.'],
        ['**3. ĐỐI TƯỢNG**', 'Con người · không gian · thời gian', 'Hoạt động của con người trong quá khứ trên mọi lĩnh vực (chính trị, kinh tế, văn hoá, xã hội, tư tưởng), **gắn với không gian, thời gian cụ thể**.'],
        ['**4. CHỨC NĂNG**', 'Nhận thức · Giáo dục · Dự báo', '**N**hận thức (cung cấp tri thức) – **G**iáo dục (đạo đức, yêu nước) – **D**ự báo (từ quá khứ đoán xu hướng). Một số tài liệu thêm chức năng giải trí/thẩm mĩ.'],
        ['**5. NHIỆM VỤ**', 'Thu thập · Phục dựng · Giải thích · Truyền bá', 'Phát hiện & xử lí sử liệu → tái hiện khách quan hiện thực lịch sử → giải thích, đánh giá, rút bài học → phổ biến tri thức, giáo dục thế hệ trẻ.'],
        ['**6. HAI MẶT**', 'Hiện thực ↔ Nhận thức', '**Hiện thực lịch sử** = cái đã xảy ra (khách quan). **Lịch sử được con người nhận thức** = cái được kể lại (có dấu ấn chủ quan).'],
    ])

add('h3', title='B. Bộ 5 định nghĩa phải thuộc lòng (dạng “câu chìa khoá”)')

add('kv', items=[
    ['**Lịch sử**',
     'Những gì **đã diễn ra trong quá khứ**. Với tư cách là đối tượng của một môn khoa học: lịch sử là **toàn bộ quá trình phát triển của xã hội loài người** từ khi có con người đến nay.'],
    ['**Sử học**',
     '**Khoa học nghiên cứu về lịch sử.** Sử học không “tạo ra” quá khứ mà **nhận thức lại, tái hiện và giải thích** quá khứ ấy một cách khách quan, có phương pháp, dựa trên **sử liệu**.'],
    ['**Sử liệu**',
     'Toàn bộ **dấu tích của quá khứ** còn lưu lại (tài liệu, hiện vật, lời kể, hình ảnh...) được dùng làm **chứng cứ** để nghiên cứu, tái hiện lịch sử.'],
    ['**Hiện thực lịch sử**',
     'Sự thật lịch sử **khách quan** đã thực sự xảy ra, tồn tại **độc lập với ý thức của con người**, dù con người có biết đến hay không.'],
    ['**Lịch sử được con người nhận thức**',
     'Sự **phản ánh / tái hiện** hiện thực lịch sử trong ý thức của con người thông qua sử liệu, kí ức, sách vở, công trình nghiên cứu — luôn **tiệm cận** nhưng không bao giờ trùng khít hoàn toàn với hiện thực.'],
])

add('h3', title='C. Đối tượng – Chức năng – Nhiệm vụ của Sử học (bảng “3C”)')

add('table', caption='Bảng 1.1 – Khung “ĐỐI – CHỨC – NHIỆM” (gợi ý cho câu I.2, I.3, I.4)', fontsize=8,
    cols=[88, 130, 281], head=['Thành phần', 'Gợi nhớ', 'Nội dung'], rows=[
        ['**Đối tượng**', '“Ai? Ở đâu? Khi nào?”', 'Con người và xã hội loài người trong quá khứ: hoạt động chính trị, kinh tế, văn hoá, xã hội, tư tưởng; **luôn gắn với không gian, thời gian xác định**. Sự kiện lịch sử là **duy nhất, không lặp lại**.'],
        ['**Chức năng 1**', '**NHẬN THỨC**', 'Cung cấp tri thức chân thực về quá khứ, giúp con người hiểu mình từ đâu đến, giải đáp “tại sao”.'],
        ['**Chức năng 2**', '**GIÁO DỤC**', 'Bồi dưỡng tư tưởng, đạo đức, lối sống, lòng yêu nước, tự hào dân tộc, ý thức công dân; “lấy lịch sử làm thầy”.'],
        ['**Chức năng 3**', '**DỰ BÁO**', 'Nhận ra quy luật, xu hướng từ quá khứ để dự báo, lựa chọn giải pháp cho hiện tại, tương lai.'],
        ['**Nhiệm vụ 1**', '**THU THẬP**', 'Phát hiện, sưu tầm, phân loại, xử lí và kiểm chứng sử liệu.'],
        ['**Nhiệm vụ 2**', '**PHỤC DỰNG**', 'Tái hiện lại hiện thực lịch sử một cách khách quan, chân thực, đúng bối cảnh.'],
        ['**Nhiệm vụ 3**', '**GIẢI THÍCH**', 'Lí giải nguyên nhân – diễn biến – kết quả – ý nghĩa; đánh giá sự kiện, nhân vật; rút ra bài học, quy luật.'],
        ['**Nhiệm vụ 4**', '**TRUYỀN BÁ**', 'Phổ biến tri thức lịch sử, giáo dục thế hệ trẻ, phục vụ đời sống và bảo tồn di sản.'],
    ])

add('box', kind='key', title='CHÌA KHOÁ GHI NHỚ BÀI 1',
    items=[
        '**“ĐỐI – 3C – 4N”**: Đối tượng (quá khứ xã hội loài người) · 3 Chức năng (**N**hận thức – **G**iáo dục – **D**ự báo) · 4 Nhiệm vụ (**T**hu thập – **P**hục dựng – **G**iải thích – **T**ruyền bá).',
        'Câu hỏi “Sử học là một **khoa học** vì sao?” → trả lời đủ 4 ý: có **đối tượng riêng**, có **sử liệu**, có **phương pháp** (phê phán nguồn, đối chiếu), hướng tới **chân lí khách quan** (có thể kiểm chứng, có thể bị hiệu chỉnh).',
    ])

add('h3', title='D. SO SÁNH quan trọng nhất: 2 mặt của lịch sử (chắc chắn có trong đề)')

add('table', caption='Bảng 1.2 – Hiện thực lịch sử ↔ Lịch sử được con người nhận thức', fontsize=7.8,
    cols=[92, 196, 211], head=['Tiêu chí', 'HIỆN THỰC LỊCH SỬ', 'LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC'], rows=[
        ['Bản chất', 'Sự thật **khách quan** đã xảy ra', 'Sự **phản ánh** sự thật ấy trong ý thức con người'],
        ['Tồn tại', '**Độc lập** với ý thức con người; không phụ thuộc vào ai kể, ai viết', '**Phụ thuộc** vào người nhận thức, lập trường, quan điểm, thời đại'],
        ['Số lượng', '**Chỉ có một** (sự kiện duy nhất, không lặp lại)', '**Có nhiều** cách kể, nhiều góc nhìn, nhiều công trình khác nhau'],
        ['Mức độ', '**Đầy đủ, trọn vẹn** nhưng không thể quan sát trực tiếp vì đã qua', '**Không đầy đủ, có thể phiến diện** vì sử liệu bị mất mát, mai một'],
        ['Khả năng thay đổi', '**Không thay đổi** (quá khứ không thể sửa lại)', '**Thay đổi, được bổ sung, hiệu chỉnh** khi có sử liệu mới, phương pháp mới'],
        ['Ví dụ', 'Trận chiến diễn ra ngày 7/5/1954 tại Điện Biên Phủ', 'Bài báo, cuốn sách, bộ phim, hồi kí, bài giảng kể lại trận chiến ấy'],
        ['Mối quan hệ', '**Là nguồn gốc, là thước đo** của nhận thức', '**Phản ánh và tiệm cận** hiện thực; phải được kiểm chứng bằng sử liệu'],
    ])

add('box', kind='exam', title='Công thức nhận diện tình huống (dùng cho I.5, I.6 và mọi câu Đ/S)',
    items=[
        'Gặp từ **“đã xảy ra, thực sự diễn ra, sự thật, sự kiện có thật”** → **hiện thực lịch sử**.',
        'Gặp từ **“kể lại, ghi chép, mô tả, tưởng tượng, quan điểm, sách, phim, hồi kí, lời kể, cách hiểu”** → **lịch sử được con người nhận thức**.',
        'Gặp **“phát hiện thêm tư liệu mới → sửa lại niên đại / đổi cách đánh giá”** → đặc điểm **tính thay đổi (được bổ sung, hiệu chỉnh)** của lịch sử được nhận thức.',
        'Gặp **“hai người cùng chứng kiến nhưng kể khác nhau”** → đặc điểm **tính chủ quan** và **tính đa chiều**.',
    ])

add('h3', title='E. 5 đặc điểm của lịch sử được con người nhận thức')

add('table', caption='Bảng 1.3 – Từ khoá “CHỦ – THIẾU – ĐA – BIẾN – XÃ”', fontsize=8,
    cols=[86, 122, 291], head=['Đặc điểm', 'Từ khoá', 'Giải thích ngắn'], rows=[
        ['1. **Tính chủ quan**', 'CHỦ', 'Mang dấu ấn cá nhân: lập trường, cảm xúc, lợi ích, trình độ của người kể/viết và của thời đại họ sống.'],
        ['2. **Tính không đầy đủ**', 'THIẾU', 'Sử liệu bị mất mát, mai một; không ai nắm bắt được mọi khía cạnh của một sự kiện đã qua.'],
        ['3. **Tính đa dạng, đa chiều**', 'ĐA', 'Cùng một sự kiện có thể được tiếp cận từ nhiều góc độ (chính trị, kinh tế, văn hoá...) và nhiều cách lí giải.'],
        ['4. **Tính thay đổi**', 'BIẾN', 'Tri thức lịch sử được **bổ sung, chỉnh sửa, thậm chí đảo ngược** khi phát hiện sử liệu mới hoặc có phương pháp mới.'],
        ['5. **Tính xã hội – lịch sử**', 'XÃ', 'Nhận thức lịch sử chịu tác động của xã hội đương thời, được truyền đạt và chia sẻ trong cộng đồng; vì vậy phải học và cập nhật **suốt đời**.'],
    ])

add('box', kind='note', title='Liên kết sang Bài 2 (rất hay ra đề nối ý)',
    items=[
        'Chính vì lịch sử được nhận thức có **tính thay đổi** và **không đầy đủ**, nên con người phải **không ngừng thu thập – kiểm chứng – cập nhật sử liệu** (Bài 2) và phải **học lịch sử suốt đời**.',
    ])

# ---------------------------------------------------------------------
add('h2', title='1.2. BÀI 2 — Tri thức lịch sử và cuộc sống')

add('p', text='**Vị trí trong đề:** 7 câu TN (I.7 – I.13) + 1 câu Đ/S gồm 4 ý (II.1a – d) = **2,75 điểm (27,5%)**. Có đủ 3 cấp độ: Biết, Hiểu, Vận dụng — bài “dễ bị mất điểm ở câu vận dụng” nhất.')

add('h3', title='A. Quy trình 6 bước thu thập, xử lí thông tin và sử liệu')

add('table', caption='Sơ đồ 1.2 – Quy trình “X – T – T – S – K – V”', fontsize=7.8,
    cols=[46, 106, 215, 132], head=['Bước', 'Tên bước', 'Làm gì cụ thể', 'Lỗi hay mắc'], rows=[
        ['**1**', '**XÁC** định nhiệm vụ', 'Xác định đề tài, câu hỏi nghiên cứu (5W1H: Ai? Cái gì? Khi nào? Ở đâu? Tại sao? Như thế nào?), phạm vi thời gian – không gian, mục tiêu sản phẩm.', 'Nhảy vào tìm tài liệu ngay mà không biết mình cần trả lời câu hỏi gì.'],
        ['**2**', '**TÌM** nguồn & lập kế hoạch', 'Chọn kênh: thư viện, bảo tàng, lưu trữ, di tích, báo chí, cơ sở dữ liệu số, phỏng vấn nhân chứng, điền dã. Phân công, dự trù thời gian.', 'Chỉ dùng một nguồn duy nhất (thường là mạng xã hội).'],
        ['**3**', '**THU** thập & ghi chép', 'Ghi chép, chụp ảnh, ghi âm, sao chép, phỏng vấn; **luôn ghi rõ nguồn** (tác giả, tên tài liệu, năm, trang, đường dẫn, ngày truy cập).', 'Quên ghi nguồn → không kiểm chứng lại được, dễ bị coi là đạo văn.'],
        ['**4**', '**SẮP** xếp, phân loại', 'Phân loại theo loại hình (thành văn / hiện vật / truyền miệng / hình ảnh – số), theo gốc – thứ cấp, theo trình tự thời gian, theo chủ đề; lập bảng, sơ đồ, timeline.', 'Trộn lẫn ý kiến cá nhân với sự thật được ghi nhận.'],
        ['**5**', '**KIỂM** chứng, đánh giá', 'Đối chiếu chéo ít nhất 2–3 nguồn độc lập; xét nguồn gốc, tác giả, thời điểm, tính nhất quán, động cơ; phát hiện tin giả, chỉnh sửa, thiên lệch.', 'Tin ngay vào bài viết “hot” vì có nhiều lượt chia sẻ.'],
        ['**6**', '**VẬN** dụng & chia sẻ', 'Phân tích – giải thích – rút ra kết luận/bài học; trình bày báo cáo, bài thuyết trình, sản phẩm số; trích dẫn nguồn đầy đủ; lưu trữ để dùng lại.', 'Chỉ chép lại thông tin mà không rút ra được bài học.'],
    ])

add('box', kind='key', title='CHÌA KHOÁ GHI NHỚ QUY TRÌNH',
    items=[
        '**“Xác – Tìm – Thu – Sắp – Kiểm – Vận”** (X – T – T – S – K – V). Gợi nhớ bằng câu: **“Xem Tin Tức, Soi Kĩ Vào”**.',
        'Bước **kiểm chứng (5)** là “trái tim” của tư duy lịch sử: **không có kiểm chứng → không có sử học**.',
        'Nếu đề hỏi “việc làm nào thể hiện bước xử lí thông tin?” → chọn hành động **phân loại / đối chiếu / đánh giá độ tin cậy**, KHÔNG phải hành động **tìm – chép – chụp**.',
    ])

add('h3', title='B. Hệ thống phân loại sử liệu')

add('table', caption='Bảng 1.4 – 4 nhóm sử liệu + 2 cấp độ', fontsize=7.9,
    cols=[104, 175, 220], head=['Loại sử liệu', 'Đặc điểm', 'Ví dụ'], rows=[
        ['**Sử liệu thành văn**', 'Thông tin được ghi bằng chữ viết; dễ lưu truyền nhưng có thể bị sao chép sai.', 'Chiếu chỉ, sắc phong, bia ký, nhật ký, thư từ, hồi ký, báo chí, văn bản lưu trữ, châu bản.'],
        ['**Sử liệu hiện vật (vật chất)**', 'Dấu tích vật chất còn lại; **khách quan, khó làm giả**, nhưng cần giải mã.', 'Trống đồng Đông Sơn, tiền cổ, vũ khí, đồ gốm, trang phục, mộ táng, công trình, di tích, cổ vật.'],
        ['**Sử liệu truyền miệng**', 'Được truyền bằng lời kể, kí ức; giàu cảm xúc nhưng **dễ tam sao thất bản**.', 'Truyền thuyết (Sơn Tinh – Thủy Tinh), dân ca, lời kể nhân chứng, hồi ức cựu chiến binh.'],
        ['**Sử liệu hình ảnh – âm thanh – số**', 'Ghi lại trực quan; cần kiểm chứng niên đại, bối cảnh, nguy cơ chỉnh sửa (AI/deepfake).', 'Ảnh tư liệu, phim tài liệu, bản ghi âm, bản đồ cổ, dữ liệu số hoá, trang web lưu trữ.'],
        ['**Sử liệu GỐC**', '**Cùng thời** sự kiện, do người trực tiếp chứng kiến tạo ra, còn nguyên bản → độ tin cậy cao nhất.', 'Bức thư viết năm 1946 của người lính; bia đá dựng ngay sau trận đánh.'],
        ['**Sử liệu THỨ CẤP**', 'Được biên soạn, sao chép, phân tích **lại** từ nguồn gốc → tiện dùng nhưng phải đối chiếu.', 'Sách giáo khoa, bài nghiên cứu, bài blog, phim tài liệu lịch sử.'],
    ])

add('h3', title='C. Vì sao phải học tập và khám phá lịch sử SUỐT ĐỜI? (6 lí do)')

add('num', items=[
    '**Hiểu nguồn cội – biết mình là ai:** lịch sử cho biết cá nhân, cộng đồng, dân tộc hình thành thế nào, từ đó có bản sắc và điểm tựa tinh thần.',
    '**Bồi dưỡng lòng yêu nước, tự hào và trách nhiệm công dân:** các tấm gương tiền bối trở thành bài học đạo đức, lối sống, lẽ sống.',
    '**Rút ra bài học kinh nghiệm, tránh lặp lại sai lầm:** quá khứ là “phòng thí nghiệm” của nhân loại về chiến tranh, hoà bình, cải cách, quản trị, ứng xử với thiên nhiên.',
    '**Rèn tư duy phản biện, chống tin giả:** quen phân tích nguồn, đối chiếu, kiểm chứng → không dễ bị thao túng bởi thông tin sai lệch, xuyên tạc lịch sử.',
    '**Tri thức lịch sử luôn được bổ sung:** vì lịch sử được nhận thức có **tính thay đổi** (Bài 1), khi có sử liệu mới, cách hiểu cũ có thể bị sửa → phải học, cập nhật **suốt đời**.',
    '**Phục vụ cuộc sống và hội nhập:** hiểu quá khứ để giải quyết vấn đề hiện tại, bảo tồn di sản, phát triển du lịch, đối ngoại và khẳng định vị thế Việt Nam trên trường quốc tế.',
])

add('h3', title='D. Bản chất của việc “kết nối tri thức lịch sử vào cuộc sống”')

add('table', caption='Sơ đồ 1.3 – Công thức 3 bước “HIỂU – SO – LÀM”', fontsize=8,
    cols=[52, 120, 327], head=['Bước', 'Tên', 'Nội dung'], rows=[
        ['1', '**HIỂU ĐÚNG**', 'Nắm đúng sự kiện, bối cảnh, nguyên nhân – kết quả; tách được bài học khỏi chi tiết ngẫu nhiên. Không “lấy lịch sử ra để minh hoạ cho ý mình có sẵn”.'],
        ['2', '**SO ĐÚNG**', 'Đối chiếu quá khứ với hiện tại: cái gì **giống** (có thể vận dụng), cái gì **khác** (không áp đặt máy móc), bài học nào còn nguyên giá trị, bài học nào cần điều chỉnh.'],
        ['3', '**LÀM ĐÚNG**', 'Chuyển hoá thành **thái độ, quyết định, hành động cụ thể**: từ lời nói, việc làm nhỏ hằng ngày đến giải pháp cho cộng đồng. Có trách nhiệm với di sản và với tương lai.'],
    ])

add('box', kind='warn', title='Nguyên tắc vàng khi vận dụng lịch sử',
    items=[
        '**Không đồng nhất quá khứ với hiện tại** (bối cảnh khác nhau). **Không cắt xén, xuyên tạc** sự thật để phục vụ mục đích riêng. **Không dùng lịch sử để khơi gợi hận thù, chia rẽ** — trái lại, dùng để xây dựng hoà bình, hợp tác và lòng vị tha.',
    ])

add('h3', title='E. Bảng vận dụng giải thích vấn đề thời sự (mẫu cho câu II.1d và câu TL)')

add('table', caption='Bảng 1.5 – 8 tình huống “quá khứ → hiện tại”', fontsize=7.6,
    cols=[110, 155, 234], head=['Vấn đề thời sự / thực tiễn', 'Bài học lịch sử', 'Cách kết nối (câu trả lời mẫu)'], rows=[
        ['Đại đoàn kết vượt qua dịch bệnh, thiên tai', 'Truyền thống đoàn kết chống ngoại xâm, “đánh giặc” và “trị thuỷ” thời Lý – Trần', 'Phát huy sức mạnh toàn dân, kỉ luật cộng đồng, “lá lành đùm lá rách”; nhà nước và nhân dân cùng hành động.'],
        ['Đổi mới, chuyển đổi số, khởi nghiệp', 'Cải cách Đổi mới 1986; các cuộc cải cách thời Hồ Quý Ly, Minh Mạng; tiếp nhận khoa học kĩ thuật phương Tây', 'Dám đổi mới tư duy, dám thử – dám sửa; nhưng phải xuất phát từ thực tiễn, có lộ trình và đặt con người làm trung tâm.'],
        ['Bảo vệ chủ quyền biển đảo (Hoàng Sa – Trường Sa)', 'Tư liệu, châu bản, bản đồ cổ khẳng định chủ quyền từ thế kỉ XVII – XIX', 'Dùng **sử liệu gốc** làm chứng cứ pháp lí, kết hợp ngoại giao, pháp luật quốc tế và sức mạnh toàn dân.'],
        ['Phát triển du lịch nhưng di tích xuống cấp', 'Bài học “trùng tu sai” ở một số di tích; quá tải khách tại Hạ Long, Hội An, Tràng An', 'Cân bằng **bảo tồn – khai thác**: kiểm soát sức chứa, quy hoạch vùng đệm, tái đầu tư doanh thu vào trùng tu.'],
        ['Biến đổi khí hậu, lũ lụt miền Trung', 'Kinh nghiệm đắp đê, trị thuỷ, thuỷ lợi từ thời Lý – Trần – Nguyễn; hệ thống làng ven sông', 'Kết hợp tri thức bản địa với khoa học hiện đại: quy hoạch vùng ngập, rừng phòng hộ, cảnh báo sớm.'],
        ['Giữ gìn tiếng Việt, áo dài, ẩm thực, lễ hội', 'Quá trình hình thành chữ Quốc ngữ; các lễ hội, làng nghề truyền thống', 'Tự hào → giữ gìn → lan toả có chọn lọc; đưa di sản vào trường học, truyền thông số, sản phẩm sáng tạo.'],
        ['Tin giả, thông tin sai lệch trên mạng', 'Phương pháp phê phán sử liệu của Sử học; lịch sử được nhận thức có tính chủ quan', 'Kiểm chứng nguồn, đối chiếu chéo, đọc ngữ cảnh, không chia sẻ khi chưa xác thực.'],
        ['Hội nhập quốc tế, giao lưu văn hoá', 'Lịch sử tiếp nhận và “Việt Nam hoá” các giá trị văn hoá nước ngoài', 'Chủ động hội nhập nhưng giữ bản sắc: “hoà nhập mà không hoà tan”.'],
    ])

add('box', kind='key', title='CHÌA KHOÁ GHI NHỚ BÀI 2',
    items=[
        '**6 bước: Xác – Tìm – Thu – Sắp – Kiểm – Vận.** **4 loại sử liệu: Văn – Vật – Miệng – Ảnh/Số.** **2 cấp: Gốc – Thứ cấp.**',
        'Câu “vì sao học suốt đời?” phải có cụm **“vì tri thức lịch sử luôn được bổ sung, hiệu chỉnh”**. Câu “bản chất kết nối” phải có cụm **“chuyển hoá bài học thành hành động trong bối cảnh hiện tại, không áp đặt máy móc”**.',
    ])

# ---------------------------------------------------------------------
add('h2', title='1.3. BÀI 3 — Vai trò của Sử học (TRỌNG TÂM 57,5%)')

add('box', kind='warn', title='Đây là bài quan trọng nhất',
    items=[
        'Bài 3 góp **7 câu TN (I.14 – I.20) + 4 ý Đ/S (II.2a – d) + 1 câu tự luận 3,0 điểm** = **5,75/10 điểm**. Phần lớn điểm vận dụng của cả bài kiểm tra nằm ở đây. Hãy học kĩ 4 bảng dưới đây.',
    ])

add('h3', title='A. Mối quan hệ hai chiều: Sử học ↔ bảo tồn & phát huy giá trị di sản')

add('table', caption='Sơ đồ 1.4 – Vòng tròn “SỬ HỌC ↔ DI SẢN”', fontsize=8,
    cols=[116, 383], head=['Chiều tác động', 'Nội dung'], rows=[
        ['**Sử học → Di sản**\n(Cơ sở khoa học)',
         '① **Xác định giá trị**: nghiên cứu niên đại, nguồn gốc, bối cảnh, ý nghĩa → lập **hồ sơ khoa học**, xếp hạng di tích, lập hồ sơ trình UNESCO.\n② **Giải mã & phục dựng đúng**: chỉ ra cấu trúc gốc, vật liệu, kĩ thuật → trùng tu, tôn tạo không làm sai lệch.\n③ **Kể chuyện (storytelling)**: cung cấp nội dung thuyết minh, trưng bày bảo tàng, lễ hội, ấn phẩm, nội dung số → di sản “sống” lại trong tâm trí công chúng.\n④ **Nhận diện nguy cơ, đánh giá tác động** của du lịch, đô thị hoá, khí hậu → đề xuất chính sách bảo vệ.'],
        ['**Di sản → Sử học**\n(Nguồn sử liệu)',
         '① Di tích, cổ vật, bia kí là **sử liệu hiện vật/gốc** giúp kiểm chứng, bổ sung, hiệu chỉnh tri thức lịch sử.\n② Di sản phi vật thể (lời kể, dân ca, nghi lễ) là **sử liệu truyền miệng** giúp hiểu đời sống tinh thần của người xưa.\n③ Chính vì vậy, **mất di sản = mất chứng cứ lịch sử**.'],
        ['**Kết luận (câu “vàng”)**',
         '**“Không có Sử học, di sản chỉ là những vật thể vô hồn; không có di sản, Sử học thiếu bằng chứng để nói về quá khứ.”** Bảo tồn không phải là “cất kĩ trong kho”, mà là **giữ lại giá trị gốc rồi phát huy nó một cách bền vững**.'],
    ])

add('box', kind='note', title='Phân biệt nhanh 2 từ hay nhầm',
    items=[
        '**BẢO TỒN** = giữ gìn, bảo vệ nguyên trạng, ngăn xuống cấp (khâu “giữ”). Ví dụ: lập hồ sơ, xếp hạng, số hoá, trùng tu đúng nguyên tắc, cấm xâm lấn.',
        '**PHÁT HUY** = đưa giá trị di sản vào đời sống hôm nay (khâu “dùng”). Ví dụ: thuyết minh, lễ hội có kiểm soát, giáo dục di sản, du lịch bền vững, sản phẩm sáng tạo.',
        '**Ghi nhớ:** “Bảo tồn là gốc, phát huy là ngọn; phát huy mà quên bảo tồn thì di sản sẽ chết dần”.',
    ])

add('h3', title='B. Hệ thống phân loại di sản (bắt buộc thuộc — câu I.14, I.15, TL)')

add('table', caption='Bảng 1.6 – Các loại hình di sản (theo Luật Di sản văn hoá & UNESCO)', fontsize=7.6,
    cols=[96, 165, 238], head=['Loại hình', 'Bao gồm', 'Ví dụ Việt Nam'], rows=[
        ['**DI SẢN VĂN HOÁ VẬT THỂ**', 'Di tích lịch sử – văn hoá; danh lam thắng cảnh; cổ vật; bảo vật quốc gia. Là sản phẩm **vật chất** có giá trị lịch sử, văn hoá, khoa học.', 'Hoàng thành Thăng Long; Văn Miếu – Quốc Tử Giám và bia tiến sĩ; Cố đô Huế; phố cổ Hội An; Thánh địa Mỹ Sơn; Thành nhà Hồ; chùa Bút Tháp; trống đồng Đông Sơn; tượng A Di Đà chùa Phật Tích.'],
        ['**DI SẢN VĂN HOÁ PHI VẬT THỂ**', 'Tiếng nói, chữ viết; tác phẩm văn học, nghệ thuật, khoa học; ngôn ngữ và chữ viết của các dân tộc; tín ngưỡng, tôn giáo; lễ hội; dân ca, dân nhạc, dân vũ, sân khấu truyền thống; nghề thủ công; tri thức dân gian (y học, ẩm thực, trang phục); trò chơi dân gian.', 'Nhã nhạc cung đình Huế; Quan họ Bắc Ninh; Ca trù; Hát Xoan Phú Thọ; **Dân ca Ví, Giặm Nghệ Tĩnh**; Đờn ca tài tử Nam Bộ; Không gian văn hoá Cồng chiêng Tây Nguyên; Tín ngưỡng thờ cúng Hùng Vương; Lễ hội Gióng; múa rối nước; nghề gốm Bát Tràng; áo dài Việt Nam.'],
        ['**DI SẢN THIÊN NHIÊN**', 'Cảnh quan thiên nhiên, vườn quốc gia, khu bảo tồn, hệ sinh thái, di chỉ địa chất – sinh thái có giá trị đặc biệt về khoa học, thẩm mĩ, đa dạng sinh học.', '**Di sản thiên nhiên thế giới:** Vịnh Hạ Long, Vườn quốc gia Phong Nha – Kẻ Bàng. **Theo nghĩa rộng** (vườn quốc gia, khu dự trữ sinh quyển, công viên địa chất UNESCO ở cấp quốc gia/khu vực): Cúc Phương, Cát Bà, Cao nguyên đá Đồng Văn, rừng ngập mặn Cần Giờ, U Minh Thượng, Pù Mát (Nghệ An).'],
        ['**DI SẢN HỖN HỢP**', 'Vừa có giá trị văn hoá vừa có giá trị thiên nhiên.', '**Quần thể danh thắng Tràng An (Ninh Bình)** — di sản thế giới hỗn hợp đầu tiên của Việt Nam (UNESCO, 2014).'],
        ['**DI SẢN TƯ LIỆU**', 'Tài liệu lưu trữ có giá trị đặc biệt (Chương trình Kí ức thế giới của UNESCO).', 'Mộc bản triều Nguyễn; Châu bản triều Nguyễn; Bia tiến sĩ Văn Miếu – Quốc Tử Giám; Mộc bản kinh Phật chùa Vĩnh Nghiêm; Thơ văn trên kiến trúc cung đình Huế.'],
    ])

add('box', kind='exam', title='Mẹo phân biệt VẬT THỂ / PHI VẬT THỂ (câu I.14 rất hay hỏi)',
    items=[
        '**Có thể cầm, sờ, chụp ảnh được (đình, chùa, thành, tượng, bia, cổ vật) → VẬT THỂ.**',
        '**Là lời, nhạc, điệu múa, nghi lễ, kĩ năng, tri thức (hát, kể, làm, tin, chơi) → PHI VẬT THỂ.**',
        'Bẫy: “**Bia tiến sĩ**” là vật thể, nhưng “**nghề khắc chữ**” là phi vật thể; “**đình làng**” là vật thể, nhưng “**lễ hội đình làng**” là phi vật thể.',
    ])

add('h3', title='C. Địa danh là tài nguyên du lịch của Việt Nam (yêu cầu “kể tên”)')

add('table', caption='Bảng 1.7 – Bản đồ du lịch di sản 3 miền', fontsize=7.7,
    cols=[76, 180, 243], head=['Vùng', 'Địa danh tiêu biểu', 'Giá trị / di sản liên quan'], rows=[
        ['**MIỀN BẮC**', 'Vịnh Hạ Long (Quảng Ninh); Hoàng thành Thăng Long, Văn Miếu – Quốc Tử Giám, Hồ Gươm (Hà Nội); Tràng An – Tam Cốc – Bích Động, chùa Bái Đính (Ninh Bình); Sa Pa – Fansipan (Lào Cai); Cát Bà (Hải Phòng); Cúc Phương (Ninh Bình); Cao nguyên đá Đồng Văn (Hà Giang); Mộc Châu (Sơn La); chùa Hương; Đền Hùng (Phú Thọ).', 'Di sản thiên nhiên thế giới (Hạ Long); di sản văn hoá thế giới (Thăng Long); **di sản hỗn hợp (Tràng An)**; tín ngưỡng thờ cúng Hùng Vương; công viên địa chất toàn cầu (Đồng Văn).'],
        ['**MIỀN TRUNG**', 'Phong Nha – Kẻ Bàng, động Thiên Đường (Quảng Bình); Cố đô Huế (Thừa Thiên Huế); phố cổ Hội An, Thánh địa Mỹ Sơn (Quảng Nam); Đà Nẵng – Bà Nà, Ngũ Hành Sơn; Thành cổ Quảng Trị, địa đạo Vịnh Mốc; **Kim Liên – quê hương Chủ tịch Hồ Chí Minh, Ngã ba Đồng Lộc, Pù Mát, Cửa Lò (Nghệ An – Hà Tĩnh)**; Thành nhà Hồ, Pù Luông, Sầm Sơn (Thanh Hoá); Gành Đá Đĩa (Phú Yên); Kỳ Co – Eo Gió (Bình Định).', 'Di sản thiên nhiên thế giới (Phong Nha – Kẻ Bàng); di sản văn hoá thế giới (Huế, Hội An, Mỹ Sơn, Thành nhà Hồ); Nhã nhạc cung đình Huế; **Dân ca Ví, Giặm Nghệ Tĩnh**; di tích lịch sử cách mạng.'],
        ['**MIỀN NAM**', 'Dinh Độc Lập, địa đạo Củ Chi, chợ Bến Thành, rừng ngập mặn Cần Giờ (TP. Hồ Chí Minh); chợ nổi Cái Răng, bến Ninh Kiều (Cần Thơ); Phú Quốc (Kiên Giang); Côn Đảo (Bà Rịa – Vũng Tàu); Đà Lạt (Lâm Đồng); Nha Trang – vịnh Vân Phong (Khánh Hòa); Mũi Né – Phan Thiết (Bình Thuận); núi Bà Đen (Tây Ninh); U Minh Thượng, mũi Cà Mau (Cà Mau); Bạc Liêu; vườn trái cây miền Tây.', 'Đờn ca tài tử Nam Bộ (phi vật thể); di tích lịch sử cách mạng (Củ Chi, Côn Đảo); cảnh quan thiên nhiên và du lịch sinh thái Đồng bằng sông Cửu Long; Không gian văn hoá Cồng chiêng Tây Nguyên (Lâm Đồng, vùng lân cận).'],
    ])

add('box', kind='key', title='CHÌA KHOÁ GHI NHỚ ĐỊA DANH',
    items=[
        'Nhớ cặp **“BẮC: Hạ Long – Thăng Long – Tràng An”**, **“TRUNG: Phong Nha – Huế – Hội An – Mỹ Sơn”**, **“NAM: Củ Chi – Cần Thơ – Phú Quốc”**.',
        'Ba “mỏ vàng” của du lịch di sản Việt Nam: **Vịnh Hạ Long (thiên nhiên)**, **Quần thể danh thắng Tràng An (hỗn hợp)**, **Cố đô Huế (văn hoá, phi vật thể + vật thể)**.',
        'Học sinh Nghệ An – Hà Tĩnh nhớ thêm: **Kim Liên, Ngã ba Đồng Lộc, Pù Mát, Cửa Lò, Dân ca Ví Giặm** — rất thuận lợi khi lấy ví dụ “địa phương em” trong câu tự luận.',
    ])

add('h3', title='D. Vai trò của lịch sử – văn hoá đối với sự phát triển du lịch')

add('num', items=[
    '**Tạo sản phẩm du lịch đặc thù, khác biệt:** di tích, lễ hội, làng nghề, ẩm thực, trang phục, dân ca trở thành **điểm nhấn** không nơi nào sao chép được (du lịch di sản, du lịch tâm linh, du lịch cộng đồng).',
    '**Tăng sức hút và giá trị trải nghiệm:** du khách không chỉ “ngắm” mà còn được “nghe – hiểu – tham gia” (thuyết minh, tái hiện nghi lễ, trải nghiệm nghề truyền thống) → ở lâu hơn, chi tiêu nhiều hơn.',
    '**Xây dựng thương hiệu, hình ảnh quốc gia:** Festival Huế, đêm phố cổ Hội An, áo dài, ẩm thực Việt giúp quảng bá Việt Nam ra thế giới, thu hút khách quốc tế và đầu tư.',
    '**Tạo việc làm, tăng thu nhập, giảm nghèo:** hướng dẫn viên, nghệ nhân, homestay, quà lưu niệm, dịch vụ ăn uống, vận tải… phát triển quanh điểm di sản.',
    '**Tạo nguồn lực tài chính tái đầu tư cho bảo tồn:** vé tham quan, phí dịch vụ, tài trợ, ngân sách từ thuế du lịch được dùng để trùng tu, quản lí, số hoá.',
    '**Khơi dậy tự hào, gắn kết cộng đồng:** khi di sản “có giá trị”, người dân địa phương trở thành chủ thể bảo vệ và truyền dạy tri thức cho thế hệ trẻ.',
    '**Thúc đẩy hạ tầng và chuyển dịch cơ cấu kinh tế:** giao thông, điện, nước, viễn thông, dịch vụ được cải thiện; nhiều địa phương chuyển từ nông nghiệp thuần tuý sang kinh tế dịch vụ – di sản.',
])

add('h3', title='E. Tác động HAI MẶT của du lịch đối với công tác bảo tồn di tích')

add('table', caption='Bảng 1.8 – Du lịch: “vừa cứu di tích, vừa làm di tích đau”', fontsize=7.7,
    cols=[48, 222, 229], head=['Mặt', 'TÁC ĐỘNG TÍCH CỰC', 'TÁC ĐỘNG TIÊU CỰC'], rows=[
        ['**Kinh tế**', 'Nguồn thu từ vé, dịch vụ, lưu trú; việc làm cho cộng đồng; có tiền trùng tu, tôn tạo, quản lí.', '**Thương mại hoá quá mức**: hàng quán, gian hàng lấn chiếm sân đình, chợ hoá không gian thiêng; tăng giá đất, đẩy cư dân bản địa ra khỏi vùng lõi.'],
        ['**Vật lí**', 'Hạ tầng được nâng cấp; di tích được quan tâm sửa chữa, chiếu sáng, bảo vệ an ninh.', '**Quá tải sức chứa**: đám đông làm mòn bậc thang, ẩm mốc, rung lắc công trình; rác thải, khí thải, tiếng ồn; sờ, leo, khắc, vẽ bậy lên cổ vật.'],
        ['**Ý nghĩa**', 'Thuyết minh, tái hiện lễ hội, bảo tàng giúp giá trị lịch sử được nhiều người biết đến.', '**“Disney hoá”**: dựng mới, sơn lại, “làm giả cổ”, biến nghi lễ thành show diễn → mất yếu tố gốc, sai lệch lịch sử, biến tướng tín ngưỡng.'],
        ['**Quản lí**', 'Địa phương có động lực lập hồ sơ, xếp hạng, quy hoạch, hợp tác UNESCO; nâng cao nhận thức cộng đồng.', 'Xây dựng công trình cao tầng, bãi đỗ xe, khách sạn **xâm lấn vùng lõi/vùng đệm**, phá vỡ cảnh quan; thiếu quy chế → xuống cấp khó đảo ngược.'],
        ['**Xã hội**', 'Nghề truyền thống, ẩm thực, dân ca được “sống lại” nhờ du khách.', 'Chảy máu lao động, phân hoá lợi ích, mâu thuẫn giữa doanh nghiệp và cộng đồng; du khách thiếu ý thức gây phản cảm.'],
    ])

add('box', kind='key', title='Câu kết luận “ăn điểm” cho mọi câu phân tích',
    items=[
        '**“Du lịch không phải là kẻ thù của bảo tồn, nhưng du lịch thiếu kiểm soát thì là kẻ thù số một. Vấn đề không phải là có đón khách hay không, mà là đón bao nhiêu, đón như thế nào và dùng lợi ích thu được vào việc gì.”**',
    ])

add('h3', title='F. 6 nhóm biện pháp bảo tồn & phát huy giá trị di sản')

add('table', caption='Bảng 1.9 – Khung “PHÁP – KIỂM – TRÙNG – GIÁO – DU LỊCH – CHUNG TAY”', fontsize=7.7,
    cols=[112, 208, 179], head=['Nhóm biện pháp', 'Việc cần làm cụ thể', 'Lí do / tác dụng'], rows=[
        ['**1. PHÁP – QUY HOẠCH**', 'Rà soát, hoàn thiện pháp luật, quy chế quản lí; phân định rõ **vùng lõi – vùng đệm**; kiểm soát xây dựng; xử phạt nghiêm hành vi xâm phạm, vẽ bậy, mua bán cổ vật.', 'Tạo “hàng rào” pháp lí, ngăn xâm lấn ngay từ đầu.'],
        ['**2. KIỂM KÊ – SỐ HOÁ**', 'Điều tra, kiểm kê, lập **hồ sơ khoa học**, xếp hạng di tích; số hoá tài liệu, quét 3D, xây dựng cơ sở dữ liệu, lưu trữ và phục chế cổ vật; đào tạo cán bộ quản lí.', 'Giữ lại thông tin vĩnh viễn ngay cả khi hiện vật bị hư hại; phục vụ nghiên cứu và thuyết minh.'],
        ['**3. TRÙNG TU ĐÚNG**', 'Giữ tối đa **yếu tố gốc**; dùng vật liệu, kĩ thuật truyền thống; có chuyên gia Sử học, kiến trúc, khảo cổ giám sát; không “làm mới”, không sơn sửa tuỳ tiện; chống ẩm, mối mọt, sạt lở.', 'Tránh biến di tích thật thành “đồ giả cổ”.'],
        ['**4. GIÁO DỤC – TRUYỀN THÔNG**', 'Đưa nội dung di sản vào trường học, câu lạc bộ, bảo tàng; thuyết minh đa ngôn ngữ; làm phim, podcast, triển lãm số; tuyên truyền quy tắc ứng xử; **vận động mọi người xung quanh cùng bảo vệ**.', 'Biến kiến thức thành **ý thức và hành động** của cả cộng đồng — đúng yêu cầu NL3 của đề.'],
        ['**5. DU LỊCH BỀN VỮNG**', 'Khảo sát **sức chứa**, giới hạn số khách/ngày, đặt lịch phân luồng; bán vé, thu phí tham quan; quy chuẩn ứng xử; cấm hàng quán trong vùng lõi; chia sẻ lợi ích với người dân; **tái đầu tư doanh thu** vào trùng tu.', 'Vừa có tiền vừa giảm áp lực lên di tích.'],
        ['**6. CHUNG TAY – HỢP TÁC**', 'Huy động ngân sách + xã hội hoá + tài trợ doanh nghiệp; hợp tác UNESCO, ICOMOS, các tổ chức quốc tế; phát triển sinh kế từ nghề truyền thống; khuyến khích thanh niên tham gia tình nguyện “trông coi di sản”.', 'Tạo nguồn lực và sức mạnh lâu dài; di sản sống cùng cộng đồng.'],
    ])

add('box', kind='tip', title='Cách “nhân đôi” điểm biện pháp',
    items=[
        'Đừng chỉ viết “cần tuyên truyền, cần trùng tu”. Hãy thêm **ai làm – làm thế nào – lấy tiền đâu – đo lường ra sao**. Ví dụ: “Chính quyền xã phối hợp với trường THPT lập **câu lạc bộ di sản**, mỗi tháng **2 buổi** dọn vệ sinh và thuyết minh cho khách, kinh phí từ **30% doanh thu vé tham quan**”. Một biện pháp có đủ 4 yếu tố này luôn được điểm tối đa.',
    ])

add('h3', title='G. Khung trả lời câu TỰ LUẬN 3,0 điểm (NL1–Biết 1,0đ + NL3–VD 2,0đ)')

add('table', caption='Bảng 1.10 – Cấu trúc bài viết “NHẬN DIỆN → ĐÁNH GIÁ → HÀNH ĐỘNG”', fontsize=8,
    cols=[76, 68, 355], head=['Phần', 'Điểm', 'Nội dung bắt buộc phải có'], rows=[
        ['**Mở bài**', '~0,25đ', 'Nêu tên di tích/di sản được chọn, vị trí, loại hình, giá trị nổi bật.'],
        ['**Ý 1 · Nhận diện**', '**1,0đ**', 'Khái niệm di sản văn hoá/di sản thiên nhiên; kể tên **ít nhất 3 loại hình** (vật thể, phi vật thể, thiên nhiên, hỗn hợp, tư liệu) kèm ví dụ; nêu **mối quan hệ Sử học – bảo tồn** (Sử học giúp xác định giá trị, lập hồ sơ, giải mã, phục dựng).'],
        ['**Ý 2 · Đánh giá**', '~0,75đ', 'Phân tích **tác động 2 mặt** của du lịch: ít nhất 2 tích cực (nguồn thu, việc làm, quảng bá, động lực trùng tu) và 2 tiêu cực (quá tải, rác thải, thương mại hoá, làm giả/xuyên tạc, xâm lấn cảnh quan).'],
        ['**Ý 2 · Giải pháp**', '~1,0đ', '**Ít nhất 4 biện pháp** thuộc 4 nhóm khác nhau trong Bảng 1.9; mỗi biện pháp có “ai làm – làm thế nào”.'],
        ['**Kết bài**', '~0,25đ', 'Khẳng định vai trò của **cộng đồng và bản thân học sinh**; lời kêu gọi hành động (tìm hiểu, tuyên truyền, không vẽ bậy, tham gia câu lạc bộ di sản...).'],
        ['**5 TỪ KHOÁ VÀNG**', '—', '**DI SẢN – GIÁ TRỊ GỐC – TÁC ĐỘNG HAI CHIỀU – GIẢI PHÁP CỤ THỂ – CỘNG ĐỒNG.** Bài viết ngắn nhưng phải đủ 5 từ khoá này; thiếu “giá trị gốc” hoặc “cộng đồng” thường mất 0,25–0,5 điểm.'],
    ])

# =====================================================================
# PHAN 2 - CONG CU GHI NHO
# =====================================================================
add('pb')
add('h1', n='PHẦN 2', title='CÔNG CỤ GHI NHỚ TỐI ƯU',
    sub='Từ khoá · flashcard · bảng dễ nhầm · lịch ôn 7 ngày')

add('h2', title='2.1. Hệ thống 12 “chìa khoá” tóm tắt toàn bộ chương trình')

add('table', caption='Bảng 2.1 – Một cụm từ nhớ cả chuỗi kiến thức', fontsize=7.9,
    cols=[62, 138, 299], head=['Bài', 'Chìa khoá', 'Mở ra điều gì'], rows=[
        ['Bài 1', '**ĐỐI – 3C – 4N**', 'Đối tượng · 3 Chức năng (Nhận thức, Giáo dục, Dự báo) · 4 Nhiệm vụ (Thu thập, Phục dựng, Giải thích, Truyền bá).'],
        ['Bài 1', '**KHÁCH ↔ CHỦ**', 'Hiện thực lịch sử = khách quan; lịch sử được nhận thức = chủ quan.'],
        ['Bài 1', '**CHỦ – THIẾU – ĐA – BIẾN – XÃ**', '5 đặc điểm của lịch sử được con người nhận thức.'],
        ['Bài 1', '**“Đã xảy ra” / “Được kể lại”**', 'Công thức phân biệt hiện thực và nhận thức trong mọi tình huống.'],
        ['Bài 2', '**X – T – T – S – K – V**', 'Xác định – Tìm nguồn – Thu thập – Sắp xếp – Kiểm chứng – Vận dụng.'],
        ['Bài 2', '**VĂN – VẬT – MIỆNG – ẢNH**', '4 loại hình sử liệu.'],
        ['Bài 2', '**GỐC – THỨ CẤP**', '2 cấp độ tin cậy của sử liệu.'],
        ['Bài 2', '**HIỂU – SO – LÀM**', 'Bản chất kết nối tri thức lịch sử vào cuộc sống.'],
        ['Bài 2', '**“CẬP NHẬT SUỐT ĐỜI”**', 'Lí do phải học lịch sử suốt đời (vì tri thức luôn được bổ sung, hiệu chỉnh).'],
        ['Bài 3', '**VẬT – PHI – THIÊN – HỖN – TƯ**', '5 loại hình di sản (vật thể, phi vật thể, thiên nhiên, hỗn hợp, tư liệu).'],
        ['Bài 3', '**SỬ HỌC ↔ DI SẢN**', 'Sử học là cơ sở khoa học; di sản là nguồn sử liệu — quan hệ hai chiều.'],
        ['Bài 3', '**PHÁP – KIỂM – TRÙNG – GIÁO – DU LỊCH – CHUNG TAY**', '6 nhóm biện pháp bảo tồn & phát huy giá trị di sản.'],
    ])

add('h2', title='2.2. Bảng “CẶP DỄ NHẦM” — đọc trước khi vào phòng thi')

add('table', caption='Bảng 2.2 – 10 cặp khái niệm hay bị đảo', fontsize=7.8,
    cols=[103, 192, 204], head=['Cặp khái niệm', 'Vế trái', 'Vế phải'], rows=[
        ['Lịch sử ↔ Sử học', '**Lịch sử** = cái đã xảy ra (đối tượng).', '**Sử học** = khoa học nghiên cứu cái đó (môn học).'],
        ['Hiện thực ↔ Nhận thức', '**Hiện thực** = khách quan, duy nhất, không đổi.', '**Nhận thức** = chủ quan, nhiều cách kể, thay đổi được.'],
        ['Chức năng ↔ Nhiệm vụ', '**Chức năng** = tác dụng với xã hội (Nhận thức, Giáo dục, Dự báo).', '**Nhiệm vụ** = việc Sử học phải làm (Thu thập, Phục dựng, Giải thích, Truyền bá).'],
        ['Sử liệu gốc ↔ thứ cấp', '**Gốc** = cùng thời, nguyên bản, người chứng kiến.', '**Thứ cấp** = chép lại, biên soạn lại, bình luận lại.'],
        ['Thu thập ↔ Xử lí', '**Thu thập** = tìm, chép, chụp, ghi âm.', '**Xử lí** = phân loại, đối chiếu, kiểm chứng, đánh giá.'],
        ['Vật thể ↔ Phi vật thể', '**Vật thể** = đình, chùa, thành, bia, cổ vật.', '**Phi vật thể** = dân ca, lễ hội, nghi lễ, nghề, tri thức.'],
        ['Di tích ↔ Danh lam', '**Di tích lịch sử – văn hoá** = công trình/địa điểm gắn sự kiện, nhân vật lịch sử.', '**Danh lam thắng cảnh** = cảnh quan thiên nhiên hoặc có công trình đẹp, có giá trị thẩm mĩ; cả hai đều là di sản vật thể.'],
        ['Bảo tồn ↔ Phát huy', '**Bảo tồn** = giữ nguyên trạng, chống xuống cấp.', '**Phát huy** = đưa giá trị vào đời sống (thuyết minh, lễ hội, giáo dục, du lịch).'],
        ['Trùng tu ↔ Tôn tạo', '**Trùng tu** = sửa chữa, phục hồi lại phần hư hỏng theo nguyên bản.', '**Tôn tạo** = làm đẹp thêm, bổ sung cảnh quan; phải tôn trọng yếu tố gốc.'],
        ['Tác động tích cực ↔ tiêu cực', '**Tích cực** = tiền, việc làm, nhận thức, động lực trùng tu.', '**Tiêu cực** = quá tải, rác thải, thương mại hoá, làm giả, xâm lấn.'],
    ])

add('h2', title='2.3. 24 thẻ ghi nhớ (flashcards) — che cột phải và tự trả lời')

add('cards', items=[
    ['Lịch sử (nghĩa hẹp) là gì?', 'Quá trình phát triển của xã hội loài người trong quá khứ.'],
    ['Sử học là gì?', 'Khoa học nghiên cứu, nhận thức lại và giải thích lịch sử dựa trên sử liệu.'],
    ['Đối tượng nghiên cứu của Sử học?', 'Hoạt động của con người và xã hội trong quá khứ, gắn với không gian, thời gian cụ thể.'],
    ['3 chức năng của Sử học?', 'Nhận thức – Giáo dục – Dự báo.'],
    ['4 nhiệm vụ của Sử học?', 'Thu thập sử liệu – Phục dựng hiện thực – Giải thích/đánh giá – Truyền bá tri thức.'],
    ['Hiện thực lịch sử là gì?', 'Sự thật khách quan đã xảy ra, độc lập với ý thức con người.'],
    ['Lịch sử được con người nhận thức là gì?', 'Sự phản ánh hiện thực lịch sử trong ý thức con người qua sử liệu, sách vở, lời kể.'],
    ['5 đặc điểm của lịch sử được nhận thức?', 'Chủ quan – Không đầy đủ – Đa dạng/đa chiều – Thay đổi – Xã hội.'],
    ['Vì sao có nhiều cách kể về một sự kiện?', 'Vì nhận thức lịch sử mang tính chủ quan, đa chiều và phụ thuộc vào sử liệu, góc nhìn.'],
    ['Phát hiện tư liệu mới sửa lại niên đại → đặc điểm gì?', 'Tính thay đổi (được bổ sung, hiệu chỉnh) của lịch sử được nhận thức.'],
    ['Sử liệu là gì?', 'Dấu tích của quá khứ còn lại, làm chứng cứ để nghiên cứu lịch sử.'],
    ['4 loại hình sử liệu?', 'Thành văn – Hiện vật (vật chất) – Truyền miệng – Hình ảnh/âm thanh/số.'],
    ['Sử liệu gốc khác thứ cấp thế nào?', 'Gốc: cùng thời, nguyên bản, do người chứng kiến tạo ra; thứ cấp: biên soạn/sao chép lại.'],
    ['6 bước xử lí thông tin, sử liệu?', 'Xác định – Tìm nguồn – Thu thập – Sắp xếp – Kiểm chứng – Vận dụng & chia sẻ.'],
    ['Bước quan trọng nhất để chống tin giả?', 'Kiểm chứng, đối chiếu chéo nhiều nguồn độc lập, ưu tiên nguồn gốc.'],
    ['Vì sao học lịch sử suốt đời?', 'Vì tri thức lịch sử luôn được bổ sung, hiệu chỉnh; đời sống luôn cần bài học quá khứ.'],
    ['Bản chất kết nối tri thức lịch sử vào cuộc sống?', 'Hiểu đúng – So đúng (không áp đặt) – Chuyển hoá thành hành động trong hiện tại.'],
    ['2 nhóm di sản văn hoá theo Luật?', 'Di sản văn hoá vật thể và di sản văn hoá phi vật thể.'],
    ['Di sản hỗn hợp đầu tiên của VN?', 'Quần thể danh thắng Tràng An (Ninh Bình), UNESCO 2014.'],
    ['Quan hệ Sử học – di sản?', 'Sử học là cơ sở khoa học để nhận diện giá trị, lập hồ sơ, phục dựng; di sản là nguồn sử liệu cho Sử học.'],
    ['4 nhóm biện pháp bảo tồn dễ nhớ nhất?', 'Pháp luật/quy hoạch – Kiểm kê/số hoá – Trùng tu đúng – Giáo dục/du lịch bền vững/cộng đồng.'],
    ['Tác động tiêu cực lớn nhất của du lịch?', 'Quá tải khách và thương mại hoá làm xuống cấp, biến dạng giá trị gốc.'],
    ['Cấu trúc câu TL 3,0 điểm?', 'Ý 1 (1,0đ) khái niệm + loại hình + quan hệ; Ý 2 (2,0đ) tác động 2 mặt + ≥4 biện pháp + cộng đồng.'],
    ['Phân bổ điểm 3 bài?', 'Bài 1: 1,5đ · Bài 2: 2,75đ · Bài 3: 5,75đ.'],
])

add('h2', title='2.4. Lịch ôn tập 7 ngày (lặp lại ngắt quãng – spaced repetition)')

add('table', caption='Bảng 2.3 – Kế hoạch 7 ngày, mỗi ngày 45–60 phút', fontsize=7.9,
    cols=[68, 118, 190, 123], head=['Ngày', 'Trọng tâm', 'Việc làm cụ thể', 'Ôn lại (5–10 phút)'], rows=[
        ['**Ngày 1**', 'Bài 1 – khái niệm', 'Đọc 1.1A–C; chép lại 5 định nghĩa và bảng ĐỐI–3C–4N vào giấy A4.', '—'],
        ['**Ngày 2**', 'Bài 1 – so sánh', 'Học Bảng 1.2, 1.3; tự giải thích lại 5 đặc điểm bằng ví dụ đời thường.', 'Ngày 1 (nhìn chìa khoá, tự kể).'],
        ['**Ngày 3**', 'Bài 2 – quy trình', 'Học 6 bước, Bảng 1.4; lấy 1 thông tin trên mạng và thực hành kiểm chứng chéo.', 'Ngày 1 + 2.'],
        ['**Ngày 4**', 'Bài 2 – vận dụng', 'Học Bảng 1.5; viết 3 đoạn 4–5 câu liên hệ thời sự.', 'Ngày 2 + 3.'],
        ['**Ngày 5**', 'Bài 3 – di sản', 'Học Bảng 1.6, 1.7; vẽ bản đồ 3 miền ghi 5 địa danh/miền.', 'Ngày 1 + 3 + 4.'],
        ['**Ngày 6**', 'Bài 3 – vận dụng', 'Học Bảng 1.8, 1.9, 1.10; **viết tay 1 bài TL hoàn chỉnh trong 13 phút**.', 'Ngày 2 + 4 + 5.'],
        ['**Ngày 7**', 'Tổng ôn & thử đề', 'Làm toàn bộ Phần 3 trong **đúng 45 phút**, tự chấm theo Phần 4; đọc lại Bảng 2.2.', 'Tất cả 12 chìa khoá ở 2.1.'],
    ])

add('box', kind='tip', title='4 kĩ thuật tự kiểm tra hiệu quả hơn đọc lại',
    items=[
        '**Blurting (nhớ rồi viết ra):** đọc 1 mục 3 phút → cất sách → viết lại mọi thứ nhớ được → so sánh và bổ sung phần thiếu (chỗ thiếu chính là chỗ cần học tiếp).',
        '**Feynman (dạy lại người khác):** giải thích “hiện thực lịch sử khác lịch sử được nhận thức thế nào?” cho một người không học sử, bằng ngôn ngữ đời thường. Nếu phải dùng từ sách → bạn chưa hiểu.',
        '**5W1H:** với mỗi sự kiện/di sản tự hỏi Ai – Cái gì – Khi nào – Ở đâu – Tại sao – Như thế nào.',
        '**Thẻ hỏi – đáp 2 mặt:** dùng 24 thẻ ở mục 2.3; thẻ nào trả lời chậm quá 5 giây → chuyển sang xếp ôn lại ngày hôm sau.',
    ])

# =====================================================================
# PHAN 3 - DE THI TAI TAO
# =====================================================================
add('pb')
add('h1', n='PHẦN 3', title='TOÀN BỘ CÂU HỎI TRONG ĐỀ KIỂM TRA',
    sub='28 lệnh hỏi trắc nghiệm + 1 câu tự luận · đúng mã câu của ma trận')

add('box', kind='note', title='Tính minh bạch của Phần 3',
    items=[
        'Như đã nói ở Phần 0, tệp DOCX gốc **không chứa câu hỏi nào**. Phần này là **bản tái tạo đầy đủ** của đề kiểm tra: giữ nguyên **số lượng, mã câu, bài, năng lực, cấp độ tư duy và yêu cầu cần đạt** theo đúng ma trận và bảng đặc tả. Mỗi câu đều có đáp án và giải thích ở **Phần 4**.',
        'Cách dùng: phô-tô/che Phần 4, bấm giờ **45 phút** và làm như một đề thi thật.',
    ])

add('h2', title='PHẦN I — 20 câu trắc nghiệm nhiều lựa chọn (5,0 điểm; mỗi câu 0,25 điểm)')

# ---- BAI 1 ----
add('h3', title='Nhóm Bài 1 (I.1 – I.6)')

add('mcq', code='I.1', meta='Bài 1 · NL1 · Biết',
     q='Trong SGK Lịch sử 10, **Sử học** được hiểu là gì?',
     opts=['A. Toàn bộ những sự kiện đã xảy ra trong quá khứ của tự nhiên và xã hội.',
           'B. Khoa học nghiên cứu về lịch sử, nhằm nhận thức, tái hiện và giải thích quá khứ của con người và xã hội loài người dựa trên sử liệu.',
           'C. Tập hợp những câu chuyện cổ tích, truyền thuyết được lưu truyền trong dân gian.',
           'D. Hoạt động sưu tầm, trưng bày các cổ vật trong bảo tàng.'],
     ans='B',
     why='**Sử học là khoa học nghiên cứu về lịch sử.** Phương án A là định nghĩa //lịch sử// (nghĩa rộng) – tức đối tượng chứ không phải môn khoa học. C là sử liệu truyền miệng, D là hoạt động bảo tồn, chỉ là một phần việc của ngành. **Mẹo:** “SỬ HỌC” luôn đi với cụm “khoa học nghiên cứu”.')

add('mcq', code='I.2', meta='Bài 1 · NL1 · Biết',
     q='**Đối tượng nghiên cứu chủ yếu của Sử học** là gì?',
     opts=['A. Toàn bộ vũ trụ, kể cả các hiện tượng thiên nhiên chưa có con người.',
           'B. Các hiện tượng tự nhiên như động đất, núi lửa, khí hậu trong quá khứ.',
           'C. Hoạt động của con người và xã hội loài người trong quá khứ, gắn với không gian, thời gian cụ thể.',
           'D. Tương lai của nhân loại được dự báo bằng trí tuệ nhân tạo.'],
     ans='C',
     why='Sử học nghiên cứu **quá khứ của con người và xã hội loài người** trên các lĩnh vực chính trị, kinh tế, văn hoá, xã hội, tư tưởng; luôn gắn với **không gian, thời gian xác định**. A, B thuộc khoa học tự nhiên; D là dự báo tương lai (chỉ là một //chức năng//, không phải đối tượng).')

add('mcq', code='I.3', meta='Bài 1 · NL1 · Biết',
     q='Nhóm từ nào dưới đây nêu đúng **3 chức năng cơ bản của Sử học**?',
     opts=['A. Thu thập – Phục dựng – Truyền bá.',
           'B. Nhận thức – Giáo dục – Dự báo.',
           'C. Sưu tầm – Trưng bày – Kinh doanh.',
           'D. Miêu tả – Tưởng tượng – Giải trí.'],
     ans='B',
     why='3 chức năng: **Nhận thức** (cung cấp tri thức), **Giáo dục** (bồi dưỡng đạo đức, yêu nước), **Dự báo** (từ quá khứ đoán xu hướng). Phương án A lại là **nhiệm vụ** của Sử học — đây là cái bẫy “chức năng ↔ nhiệm vụ” kinh điển. **Mẹo nhớ: N – G – D.**')

add('mcq', code='I.4', meta='Bài 1 · NL1 · Hiểu',
     q='Vì sao có thể khẳng định **Sử học là một khoa học**?',
     opts=['A. Vì Sử học kể lại được nhiều câu chuyện hấp dẫn về các danh nhân.',
           'B. Vì các nhà sử học luôn thống nhất với nhau về mọi sự kiện.',
           'C. Vì Sử học có đối tượng nghiên cứu riêng, dựa trên sử liệu được kiểm chứng, có phương pháp phê phán nguồn và hướng tới nhận thức khách quan, có thể kiểm chứng lại.',
           'D. Vì lịch sử được viết ra là hoàn toàn đúng và không bao giờ thay đổi.'],
     ans='C',
     why='Một ngành được gọi là khoa học khi có **đối tượng riêng**, **nguồn dữ liệu (sử liệu)**, **phương pháp (kiểm chứng, đối chiếu, phê phán nguồn)** và **khả năng kiểm chứng/hiệu chỉnh**. B và D sai vì lịch sử được nhận thức vừa **đa chiều** vừa **có thể thay đổi**; A chỉ là chức năng giải trí.')

add('mcq', code='I.5', meta='Bài 1 · NL2 · Hiểu',
     q='Bạn Minh đọc một cuốn sách viết về cuộc khởi nghĩa Lam Sơn (1418 – 1427). Trong trường hợp này, “cuộc khởi nghĩa Lam Sơn đã thật sự diễn ra” và “lời kể trong cuốn sách” lần lượt là:',
     opts=['A. Lịch sử được con người nhận thức / hiện thực lịch sử.',
           'B. Hiện thực lịch sử / lịch sử được con người nhận thức.',
           'C. Sử liệu gốc / sử liệu thứ cấp.',
           'D. Chức năng / nhiệm vụ của Sử học.'],
     ans='B',
     why='**Cái đã xảy ra = hiện thực lịch sử (khách quan). Cái được kể lại = lịch sử được con người nhận thức (chủ quan).** C sai vì cuốn sách là sử liệu //thứ cấp//, còn bản thân sự kiện không phải sử liệu. **Công thức: “đã xảy ra” → hiện thực; “được kể/ghi/chép” → nhận thức.**')

add('mcq', code='I.6', meta='Bài 1 · NL2 · Hiểu',
     q='Các nhà khảo cổ vừa phát hiện một tấm bia đá thời Trần, theo đó phải **sửa lại niên đại** của một sự kiện vốn được ghi trong sách cũ. Trường hợp này thể hiện rõ nhất đặc điểm nào của lịch sử được con người nhận thức?',
     opts=['A. Tính khách quan tuyệt đối.',
           'B. Tính duy nhất, không lặp lại.',
           'C. Tính thay đổi – được bổ sung, hiệu chỉnh khi có sử liệu mới.',
           'D. Tính độc lập với ý thức con người.'],
     ans='C',
     why='Khi có **sử liệu mới**, nhận thức cũ được **bổ sung, chỉnh sửa** → **tính thay đổi**. A, B, D là đặc điểm của **hiện thực lịch sử**, không phải của lịch sử được nhận thức. Đây chính là lí do phải **học lịch sử suốt đời** (liên kết sang Bài 2).')

# ---- BAI 2 ----
add('h3', title='Nhóm Bài 2 (I.7 – I.13)')

add('mcq', code='I.7', meta='Bài 2 · NL1 · Biết',
     q='**Bước đầu tiên** trong quy trình thu thập, xử lí thông tin và sử liệu là:',
     opts=['A. Tìm kiếm thật nhiều tài liệu trên Internet.',
           'B. Chụp ảnh, ghi chép ngay mọi thứ nhìn thấy.',
           'C. Xác định nhiệm vụ, đề tài và câu hỏi nghiên cứu cần trả lời.',
           'D. Viết ngay báo cáo kết quả để còn nộp đúng hạn.'],
     ans='C',
     why='Quy trình **X – T – T – S – K – V** bắt đầu bằng **Xác định nhiệm vụ** (đề tài, câu hỏi 5W1H, phạm vi). Chưa biết cần trả lời điều gì thì không thể chọn nguồn. Đây là câu “bước đầu tiên” rất hay bị chọn nhầm sang A.')

add('mcq', code='I.8', meta='Bài 2 · NL1 · Biết',
     q='Trong các tư liệu dưới đây, đâu là **sử liệu gốc**?',
     opts=['A. Một bài blog viết năm 2024 kể về năm 1946.',
           'B. Một bộ phim tài liệu sản xuất năm 2020 về năm 1946.',
           'C. Bức thư do chính một người lính viết tay vào tháng 12 năm 1946, còn giữ được bản gốc.',
           'D. Chương trong SGK Lịch sử 10 viết về năm 1946.'],
     ans='C',
     why='**Sử liệu gốc = cùng thời sự kiện, do người trực tiếp chứng kiến tạo ra, còn nguyên bản.** A, B, D đều là sử liệu **thứ cấp** (biên soạn, kể lại, tái hiện sau này). **Mẹo: hỏi “ai viết, viết khi nào?”**.')

add('mcq', code='I.9', meta='Bài 2 · NL1 · Biết',
     q='Cách làm **đúng** khi một học sinh gặp thông tin lịch sử gây tranh cãi trên mạng xã hội là:',
     opts=['A. Tin ngay vì bài viết có hàng nghìn lượt chia sẻ.',
           'B. Bỏ qua vì thông tin trên mạng không bao giờ đáng tin.',
           'C. Đối chiếu với ít nhất 2 – 3 nguồn độc lập, ưu tiên nguồn gốc, kiểm tra tác giả, thời điểm và ngữ cảnh trước khi kết luận.',
           'D. Sửa lại thông tin theo trí nhớ cá nhân rồi đăng lại.'],
     ans='C',
     why='Nguyên tắc vàng của Bài 2: **kiểm chứng chéo + ưu tiên nguồn gốc + xét ngữ cảnh**. A là “tin theo đám đông”, B là cực đoan (mạng vẫn có nguồn tốt, chỉ cần kiểm chứng), D là tự ý bịa lại thông tin.')

add('mcq', code='I.10', meta='Bài 2 · NL1 · Hiểu',
     q='Giải thích nào **đúng nhất** về sự cần thiết phải học tập và khám phá lịch sử **suốt đời**?',
     opts=['A. Vì lịch sử là môn học bắt buộc phải thi tốt nghiệp.',
           'B. Vì quá khứ có thể thay đổi theo thời gian nên cần phải viết lại nó mỗi năm.',
           'C. Vì tri thức lịch sử luôn được bổ sung, hiệu chỉnh khi có sử liệu và phương pháp mới, đồng thời cuộc sống luôn đặt ra những vấn đề mới cần bài học từ quá khứ.',
           'D. Vì các nhà sử học chưa bao giờ thống nhất được với nhau.'],
     ans='C',
     why='C nối được 2 ý: (1) **tính thay đổi của lịch sử được nhận thức** → tri thức không bao giờ “xong”; (2) **thực tiễn luôn đổi mới** → cần bài học quá khứ. B sai vì **hiện thực lịch sử không đổi**, chỉ có nhận thức về nó đổi. A, D là lí do bề mặt.')

add('mcq', code='I.11', meta='Bài 2 · NL1 · Hiểu',
     q='**Bản chất** của việc kết nối tri thức, bài học lịch sử vào cuộc sống là:',
     opts=['A. Học thuộc lòng nhiều mốc năm để kể lại cho người khác nghe.',
           'B. Hiểu đúng bài học quá khứ, đối chiếu với bối cảnh hiện tại rồi chuyển hoá thành thái độ và hành động phù hợp, không áp đặt máy móc.',
           'C. Dùng sự kiện lịch sử để chứng minh mọi quan điểm cá nhân đều đúng.',
           'D. Thay thế các kiến thức khoa học hiện đại bằng kinh nghiệm của người xưa.'],
     ans='B',
     why='Công thức **HIỂU – SO – LÀM**. A mới dừng ở mức ghi nhớ; C là xuyên tạc lịch sử; D là cực đoan, phản khoa học. Cụm từ ăn điểm: **“chuyển hoá thành hành động, không áp đặt máy móc”.**')

add('mcq', code='I.12', meta='Bài 2 · NL2 · Biết',
     q='Tư liệu nào sau đây thuộc loại **sử liệu truyền miệng**?',
     opts=['A. Tấm bia đá khắc năm 1484 tại Văn Miếu.',
           'B. Truyền thuyết Sơn Tinh – Thủy Tinh được ông bà kể lại cho con cháu qua nhiều đời.',
           'C. Chiếc trống đồng Đông Sơn được khai quật năm 1924.',
           'D. Bức ảnh chụp năm 1954 tại chiến trường Điện Biên Phủ.'],
     ans='B',
     why='**Truyền miệng = lời kể, kí ức, truyền thuyết, dân ca, lời nhân chứng.** A là sử liệu thành văn, C là hiện vật, D là hình ảnh. **Mẹo: “nghe bằng tai” → truyền miệng; “nhìn bằng mắt” → hiện vật; “đọc bằng chữ” → thành văn.**')

add('mcq', code='I.13', meta='Bài 2 · NL2 · Biết',
     q='Hoạt động nào sau đây thuộc **giai đoạn xử lí** thông tin, sử liệu (không phải giai đoạn thu thập)?',
     opts=['A. Phỏng vấn cụ ông 85 tuổi ở địa phương.',
           'B. Chụp ảnh lại tấm bia đá trong đình làng.',
           'C. Đối chiếu lời kể với văn bản lưu trữ để đánh giá độ tin cậy, rồi phân loại theo chủ đề.',
           'D. Tải tài liệu từ thư viện số về máy tính.'],
     ans='C',
     why='**Xử lí = phân loại, sắp xếp, đối chiếu, kiểm chứng, đánh giá.** A, B, D đều là **thu thập** (lấy thông tin về). Câu này kiểm tra NL2 ở mức nhận biết — hãy nhớ cặp “**lấy về ↔ soi lại**”.')

# ---- BAI 3 ----
add('h3', title='Nhóm Bài 3 (I.14 – I.20)')

add('mcq', code='I.14', meta='Bài 3 · NL1 · Biết',
     q='Theo Luật Di sản văn hoá Việt Nam, di sản văn hoá được chia thành hai loại hình chính là:',
     opts=['A. Di sản văn hoá vật thể và di sản văn hoá phi vật thể.',
           'B. Di sản văn hoá và di sản thiên nhiên.',
           'C. Di tích lịch sử và danh lam thắng cảnh.',
           'D. Di sản quốc gia và di sản thế giới.'],
     ans='A',
     why='**Di sản văn hoá = vật thể + phi vật thể.** C là hai loại trong nhóm //vật thể//; B là phân loại rộng hơn (có thêm di sản thiên nhiên); D là phân loại theo **cấp quản lí/công nhận**.')

add('mcq', code='I.15', meta='Bài 3 · NL1 · Biết',
     q='Địa danh nào sau đây là **di sản thế giới hỗn hợp** (vừa giá trị văn hoá, vừa giá trị thiên nhiên) đầu tiên của Việt Nam được UNESCO công nhận?',
     opts=['A. Vịnh Hạ Long (Quảng Ninh).',
           'B. Vườn quốc gia Phong Nha – Kẻ Bàng (Quảng Bình).',
           'C. Quần thể danh thắng Tràng An (Ninh Bình).',
           'D. Cố đô Huế (Thừa Thiên Huế).'],
     ans='C',
     why='**Tràng An (2014)** là di sản **hỗn hợp** đầu tiên và (tính đến nay) là di sản hỗn hợp duy nhất của Việt Nam. Hạ Long và Phong Nha – Kẻ Bàng là di sản **thiên nhiên**; Cố đô Huế là di sản **văn hoá**. **Mẹo: “HỖN HỢP = TRÀNG AN”.**')

add('mcq', code='I.16', meta='Bài 3 · NL1 · Hiểu',
     q='Vai trò của lịch sử – văn hoá đối với sự phát triển du lịch được thể hiện **rõ nhất** ở việc:',
     opts=['A. Giảm chi phí xây dựng khách sạn và đường giao thông.',
           'B. Tạo ra sản phẩm du lịch đặc thù, tăng sức hút, giá trị trải nghiệm và thời gian lưu trú của du khách.',
           'C. Thay thế hoàn toàn các hoạt động kinh tế khác của địa phương.',
           'D. Miễn mọi loại thuế, phí cho doanh nghiệp du lịch.'],
     ans='B',
     why='Giá trị cốt lõi của lịch sử – văn hoá với du lịch là tạo **sự khác biệt và chiều sâu trải nghiệm** (di tích, lễ hội, ẩm thực, làng nghề). A, D không đúng thực tế; C là cực đoan — du lịch chỉ là một ngành trong cơ cấu kinh tế.')

add('mcq', code='I.17', meta='Bài 3 · NL2 · Biết',
     q='Nhận định nào **đúng** về mối quan hệ giữa Sử học và công tác bảo tồn, phát huy giá trị di sản?',
     opts=['A. Sử học chỉ nghiên cứu sách vở, không liên quan đến di tích, hiện vật.',
           'B. Di sản chỉ cần được quảng bá du lịch, không cần nghiên cứu lịch sử.',
           'C. Sử học cung cấp cơ sở khoa học để xác định niên đại, giá trị, lập hồ sơ và phục dựng di sản; ngược lại, di sản chính là nguồn sử liệu quý giá cho Sử học.',
           'D. Sử học có nhiệm vụ thay thế toàn bộ công việc của cán bộ quản lí di tích.'],
     ans='C',
     why='**Quan hệ hai chiều**: Sử học → di sản (cơ sở khoa học); di sản → Sử học (nguồn sử liệu hiện vật). A, B phủ nhận vai trò của Sử học; D nhầm lẫn giữa **nghiên cứu** và **quản lí**. Đây là câu “nền tảng” của toàn bộ Bài 3.')

add('mcq', code='I.18', meta='Bài 3 · NL2 · Biết',
     q='Hoạt động nào dưới đây chủ yếu nhằm **PHÁT HUY** giá trị di sản (thay vì chủ yếu nhằm BẢO TỒN)?',
     opts=['A. Lập hồ sơ khoa học và đề nghị xếp hạng di tích cấp tỉnh.',
           'B. Số hoá (quét 3D) toàn bộ hoa văn trên cột đá để lưu trữ lâu dài.',
           'C. Tổ chức lễ hội truyền thống gắn với đình làng, có thuyết minh và quy tắc ứng xử cho du khách.',
           'D. Gia cố mái ngói, chống mối mọt bằng vật liệu và kĩ thuật truyền thống.'],
     ans='C',
     why='**Phát huy = đưa giá trị vào đời sống hôm nay** (lễ hội, thuyết minh, giáo dục, du lịch có kiểm soát). A, B, D là **bảo tồn** (lập hồ sơ, số hoá, trùng tu). **Mẹo: “giữ lại” → bảo tồn; “đem ra dùng” → phát huy.**')

add('mcq', code='I.19', meta='Bài 3 · NL2 · Hiểu',
     q='Tại một phố cổ, lượng khách tăng gấp 5 lần trong một năm. Nhiều hộ dân mở quán ngay trong ngõ di tích, rác thải tăng, một số bức tường cổ bị sơn vẽ bậy, chính quyền còn dự định xây bãi đỗ xe sát cổng đình. **Nhận xét đúng nhất** về tình huống này là:',
     opts=['A. Du lịch hoàn toàn có hại, tốt nhất nên đóng cửa điểm đến.',
           'B. Du lịch mang lại nguồn thu và việc làm nhưng đang gây quá tải, xâm lấn không gian và làm xuống cấp di tích; cần kiểm soát sức chứa, quy hoạch vùng đệm và tái đầu tư doanh thu vào bảo tồn.',
           'C. Đây chỉ là vấn đề kĩ thuật của ngành giao thông, không liên quan đến Sử học.',
           'D. Cứ để tự phát phát triển, vì thị trường sẽ tự điều chỉnh mọi tác động.'],
     ans='B',
     why='Đề yêu cầu **phân tích tác động của du lịch** → phải thấy **cả 2 mặt** và nêu được hướng xử lí (sức chứa, vùng đệm, tái đầu tư). A cực đoan một chiều; C tách rời Sử học khỏi quản lí di sản; D buông lỏng quản lí. **Cấu trúc “lợi – hại – giải pháp” luôn là đáp án đúng.**')

add('mcq', code='I.20', meta='Bài 3 · NL2 · Hiểu',
     q='Vì sao **thiếu tri thức Sử học** lại gây nguy hại cho công tác bảo tồn di tích?',
     opts=['A. Vì khi đó sẽ không có đủ khách du lịch đến tham quan.',
           'B. Vì không hiểu bối cảnh, niên đại và giá trị gốc nên việc trùng tu, tôn tạo dễ bị làm sai lệch, biến di tích thành “đồ giả cổ” hoặc làm mất ý nghĩa lịch sử.',
           'C. Vì luật pháp cấm trùng tu khi chưa có nhà sử học.',
           'D. Vì di tích lúc đó sẽ tự động biến mất.'],
     ans='B',
     why='Sử học là **cơ sở khoa học của bảo tồn**. Không có nó, người ta dễ “làm mới”, sơn lại, dựng thêm các chi tiết không có thật → **mất yếu tố gốc**. Đây chính là dạng câu “giải thích vai trò” ở mức Thông hiểu; hãy nhớ cụm **“giữ yếu tố gốc”.**')

add('h2', title='PHẦN II — 2 câu trắc nghiệm Đúng/Sai (2,0 điểm; mỗi ý 0,25 điểm)')

add('box', kind='tip', title='Cách làm dạng Đúng/Sai',
    items=[
        'Mỗi câu có 4 ý **a, b, c, d**; xét **độc lập** từng ý. Một ý chỉ Đúng khi **toàn bộ** các vế trong ý đều đúng. Đọc kĩ các từ nối “vì”, “nên”, “do đó” — đây là nơi giấu mệnh đề sai.',
    ])

add('tf', code='II.1', meta='Bài 2 · NL2 & NL3 · Biết – Hiểu – Vận dụng',
     q='Đọc tình huống sau và xét tính đúng/sai của các ý a, b, c, d.\n\n//Tình huống:// Nhóm học sinh lớp 10A1 thực hiện đề tài “Tìm hiểu di tích lịch sử ở địa phương”. Các em ghi âm lời kể của cụ Nguyễn Văn H. (85 tuổi) về trận đánh năm 1954, chụp ảnh tấm bia đá trong đình làng, tải thêm một bài blog viết năm 2024 về ngôi đình. Trước khi viết báo cáo, nhóm mang toàn bộ tư liệu lên đối chiếu với hồ sơ lưu trữ của thư viện tỉnh và ghi rõ nguồn gốc từng tư liệu.',
     items=[
         ['a', 'Lời kể của cụ Nguyễn Văn H. là **sử liệu truyền miệng**; đây là nguồn quý nhưng cần được đối chiếu với các nguồn khác trước khi dùng làm kết luận.', 'Đ',
          '**ĐÚNG (NL2 – Biết).** Lời kể nhân chứng thuộc nhóm sử liệu truyền miệng; vì dễ “tam sao thất bản” nên phải **kiểm chứng chéo** — đúng tinh thần Bước 5 của quy trình xử lí sử liệu.'],
         ['b', 'Bài blog năm 2024 có thể được dùng ngay làm kết luận cuối cùng vì nó được viết gần đây, dễ đọc và có nhiều hình ảnh minh hoạ.', 'S',
          '**SAI (NL2 – Hiểu).** “Mới – dễ đọc – nhiều ảnh” **không** bảo chứng cho độ tin cậy. Blog là **sử liệu thứ cấp**, cần kiểm tra tác giả, nguồn trích dẫn và đối chiếu với sử liệu gốc.'],
         ['c', 'Việc đối chiếu tư liệu với hồ sơ lưu trữ của thư viện tỉnh giúp nâng cao độ tin cậy của thông tin lịch sử mà nhóm thu thập được.', 'Đ',
          '**ĐÚNG (NL3 – Biết).** Đây chính là thao tác **kiểm chứng chéo**, tiêu chí quan trọng nhất để đánh giá sử liệu.'],
         ['d', 'Sau khi hoàn thành, nhóm nên ghi rõ nguồn tư liệu, chia sẻ kết quả với cộng đồng địa phương và tham gia các hoạt động tìm hiểu, giữ gìn di tích — đó là cách vận dụng tri thức lịch sử vào cuộc sống.', 'Đ',
          '**ĐÚNG (NL3 – Vận dụng).** Đúng yêu cầu cần đạt: “quan tâm, yêu thích và tham gia các hoạt động tìm hiểu lịch sử, văn hoá”. Việc trích nguồn cũng thể hiện đạo đức thông tin.'],
     ])

add('tf', code='II.2', meta='Bài 3 · NL2 & NL3 · Biết – Hiểu – Vận dụng',
     q='Đọc tình huống sau và xét tính đúng/sai của các ý a, b, c, d.\n\n//Tình huống:// Đình làng Đông (xã A) là di tích lịch sử – văn hoá đã được xếp hạng. Sau khi một video ngắn về ngôi đình lan truyền trên mạng, lượng khách đến tăng đột biến. Chính quyền địa phương dự kiến: (1) mở rộng bãi đỗ xe ngay sát tường đình; (2) cho thuê nhiều gian hàng lưu niệm ngay trong sân đình; (3) tổ chức biểu diễn nhạc pop hằng đêm để “trẻ hoá” di sản; (4) dùng một phần doanh thu vé để sửa lại mái ngói theo đúng kĩ thuật truyền thống.',
     items=[
         ['a', 'Đình làng Đông thuộc **di sản văn hoá vật thể**; việc được xếp hạng là căn cứ pháp lí quan trọng để bảo vệ di tích.', 'Đ',
          '**ĐÚNG (NL2 – Biết).** Đình là công trình vật chất có giá trị lịch sử – văn hoá → di sản vật thể. Xếp hạng di tích tạo hành lang pháp lí để quản lí, ngăn xâm lấn.'],
         ['b', 'Tổ chức biểu diễn nhạc pop hằng đêm trong sân đình là cách phát huy giá trị di sản đúng đắn vì thu hút được đông đảo giới trẻ.', 'S',
          '**SAI (NL2 – Hiểu).** Phát huy phải **dựa trên giá trị gốc**. Nhạc pop hằng đêm trong không gian thiêng dễ làm biến dạng ý nghĩa lịch sử, gây ồn ào, thương mại hoá — tức là “phát huy sai”. Có thể tổ chức ở không gian riêng, có kiểm soát, nhưng không được thay thế nghi lễ gốc.'],
         ['c', 'Lượng khách tăng đột biến có thể gây quá tải sức chứa, rác thải, ồn ào và làm xuống cấp công trình nếu không có quy chế quản lí.', 'Đ',
          '**ĐÚNG (NL3 – Biết).** Đây là mặt trái điển hình của du lịch đối với bảo tồn (Bảng 1.8).'],
         ['d', 'Thay vì mở bãi đỗ xe sát tường và cho thuê gian hàng trong sân đình, nên quy hoạch vùng đệm, giới hạn số khách mỗi ngày, dùng một phần doanh thu để trùng tu đúng nguyên tắc và có sự tham gia giám sát của cộng đồng địa phương.', 'Đ',
          '**ĐÚNG (NL3 – Vận dụng).** Đây là gói giải pháp “đủ bộ”: quy hoạch + kiểm soát sức chứa + tái đầu tư + trùng tu đúng + cộng đồng — khớp hoàn toàn Bảng 1.9.'],
     ])

add('h2', title='PHẦN III — 1 câu tự luận (3,0 điểm)')

add('essay', code='TL', meta='Bài 3 · ½ NL1 – Biết (1,0đ) + ½ NL3 – Vận dụng (2,0đ)',
     q='**Câu hỏi:** Di sản là “tài sản” của quá khứ nhưng lại là “nguồn lực” của hiện tại. Em hãy:\n\n**(1)** Nêu hiểu biết của em về **di sản văn hoá, di sản thiên nhiên** và kể tên ít nhất **3 loại hình di sản** ở Việt Nam (mỗi loại cho 1 ví dụ cụ thể). Đồng thời, hãy chỉ ra **mối quan hệ giữa Sử học với công tác bảo tồn, phát huy giá trị di sản**. //(1,0 điểm)//\n\n**(2)** Chọn **một di tích/danh lam ở địa phương em hoặc một di sản mà em biết**. Hãy phân tích **những tác động (cả tích cực lẫn tiêu cực) của hoạt động du lịch** đối với công tác bảo tồn di tích đó và **đề xuất ít nhất 4 biện pháp** cụ thể, khả thi để bảo tồn và phát huy giá trị của di sản ấy. //(2,0 điểm)//',
     guide=[
         '**Gợi ý dàn ý (không bắt buộc, nhưng bám sát thang điểm):**',
         '• **Mở bài (~0,25đ):** tên di tích, vị trí, loại hình, giá trị nổi bật.',
         '• **Ý 1 (1,0đ):** khái niệm di sản; ít nhất 3 loại hình (vật thể / phi vật thể / thiên nhiên / hỗn hợp / tư liệu) kèm ví dụ; quan hệ hai chiều Sử học ↔ di sản.',
         '• **Ý 2a (~0,75đ):** ít nhất 2 tác động tích cực + 2 tác động tiêu cực của du lịch.',
         '• **Ý 2b (~1,0đ):** ít nhất 4 biện pháp thuộc 4 nhóm khác nhau; mỗi biện pháp nêu rõ ai làm, làm thế nào.',
         '• **Kết bài (~0,25đ):** vai trò của cộng đồng, của bản thân học sinh; lời kêu gọi hành động.',
     ])

# =====================================================================
# PHAN 4 - DAP AN
# =====================================================================
add('pb')
add('h1', n='PHẦN 4', title='ĐÁP ÁN & GIẢI THÍCH CHI TIẾT',
    sub='Cho toàn bộ 28 lệnh hỏi trắc nghiệm + 1 câu tự luận')

add('box', kind='key', title='Cách dùng Phần 4',
    items=[
        'Xem **bảng đáp án nhanh** để tự chấm điểm (mỗi lệnh hỏi 0,25đ; riêng câu TL 3,0đ). Sau đó đọc kĩ phần **giải thích** — đặc biệt là dòng “Mẹo/Công thức” — vì đó là nơi chứa kĩ năng làm bài cho những đề tương lai.',
    ])

add('h2', title='4.1. Bảng đáp án nhanh')

add('p', text='Hai bảng dưới đây cho phép tự chấm **toàn bộ 28 lệnh hỏi trắc nghiệm** trong chưa đầy 2 phút. '
              'Cách tính: Phần I (20 câu × 0,25đ) = 5,0đ; Phần II (8 ý × 0,25đ) = 2,0đ; Phần III (TL) = 3,0đ → **tổng 10,0đ**.')

add('answers')

# =====================================================================
# PHAN 5 - DE LUYEN THEM
# =====================================================================
add('h2', title='4.6. Bài mẫu cho câu TỰ LUẬN (3,0 điểm)')

add('box', kind='sample', title='Bài làm mẫu – chọn Quần thể danh thắng Tràng An (Ninh Bình)',
     items=[
         '**Mở bài.** Quần thể danh thắng Tràng An (Ninh Bình) là di sản thế giới **hỗn hợp** đầu tiên của Việt Nam, được UNESCO công nhận năm 2014, nổi bật với hệ thống núi đá vôi, hang động, sông ngầm và các di tích gắn với lịch sử lập quốc Đại Cồ Việt thế kỉ X.',
         '**(1) Khái niệm và phân loại.** Di sản là những giá trị vật chất và tinh thần do quá khứ để lại, có ý nghĩa lịch sử, văn hoá, khoa học, cần được bảo tồn và phát huy. Ở Việt Nam có các loại hình: **di sản văn hoá vật thể** (Hoàng thành Thăng Long, Văn Miếu – Quốc Tử Giám, đình làng Đông); **di sản văn hoá phi vật thể** (dân ca Ví, Giặm Nghệ Tĩnh, Nhã nhạc cung đình Huế, Quan họ Bắc Ninh); **di sản thiên nhiên** (Vịnh Hạ Long, Phong Nha – Kẻ Bàng); **di sản hỗn hợp** (Tràng An) và **di sản tư liệu** (Mộc bản, Châu bản triều Nguyễn). **Sử học có quan hệ hai chiều với di sản:** một mặt, Sử học nghiên cứu niên đại, bối cảnh, giá trị để lập hồ sơ khoa học, xếp hạng, giải mã và trùng tu đúng nguyên tắc, đồng thời cung cấp nội dung thuyết minh, giáo dục; mặt khác, chính di tích, cổ vật, bia kí lại là **sử liệu gốc** giúp kiểm chứng và bổ sung tri thức lịch sử. Vì vậy, mất di sản cũng có nghĩa là mất chứng cứ lịch sử.',
         '**(2) Tác động của du lịch.** Du lịch đem lại nhiều lợi ích: vé tham quan và dịch vụ tạo **nguồn thu** để trùng tu, tạo **việc làm** cho người dân (chèo thuyền, homestay, hướng dẫn viên), **quảng bá** hình ảnh Ninh Bình ra thế giới và khơi dậy **tự hào** của cộng đồng. Tuy nhiên, lượng khách tăng nhanh cũng gây **quá tải sức chứa**: rác thải xuống dòng sông, khí thải động cơ, tiếng ồn làm ảnh hưởng hệ sinh thái hang động; nhiều công trình dịch vụ mọc lên sát vùng lõi, hàng quán và biển hiệu làm **thương mại hoá** không gian di sản; không ít nơi “sơn mới, làm giả cổ” khiến **yếu tố gốc** bị biến dạng, câu chuyện lịch sử bị kể sai để chiều lòng du khách.',
         '**Biện pháp.** Thứ nhất, **hoàn thiện quy hoạch và pháp luật**: UBND tỉnh cần khoanh vùng lõi – vùng đệm, cấm xây dựng công trình cao tầng trong bán kính bảo vệ và xử phạt nghiêm hành vi khắc, vẽ lên đá. Thứ hai, **kiểm kê, số hoá và trùng tu đúng nguyên tắc**: cơ quan quản lí phối hợp với viện nghiên cứu quét 3D hang động, lập hồ sơ khoa học từng điểm, sửa chữa bằng vật liệu, kĩ thuật truyền thống dưới sự giám sát của chuyên gia Sử học và khảo cổ. Thứ ba, **du lịch bền vững**: khảo sát sức chứa, giới hạn số thuyền và số khách mỗi ngày, bán vé điện tử, bố trí thuyền theo khung giờ, trích **tối thiểu 30% doanh thu vé** cho công tác bảo tồn và chia sẻ lợi ích với hộ dân trong vùng đệm. Thứ tư, **giáo dục và truyền thông**: Sở Giáo dục đưa nội dung di sản Tràng An vào hoạt động trải nghiệm, trường THPT lập câu lạc bộ “Trẻ em kể chuyện di sản”, làm thuyết minh đa ngôn ngữ, video ngắn và quy tắc ứng xử đặt tại bến thuyền.',
         '**Kết bài.** Bảo tồn không phải là khoá kín di sản, mà là giữ được **giá trị gốc** rồi trao nó cho thế hệ sau bằng cách khai thác có trách nhiệm. Là học sinh, em sẽ không vẽ bậy, không xả rác, chủ động tìm hiểu lịch sử địa phương, chia sẻ thông tin đã được kiểm chứng và vận động bạn bè, gia đình cùng tham gia giữ gìn di sản — để “mỗi người dân trở thành một người gác cổng cho kí ức của dân tộc”.',
     ])

add('table', caption='Bảng 4.2 – Thang điểm gợi ý cho câu tự luận (tổng 3,0đ)', fontsize=8,
    cols=[128, 65, 306], head=['Tiêu chí', 'Điểm tối đa', 'Cách chấm'], rows=[
        ['Khái niệm + kể tên ≥3 loại hình di sản kèm ví dụ', '**0,60**', 'Mỗi loại hình đúng kèm ví dụ 0,15đ; thiếu ví dụ trừ một nửa. Sai loại hình (nhầm vật thể ↔ phi vật thể) không tính điểm.'],
        ['Mối quan hệ Sử học ↔ di sản', '**0,40**', 'Nêu được chiều Sử học → di sản (0,25đ) và di sản → Sử học (0,15đ).'],
        ['Tác động 2 mặt của du lịch', '**0,75**', '≥2 tích cực (0,35đ) + ≥2 tiêu cực (0,40đ). Chỉ nêu 1 mặt tối đa 0,4đ.'],
        ['≥4 biện pháp cụ thể, thuộc ≥3 nhóm', '**1,00**', 'Mỗi biện pháp 0,25đ. Biện pháp chung chung (“cần tuyên truyền”, “cần bảo vệ”) chỉ tính 0,1đ.'],
        ['Vai trò cộng đồng / bản thân + kết cấu, diễn đạt', '**0,25**', 'Có lời kêu gọi, bố cục 3 phần, không sai lịch sử, chữ viết rõ ràng.'],
    ])

# =====================================================================
add('pb')
add('h1', n='PHẦN 5', title='NGÂN HÀNG CÂU HỎI LUYỆN THÊM',
    sub='12 câu trắc nghiệm + 2 câu tự luận ngắn (có đáp án)')

add('p', text='Phần này **không nằm trong ma trận đề**, nhưng được biên soạn để luyện thêm các “góc khuất” của 3 bài. Mỗi câu 0,25 điểm (tổng 3,0đ); 2 câu tự luận ngắn mỗi câu 1,0đ — dùng để tự kiểm tra sau khi đã làm xong Phần 3.')

add('h2', title='5.1. 12 câu trắc nghiệm bổ sung')

add('mcq', code='P.1', meta='Bài 1 · luyện thêm',
     q='Từ nào điền vào chỗ trống cho đúng: “Lịch sử được con người nhận thức mang tính ____ vì luôn chịu tác động của lập trường, cảm xúc và thời đại của người viết”?',
     opts=['A. khách quan', 'B. chủ quan', 'C. duy nhất', 'D. vĩnh cửu'], ans='B', why='Tính **chủ quan** là đặc điểm thứ nhất. “Khách quan, duy nhất, không đổi” thuộc về hiện thực lịch sử.', extra=True)

add('mcq', code='P.2', meta='Bài 1 · luyện thêm',
     q='Phát biểu nào **SAI**?',
     opts=['A. Hiện thực lịch sử tồn tại độc lập với ý thức con người.',
           'B. Sự kiện lịch sử là duy nhất, không lặp lại.',
           'C. Lịch sử được con người nhận thức phản ánh hoàn toàn chính xác, trọn vẹn hiện thực lịch sử.',
           'D. Lịch sử được nhận thức có thể được bổ sung khi có tư liệu mới.'],
     ans='C', why='C sai vì nhận thức chỉ **tiệm cận** hiện thực, thường **không đầy đủ** và có dấu ấn chủ quan.', extra=True)

add('mcq', code='P.3', meta='Bài 1 · luyện thêm',
     q='Hoạt động nào thể hiện **chức năng dự báo** của Sử học?',
     opts=['A. Kể lại diễn biến trận Bạch Đằng năm 938.',
           'B. Dùng bài học khủng hoảng kinh tế 1929 – 1933 để nhận diện nguy cơ suy thoái và thiết kế chính sách ổn định vĩ mô hiện nay.',
           'C. Trưng bày chiếc áo của một danh nhân trong bảo tàng.',
           'D. Tổ chức cho học sinh viết bài phát biểu về lòng yêu nước.'],
     ans='B', why='**Dự báo** = dùng quy luật quá khứ để nhận diện xu hướng, lựa chọn giải pháp hiện tại. A là nhận thức, C là bảo tồn, D là giáo dục.', extra=True)

add('mcq', code='P.4', meta='Bài 2 · luyện thêm',
     q='Một nhóm học sinh ghi chép được 10 tư liệu nhưng không ghi tên tác giả, năm xuất bản và nguồn trích. Hệ quả trực tiếp là:',
     opts=['A. Nhóm sẽ có bài báo cáo dài hơn.',
           'B. Các tư liệu tự động trở thành sử liệu gốc.',
           'C. Không thể kiểm chứng, đối chiếu lại → độ tin cậy của báo cáo bị giảm.',
           'D. Không có hệ quả gì vì nội dung vẫn đúng.'],
     ans='C', why='**Ghi nguồn** là một phần của bước thu thập; thiếu nguồn thì bước kiểm chứng (bước 5) không thực hiện được.', extra=True)

add('mcq', code='P.5', meta='Bài 2 · luyện thêm',
     q='Đâu là ví dụ đúng về **vận dụng bài học lịch sử vào thực tiễn**?',
     opts=['A. Học thuộc 10 mốc năm rồi viết lại vào vở.',
           'B. Dùng truyền thống đoàn kết chống ngoại xâm để giải thích sức mạnh của tinh thần cộng đồng trong phòng, chống dịch bệnh.',
           'C. Chép nguyên một đoạn trong sách sử vào bài kiểm tra.',
           'D. Xem một bộ phim lịch sử để giải trí cuối tuần.'],
     ans='B', why='Vận dụng = **lấy bài học quá khứ để giải thích/giải quyết vấn đề hiện tại**. A, C là ghi nhớ/chép lại; D là giải trí.', extra=True)

add('mcq', code='P.6', meta='Bài 2 · luyện thêm',
     q='Cách ứng xử **đúng** với thông tin lịch sử sai lệch trên mạng là:',
     opts=['A. Chia sẻ thật nhanh để nhiều người biết.',
           'B. Im lặng, coi như không thấy.',
           'C. Kiểm chứng nguồn, đối chiếu với tư liệu gốc, báo cáo/góp ý chính xác kèm đường dẫn nguồn tin cậy.',
           'D. Viết một bài khác sai hơn để “trừng trị” người đăng sai.'],
     ans='C', why='Tư duy phản biện = **kiểm chứng + phản hồi có căn cứ**, không lan truyền cũng không thờ ơ.', extra=True)

add('mcq', code='P.7', meta='Bài 3 · luyện thêm',
     q='Nhóm nào dưới đây gồm **toàn di sản văn hoá phi vật thể**?',
     opts=['A. Quan họ Bắc Ninh – Ca trù – Dân ca Ví, Giặm Nghệ Tĩnh.',
           'B. Hoàng thành Thăng Long – phố cổ Hội An – Thánh địa Mỹ Sơn.',
           'C. Vịnh Hạ Long – Phong Nha – Kẻ Bàng – Cúc Phương.',
           'D. Văn Miếu – Quốc Tử Giám – Thành nhà Hồ – chùa Bút Tháp.'],
     ans='A', why='A là các loại hình **hát/dân ca**. B, D là di sản **vật thể**; C là di sản **thiên nhiên**.', extra=True)

add('mcq', code='P.8', meta='Bài 3 · luyện thêm',
     q='“Sử học giúp lập hồ sơ khoa học cho di tích” — đây là ví dụ của chiều tác động nào?',
     opts=['A. Di sản → Sử học (di sản là nguồn sử liệu).',
           'B. Sử học → di sản (Sử học là cơ sở khoa học của bảo tồn).',
           'C. Du lịch → di sản.',
           'D. Thiên nhiên → văn hoá.'],
     ans='B', why='Lập hồ sơ, xác định niên đại, giải mã giá trị là **Sử học phục vụ bảo tồn**.', extra=True)

add('mcq', code='P.9', meta='Bài 3 · luyện thêm',
     q='Biện pháp nào **KHÔNG** phù hợp với nguyên tắc bảo tồn di tích?',
     opts=['A. Giữ tối đa yếu tố gốc, dùng vật liệu truyền thống khi trùng tu.',
           'B. Sơn lại toàn bộ cột gỗ bằng sơn công nghiệp màu mới để “trông sạch sẽ hơn”.',
           'C. Số hoá, quét 3D các hoa văn để lưu trữ lâu dài.',
           'D. Quy hoạch vùng đệm, giới hạn số khách mỗi ngày.'],
     ans='B', why='“Sơn lại bằng vật liệu mới” phá huỷ **yếu tố gốc** — lỗi kinh điển của “trùng tu sai”.', extra=True)

add('mcq', code='P.10', meta='Bài 3 · luyện thêm',
     q='Cặp địa danh – giá trị nào **sai**?',
     opts=['A. Vịnh Hạ Long – di sản thiên nhiên thế giới.',
           'B. Tràng An – di sản thế giới hỗn hợp.',
           'C. Cố đô Huế – di sản văn hoá thế giới và Nhã nhạc cung đình Huế.',
           'D. Phong Nha – Kẻ Bàng – di sản văn hoá phi vật thể.'],
     ans='D', why='Phong Nha – Kẻ Bàng là **di sản thiên nhiên thế giới**, không phải phi vật thể.', extra=True)

add('mcq', code='P.11', meta='Bài 3 · luyện thêm',
     q='Điểm khác biệt cốt lõi giữa **bảo tồn** và **phát huy** giá trị di sản là:',
     opts=['A. Bảo tồn dành cho di sản vật thể; phát huy dành cho di sản phi vật thể.',
           'B. Bảo tồn là giữ nguyên trạng, chống xuống cấp; phát huy là đưa giá trị di sản vào đời sống hiện tại.',
           'C. Bảo tồn do Nhà nước làm; phát huy chỉ do doanh nghiệp làm.',
           'D. Hai khái niệm hoàn toàn giống nhau.'],
     ans='B', why='**Bảo tồn = giữ; phát huy = dùng có trách nhiệm.** Cả hai đều áp dụng cho mọi loại hình di sản và cần nhiều chủ thể cùng tham gia.', extra=True)

add('mcq', code='P.12', meta='Bài 3 · luyện thêm',
     q='Trong câu tự luận của đề, phần “đề xuất biện pháp” chiếm khoảng bao nhiêu điểm?',
     opts=['A. 0,5 điểm', 'B. 1,0 điểm', 'C. 2,0 điểm', 'D. 3,0 điểm'],
     ans='B', why='Theo Bảng 4.2, 4 biện pháp cụ thể = **1,0đ**; cộng thêm 0,75đ phân tích tác động tạo thành 2,0đ của ý vận dụng (cộng dòng vai trò cộng đồng).', extra=True)

add('h2', title='5.2. 2 câu tự luận ngắn (mỗi câu 1,0 điểm)')

add('box', kind='question', title='Câu LT.1 (Bài 1 + Bài 2)',
     items=[
         'Hai tờ báo đưa tin về cùng một trận đánh nhưng mô tả **khác nhau về số lượng binh lính** tham chiến. Em hãy giải thích vì sao lại có sự khác biệt đó và nêu **3 việc cần làm** để tiếp cận thông tin này một cách khoa học. //(1,0 điểm)//',
         '**Gợi ý đáp án:** Khác biệt vì **lịch sử được con người nhận thức mang tính chủ quan, không đầy đủ, đa chiều** — mỗi tờ báo dùng nguồn, góc nhìn, thời điểm và mục đích khác nhau; sử liệu về trận đánh có thể bị mất mát. (0,4đ) Việc cần làm: (1) xác định rõ câu hỏi cần làm rõ là “số lượng binh lính”; (2) truy về **sử liệu gốc** (báo cáo quân sự, nhật ký, tư liệu lưu trữ cùng thời) và đối chiếu chéo ít nhất 2–3 nguồn độc lập; (3) đánh giá tác giả, thời điểm, ngữ cảnh, ghi rõ nguồn và chỉ kết luận mức độ tin cậy (có thể nêu khoảng ước lượng thay vì con số tuyệt đối). (0,6đ)',
     ])

add('box', kind='question', title='Câu LT.2 (Bài 3)',
     items=[
         'Một bạn trong lớp nói: “Muốn phát huy giá trị di tích thì cứ cho xây thật nhiều gian hàng, tổ chức thật nhiều show ca nhạc và đón thật đông khách — có thế mới có tiền mà trùng tu.” Em có đồng ý không? Hãy giải thích quan điểm của em trong 6 – 8 câu. //(1,0 điểm)//',
         '**Gợi ý đáp án:** Chỉ đồng ý một phần (0,2đ). Đúng là du lịch tạo nguồn thu, việc làm, quảng bá và động lực trùng tu (0,2đ). Nhưng khai thác quá mức gây quá tải, rác thải, ồn ào, xâm lấn vùng lõi, thương mại hoá và “Disney hoá” làm mất **yếu tố gốc** — tức là phá huỷ chính thứ đang muốn phát huy (0,3đ). Vì vậy cần **phát huy trên nền bảo tồn**: quy hoạch vùng đệm, kiểm soát sức chứa, trùng tu đúng nguyên tắc, dùng một phần doanh thu tái đầu tư, có sự tham gia của cộng đồng và chuyên gia Sử học; các hoạt động vui chơi nên đặt ngoài không gian thiêng, có quy tắc ứng xử (0,3đ).',
     ])

add('h2', title='5.3. Đáp án nhanh 12 câu bổ sung')

add('p', text='**P.1 – B · P.2 – C · P.3 – B · P.4 – C · P.5 – B · P.6 – C · P.7 – A · P.8 – B · P.9 – B · P.10 – D · P.11 – B · P.12 – B.** Giải thích ngắn cho từng câu đã được ghi ngay dưới mỗi câu ở mục 5.1.')

# =====================================================================
# PHU LUC
# =====================================================================
add('h1', n='PHỤ LỤC', title='BẢNG KIỂM TRA & THUẬT NGỮ',
    sub='Checklist trước giờ thi · bảng từ khoá Anh – Việt · nguồn tham khảo')

add('h2', title='A. Checklist 12 mục trước khi vào phòng thi')

add('checklist', items=[
    'Thuộc 5 định nghĩa: lịch sử, sử học, sử liệu, hiện thực lịch sử, lịch sử được nhận thức.',
    'Kể được 3 chức năng (N–G–D) và 4 nhiệm vụ (T–P–G–T) của Sử học.',
    'Kể được 5 đặc điểm của lịch sử được con người nhận thức (Chủ – Thiếu – Đa – Biến – Xã).',
    'Vẽ được sơ đồ 6 bước xử lí thông tin, sử liệu (X–T–T–S–K–V) từ trí nhớ.',
    'Phân loại được 4 nhóm sử liệu và phân biệt gốc / thứ cấp; biết cách kiểm chứng chéo.',
    'Viết được 6 lí do học lịch sử suốt đời và công thức Hiểu – So – Làm.',
    'Kể được 5 loại hình di sản, mỗi loại ít nhất 2 ví dụ Việt Nam.',
    'Biết Tràng An là di sản hỗn hợp; Hạ Long, Phong Nha là thiên nhiên; Huế, Hội An, Mỹ Sơn, Thăng Long là văn hoá.',
    'Giải thích được quan hệ hai chiều Sử học ↔ di sản (có câu “vàng”).',
    'Kể được 3 tác động tích cực và 3 tác động tiêu cực của du lịch với bảo tồn.',
    'Kể được 6 nhóm biện pháp, trong đó ít nhất 4 nhóm có ví dụ cụ thể kèm “ai làm – làm thế nào”.',
    'Đã viết tay ít nhất 1 bài tự luận hoàn chỉnh trong đúng 13 phút và tự chấm theo Bảng 4.2.',
])

add('h2', title='B. Bảng thuật ngữ then chốt (có thể gặp trong đề nâng cao)')

add('table', caption='Bảng PL.1 – 18 thuật ngữ', fontsize=8,
    cols=[132, 148, 219], head=['Thuật ngữ tiếng Việt', 'Tiếng Anh gợi nhớ', 'Ý cần nhớ'], rows=[
        ['Sử học', 'History / Historiography', 'Khoa học nghiên cứu quá khứ; phân biệt với “lịch sử” là đối tượng.'],
        ['Hiện thực lịch sử', 'Historical reality / the past', 'Cái đã xảy ra, khách quan, duy nhất.'],
        ['Lịch sử được nhận thức', 'Historical knowledge / written history', 'Cái được tái hiện, chủ quan, có thể hiệu chỉnh.'],
        ['Sử liệu', 'Historical source', 'Chứng cứ của quá khứ; nền tảng của mọi nghiên cứu.'],
        ['Sử liệu gốc', 'Primary source', 'Cùng thời, nguyên bản, người chứng kiến.'],
        ['Sử liệu thứ cấp', 'Secondary source', 'Biên soạn, bình luận, sao chép lại.'],
        ['Phê phán nguồn', 'Source criticism', 'Đánh giá nguồn gốc, tác giả, niên đại, độ tin cậy.'],
        ['Đối chiếu chéo', 'Cross-checking', 'So sánh nhiều nguồn độc lập để kiểm chứng.'],
        ['Tính chủ quan', 'Subjectivity', 'Dấu ấn của người nhận thức.'],
        ['Tính khách quan', 'Objectivity', 'Thuộc về hiện thực; là mục tiêu cần hướng tới.'],
        ['Di sản văn hoá vật thể', 'Tangible cultural heritage', 'Di tích, danh lam, cổ vật, bảo vật quốc gia.'],
        ['Di sản văn hoá phi vật thể', 'Intangible cultural heritage', 'Lễ hội, dân ca, nghi lễ, nghề, tri thức dân gian.'],
        ['Di sản thiên nhiên', 'Natural heritage', 'Cảnh quan, hệ sinh thái, vườn quốc gia.'],
        ['Di sản hỗn hợp', 'Mixed heritage', 'Văn hoá + thiên nhiên (Tràng An).'],
        ['Bảo tồn', 'Conservation / Preservation', 'Giữ nguyên trạng, chống xuống cấp.'],
        ['Phát huy giá trị', 'Promotion / Valorisation', 'Đưa giá trị vào đời sống, có kiểm soát.'],
        ['Trùng tu', 'Restoration', 'Phục hồi theo nguyên bản, giữ yếu tố gốc.'],
        ['Sức chứa du lịch', 'Carrying capacity', 'Số khách tối đa không gây tổn hại di tích.'],
    ])

add('box', kind='key', title='Lời cuối cho bạn học sinh',
     items=[
         'Bài kiểm tra này **không khó về kiến thức nhưng dễ mất điểm ở cách đọc đề**. Nắm chắc 12 chìa khoá ở Phần 2, làm chậm 20 câu trắc nghiệm, và dành trọn 13 phút cuối cho câu tự luận với đủ **4 biện pháp cụ thể + lời kêu gọi cộng đồng**. Chúc bạn đạt điểm cao!',
     ])

add('h2', title='C. Nguồn tài liệu và phạm vi biên soạn')

add('bul', items=[
    '**Nguồn chính (phân tích trực tiếp):** `LS10- MTGK1-26-27-HHT.docx` — Ma trận kiểm tra định kì giữa học kì I khối 10, năm học 2026 – 2027 (2 bảng: ma trận và bảng đặc tả).',
    '**Cơ sở chương trình:** Chương trình Giáo dục phổ thông 2018 (môn Lịch sử, cấp THPT) — chủ đề “Lịch sử và sử học”, “Vai trò của Sử học”; yêu cầu cần đạt về 3 năng lực đặc thù: Tìm hiểu lịch sử; Nhận thức và tư duy lịch sử; Vận dụng kiến thức, kĩ năng.',
    '**Sách giáo khoa:** Lịch sử 10, bộ **Kết nối tri thức với cuộc sống** (Bài 1: Hiện thực lịch sử và lịch sử được con người nhận thức; Bài 2: Tri thức lịch sử và cuộc sống; Bài 3: Vai trò của Sử học).',
    '**Tham khảo bổ trợ:** Luật Di sản văn hoá Việt Nam (2001, sửa đổi bổ sung qua các năm, cùng các văn bản hướng dẫn hiện hành); Công ước Di sản thế giới của UNESCO; danh mục di sản thế giới, di sản văn hoá phi vật thể đại diện nhân loại và Kí ức thế giới của Việt Nam. **Lưu ý:** bảng phân loại trong đề cương mang tính học tập, người dùng nên đối chiếu với văn bản pháp luật và danh mục UNESCO cập nhật tại thời điểm học.',
    '**Về phần câu hỏi:** như đã nêu rõ ở Phần 0 và Phần 3, tệp DOCX gốc không chứa câu hỏi hay đáp án. Toàn bộ câu hỏi trong tài liệu là **phiên bản tái tạo theo đúng cấu trúc, mã câu, năng lực, cấp độ tư duy và yêu cầu cần đạt của ma trận**; đáp án và giải thích được biên soạn tương ứng. Người dùng nên đối chiếu với đề chính thức do tổ bộ môn phát hành (nếu có).',
    '**Phông chữ:** Be Vietnam Pro (Google Fonts, giấy phép SIL Open Font License 1.1); phông dự phòng cho kí hiệu: DejaVu Sans.',
])

add('h2', title='D. Phiếu tự chấm điểm & theo dõi tiến bộ')

add('p', text='In riêng bảng này hoặc chép vào vở. Mỗi lần làm thử Phần 3 trong đúng 45 phút, hãy điền điểm và **ghi lại 3 lỗi sai cụ thể** — đó là cách nhanh nhất để nâng điểm ở lần thi thật.')

add('table', caption='Bảng PL.2 – Phiếu theo dõi 3 lần thử đề', fontsize=8,
    cols=[74, 78, 78, 78, 70, 125],
    head=['Lần thử', 'Phần I\n(5,0đ)', 'Phần II\n(2,0đ)', 'Phần III\n(3,0đ)', 'TỔNG\n(10đ)', '3 lỗi sai cần sửa'], rows=[
        ['**Lần 1**', '…………', '…………', '…………', '…………', '…………………………………………'],
        ['**Lần 2**', '…………', '…………', '…………', '…………', '…………………………………………'],
        ['**Lần 3**', '…………', '…………', '…………', '…………', '…………………………………………'],
        ['**Mục tiêu**', '≥ 4,0', '≥ 1,5', '≥ 2,0', '**≥ 8,0**', 'Không lặp lại lỗi đã sửa'],
    ])

add('box', kind='tip', title='Quy tắc “3 – 2 – 1” sau mỗi lần thử đề',
     items=[
         '**3** lỗi sai viết lại thành 3 câu đúng ngắn gọn; **2** chìa khoá trong Phần 2 đọc lại to tiếng; **1** câu tự luận viết lại đoạn kết hay hơn lần trước. Làm đều trong 7 ngày theo Bảng 2.3, điểm số sẽ tăng mà không cần học thêm kiến thức mới.',
     ])
