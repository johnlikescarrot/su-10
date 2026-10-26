"""Smoke checks for the generated PDF: coverage, Unicode and page bounds."""
from pathlib import Path
import pymupdf
root = Path(__file__).resolve().parents[1]
pdf = pymupdf.open(root / 'docs/de-cuong-lich-su-10-giua-ki-1.pdf')
text = '\n'.join(page.get_text() for page in pdf)
assert len(pdf) > 0
assert '\ufffd' not in text
for word in ['HIỆN THỰC', 'ĐÁP ÁN', 'NGUỒN', 'TỰ BIÊN SOẠN']:
    assert word in text, word
for n in range(1, 21):
    assert f'Câu {n}.' in text, n
for n in [1, 2]:
    for letter in 'abcd':
        assert f'II.{n}{letter}' in text
assert 'Câu III.1.' in text
for i, page in enumerate(pdf):
    assert len(page.get_text()) > 100, f'Empty page {i+1}'
    for block in page.get_text('blocks'):
        assert block[0] >= 40 and block[2] <= 556, (i+1, block)
        assert block[1] >= 20 and block[3] <= 815, (i+1, block)
print(f'PASS: {len(pdf)} pages; 20 multiple-choice questions, 8 true/false answers, essay, Unicode and margins.')
