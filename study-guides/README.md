# Đề cương Lịch sử 10 — giữa học kì I 2026–2027

**Tệp chính:** [PDF 20 trang](LS10-de-cuong-on-tap-giua-ki-1-2026-2027.pdf).

## Nội dung

- Phân tích cấu trúc, mã câu và bất nhất phần tỉ lệ của ma trận.
- Kiến thức Bài 1–3 theo phạm vi bộ Kết nối tri thức được nêu trong nguồn.
- Ví dụ, phân biệt khái niệm, quy trình xử lí sử liệu, liên hệ Ví, Giặm Nghệ Tĩnh.
- Thẻ truy hồi, kế hoạch ôn 7 ngày và chiến thuật làm bài 45 phút.
- Đề luyện tự biên soạn: 20 câu nhiều lựa chọn, 2 câu đúng/sai với 8 ý, 1 tự luận hai ý; đầy đủ đáp án, giải thích và thang tự chấm.
- Đối chiếu từng yêu cầu trong bảng đặc tả với nội dung ôn.

## Giới hạn quan trọng

DOCX gốc chỉ có **hai bảng: ma trận và đặc tả**, không chứa đề thi hay đáp án. Không thể tái hiện câu hỏi đề thật từ các mã vị trí. Các câu trong PDF là **luyện tập tự biên soạn**, không phải đề thi gốc; điểm từng phần là quy ước tự luyện. Cần thêm tệp đề thi để đáp ứng yêu cầu chép đầy đủ câu hỏi và đáp án gốc.

Không có SGK cụ thể được cung cấp để đối chiếu từng trang. Kiến thức là tổng hợp theo chủ điểm, không trích nguyên văn hoặc gán số trang SGK. Nên đối chiếu SGK và hướng dẫn của giáo viên; kiểm tra tự động không thay thẩm định chuyên môn.

## Tái tạo và kiểm tra

Từ thư mục gốc, với Python 3.11+ và phông DejaVu Sans (Debian: gói `fonts-dejavu-core`):

```sh
python3 -m venv .venv
.venv/bin/pip install -r study-guides/requirements.txt
.venv/bin/python scripts/build_study_guide.py
.venv/bin/python scripts/check_study_guide.py
```

Có thể đặt `DEJAVU_FONT_DIR` nếu phông không nằm trong `/usr/share/fonts/truetype/dejavu`.

- `de-cuong-lich-su-10.md`: nội dung biên soạn để đọc và sửa.
- `source-extracted.txt`: toàn bộ chữ từ đoạn văn và ô bảng DOCX, theo thứ tự XML; không tái hiện vị trí/cột bảng. Đọc DOCX gốc để kiểm tra bố cục.
- `scripts/build_study_guide.py`: sinh PDF A4, nhúng phông tiếng Việt, giữ câu hỏi cùng các lựa chọn.
- `scripts/check_study_guide.py`: trích lại nguồn, kiểm số bảng và ảnh; kiểm đủ câu/lựa chọn/lời giải; kiểm trích chữ tiếng Việt, trang trắng và biên chữ của mọi trang PDF. Không tự xác minh đáp án về mặt học thuật.

Đã xem ảnh mẫu trang mở đầu, lý thuyết, đề luyện và checklist. Kiểm biên chữ toàn bộ PDF đạt; chưa có phản biện độc lập của giáo viên.
