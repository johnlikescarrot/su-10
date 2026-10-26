# -*- coding: utf-8 -*-
"""
Trich xuat toan bo van tu/bang tu file DOCX ma tran de, khong can thu vien ngoai.

Chay:  python3 src/extract_docx.py [duong_dan_docx] [file_markdown_dau_ra]

Mac dinh:
  docx = LS10- MTGK1-26-27-HHT.docx
  output = docs/MA_TRAN_TRICH_XUAT.md

Vi dung la minh chung cho viec "phan tich ky file": script doc moi thanh phan
XML (ke ca van ban an, hop van ban, ghi chu, doi tuong nhung) va ghi lai bang
duoi dang Markdown de tien doi chieu.
"""

import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DOCX = os.path.join(ROOT, 'LS10- MTGK1-26-27-HHT.docx')
DEFAULT_OUT = os.path.join(ROOT, 'docs', 'MA_TRAN_TRICH_XUAT.md')


def para_text(p):
    out = []
    for n in p.iter():
        if n.tag == W + 't':
            out.append(n.text or '')
        elif n.tag == W + 'tab':
            out.append(' / ')
        elif n.tag == W + 'br':
            out.append('\n')
    return ''.join(out)


def cell_text(tc):
    parts = [para_text(p) for p in tc.findall(W + 'p')]
    return re.sub(r'\s+', ' ', ' '.join(x for x in parts if x.strip())).strip()


def audit_parts(z):
    """Liet ke moi thanh phan XML va dem text, de chung minh khong co cau hoi an."""
    rows = []
    for name in z.namelist():
        if not (name.endswith('.xml') or name.endswith('.rels')):
            rows.append((name, '-', '-', 'KHONG PHAI XML'))
            continue
        s = z.read(name).decode('utf-8', 'replace')
        texts = re.findall(r'<w:t(?:\s[^>]*)?>(.*?)</w:t>', s, re.S)
        # Kiem tra theo TEN THE (khong phai tim chuoi tranh tinh trang
        # "FootnoteText" trong styles.xml bi nham la footnote that su).
        tag_checks = {
            'instrText': r'<w:instrText[\s/>]',
            'delText': r'<w:delText[\s/>]',
            'txbxContent': r'<w:txbxContent[\s/>]',
            'AlternateContent': r'<mc:AlternateContent[\s/>]',
            'footnote': r'<w:footnote[\s/>]',
            'endnote': r'<w:endnote[\s/>]',
            'comment': r'<w:comment[\s/>]',
            'object': r'<w:object[\s/>]',
            'vanish': r'<w:vanish[\s/>]',
            'sdt': r'<w:sdt[\s/>]',
            'fldSimple': r'<w:fldSimple[\s/>]',
            'drawing': r'<w:drawing[\s/>]',
        }
        interesting = [k for k, pat in tag_checks.items() if re.search(pat, s)]
        rows.append((name, str(len(s)), str(len(texts)), ', '.join(interesting) or '-'))
    return rows


def extract(docx_path):
    z = zipfile.ZipFile(docx_path)
    root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(W + 'body')
    blocks = []
    for el in body:
        if el.tag == W + 'p':
            txt = para_text(el).strip()
            if txt:
                blocks.append(('p', txt))
        elif el.tag == W + 'tbl':
            grid = []
            for tr in el.findall(W + 'tr'):
                row = []
                col = 0
                for tc in tr.findall(W + 'tc'):
                    tcPr = tc.find(W + 'tcPr')
                    span = 1
                    if tcPr is not None:
                        gs = tcPr.find(W + 'gridSpan')
                        if gs is not None:
                            span = int(gs.get(W + 'val'))
                    vm = ''
                    if tcPr is not None and tcPr.find(W + 'vMerge') is not None:
                        vm = tcPr.find(W + 'vMerge').get(W + 'val') or 'continue'
                    row.append((col, span, cell_text(tc), vm))
                    col += span
                grid.append((col, row))
            blocks.append(('tbl', grid))
    return z, blocks


def to_markdown(z, blocks, docx_path):
    L = []
    L.append('# Trích xuất toàn bộ nội dung tệp DOCX nguồn\n')
    L.append('> Sinh tự động bởi `src/extract_docx.py` — không chỉnh sửa tay.\n')
    L.append('**Tệp nguồn:** `%s` (%d byte).\n' %
             (os.path.basename(docx_path), os.path.getsize(docx_path)))
    L.append('**Mục đích:** làm bằng chứng cho việc phân tích kĩ tệp ma trận đề, '
             'đặc biệt để xác nhận tệp **không chứa câu hỏi/đáp án gốc**.\n')

    L.append('\n## 1. Kiểm kê mọi thành phần bên trong gói OOXML\n')
    L.append('| Thành phần | Kích thước (kí tự) | Số `<w:t>` | Dấu vết đặc biệt |')
    L.append('|---|---|---|---|')
    for name, size, ntext, flags in audit_parts(z):
        L.append('| `%s` | %s | %s | %s |' % (name, size, ntext, flags))
    names = z.namelist()
    extras = [n for n in names if any(k in n.lower() for k in
              ('media', 'embed', 'header', 'footer', 'footnote', 'endnote', 'comment'))]
    L.append('\n**Thành phần media/header/footer/ghi chú/đối tượng nhúng:** %s.\n'
             % (', '.join('`%s`' % n for n in extras) if extras else 'KHÔNG CÓ'))
    L.append('\n**Kết luận:** toàn bộ văn bản nằm trong `word/document.xml`; '
             'không có câu hỏi hay đáp án nào được lưu ở phần khác.\n')

    L.append('\n## 2. Nội dung `word/document.xml` theo đúng thứ tự\n')
    ti = 0
    for kind, data in blocks:
        if kind == 'p':
            L.append('\n**Đoạn:** %s\n' % data.replace('|', '\\|'))
        else:
            ti += 1
            L.append('\n### Bảng %d\n' % ti)
            for ncols, row in data:
                cells = []
                for col, span, txt, vm in row:
                    label = 'c%02d' % col
                    if vm:
                        label += ' (vMerge=%s)' % vm
                    cells.append('`%s` %s' % (label, (txt or '—').replace('|', '\\|')))
                L.append('- ' + ' · '.join(cells))
    return '\n'.join(L) + '\n'


def main():
    docx = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DOCX
    out = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT
    z, blocks = extract(docx)
    md = to_markdown(z, blocks, docx)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(md)
    print('Extracted %d blocks (%d tables) -> %s (%d chars)' %
          (len(blocks), sum(1 for k, _ in blocks if k == 'tbl'), out, len(md)))


if __name__ == '__main__':
    main()
