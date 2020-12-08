import requests
import functools

puzzle = requests.get("https://adventofcode.com/2020/day/3/input", cookies={
                      "session": "53616c7465645f5f8ac95906a4c2e8b5418363f7c1cea6b3b565fbc839a5c4e7a81757e7f2af0bd6f943554e78caf024"})

input = puzzle.text.splitlines()

def count_trees(actual_position, my_map, map_width, slope, total_trees):
  if len(my_map) == 1:
    return total_trees
  if my_map[slope[1]][(actual_position + slope[0]) % map_width] == "#":
    return count_trees(actual_position + slope[0], my_map[slope[1]:], map_width, slope, total_trees + 1)
  else:
    return count_trees(actual_position + slope[0], my_map[slope[1]:], map_width, slope, total_trees)

# Exercise 1
print(count_trees(0, input, len(input[0]), [3, 1], 0))

# Exercise 2
multiply_trees = lambda count, slope: count * count_trees(0, input, len(input[0]), slope, 0)
print(functools.reduce(multiply_trees, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]], 1))
