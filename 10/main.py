import sys

input_filename = sys.argv[1]


def process_input(raw_input):
    for instr in raw_input:
        if  instr[0] == 'noop':
            yield None
        else:
            yield None
            yield int(instr[1])


with open(input_filename) as f:
    raw_input = [line.strip().split(' ') for line in f]


x = 1
cycle = 0
output = 0
is_processing_add = False
current_instr = None
rows = []
current_row = []
while True:
    cycle += 1
    if (cycle + 20) % 40 == 0:
        signal_strength = x * cycle
        output += signal_strength
        print(f"{cycle=} {x=} {signal_strength=}")
    if is_processing_add:
        is_processing_add = False
        x += int(current_instr[1])
    else:
        if not raw_input:
            break
        current_instr = raw_input.pop(0)
        if current_instr[0] == 'addx':
            is_processing_add = True
    pixel_pos = (cycle % 40)
    if pixel_pos >= x - 1 and pixel_pos <= x + 1:
        current_row.append('#')
    else:
        current_row.append('.')
    if cycle % 40 == 0:
        rows.append(current_row)
        current_row = []

print(output)
for row in rows:
    print(''.join(row))
