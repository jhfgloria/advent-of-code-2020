import requests
import re

puzzle = requests.get("https://adventofcode.com/2020/day/2/input", cookies={
                      "session": "53616c7465645f5f8ac95906a4c2e8b5418363f7c1cea6b3b565fbc839a5c4e7a81757e7f2af0bd6f943554e78caf024"})

def parse_line(line):
    regex = r'(\d*)-(\d*) ([a-z]): ([a-z]*)'
    tuple = re.findall(regex, line)

    return {"min": int(tuple[0][0]), "max": int(tuple[0][1]), "char": tuple[0][2], "password": tuple[0][3]}

def has_min_max_occurrences(policy):
    count = policy["password"].count(policy["char"])
    return count >= policy["min"] and count <= policy["max"]

def has_at_most_one_position(policy):
    first_position = policy["password"][policy["min"]-1] == policy["char"]
    second_position = policy["password"][policy["max"]-1] == policy["char"]
    return first_position ^ second_position

input = list(map(parse_line, puzzle.text.splitlines()))

# Exercise 1
print(len(list(filter(has_min_max_occurrences, input))))

# Exercise 2
print(len(list(filter(has_at_most_one_position, input))))
