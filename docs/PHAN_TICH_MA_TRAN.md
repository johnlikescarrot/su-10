# Phân tích kĩ tệp `LS10- MTGK1-26-27-HHT.docx`

> Tài liệu đi kèm PDF **`DeCuong_OnTap_GK1_LichSu10_KNTT.pdf`**.
> Bản trích xuất thô (từng ô của cả 2 bảng, kiểm kê mọi thành phần OOXML) nằm ở
> [`MA_TRAN_TRICH_XUAT.md`](MA_TRAN_TRICH_XUAT.md), được sinh tự động bởi
> `src/extract_docx.py`.

---

## 1. Tệp này thực sự chứa gì?

| Thuộc tính | Giá trị |
|---|---|
| Kích thước | 32.101 byte |
| Số thành phần trong gói OOXML | 15 (toàn bộ là XML/.rels; **không có** media, header, footer, footnote, endnote, comment, hộp văn bản hay đối tượng nhúng) |
| Nơi chứa văn bản | Duy nhất `word/document.xml` (449 thẻ `<w:t>`, ~3.335 kí tự văn bản) |
| Số phần tử cấp body | 44 |
| Số bảng | **2** |
| Số đoạn có nội dung | 5 (tiêu đề + 3 dòng thông tin + 1 dòng cấu trúc đề) |

Hai bảng đó là:

1. **MA TRẬN KIỂM TRA ĐỊNH KÌ GIỮA HỌC KÌ 1 – KHỐI 10**
2. **BẢNG ĐẶC TẢ MA TRẬN ĐỀ KIỂM TRA GIỮA HỌC KÌ 1 – LỚP 10**

Nói cách khác: đây là **bản thiết kế của đề thi** (ma trận + đặc tả yêu cầu cần đạt),
**không phải đề thi**. Tệp **không có bất kì câu hỏi hay đáp án cụ thể nào**.

### Hệ quả quan trọng

Yêu cầu của người dùng là *"bao gồm TẤT CẢ các câu hỏi cùng đáp án tương ứng từ bài
kiểm tra giữa học kì"*. Vì câu hỏi gốc không tồn tại trong tệp, đề cương đã **tái tạo
trọn vẹn đề thi theo chính mã lệnh hỏi của ma trận**:

| Thành phần | Số lượng | Mã trong đề cương |
|---|---|---|
| Trắc nghiệm nhiều lựa chọn | 20 câu | `I.1` – `I.20` |
| Trắc nghiệm Đúng/Sai | 2 câu × 4 ý | `II.1a–d`, `II.2a–d` |
| Tự luận | 1 câu (2 ý) | `TL` |
| **Tổng** | **28 lệnh hỏi TN + 1 TL** | đúng như dòng “Tổng số lệnh” của ma trận |

Mỗi câu được gắn đúng **bài**, đúng **năng lực (NL1/NL2/NL3)** và đúng **cấp độ tư duy
(Biết/Hiểu/Vận dụng)** theo ô tương ứng của ma trận; toàn bộ có đáp án và giải thích ở
Phần 4 của PDF. Việc này được ghi rõ ngay trong PDF (Phần 0 và Phần 3) để người học
không nhầm tưởng đó là đề gốc do trường phát hành.

---

## 2. Giải mã cấu trúc đề

Thông tin từ 5 đoạn văn bản đầu tệp:

- Kì kiểm tra: **giữa học kì I, khối 10, năm học 2026 – 2027**.
- Thời gian: **45 phút**.
- Cấu trúc: **20 câu TN nhiều lựa chọn + 2 câu TN Đúng/Sai + 1 câu TL**.
- Thang điểm (suy ra từ ma trận): **10 điểm**.

### Ma trận lệnh hỏi (giữ nguyên kí hiệu của tệp gốc)

| Bài | NL1·Biết | NL1·Hiểu | NL2·Biết | NL2·Hiểu | NL3·Biết | NL3·VD |
|---|---|---|---|---|---|---|
| Bài 1 | `I.1,2,3` | `I.4` | — | `I.5,6` | — | — |
| Bài 2 | `I.7,8,9` | `I.10,11` | `I.12,13` + `II.1a` | `II.1b` | `II.1c` | `II.1d` |
| Bài 3 | `I.14,15` + `½TL` | `I.16` | `I.17,18` + `II.2a` | `I.19,20` + `II.2b` | `II.2c` | `II.2d` + `½TL` |

Dòng “Tổng số lệnh”: `8+½TL | 4 | 0 | 6 | 6 | 0 | 2 | 0 | 2+½TL` → **28 lệnh hỏi TN + 1 TL**.

### Phân phối điểm (tự tính, khớp dòng “Tổng số điểm”)

Mỗi lệnh hỏi trắc nghiệm (kể cả mỗi ý Đ/S) = **0,25 điểm** → 28 × 0,25 = **7,0 điểm**.
Câu tự luận = 10 − 7 = **3,0 điểm**.

| Bài | Thành phần | Điểm | Tỉ lệ |
|---|---|---|---|
| Bài 1 | 6 câu TN | 1,50 | 15,0% |
| Bài 2 | 7 câu TN + 4 ý Đ/S | 2,75 | 27,5% |
| Bài 3 | 7 câu TN + 4 ý Đ/S + 1 TL | **5,75** | **57,5%** |
| **Tổng** | 20 TN + 8 ý Đ/S + 1 TL | **10,00** | **100%** |

Theo cấp độ tư duy: **Biết 5,0 (50%) · Hiểu 2,5 (25%) · Vận dụng 2,5 (25%)**.

> **Kết luận chiến thuật:** Bài 3 chiếm hơn một nửa điểm, và riêng nửa câu tự luận
> vận dụng đáng **2,0 điểm**. Đây là lí do đề cương dành nhiều trang nhất cho Bài 3.

