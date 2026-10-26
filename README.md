# Đề cương ôn tập Giữa học kì 1 – Lịch sử 10 (Kết nối tri thức với cuộc sống)

Tài liệu ôn thi được biên soạn **bám sát ma trận và bảng đặc tả** của đề kiểm tra
định kì giữa học kì 1 môn Lịch sử lớp 10, năm học 2026 – 2027.

## Sản phẩm

| Tệp | Mô tả |
|---|---|
| [`De-cuong-on-tap-Giua-HK1-Lich-su-10-KNTT.pdf`](De-cuong-on-tap-Giua-HK1-Lich-su-10-KNTT.pdf) | **Đề cương hoàn chỉnh (42 trang)** – bản PDF chính thức |
| `LS10- MTGK1-26-27-HHT.docx` | Tệp ma trận + bảng đặc tả đề kiểm tra (nguồn gốc, không chỉnh sửa) |
| `tools/decuong/` | Mã nguồn Python sinh ra PDF (có thể tái tạo) |

## Nội dung tài liệu

| Phần | Nội dung |
|---|---|
| **A** | Phân tích đề: cấu trúc, ma trận, bảng đặc tả, chiến thuật phòng thi 45 phút |
| **B** | Chủ đề 1 – Bài 1 (Hiện thực lịch sử và lịch sử được con người nhận thức) và Bài 2 (Tri thức lịch sử và cuộc sống) |
| **C** | Chủ đề 2 – Bài 3 (Vai trò của Sử học): Sử học với di sản và với du lịch |
| **D** | Tổng hợp ghi nhớ nhanh: bảng tổng hợp, 15 mẹo nhớ, bẫy đề, từ khoá nhận diện |
| **E** | Ngân hàng câu hỏi: **50 câu trắc nghiệm + 8 câu Đúng/Sai (32 ý) + 6 câu tự luận**, có đáp án và giải thích |
| **F** | Đề mẫu bám ma trận (20 TN + 2 Đ/S + 1 TL) kèm thang điểm chi tiết |
| **G** | Checklist tự kiểm tra, lịch ôn 7 ngày, ghi chú |

## Điểm nổi bật

- **Bám đúng ma trận**: mọi nội dung đều xuất phát từ bảng đặc tả trong tệp `.docx` gốc.
- **Tối ưu ghi nhớ**: sơ đồ khối, bảng so sánh, bảng phân loại, mẹo nhớ có vần điệu, câu chốt.
- **Đầy đủ đáp án**: mỗi câu hỏi đều có đáp án; các câu dễ sai đều có giải thích nguyên nhân.
- **Tự kiểm tra được**: đề mẫu 45 phút + thang điểm + bảng quy đổi điểm.

## Tái tạo PDF

```bash
pip install reportlab
cd tools/decuong
python build.py ../../De-cuong-on-tap-Giua-HK1-Lich-su-10-KNTT.pdf
```

Chi tiết xem [`tools/decuong/README.md`](tools/decuong/README.md).
