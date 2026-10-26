# Đề cương ôn tập giữa học kì I — Lịch sử 10 (Kết nối tri thức)

Kho lưu trữ tài liệu ôn tập môn **Lịch sử 10** bộ sách *Kết nối tri thức với cuộc sống*, biên soạn
bám sát **ma trận đề và bảng đặc tả** của đề kiểm tra định kì giữa học kì I năm học 2026–2027.

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| `De-cuong-on-tap-Giua-ky-1-Lich-su-10-KNTT.pdf` | **Đề cương hoàn chỉnh (32 trang)** — bản PDF có mục lục liên kết, dàn trang A4 |
| `LS10- MTGK1-26-27-HHT.docx` | Tệp đề gốc: ma trận + bảng đặc tả của đề kiểm tra |
| `build/` | Mã nguồn dựng PDF (Python + ReportLab) |
| `assets/fonts/` | Phông Be Vietnam Pro (SIL Open Font License 1.1) |

## Cấu trúc đề cương

0. **Bản đồ ôn tập** — phân tích ma trận/đặc tả, bản đồ phân bổ câu hỏi, chiến lược phân bổ 45 phút.
1. **Bài 1. Hiện thực lịch sử và lịch sử được con người nhận thức** — khái niệm, đối tượng,
   3 chức năng, 4 nguyên tắc, bảng so sánh 7 tiêu chí, mẹo nhớ, 4 bẫy đề.
2. **Bài 2. Tri thức lịch sử và cuộc sống** — vai trò của tri thức lịch sử, học tập suốt đời,
   sử liệu (loại hình, gốc/phái sinh, đánh giá nguồn), quy trình 4 bước.
3. **Bài 3. Vai trò của Sử học** — di sản văn hoá/thiên nhiên, bảng di sản UNESCO của Việt Nam,
   5 vai trò của Sử học với bảo tồn, tác động hai chiều của du lịch, 6 nhóm biện pháp, liên hệ Nghệ An.
4. **Hệ thống câu hỏi và đáp án** — 20 câu trắc nghiệm nhiều lựa chọn + 2 câu đúng/sai (8 ý) +
   1 câu tự luận. Mỗi câu đều có đáp án, giải thích “Vì sao”, dàn ý và bài làm tham khảo.
5. **Ôn nhanh & chiến lược** — sơ đồ tư duy tổng kết, 36 flashcard, kế hoạch ôn 5 ngày,
   checklist tự đánh giá, 10 lỗi mất điểm, 3 đề tự luận luyện thêm.

## Dựng lại bản PDF

```bash
python -m venv .venv
.venv/bin/pip install reportlab
.venv/bin/python build/build_pdf.py
```

Kết quả được ghi đè vào `De-cuong-on-tap-Giua-ky-1-Lich-su-10-KNTT.pdf`.

## Ghi chú

Tệp đề gốc cung cấp **ma trận và bảng đặc tả** (số lệnh hỏi, dạng câu, mức độ tư duy, đơn vị kiến thức
cho từng câu) nhưng không chứa nội dung chữ của câu hỏi. Vì vậy bộ câu hỏi ở Phần 4 được biên soạn
bám sát từng dòng của bảng đặc tả; khi có tệp đề chính thức, chỉ cần thay nội dung câu hỏi — phần kiến
thức của đề cương vẫn dùng được nguyên vẹn.
