"""Convert thesis .docx to a diff-friendly Markdown snapshot.

Usage: python paper/scripts/docx_to_md.py <input.docx> <output.md>

The .docx remains the authoritative source; the .md is regenerated after
each Word revision. Do not edit the .md by hand.
"""

import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

STYLE_MAP = {
    'Title': '# ',
    'Heading1': '## ',
    'Heading2': '### ',
    'Heading3': '#### ',
}

GENERATED_NOTE = (
    '<!-- 本文件由 Word 正文自动生成，仅用于版本比对，请勿直接编辑；'
    'Word 修订后运行 paper/scripts/docx_to_md.py 重新生成。 -->\n'
)


def para_text(p):
    return ''.join(t.text or '' for t in p.iter(W + 't'))


def para_style(p):
    pPr = p.find(W + 'pPr')
    if pPr is None:
        return ''
    st = pPr.find(W + 'pStyle')
    return st.get(W + 'val') if st is not None else ''


def split_sentences(text):
    # One sentence per line for readable diffs; split only after Chinese
    # sentence-ending punctuation to avoid breaking references and URLs.
    parts = re.split(r'(?<=[。！？])', text)
    return [s for s in (p.strip() for p in parts) if s]


def table_rows(tbl):
    rows = []
    for tr in tbl.findall(W + 'tr'):
        cells = []
        for tc in tr.findall(W + 'tc'):
            text = ' '.join(para_text(p) for p in tc.findall('.//' + W + 'p'))
            cells.append(text.strip().replace('|', '\\|'))
        rows.append(cells)
    return rows


def main(src, dst):
    with zipfile.ZipFile(src) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(W + 'body')
    lines = [GENERATED_NOTE]
    for el in body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            text = para_text(el).strip()
            if not text:
                continue
            style = para_style(el)
            if style in STYLE_MAP:
                lines.append(STYLE_MAP[style] + text)
            elif style == 'Caption':
                lines.append('**' + text + '**')
            else:
                lines.extend(split_sentences(text))
            lines.append('')
        elif tag == 'tbl':
            rows = table_rows(el)
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [''] * (width - len(r)) for r in rows]
                lines.append('| ' + ' | '.join(rows[0]) + ' |')
                lines.append('| ' + ' | '.join(['---'] * width) + ' |')
                for r in rows[1:]:
                    lines.append('| ' + ' | '.join(r) + ' |')
                lines.append('')
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines).rstrip() + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
