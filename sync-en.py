# Sync English translations from Wahl-Jespersen.md into en-ja.md.
#
# Algorithm:
# - From Wahl-Jespersen.md: extract non-empty lines that are NOT quoted (>),
#   NOT section headers (#), NOT separator lines (&nbsp;), NOT signatures (***)
#   These are the English translation lines (113 total).
# - From en-ja.md: find lines starting with '> ' (quoted English, 113 total).
#   Blank quoted lines ('> ' with trailing space only) are excluded via rstrip().
# - Replace each '> ' line in en-ja.md with '> ' + the corresponding WJ line,
#   matched positionally from the top.

with open('Wahl-Jespersen.md') as f:
    wj = f.readlines()
with open('en-ja.md') as f:
    enja = f.readlines()

wj_en = [l.rstrip('\n') for l in wj
         if l.strip()
         and not l.startswith('>')
         and not l.startswith('#')
         and not l.startswith('&')
         and not l.startswith('***')]

result = []
wj_idx = 0
for l in enja:
    l = l.rstrip('\n')
    if l.rstrip().startswith('> ') and wj_idx < len(wj_en):
        result.append('> ' + wj_en[wj_idx])
        wj_idx += 1
    else:
        result.append(l)

with open('en-ja.md', 'w') as f:
    f.write('\n'.join(result) + '\n')

print(f'Updated {wj_idx} lines in en-ja.md')
