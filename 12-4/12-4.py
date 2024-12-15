lines = []

with open('12-4.txt', 'r') as f:
    for l in f:
        lines.append(l.replace('\n', ''))

ROW_WIDTH = len(lines[0])
ROW_HEIGHT = len(lines)
WORD_LENGTH = 4

word_count = 0

# Find horizontal
for i, line in enumerate(lines):
    for j, val in enumerate(line[:138]):
        if lines[i][j:j+WORD_LENGTH] == 'XMAS' or lines[i][j:j+WORD_LENGTH] == 'SAMX':
            word_count += 1

print('horizontal', word_count)

# Find vertical
for i, line in enumerate(lines[:137]):
    for j, val in enumerate(line):
        result = ''.join([line[j] for line in lines[i:i+WORD_LENGTH][j]])
        print(result)
        if lines[i:i+WORD_LENGTH][j] == 'XMAS' or lines[i:i+WORD_LENGTH][j] == 'SAMX':
            word_count += 1