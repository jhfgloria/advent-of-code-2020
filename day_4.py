import requests
import functools
import re

puzzle = requests.get("https://adventofcode.com/2020/day/4/input", cookies={
                      "session": "53616c7465645f5f8ac95906a4c2e8b5418363f7c1cea6b3b565fbc839a5c4e7a81757e7f2af0bd6f943554e78caf024"})

input = puzzle.text.replace(" ", "\n").splitlines()

def create_credential(credential):
  regex = r'([a-z]*):(.*)'
  tuple = re.findall(regex, credential)
  return (tuple[0][0], tuple[0][1])

def create_passport(credentials):
  return list(map(create_credential, credentials))

def parse_credentials(batch):
  passports = []
  credentials = []

  for i in range(len(batch) + 1):
    if i == len(batch) or not batch[i]:
      passports.append(create_passport(credentials))
      credentials = []
    else:
      credentials.append(batch[i])

  return passports

def is_valid_password_one(passport, mandatory_fields):
  keys = list(zip(*passport))[0]
  return functools.reduce(lambda is_valid, field: (field in keys) and is_valid, mandatory_fields, True)

def is_valid_password_two(passport):
  if not is_valid_password_one(passport, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
    return False

  for key, value in passport:
    if key == "byr" and (int(value) < 1920 or int(value) > 2002):
      return False
    if key == "iyr" and (int(value) < 2010 or int(value) > 2020):
      return False
    if key == "eyr" and (int(value) < 2020 or int(value) > 2030):
      return False
    if key == "hgt":
      regex = r'^(\d*)(cm|in)$'
      if not re.match(regex, value):
        return False
      tuple = re.findall(regex, value)
      if tuple[0][1] == 'in' and (int(tuple[0][0]) < 59 or int(tuple[0][0]) > 76):
        return False
      if tuple[0][1] == 'cm' and (int(tuple[0][0]) < 150 or int(tuple[0][0]) > 193):
        return False
    if key == "hcl":
      regex = r'^(#){1}([a-f]*[0-9]*){6}$'
      if not re.match(regex, value):
        return False
    if key == "ecl":
      regex = r'^(amb|blu|brn|gry|grn|hzl|oth)$'
      if not re.match(regex, value):
        return False
    if key == "pid":
      regex = r'^([0-9]{9})$'
      if not re.match(regex, value):
        return False

  return True
      
passports = parse_credentials(input)

# Exercise 1
print(list(map(lambda passport: is_valid_password_one(passport, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]), passports)).count(True))

# Exercise 2
print(list(map(is_valid_password_two, passports)).count(True))
