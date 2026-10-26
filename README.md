# Ôn tập giữa học kì I — Lịch sử 10

## Tài liệu chính

**[Tải PDF đề cương](docs/de-cuong-lich-su-10-giua-ki-1.pdf)** — tiếng Việt, phạm vi Bài 1–3 theo ma trận Kết nối tri thức, năm học 2026–2027.

Bao gồm phân tích ma trận, kiến thức chi tiết, mẹo ghi nhớ, 23 câu tự kiểm tra có đáp án, đề luyện 20 câu lựa chọn + 2 câu đúng/sai (8 ý) + 1 câu tự luận, đáp án giải thích, bài mẫu và lịch ôn.

**Giới hạn quan trọng:** tệp Word gốc chỉ chứa ma trận và bảng đặc tả, không chứa đề thi hoặc đáp án chính thức. Không thể trích xuất câu hỏi chưa được cung cấp. Mọi câu luyện tập đều là nội dung tự biên soạn và được ghi nhãn rõ, không phải đề thi chính thức. Bản SGK không được cung cấp để kiểm chứng nguyên văn từng trang. Tài liệu ghi rõ lỗi tỉ lệ phần trăm trong bảng gốc, không tự suy diễn thang chấm từng câu.

## Các tệp

- `LS10- MTGK1-26-27-HHT.docx`: nguồn gốc, được giữ nguyên.
- `docs/nguon-docx-trich-xuat.txt`: văn bản toàn bộ đoạn và ô bảng theo thứ tự XML; bố cục ô gộp xem Word gốc.
- `docs/de-cuong-lich-su-10.md`: nội dung có thể chỉnh sửa.
- `docs/de-cuong-lich-su-10-giua-ki-1.pdf`: bản dùng để học, in hoặc chia sẻ.
- `scripts/build_pdf.py`: xuất PDF A4, nhúng phông tiếng Việt, đánh số trang.
- `scripts/check_pdf.py`: kiểm tra câu hỏi, đáp án, Unicode và lề trang.

## Tạo lại và kiểm tra PDF

Yêu cầu Python 3.11+ và phông DejaVu Sans (`/usr/share/fonts/truetype/dejavu/`, gói hệ thống thường là `fonts-dejavu-core`).

```sh
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_pdf.py
.venv/bin/python scripts/check_pdf.py
```

Đã kiểm tra tự động toàn bộ trang và xem ảnh kết xuất các trang mẫu để xác nhận tiếng Việt, ngắt dòng, lề và số trang. Kiểm tra tự động không thay thế việc rà soát chuyên môn hay đối chiếu đề thi thực tế khi được bổ sung.
