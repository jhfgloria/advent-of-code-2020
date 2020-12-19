import requests
import math

puzzle = requests.get("https://adventofcode.com/2020/day/5/input", cookies={
                      "session": "53616c7465645f5f8ac95906a4c2e8b5418363f7c1cea6b3b565fbc839a5c4e7a81757e7f2af0bd6f943554e78caf024"})

boarding_passes = puzzle.text.splitlines()


def calculate_position(min, max, rest):
    if len(rest) == 0:
        return max
    if rest[0] == "F" or rest[0] == "L":
        return calculate_position(min, math.floor(min + (max-min) / 2), rest[1:])
    if rest[0] == "B" or rest[0] == "R":
        return calculate_position(math.ceil(max - (max-min) / 2), max, rest[1:])


def calculate_row_and_column(start_row, end_row, boarding_pass):
    return {
        "row": calculate_position(start_row, end_row, boarding_pass[0:7]),
        "column": calculate_position(0, 7, boarding_pass[7:10])
    }


def find_seat_ids_gap(ids):
    if ids[1] - ids[0] == 2:
        return ids[0] + 1
    else:
        return find_seat_ids_gap(ids[1:])


# Exercise 1
seats_one = map(lambda boarding_pass: calculate_row_and_column(
    0, 127, boarding_pass), boarding_passes)
seat_ids_one = map(lambda seat: seat["row"] * 8 + seat["column"], seats_one)
print(max(seat_ids_one))

# Exercise 2
seats_two = map(lambda boarding_pass: calculate_row_and_column(
    1, 126, boarding_pass), boarding_passes)
seat_ids_two = map(lambda seat: seat["row"] * 8 + seat["column"], seats_two)
print(find_seat_ids_gap(sorted(seat_ids_two)))
