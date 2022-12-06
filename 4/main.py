from collections import namedtuple
import sys

Range = namedtuple('Range', ['start', 'end'])
input_filename = sys.argv[1]


def to_range(s):
    raw_start, raw_end = s.split('-')
    return Range(start=int(raw_start), end=int(raw_end))


def is_range_in_range(inner, outer):
    return outer.start <= inner.start and inner.end <= outer.end

def do_ranges_overlap(r1, r2):
    return (r1.start <= r2.start and r2.start <= r1.end) or (r2.start <= r1.start and r1.start <= r2.end)


with open(input_filename) as f:
    range_pairs = []
    for line in f:
        raw_ranges = line.strip().split(',')
        range_pairs.append([to_range(s) for s in raw_ranges])


total_1 = 0
total_2 = 0
for r1, r2 in range_pairs:
    if is_range_in_range(r1, r2) or is_range_in_range(r2, r1):
        total_1 += 1
    if do_ranges_overlap(r1, r2):
        total_2 += 1

print(total_1)
print(total_2)
