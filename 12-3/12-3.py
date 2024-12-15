import re

def parse_mul(s):
    s = s.replace('mul(', '')
    s = s.replace(')', '')
    nums = s.split(',')
    return int(nums[0])*int(nums[1])

def parse_matches(l):
    EXECUTE = True
    total_sum = 0
    for s in l:
        if s == 'do()':
            EXECUTE = True
        
        elif s == "don't()":
            EXECUTE = False

        else:
            if EXECUTE: total_sum += parse_mul(s)
    
    print(total_sum)
        
text = ""

with open('12-3.txt', 'r') as f:
    text = f.read()
    
pattern = r'mul\(\d+,\d+\)'
matches = re.findall(pattern, text)
print(sum([parse_mul(s) for s in matches]))

patterns = [
    r'mul\(\d+,\d+\)',
    r"don't\(\)",
    r"do\(\)"
]

all_matches = []

for pattern in patterns:
    for match in re.finditer(pattern, text):
        all_matches.append({
            'match': match.group(0),   # The matched string
            'start': match.start(),    # Starting position in the text
            'end': match.end()         # Ending position in the text
        })

all_matches_ordered = sorted(all_matches, key=lambda x: x['start'])
all_matches_ordered = [x['match'] for x in all_matches_ordered]

parse_matches(all_matches_ordered)

    