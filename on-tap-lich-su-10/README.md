# Đề cương ôn tập Giữa học kì I — Lịch sử 10 (Kết nối tri thức)

Bộ công cụ dựng **đề cương ôn tập giữa học kì I môn Lịch sử lớp 10** thành tệp PDF, biên soạn bám
theo ma trận và bản đặc tả trong tệp `LS10- MTGK1-26-27-HHT.docx` ở thư mục gốc của kho lưu trữ.

**Tệp thành phẩm:** [`dist/De-cuong-on-tap-Giua-ky-I-Lich-su-10.pdf`](dist/De-cuong-on-tap-Giua-ky-I-Lich-su-10.pdf)
— 42 trang A4, có mục lục, dấu trang PDF (bookmark) và đánh số trang.

---

## 1. Tệp nguồn nói gì?

Tệp `.docx` được phân tích trực tiếp từ XML của Word (45 khối nội dung, **2 bảng**):

| Nội dung | Chi tiết |
|---|---|
| Bảng 1 | Ma trận kiểm tra định kì giữa học kì 1 — khối 10, năm học 2026–2027, 45 phút |
| Bảng 2 | Bảng đặc tả ma trận: yêu cầu cần đạt gắn với từng số hiệu câu hỏi |
| Cấu trúc đề | 20 câu trắc nghiệm nhiều lựa chọn + 2 câu trắc nghiệm đúng/sai (4 ý/câu) + 1 câu tự luận |
| Phạm vi | Chủ đề 1 (Bài 1, Bài 2) và Chủ đề 2 (Bài 3) |
| Trọng số | NL1 30% + 10%; NL2 15% + 15%; NL3 5% + 25% |

Tệp nguồn **không chứa** nội dung câu hỏi và đáp án. Vì vậy tài liệu gồm hai lớp: phần nguyên văn
từ nguồn (cấu trúc, phân bố câu, yêu cầu cần đạt, trọng số) và phần biên soạn (hệ thống kiến thức,
đề tham khảo, đáp án, kế hoạch ôn tập). Đề ở Phần VII bám đúng từng dòng của ma trận: 20 câu nhiều
lựa chọn, 2 câu đúng/sai × 4 ý, 1 câu tự luận hai phần.

## 2. Cấu trúc tài liệu

| Phần | Nội dung |
|---|---|
| I | Định hướng ôn tập — đọc ma trận, bảng đối chiếu từng câu với bài, trọng số điểm |
| II | Bài 1 — Hiện thực lịch sử và lịch sử được con người nhận thức |
| III | Bài 2 — Tri thức lịch sử và cuộc sống |
| IV | Bài 3 — Vai trò của Sử học (di sản, du lịch, tác động hai chiều) |
| V | Bảng tổng hợp ghi nhớ nhanh, 10 câu “thần chú” |
| VI | Kĩ năng làm bài và chiến lược 45 phút |
| VII | **Đề kiểm tra tham khảo** (20 TN + 2 Đ/S + 1 TL) |
| VIII | **Đáp án, giải thích từng câu, biểu điểm, bài tự luận mẫu, bảng tự đánh giá** |
| IX | 30 câu tự kiểm tra kèm đáp án ngắn |
| X | Kế hoạch ôn tập 7 ngày, checklist, 15 phút cuối trước giờ thi |
| Phụ lục | Ghi chú biên soạn, đối chiếu nguồn, hướng dẫn tái tạo |

## 3. Tái tạo tệp PDF

Yêu cầu: Python 3.9+ và gói `reportlab`.

```bash
pip install -r requirements.txt
python build.py                                   # xuất ra dist/…
python build.py --output /duong/dan/khac.pdf      # xuất ra đường dẫn khác
```

Quy trình dựng gồm hai lượt: lượt 1 ghi lại số trang của từng tiêu đề, lượt 2 dựng mục lục có số
trang thật. Hai lượt có cùng số dòng mục lục nên số trang không lệch.

### Cấu trúc mã nguồn

```
build.py                 điểm vào: ghép các phần, dựng mục lục hai lượt, xuất PDF
lib/theme.py             bảng màu, phông chữ, kiểu đoạn
lib/blocks.py            dải tiêu đề, hộp ghi nhớ/bẫy/ví dụ, bảng biểu, DSL nội dung
lib/document.py          khuôn trang A4, đầu–chân trang, bìa, dấu trang PDF
content/part1…part11.py  nội dung từng phần (Phần I → Phụ lục)
assets/fonts/            DejaVu Serif & Sans (đủ dấu tiếng Việt) + giấy phép
dist/                    tệp PDF thành phẩm
```

Nội dung được viết bằng một DSL nhỏ: mỗi khối là một tuple `("kiểu", …)` — `p`, `lead`, `h2`, `h3`,
`h4`, `bul`, `num`, `dash`, `box` (định nghĩa / mẹo nhớ / bẫy / ví dụ), `tbl`, `q`, `opts`, `stmt`,
`examhead`, `qgroup`, `note`, `small`, `sp`, `rule`, `pb`. Muốn sửa nội dung chỉ cần sửa `content/`.

## 4. Phông chữ và giấy phép

* Nội dung: dùng phông **DejaVu Serif** / **DejaVu Sans** — giấy phép tự do, xem
  `assets/fonts/LICENSE_DEJAVU`; bộ ký tự Latin Extended Additional phủ đủ tiếng Việt.
* Mã nguồn dựng tài liệu: MIT (xem `LICENSE`).
* Nội dung kiến thức biên soạn theo sách giáo khoa *Lịch sử 10 — Kết nối tri thức với cuộc sống*
  và bản đặc tả của đề, không sao chép nguyên văn sách giáo khoa.

## 5. Lưu ý khi sử dụng

* Đề ở Phần VII là **đề tham khảo**, không phải đề chính thức của trường. Nếu có đề gốc, chỉ cần thay
  `content/part7_exam.py` và `content/part8_answers.py`.
* Số liệu di sản (8 di sản thế giới của Việt Nam) tính đến 2025; cần cập nhật nếu UNESCO ghi danh thêm.
* Tài liệu dùng cho mục đích ôn tập nội bộ.
