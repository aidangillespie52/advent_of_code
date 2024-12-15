import re

def parse_mul(s):
    s = s.replace('mul(', '')
    s = s.replace(')', '')
    nums = s.split(',')
    return int(nums[0])*int(nums[1])

pattern = r'mul\(\d+,\d+\)'

with open('12-3.txt', 'r') as f:
    matches = re.findall(pattern, f.read())
    
    print(sum([parse_mul(s) for s in matches]))


        