# Đề cương ôn tập Giữa học kì I — Lịch sử 10 (Kết nối tri thức với cuộc sống)

> Năm học **2026 – 2027** · Thời gian làm bài **45 phút** · Thang điểm **10**
> Bám sát **ma trận đề & bảng đặc tả** trong `LS10- MTGK1-26-27-HHT.docx`.

## 📄 Tài liệu chính

**[`DeCuong_OnTap_GK1_LichSu10_KNTT.pdf`](DeCuong_OnTap_GK1_LichSu10_KNTT.pdf)** — 39 trang, tiếng Việt đầy đủ dấu, có mục lục tương tác và bookmark điều hướng.

Nội dung gồm 6 phần + phụ lục:

| Phần | Nội dung |
|---|---|
| **0** | Giải mã đề kiểm tra: ma trận, bảng đặc tả, phân phối điểm, 8 điểm bất cập trong tệp gốc, chiến lược 45 phút |
| **1** | Hệ thống kiến thức 3 bài (Bài 1, Bài 2, Bài 3) dưới dạng sơ đồ, bảng so sánh, ví dụ, công thức trả lời |
| **2** | Công cụ ghi nhớ: 12 chìa khoá, 10 cặp dễ nhầm, 24 flashcard, lịch ôn 7 ngày (spaced repetition) |
| **3** | **Toàn bộ 28 lệnh hỏi trắc nghiệm + 1 câu tự luận** theo đúng mã `I.1–I.20`, `II.1a–d`, `II.2a–d`, `TL` |
| **4** | Bảng đáp án nhanh, giải thích chi tiết từng câu, bài mẫu tự luận 3,0đ và thang điểm tự chấm |
| **5** | 12 câu trắc nghiệm + 2 câu tự luận ngắn luyện thêm (có đáp án) |
| **Phụ lục** | Checklist trước giờ thi, 18 thuật ngữ Anh – Việt, nguồn tài liệu, phiếu tự chấm 3 lần thử đề |

## ⚠️ Điểm cần làm rõ (rất quan trọng)

Tệp `LS10- MTGK1-26-27-HHT.docx` **không phải đề thi**: nó chỉ chứa **2 bảng** là *ma trận đề* và *bảng đặc tả yêu cầu cần đạt*. Đã kiểm kê toàn bộ 15 thành phần OOXML của tệp (kể cả văn bản ẩn, hộp văn bản, ghi chú, đối tượng nhúng) — **không có câu hỏi hay đáp án nào** (xem [`docs/MA_TRAN_TRICH_XUAT.md`](docs/MA_TRAN_TRICH_XUAT.md)).

Vì vậy, để đáp ứng yêu cầu “bao gồm **TẤT CẢ các câu hỏi cùng đáp án tương ứng**”, đề cương **tái tạo trọn vẹn đề thi** theo đúng **số lượng, mã câu, bài học, năng lực và cấp độ tư duy** đã ghi trong ma trận — và mỗi câu đều có đáp án kèm giải thích. Sự thật này được ghi rõ trong PDF (Phần 0.5 và đầu Phần 3) để người học không nhầm với đề chính thức do tổ bộ môn phát hành.

Chi tiết phân tích (cách tính điểm, cách chia ½ câu tự luận, 8 lỗi kĩ thuật của tệp gốc) nằm ở [`docs/PHAN_TICH_MA_TRAN.md`](docs/PHAN_TICH_MA_TRAN.md).

## 🔢 3 con số đáng nhớ

- **Bài 3 chiếm 5,75/10 điểm (57,5%)** → ưu tiên ôn cao nhất.
- **Mức độ Biết chiếm 50%** → nắm chắc định nghĩa, tên riêng, địa danh là có một nửa điểm.
- **Câu tự luận 3,0 điểm** = 1,0đ nhận biết + **2,0đ vận dụng** (đề xuất biện pháp) — nơi dễ mất điểm nhất.

## 🛠️ Tái tạo / kiểm tra

```bash
python3 -m pip install -r requirements.txt

python3 src/extract_docx.py     # trich xuat 2 bang tu DOCX -> docs/MA_TRAN_TRICH_XUAT.md
python3 src/build_outline.py    # sinh PDF (2 pass de co "Trang x / N" chinh xac)
python3 src/verify_pdf.py       # 65 kiem tra: ma cau, dap an, font, bookmark, glyph
```

`src/build_outline.py` dùng **reportlab** và font **Be Vietnam Pro** (Google Fonts,
giấy phép [SIL OFL 1.1](assets/fonts/OFL.txt)); kí hiệu toán/hình học lấy từ
**DejaVu Sans** có sẵn trên hệ thống. `pymupdf`/`pypdf` chỉ dùng cho bước QA.

## 📁 Cấu trúc

```
DeCuong_OnTap_GK1_LichSu10_KNTT.pdf   <- san pham chinh (PDF)
LS10- MTGK1-26-27-HHT.docx            <- nguon (ma tran + bang dac ta)
docs/
  MA_TRAN_TRICH_XUAT.md               <- trich xuat tho tu DOCX (tu dong)
  PHAN_TICH_MA_TRAN.md                <- phan tich ky, giai ma diem so, loi ky thuat
src/
  extract_docx.py                     <- trich xuat DOCX (chi dung stdlib)
  content.py                          <- toan bo noi dung de cuong (dang block)
  build_outline.py                    <- renderer reportlab -> PDF
  verify_pdf.py                       <- kiem tra chat luong PDF
assets/fonts/                         <- BeVietnamPro *.ttf + OFL.txt
requirements.txt
```

## 📚 Cơ sở biên soạn

Chương trình GDPT 2018 môn Lịch sử cấp THPT; SGK **Lịch sử 10 – Kết nối tri thức với
cuộc sống** (Chủ đề 1: *Lịch sử và sử học*; Chủ đề 2: *Vai trò của sử học*); ma trận và
bảng đặc tả trong tệp DOCX nguồn; Luật Di sản văn hoá và các danh mục di sản của UNESCO.
Học sinh nên đối chiếu thêm với vở ghi, tài liệu của giáo viên bộ môn và đề chính thức
(nếu có).
