import sys


class Node:
    def __init__(self, name, parent, size=None):
        self.name = name
        self.parent = parent
        self.children = []
        # Assume a node created without a size is a directory
        self.is_dir = size is None
        self.size = size


def calculate_size(node):
    if node.size is not None:
        return node.size
    size = 0
    for child in node.children:
        size += calculate_size(child)
    node.size = size
    return node.size


input_filename = sys.argv[1]


cur_node = Node("/", parent=None)
root = cur_node
with open(input_filename) as f:
    for raw_line in f:
        line = raw_line.strip()  # Remove trailing newline
        if line == '$ cd /':  # Skip first line
            continue
        elif line.startswith("$ cd"):
            dirname = line.split("$ cd ")[-1]
            if dirname == "..":
                cur_node = cur_node.parent
            else:
                cur_node = [node for node in cur_node.children if node.name == dirname][0]
        elif line.startswith("$"):
            continue
        elif line.startswith("dir"):
            ls_dir = line.split("dir ")[-1]
            node = Node(ls_dir, parent=cur_node)
            cur_node.children.append(node)
        else:
            raw_filesize, filename = line.split(" ")
            filesize = int(raw_filesize)
            node = Node(filename, parent=cur_node, size=filesize)
            cur_node.children.append(node)


def part_1(node):
    result = sum(part_1(child) for child in node.children)
    if node.is_dir and node.size < 100000:
        result += node.size
    return result

def part_2(space_required, node, best_candidate=None):
    if not node.is_dir:
        return best_candidate
    if best_candidate is None or (node.size >= space_required and node.size < best_candidate):
        best_candidate = node.size
    return min(part_2(space_required, child, best_candidate) for child in node.children)

calculate_size(root)
print(part_1(root))
required_space = 30000000 - (70000000 - root.size)
print(required_space)
print(part_2(required_space, root))
