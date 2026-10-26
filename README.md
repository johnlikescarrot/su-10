# Ôn tập Giữa học kì I – Lịch sử 10 (Kết nối tri thức)

Đề cương ôn tập + đề kiểm tra minh hoạ + đáp án, biên soạn bám sát **ma trận và bản đặc tả** trong
`LS10- MTGK1-26-27-HHT.docx` (năm học 2026 – 2027).

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| `ON_TAP_LS10_GK1_KNTT.pdf` | **Sản phẩm chính – 20 trang A4**, có mục lục (bookmark) trong trình đọc PDF |
| `LS10- MTGK1-26-27-HHT.docx` | Văn bản gốc: ma trận + bản đặc tả đề của tổ bộ môn |
| `tools/content.py` | Toàn bộ nội dung tài liệu (dạng block, dễ sửa) |
| `tools/build_pdf.py` | Bộ render reportlab → PDF (font DejaVu, hỗ trợ đầy đủ tiếng Việt) |

## Cấu trúc tài liệu

1. **Phần mở đầu** – cấu trúc đề, tỉ lệ mức độ tư duy, lộ trình ôn 3 ngày, 3 nguyên tắc học nhanh nhớ lâu.
2. **Phần A – Kiến thức trọng tâm** (Bài 1, 2, 3): khái niệm, bảng so sánh, mẹo nhớ (mnemonic), bẫy trắc nghiệm.
3. **Phần A (tiếp)** – sơ đồ tóm tắt 3 bài trong một trang + 12 cặp từ khoá dễ nhầm.
4. **Phần B – Đề kiểm tra minh hoạ** đúng ma trận: 20 câu TN nhiều lựa chọn + 2 câu Đúng/Sai (8 ý) +
   1 câu tự luận (2 ý) + phiếu trả lời.
5. **Phần C – Đáp án**: đáp án nhanh, giải thích chi tiết từng câu (vì sao đúng/sai), đáp án Đúng/Sai,
   dàn ý và biểu điểm tự luận, mẫu câu viết sẵn, chiến thuật phòng thi, checklist.
6. **Phụ lục** – 3 sơ đồ tư duy dạng chữ để tự chép lại và tự kiểm tra.

> Lưu ý: văn bản gốc chỉ chứa ma trận và bản đặc tả (chưa có đề/đáp án chi tiết), nên đề ở Phần B được
> biên soạn bám đúng từng lệnh hỏi I.1–I.20, II.1a–d, II.2a–d và câu tự luận mà bản đặc tả quy định.

## Xuất lại PDF

```bash
pip install reportlab          # cần font DejaVu (có sẵn trên hầu hết Linux)
python3 tools/build_pdf.py ON_TAP_LS10_GK1_KNTT.pdf
```
