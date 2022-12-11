import sys
from functools import reduce


def get_surrounding_coords(pos):
    result = []
    for delta in [(-1, 0),
                   (1, 0),
                   (0, -1),
                   (0, 1)]:
        coord = (pos[0] + delta[0], pos[1] + delta[1]) 
        if coord[0] >= 0 and coord[0] < UPPER_X and coord[1] >= 0 and coord[1] < UPPER_Y:
            result.append(coord)
    return result


def left_side(pos, i):
    return (i, pos[1])


def right_side(pos, i):
    return (pos[0], i)


def is_visible(pos, height):
    # If a tree is on an outside edge, it is visible
    if len(get_surrounding_coords(pos)) < 4:
        return True
    # Otherwise, just check.
    # Hack to void writing four for loops
    x, y = pos
    args = [
        ((y - 1, -1, -1), right_side),  # Up
        ((y + 1, UPPER_Y), right_side),  # Down
        ((x - 1, -1, -1), left_side),  # Left
        ((x + 1, UPPER_X), left_side),  # Right
    ]
    for range_args, pos_func in args:
        for i in range(*range_args):
            if tree_heights[pos_func(pos, i)] >= height:
                break
        else:
            return True
    return False


def calc_scenic_score(pos, height):
    # Zero if on edge
    if len(get_surrounding_coords(pos)) < 4:
        return 0
    x, y = pos
    scores = []
    # Hack to void writing four for loops
    args = [
        ((y - 1, -1, -1), right_side),  # Up
        ((y + 1, UPPER_Y), right_side),  # Down
        ((x - 1, -1, -1), left_side),  # Left
        ((x + 1, UPPER_X), left_side),  # Right
    ]
    # Check up
    for range_args, pos_func in args:
        score = 0
        for i in range(*range_args):
            score += 1
            if tree_heights[pos_func(pos, i)] >= height:
                break
        scores.append(score)

    return reduce(lambda x, y: x * y, scores)

input_filename = sys.argv[1]


with open(input_filename) as f:
    input = [[int(c) for c in line.strip()] for line in f]


UPPER_Y = len(input)
UPPER_X = len(input[0])


# Create a node for each input
tree_heights = {}
for y, l in enumerate(input):
    for x, height in enumerate(l):
        pos = (x, y)
        tree_heights[pos] = height


# Calculate whether each node is visible
total_visible = 0
for pos, height in tree_heights.items():
    if is_visible(pos, height):
        total_visible += 1
print(total_visible)
print()

# Calculate scenic scores
scenic_scores = set()
for pos, height in tree_heights.items():
    scenic_scores.add(calc_scenic_score(pos, height))
print(max(scenic_scores))
