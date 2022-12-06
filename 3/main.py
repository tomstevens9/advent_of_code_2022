import sys
from itertools import chain

input_filename = sys.argv[1]

with open(input_filename) as f:
  input = [line.strip() for line in f]


def to_priority(c):
  return ord(c) - (96 if c >= 'a' and c <= 'z' else 38)

# part 1
in_common = []
for line in input:
  first, second = line[:len(line)//2], line[len(line)//2:]
  in_common.append(set(first) & set(second))


total = 0
for p in chain(*in_common):
  total += to_priority(p)
print(total)


# part 2
badges = []
while input:
  elf1, elf2, elf3 = input.pop(0), input.pop(0), input.pop(0)
  badges.append(set(elf1) & set(elf2) & set(elf3))

total = 0
for b in chain(*badges):
  total += to_priority(b)
print(total)
