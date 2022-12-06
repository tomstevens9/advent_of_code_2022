import sys
from collections import namedtuple


Instruction = namedtuple('Instruction', ['quantity', 'frm', 'to'])


def parse_state(raw_state):
    # Reverse stacks and drop stack numbers
    cleaned_state = list(reversed(raw_state.split('\n')[:-1]))
    number_of_stacks = (len(cleaned_state[0]) + 1) // 4
    stacks = [[] for _ in range(number_of_stacks)]
    for line in cleaned_state:
        stack_no = 0
        while stack_no * 4 + 3 <= len(line):
            offset = stack_no * 4
            value = line[offset: offset + 3]
            if value.startswith('['):
                stacks[stack_no].append(value[1])

            stack_no += 1
    return stacks


def parse_instructions(raw_instructions):
    instructions = []
    for raw_instruction in raw_instructions.strip().split('\n'):
        (_, quantity, _, frm, _, to) = raw_instruction.split(' ')
        instructions.append(Instruction(int(quantity), int(frm), int(to)))
    return instructions



input_filename = sys.argv[1]


with open(input_filename) as f:
    input = f.read()


raw_state, raw_instructions = input.split('\n\n')

# Part 1
print('Part 1')
print('------')
state = parse_state(raw_state)
instructions = parse_instructions(raw_instructions)
for instruction in instructions:
    from_offset = instruction.frm - 1
    to_offset = instruction.to - 1
    for _ in range(instruction.quantity):
        value = state[from_offset].pop()
        state[to_offset].append(value)

for stack in state:
    if stack:
        print(stack[-1], end='')
print()
print()

# Part 2
print('Part 2')
print('------')
state = parse_state(raw_state)
instructions = parse_instructions(raw_instructions)
for instruction in instructions:
    from_offset = instruction.frm - 1
    to_offset = instruction.to - 1
    # Get the top X crates
    crates_to_move = state[from_offset][-instruction.quantity:]
    # Remove the crates from the dat
    state[from_offset] = state[from_offset][:-instruction.quantity]
    # Add the crates to the new stack
    state[to_offset] += crates_to_move
for stack in state:
    if stack:
        print(stack[-1], end='')
print()
