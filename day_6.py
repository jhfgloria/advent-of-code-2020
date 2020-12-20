import requests
import re
import functools

puzzle = requests.get("https://adventofcode.com/2020/day/6/input", cookies={
                      "session": "53616c7465645f5f8ac95906a4c2e8b5418363f7c1cea6b3b565fbc839a5c4e7a81757e7f2af0bd6f943554e78caf024"})

# Exercise 1
forms = re.sub(r'(\n){2}', ',', puzzle.text).replace('\n', '').split(',')
print(functools.reduce(lambda count, form: count + len(set(form)), forms, 0))

# Exercise 2
input = puzzle.text.splitlines()
groups = []
group = []

for i in range(len(input)):
  if i == len(input) - 1:
    group.append(input[i])
    groups.append(group)
    break

  if input[i] == '':
    groups.append(group)
    group = []

  else:
    group.append(input[i])

def find_matching_answers(forms, matches = None):
  if len(forms) == 1 and matches == None:
    return set(forms[0])

  if len(forms) == 0:
    return matches or set()

  if matches == None:
    return find_matching_answers(forms[1:], set(forms[0]) & set(forms[1]))
  
  return find_matching_answers(forms[1:], set(forms[0]) & matches)

print(functools.reduce(lambda count, matches: count + len(matches), map(find_matching_answers, groups), 0))
