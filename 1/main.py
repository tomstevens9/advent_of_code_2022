import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
  raw_input = f.read()

input = [[int(y) for y in x.split('\n') if y]
         for x
         in raw_input.split('\n\n')]


# Part 1
# print(max(sum(elem) for elem in input))

# Part 2
print(sum(sorted(sum(elem) for elem in input)[-3:]))
