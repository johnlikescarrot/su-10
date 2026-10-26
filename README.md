# Đề cương ôn tập giữa học kì I – Lịch sử 10 (Kết nối tri thức)

Tài liệu ôn tập được biên soạn từ **ma trận và bảng đặc tả** của đề kiểm tra định kì giữa học kì I
môn Lịch sử 10, năm học 2026 – 2027 (tệp nguồn: `LS10- MTGK1-26-27-HHT.docx`).

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| `De-cuong-on-tap-Giua-ki-1-Lich-su-10-KNTT.pdf` | **Bản PDF hoàn chỉnh** – 33 trang, có bìa, mục lục tương tác, bookmark |
| `src/00_intro.md` … `src/07_chienluoc.md` | Nội dung nguồn (Markdown nhẹ) của từng phần |
| `build_pdf.py` | Script dựng PDF bằng ReportLab |

## Cấu trúc tài liệu

- **Phần 0** – Phân tích ma trận, bảng đặc tả, trọng số điểm và chiến lược ôn tập.
- **Phần 1 – 3** – Hệ thống kiến thức Bài 1, Bài 2, Bài 3: khái niệm, bảng so sánh, sơ đồ tổng kết,
  mẹo ghi nhớ, câu hỏi tự luận kèm bài trả lời mẫu.
- **Phần 4** – 10 cặp khái niệm dễ nhầm, bảng động từ đề bài, 20 thẻ ghi nhớ nhanh, bản đồ từ khoá.
- **Phần 5** – Đề luyện tập mô phỏng đúng cấu trúc: 20 câu trắc nghiệm + 2 câu Đúng/Sai (8 ý) + 1 câu tự luận.
- **Phần 6** – Đáp án, giải thích từng câu, bảng Đúng/Sai, thang điểm và bài làm mẫu.
- **Phần 7** – Phân bổ 45 phút, kỹ thuật làm từng dạng câu, lộ trình ôn 5 ngày, checklist.

## Dựng lại PDF

```bash
pip install reportlab
python3 build_pdf.py
```

Yêu cầu font DejaVu (`/usr/share/fonts/truetype/dejavu`) để hiển thị đầy đủ tiếng Việt.
Script dựng hai lượt và lưu số trang mục lục trong `.toc_cache.json` để mục lục khớp chính xác.
