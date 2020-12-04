import requests
puzzle = requests.get("https://adventofcode.com/2020/day/1/input", cookies={
                      "session": "53616c7465645f5f8ac95906a4c2e8b5418363f7c1cea6b3b565fbc839a5c4e7a81757e7f2af0bd6f943554e78caf024"})

input = list(map(int, puzzle.text.splitlines()))

def find2020Tuple(value, rest):
  if value + rest[0] == 2020:
    return value, rest[0]
  
  if len(rest) == 1:
    return ()

  else:
    return find2020Tuple(value, rest[1:])

def find2020Triple(first, second, rest):
  if first + second + rest[0] == 2020:
    return first, second, rest[0]
  
  if len(rest) == 1:
    return ()

  else:
    return find2020Triple(first, second, rest[1:])
  
# Exercise one
for i in range(len(input)):
  result = find2020Tuple(input[i], input[1:])

  if len(result) > 0:
    print(result[0] * result[1])
    break

# Exercise two
for i in range(len(input)):
  for j in range(len(input)):
    result = find2020Triple(input[i], input[j], input[1:])

    if len(result) > 0:
      print(result[0] * result[1] * result[2])
      break
