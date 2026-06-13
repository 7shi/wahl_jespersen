# Build a Japanese introductory article (intro-ja.md) from existing files.
#
# The article layout lives in intro-ja.template.md, which contains two
# placeholders:
#   {summary} - replaced with summary-ja.md. Its '# ' title and the '## 要約'
#               heading are dropped (they duplicate the article title and the
#               template's '## 概要'); any other '## ' section is demoted to
#               '### ' so it nests under 概要.
#   {body}    - replaced with Wahl-Jespersen-ja.md, minus the English quotes.
#
# Filtering of the body:
# - Drop every line starting with '>' (the English source quotes).
# - Collapse the blank-line runs left behind so paragraphs stay single-spaced.
# - Demote section headers by one level (# -> ##) so they nest under the
#   article title alongside the 概要 section.
# Separators (&nbsp;) and signatures (***) are kept.


from pathlib import Path
HERE = Path(__file__).parent
ROOT = HERE.parent


def collapse_blanks(lines):
    out = []
    for l in lines:
        if l == '' and (not out or out[-1] == ''):
            continue
        out.append(l)
    while out and out[-1] == '':
        out.pop()
    return out


with open(ROOT / 'summary-ja.md') as f:
    summary = [l.rstrip('\n') for l in f]
# Drop the '# ' title and the '## 要約' heading (both overlap the template);
# demote any remaining '## ' section (## 二つの立場) to '### '.
out = []
for l in summary:
    if l.startswith('# ') or l == '## 要約':
        continue
    if l.startswith('## '):
        l = '#' + l
    out.append(l)
summary = '\n'.join(collapse_blanks(out))

with open(ROOT / 'Wahl-Jespersen-ja.md') as f:
    body = [l.rstrip('\n') for l in f]
# Remove English quote lines, demote section headers, then collapse the gaps.
# The first non-blank line (document title in Japanese) becomes a '## ' heading.
body = [l for l in body if not l.startswith('>')]
body = ['#' + l if l.startswith('# ') else l for l in body]
for i, l in enumerate(body):
    if l.strip():
        body[i] = '## ' + l
        break
body = '\n'.join(collapse_blanks(body))

with open(HERE / 'intro-ja.template.md') as f:
    template = f.read()

result = template.replace('{summary}', summary).replace('{body}', body)

with open(HERE / 'intro-ja.md', 'w') as f:
    f.write(result)

print('Wrote intro-ja.md')
