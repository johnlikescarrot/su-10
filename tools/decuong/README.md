# Nguồn sinh PDF – Đề cương ôn tập Giữa HK1 Lịch sử 10 (KNTT)

Thư mục này chứa mã nguồn Python dùng để sinh ra tệp
`De-cuong-on-tap-Giua-HK1-Lich-su-10-KNTT.pdf` ở thư mục gốc của kho.

## Yêu cầu

- Python 3.11+
- ReportLab 4.x hoặc 5.x: `pip install reportlab`
- Font DejaVu (thường có sẵn trên Linux tại `/usr/share/fonts/truetype/dejavu/`).
  Font này có đầy đủ dấu tiếng Việt.

## Cách sinh lại PDF

```bash
cd tools/decuong
python build.py ../../De-cuong-on-tap-Giua-HK1-Lich-su-10-KNTT.pdf
```

## Cấu trúc mã nguồn

| Tệp | Nội dung |
|---|---|
| `style.py` | Khung trình bày: font, màu, style, page template, mục lục, bookmark, các component (bảng, ô ghi chú, sơ đồ, câu hỏi…) |
| `build.py` | Ghép toàn bộ nội dung và xuất PDF |
| `content_intro.py` | Lời nói đầu, hướng dẫn sử dụng |
| `content_a.py` | Phần A – Phân tích đề và chiến lược ôn tập |
| `content_b.py` | Phần B – Chủ đề 1 (Bài 1, Bài 2) |
| `content_c.py` | Phần C – Chủ đề 2 (Bài 3) |
| `content_d.py` | Phần D – Tổng hợp ghi nhớ nhanh |
| `content_e.py` | Phần E – Ngân hàng câu hỏi (50 TN + 8 Đ/S + 6 TL) |
| `content_f.py` | Phần F – Đề mẫu bám ma trận + thang điểm |
| `content_g.py` | Phần G – Checklist tự kiểm tra |
| `qbank.py` | Tiện ích cân bằng phân bố đáp án A/B/C/D |

## Ghi chú kỹ thuật

- Bố cục dùng A4, lề trái 48pt, phải 42pt, trên 62pt, dưới 52pt.
- Mục lục và bookmark được tạo tự động nhờ lớp `Anchor` (Flowable rỗng)
  đặt ngay trước mỗi tiêu đề, nên số trang trong mục lục luôn khớp.
- Một số ký hiệu (`☐`, `✓`, `★`, `⚠`) không có trong DejaVu Serif nên được
  tự động chuyển sang DejaVu Sans bằng hàm `fix()` trong `style.py`
  để tránh hiện tượng ô vuông trống.
