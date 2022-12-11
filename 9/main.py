from collections import namedtuple

import sys


Movement = namedtuple("Movement", ["direction", "amount"])


input_filename = sys.argv[1]
char_to_vector = {
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, -1),
    "U": (0, 1),
}


def input_to_movement(s):
    raw_dir, raw_amount = s.strip().split(" ")
    return Movement(char_to_vector[raw_dir], int(raw_amount))


def vec_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def vec_subtract(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])


def should_move_tail(head_pos, tail_pos):
    diff = vec_subtract(head_pos, tail_pos)
    return abs(diff[0]) > 1 or abs(diff[1]) > 1


def get_movement(head_pos, tail_pos):
    raw_movement = vec_subtract(head_pos, tail_pos)
    return (0 if raw_movement[0] == 0 else raw_movement[0] // abs(raw_movement[0]),
            0 if raw_movement[1] == 0 else raw_movement[1] // abs(raw_movement[1]))


with open(input_filename) as f:
    input = [input_to_movement(line) for line in f]


# Parts one and two. knots = [(0, 0), (0, 0)] for part 1
knots = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
]
tail_positions = set([knots[-1]])
for movement in input:
    for i in range(movement.amount):
        new_knots = [vec_add(knots[0], movement.direction)]
        for i in range(1, len(knots)):
            head_pos = new_knots[i - 1]
            tail_pos = knots[i]
            if (should_move_tail(head_pos, tail_pos)):
                tail_movement = get_movement(head_pos, tail_pos)
                new_knots.append(vec_add(tail_pos, tail_movement))
            else:
                new_knots.append(tail_pos)
        knots = new_knots
        tail_positions.add(knots[-1])
        print(knots[0])
        print(knots[1])
        print()
print(len(tail_positions))