### Về kí hiệu “½ TL”

Ma trận ghi `TL(1/2)` ở ô NL1–Biết và ô NL3–Vận dụng, nhưng **hai nửa không có trọng
số bằng nhau**. Từ dòng “Tổng số điểm”:

- NL1–Biết: 3,0 = (8 lệnh × 0,25 = 2,0) + **1,0** → nửa TL thứ nhất = **1,0 điểm**.
- NL3–VD: 2,5 = (2 lệnh × 0,25 = 0,5) + **2,0** → nửa TL thứ hai = **2,0 điểm**.

Vì vậy câu tự luận (3,0 điểm) gồm: **ý nhận biết 1,0đ + ý vận dụng 2,0đ**. Đề cương
đã dùng đúng thang điểm này (Bảng 4.2 trong PDF).

---

## 3. 8 điểm bất cập / lỗi kĩ thuật trong tệp gốc

Việc chỉ ra các lỗi này là một phần của “phân tích kĩ”: nếu học sinh đọc theo nguyên
bản sẽ tính sai tỉ lệ và ôn sai trọng tâm.

1. **Tệp không có đề thi thật** — chỉ là ma trận + đặc tả (xem mục 1).
2. Ma trận, dòng “Tỷ lệ”, ô NL3–Biết ghi **`0,5%`** trong khi điểm là 0,5/10 → phải là **5%**.
3. Bảng đặc tả, dòng “Tỷ lệ”, ô NL3–Vận dụng ghi **`2,5%`** trong khi điểm là 2,5/10 → phải là **25%**. Cộng dòng này theo nguyên bản chỉ được **77,5%**, không phải 100%.
4. **Hai bảng mâu thuẫn nhau** ở chính ô trên: ma trận ghi 25%, bảng đặc tả ghi 2,5%. Căn cứ dòng “Tổng số điểm” (2,5/10) → **25% là đúng**.
5. Bảng đặc tả, dòng “Tổng số lệnh”, cột “Tổng điểm” bị ghi nhầm thành **`2+1/2 TL`** (sao chép từ ô bên trái); đúng ra phải là **“28 lệnh hỏi TN + 1 TL”** như ma trận.
6. Kí hiệu **`½ TL`** dễ hiểu nhầm là chia đôi điểm (xem mục 2).
7. Lỗi nhỏ: `I. 5.6` → `I.5, I.6`; `3, 0` → `3,0`; `Bài 2:Tri thức…` thiếu dấu cách; một số ô tỉ lệ ghi `0` thay vì `0%`.
8. Cột **“Tổng điểm” bị bỏ trống ở cả 3 hàng bài** trong ma trận — điểm từng bài chỉ có thể suy ra bằng cách đếm lệnh hỏi. Đây là nguyên nhân phổ biến khiến người học đánh giá thấp Bài 3.

---

## 4. Phạm vi kiến thức cần ôn (theo bảng đặc tả)

| Chủ đề | Bài | Trọng tâm yêu cầu cần đạt |
|---|---|---|
| **Chủ đề 1. Lịch sử và sử học** | Bài 1. Hiện thực lịch sử và lịch sử được con người nhận thức | Khái niệm lịch sử, sử học; đối tượng, chức năng, nhiệm vụ của Sử học; nhận diện và phân biệt hiện thực lịch sử ↔ lịch sử được nhận thức; đặc điểm của lịch sử được nhận thức. |
| | Bài 2. Tri thức lịch sử và cuộc sống | Các bước thu thập, xử lí thông tin và sử liệu; cách sưu tầm, xử lí sử liệu; học và khám phá lịch sử suốt đời; bản chất kết nối tri thức lịch sử vào cuộc sống; vận dụng giải thích vấn đề thời sự. |
| **Chủ đề 2. Vai trò của sử học** | Bài 3. Vai trò của Sử học | Quan hệ Sử học ↔ bảo tồn/phát huy di sản; địa danh tài nguyên du lịch; các loại hình di sản văn hoá; vai trò của lịch sử – văn hoá với du lịch; tác động 2 mặt của du lịch với bảo tồn di tích; đề xuất biện pháp bảo tồn, phát huy. |

---

## 5. Cách các phát hiện trên được dùng trong PDF

| Phát hiện | Vị trí trong PDF |
|---|---|
| Cấu trúc 20 + 2 + 1, 45 phút, 10 điểm | Trang bìa; Bảng 0.1; mục 0.6 (chiến lược 45 phút) |
| Ma trận mã câu | Bảng 0.2 (Phần 0) và toàn bộ Phần 3 |
| Bảng đặc tả yêu cầu cần đạt | Bảng 0.3 (Phần 0) |
| Phân phối điểm theo bài / theo cấp độ | Bảng 0.4, 0.5 → quyết định thứ tự ưu tiên ôn tập |
| 8 lỗi kĩ thuật | Mục 0.5 |
| ½ TL = 1,0đ + 2,0đ | Bảng 1.10 (khung trả lời TL), Bảng 4.2 (thang điểm), bài mẫu 4.6 |
| Toàn bộ câu hỏi + đáp án | Phần 3 (đề) và Phần 4 (đáp án & giải thích chi tiết) |

---

## 6. Tái tạo kết quả

```bash
python3 -m pip install -r requirements.txt
python3 src/extract_docx.py                 # -> docs/MA_TRAN_TRICH_XUAT.md
python3 src/build_outline.py                # -> DeCuong_OnTap_GK1_LichSu10_KNTT.pdf
python3 src/verify_pdf.py                   # kiem tra tinh toan ven cua PDF
```
