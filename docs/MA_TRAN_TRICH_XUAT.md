# Trích xuất toàn bộ nội dung tệp DOCX nguồn

> Sinh tự động bởi `src/extract_docx.py` — không chỉnh sửa tay.

**Tệp nguồn:** `LS10- MTGK1-26-27-HHT.docx` (32101 byte).

**Mục đích:** làm bằng chứng cho việc phân tích kĩ tệp ma trận đề, đặc biệt để xác nhận tệp **không chứa câu hỏi/đáp án gốc**.


## 1. Kiểm kê mọi thành phần bên trong gói OOXML

| Thành phần | Kích thước (kí tự) | Số `<w:t>` | Dấu vết đặc biệt |
|---|---|---|---|
| `[Content_Types].xml` | 1577 | 0 | - |
| `_rels/.rels` | 590 | 0 | - |
| `word/document.xml` | 227518 | 449 | - |
| `word/_rels/document.xml.rels` | 1092 | 0 | - |
| `word/theme/theme1.xml` | 8277 | 0 | - |
| `word/settings.xml` | 5704 | 0 | - |
| `customXml/item1.xml` | 289 | 0 | - |
| `customXml/itemProps1.xml` | 341 | 0 | - |
| `word/numbering.xml` | 30955 | 0 | - |
| `word/styles.xml` | 34269 | 0 | - |
| `word/webSettings.xml` | 1898 | 0 | - |
| `word/fontTable.xml` | 1833 | 0 | - |
| `docProps/core.xml` | 794 | 0 | - |
| `docProps/app.xml` | 993 | 0 | - |
| `customXml/_rels/item1.xml.rels` | 296 | 0 | - |

**Thành phần media/header/footer/ghi chú/đối tượng nhúng:** KHÔNG CÓ.


**Kết luận:** toàn bộ văn bản nằm trong `word/document.xml`; không có câu hỏi hay đáp án nào được lưu ở phần khác.


## 2. Nội dung `word/document.xml` theo đúng thứ tự


**Đoạn:** MA TRẬN KIỂM TRA ĐỊNH KÌ GIỮA HỌC  KÌ 1- KHỐI 10


**Đoạn:** NĂM HỌC 2026 -2027


**Đoạn:** THỜI GIAN LÀM BÀI: 45 PHÚT


**Đoạn:** Đề kiểm tra gồm: 20 câu TN nhiều lựa chọn+2 câu TN Đ/S+ 1câu TL


**Đoạn:** /


### Bảng 1

- `c00 (vMerge=restart)` Chủ đề · `c01 (vMerge=restart)` Nội dung/đơn vị kiến thức · `c02` Năng lực môn học
- `c00 (vMerge=continue)` — · `c01 (vMerge=continue)` — · `c02` NL1: Tìm hiểu lịch sử · `c05` NL2: Nhận thức và tư duy lịch sử · `c08` NL3: Vận dụng kiến thức, kĩ năng · `c11` Tổng điểm
- `c00 (vMerge=continue)` — · `c01 (vMerge=continue)` — · `c02` Các cấp độ tư duy · `c05` Các cấp độ tư duy · `c08` Các cấp độ tư duy · `c11` …
- `c00 (vMerge=continue)` — · `c01 (vMerge=continue)` — · `c02` Biết · `c03` Hiểu · `c04` Vận dụng · `c05` Biết · `c06` Hiểu · `c07` Vận dụng · `c08` Biết · `c09` Hiểu · `c10` Vận dụng · `c11` —
- `c00 (vMerge=restart)` Chủ đề 1. Lịch sử và sử học · `c01` Bài 1: Hiện thực lịch sử và lịch sử được con người nhận thức · `c02` I.1,2,3 · `c03` I.4 · `c04` — · `c05` — · `c06` I. 5.6 · `c07` — · `c08` — · `c09` — · `c10` — · `c11` —
- `c00 (vMerge=continue)` — · `c01` Bài 2:Tri thức lịch sử và cuộc sống · `c02` I.7,8,9 · `c03` I.10,11 · `c04` — · `c05` I.12, 13 II.1a · `c06` II.1b · `c07` — · `c08` II.1c · `c09` — · `c10` II.1d · `c11` —
- `c00` Chủ đề 2. Vai trò của sử học · `c01` Bài 3. Vai trò của Sử học · `c02` I.14, 15, TL.(1/2) · `c03` I. 16 · `c04` — · `c05` I.17, 18 II.2a · `c06` I.19,20 II.2b · `c07` — · `c08` II.2c · `c09` — · `c10` II.2d TL(1/2) · `c11` —
- `c00` Tổng số lệnh · `c01` — · `c02` 8+1/2TL · `c03` 4 · `c04` 0 · `c05` 6 · `c06` 6 · `c07` 0 · `c08` 2 · `c09` 0 · `c10` 2+ ½ TL · `c11` 28 lệnh hỏi TN+1TL
- `c00` Tổng số điểm · `c01` — · `c02` 3, 0 · `c03` 1,0 · `c04` 0 · `c05` 1,5 · `c06` 1,5 · `c07` 0 · `c08` 0,5 · `c09` 0 · `c10` 2,5 · `c11` 10 điểm
- `c00` Tỷ lệ giữa các cấp độ tư duy · `c01` — · `c02` 30% · `c03` 10% · `c04` 0 · `c05` 15% · `c06` 15% · `c07` 0 · `c08` 0,5% · `c09` 0 · `c10` 25% · `c11` 100%

