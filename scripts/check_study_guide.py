"""Structural and PDF-layout checks; not an independent academic review."""
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'LS10- MTGK1-26-27-HHT.docx'
with zipfile.ZipFile(source) as archive:
    root = ET.fromstring(archive.read('word/document.xml'))
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
paragraphs = [''.join(t.text or '' for t in p.findall('.//w:t', ns))
              for p in root.findall('.//w:p', ns)]
source_text = '\n'.join(p for p in paragraphs if p)
assert 'BẢNG ĐẶC TẢ' in source_text
assert '20 câu TN' in source_text
assert len(root.findall('.//w:tbl', ns)) == 2
assert not root.findall('.//w:drawing', ns), 'Inspect embedded images manually'
assert not root.findall('.//w:pict', ns), 'Inspect legacy images manually'
(ROOT / 'study-guides/source-extracted.txt').write_text(source_text + '\n', encoding='utf-8')

md = (ROOT / 'study-guides/de-cuong-lich-su-10.md').read_text(encoding='utf-8')
practice = md.split('### Phần I.')[1].split('### Phần II.')[0]
assert re.findall(r'^I\.(\d+)\. ', practice, re.M) == [str(n) for n in range(1, 21)]
assert len(re.findall(r'^[A-D]\. ', practice, re.M)) == 80
true_false = md.split('### Phần II.')[1].split('### Phần III.')[0]
assert len(re.findall(r'^[a-d]\) ', true_false, re.M)) == 8
for n in range(1, 21):
    assert re.search(rf'^I\.{n} — [ABCD]\. ', md, re.M), f'Missing explanation {n}'
for q in (1, 2):
    for sub in 'abcd':
        assert f'II.{q}{sub} — ' in md
assert 'III.1.' in md and '7.4. Bài trả lời tham khảo' in md
pdf = pymupdf.open(ROOT / 'study-guides/LS10-de-cuong-on-tap-giua-ki-1-2026-2027.pdf')
text = '\n'.join(p.get_text() for p in pdf)
assert 'KHÔNG PHẢI ĐỀ THI GỐC' in text
assert 'Hiện thực' in text and 'Ví, Giặm' in text
assert '\ufffd' not in text
for i, page in enumerate(pdf, 1):
    assert page.get_text().strip(), f'Blank page {i}'
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                x0, y0, x1, y1 = span['bbox']
                assert x0 >= 40 and x1 <= page.rect.width - 40, (i, span)
                assert y0 >= 30 and y1 < page.rect.height - 17, (i, span)
for n in range(1, 21):
    assert f'I.{n}.' in text and f'I.{n} —' in text
print(f'PASS: 2 source tables, 20 MCQs / 80 options, 8 T/F judgments, 1 essay with model answer; {len(pdf)} PDF pages within margins.')
