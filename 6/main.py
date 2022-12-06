import sys

input_filename = sys.argv[1]


with open(input_filename) as f:
    input = f.read().strip()


def find_marker(input, window_size):
    offset = 0
    while len(set(input[offset:offset + window_size])) != window_size:
        offset += 1
    return offset + window_size


print(find_marker(input, 4))
print(find_marker(input, 14))
