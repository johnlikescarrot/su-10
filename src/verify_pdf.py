# -*- coding: utf-8 -*-
"""
Kiem tra chat luong PDF de cuong: tinh day du cau hoi, dap an, font, lien ket.

Chay: python3 src/verify_pdf.py
Can: pymupdf (hoac pypdf nhu phuong an du phong).
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, 'DeCuong_OnTap_GK1_LichSu10_KNTT.pdf')


def load():
    try:
        import pymupdf
        d = pymupdf.open(PDF)
        text = '\n'.join(p.get_text() for p in d)
        return d, text, 'pymupdf'
    except ImportError:
        pass
    from pypdf import PdfReader
    r = PdfReader(PDF)
    text = '\n'.join((p.extract_text() or '') for p in r.pages)
    return r, text, 'pypdf'


def main():
    if not os.path.exists(PDF):
        print('FAIL: khong tim thay', PDF)
        return 1
    d, text, backend = load()
    npages = d.page_count if backend == 'pymupdf' else len(d.pages)
    errors = []
    checks = []

    def need(cond, label):
        checks.append((cond, label))
        if not cond:
            errors.append(label)

    need(npages >= 30, 'So trang >= 30 (hien: %d)' % npages)
    need(len(text) > 60000, 'Luong van ban lon (>60k ky tu; hien: %d)' % len(text))

    # Tat ca ma cau
    for i in range(1, 21):
        need(('I.%d' % i) in text, 'Co cau I.%d' % i)
    for q in ('II.1', 'II.2'):
        need(('CÂU ' + q) in text, 'Co cau %s' % q)
        for l in 'abcd':
            need(re.search(r'\b%s\.\s' % l, text) is not None, 'Co y %s.%s' % (q, l))
    need('CÂU TL' in text or 'TL' in text, 'Co cau tu luan TL')
    for i in range(1, 13):
        need(('P.%d' % i) in text, 'Co cau bo sung P.%d' % i)

    # Dap an nhanh
    need('Bảng đáp án nhanh' in text or 'đáp án nhanh' in text.lower(),
         'Co bang dap an nhanh')
    need('4.5. Giải thích chi tiết' in text, 'Co muc giai thich 8 y Dung/Sai')
    need('4.6. Bài mẫu' in text, 'Co bai mau tu luan')

    # Noi dung cot loi
    for kw in ('Hiện thực lịch sử', 'Sử học', 'sử liệu', 'di sản văn hoá phi vật thể',
               'Tràng An', 'Kết nối tri thức', 'ma trận', 'Phong Nha'):
        need(kw in text, 'Co tu khoa: %s' % kw)

    # Tieng Viet & khong co ky tu loi
    need('Tiếng Việt' in text or 'tiếng' in text.lower(), 'Co dau tieng Viet')
    need('\x00' not in text, 'Khong co ky tu NULL (glyph loi)')
    need('\ufffd' not in text, 'Khong co ky tu thay the U+FFFD')
    need('**' not in text, 'Khong con markup **bold** bi bo sot')
    need('*Tình huống:*' not in text, 'Khong con markup *italic* bi bo sot')

    # Lien ket / bookmark
    if backend == 'pymupdf':
        toc = d.get_toc()
        need(len(toc) >= 40, 'Co >= 40 bookmark (hien: %d)' % len(toc))
        bad = [t for t in toc if t[2] < 4]
        need(not bad, 'Bookmark deu tro toi trang noi dung (>=4)')
        nlinks = sum(len(p.get_links()) for p in d)
        need(nlinks >= 50, 'Co >= 50 lien ket noi bo (hien: %d)' % nlinks)
        fonts = set()
        for p in d:
            for f in p.get_fonts():
                fonts.add(f[3])
        need(any('BeVietnam' in f or 'BV' in f for f in fonts),
             'Font Be Vietnam Pro duoc nhung vao PDF')

    ok = sum(1 for c, _ in checks if c)
    print('Backend: %s | Trang: %d | Ky tu: %d' % (backend, npages, len(text)))
    print('Kiem tra: %d/%d dat' % (ok, len(checks)))
    if errors:
        print('\nCAC LOI:')
        for e in errors:
            print('  -', e)
        return 1
    print('PASS: PDF dat yeu cau.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