**Đoạn:** BẢNG ĐẶC TẢ MA TRẬN ĐỀ KIỂM TRA GIỮA HỌC KÌ 1 - LỚP 10


**Đoạn:** /


### Bảng 2

- `c00 (vMerge=restart)` Chủ đề · `c01 (vMerge=restart)` — · `c02 (vMerge=restart)` — · `c03` Năng lực môn học
- `c00 (vMerge=continue)` — · `c01 (vMerge=continue)` — · `c02 (vMerge=continue)` — · `c03` NL1: Tìm hiểu lịch sử · `c06` NL2: Nhận thức và tư duy lịch sử · `c09` NL3: Vận dụng kiến thức, kĩ năng · `c12` Tổng điểm
- `c00 (vMerge=continue)` — · `c01 (vMerge=continue)` — · `c02 (vMerge=continue)` — · `c03` Các cấp độ tư duy · `c06` Các cấp độ tư duy · `c09` Các cấp độ tư duy · `c12` …
- `c00 (vMerge=continue)` — · `c01 (vMerge=continue)` — · `c02 (vMerge=continue)` — · `c03` Biết · `c04` Hiểu · `c05` Vận dụng · `c06` Biết · `c07` Hiểu · `c08` Vận dụng · `c09` Biết · `c10` Hiểu · `c11` Vận dụng · `c12` —
- `c00 (vMerge=restart)` Chủ đề 1. Lịch sử và sử học · `c01` Bài 1: Hiện thực lịch sử và lịch sử được con người nhận thức · `c02` Nhận biết: -Trình bày được khái niệm lịch sử, sử học - Nêu được đối tượng, chức năng và nhiệm vụ của Sử học. - Nhận diện được hiện thực lịch sử và lịch sử được con người nhận thức qua sự kiện cụ thể. - Chỉ ra được đặc điểm của lịch sử được con người nhận thức. Thông hiểu: -Giải thích được khái niệm sử học. -Phân biệt được hiện thực lịch sử và lịch sử được con người nhận thức qua tình huống cụ thể. · `c03` I.1,2,3 · `c04` I.4 · `c05` — · `c06` — · `c07` I.5,6 · `c08` — · `c09` — · `c10` — · `c11` — · `c12` —
- `c00 (vMerge=continue)` — · `c01` Bài 2:Tri thức lịch sử và cuộc sống · `c02` Nhận biết: -Nêu được các bước trong việc thu thập, xử lý thông tin và sử liệu. - Biết cách sưu tầm, thu thập, xử lí thông tin, sử liệu để học tập, khám phá lịch sử Thông hiểu: - Giải thích được sự cần thiết phải học tập và khám phá lịch sử suốt đời. - Hiểu được bản chất của việc kết nối tri thức, bài học lịch sử vào cuộc sống / - Vận dụng / Vận dụng được kiến thức, bài học lịch sử để giải thích những vấn đề thời sự trong nước và thế giới, những vấn đề trong thực tiễn cuộc sống (ở mức độ đơn giản). - Quan tâm, yêu thích và tham gia các hoạt động tìm hiểu lịch sử, văn hoá của dân tộc Việt Nam và thế giới. · `c03` I.7,8,9 · `c04` I.10,11 · `c05` — · `c06` I.12,13 II.1a · `c07` II.1b · `c08` — · `c09` II.1c · `c10` — · `c11` II.1d · `c12` —
- `c00` Chủ đề 2. Vai trò của sử học · `c01` Bài 3: Vai trò của Sử học · `c02` Nhận biết: - Nêu được mối quan hệ giữa Sử học với công tác bảo tồn và phát huy giá trị di sản văn hóa, di sản thiên nhiên. - Kể tên được một số địa danh là tài nguyên du lịch của nước ta. -Kể tên được các loại hình di sản văn hóa Thông hiểu: - Hiểu được rõ vai trò của Sử học với công tác bảo tồn và phát huy giá trị di sản văn hóa, di sản thiên nhiên. - Giải thích được rõ vai trò của lịch sử - văn hóa đối với sự phát triển du lịch thông qua một số tình huống cụ thể. - Phân tích tác động của du lịch đối với công tác bảo tồn di tích lịch sử, di tích văn hóa Vận dụng: -Đề xuất biện pháp bảo tồn ,phát huy các giá trị của di sản - Có ý thức vận động mọi người xung quanh cùng tham gia bảo vệ di sản văn hóa, di sản thiên nhiên ở nhiều địa phương · `c03` I.14,15 1/2 TL · `c04` I.16 · `c05` — · `c06` I. 17,18 II.2a · `c07` I. 19,20 II.2b · `c08` — · `c09` II.2c · `c10` — · `c11` II.2d 1/2 TL · `c12` —
- `c00` Tổng số lệnh · `c02` — · `c03` 8+1/2TL · `c04` 4 · `c05` 0 · `c06` 6 · `c07` 6 · `c08` 0 · `c09` 2 · `c10` 0 · `c11` 2+1/2 TL · `c12` 2+1/2 TL
- `c00` Tổng số điểm · `c02` — · `c03` 3,0 · `c04` 1,0 · `c05` 0 · `c06` 1,5 · `c07` 1,5 · `c08` 0 · `c09` 0,5 · `c10` 0 · `c11` 2,5 · `c12` 10 điểm
- `c00` Tỷ lệ giữa các cấp độ tư duy · `c02` — · `c03` 30% · `c04` 10% · `c05` 0% · `c06` 15% · `c07` 15% · `c08` 0% · `c09` 5% · `c10` 0% · `c11` 2,5% · `c12` 100%
