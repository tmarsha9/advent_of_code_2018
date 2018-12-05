#!/usr/bin/env python3

def count(line):
  checked  = set()
  two_rv   = False
  three_rv = False

  for i,char in enumerate(line):
    if char not in checked:
      checked.add(char)
      count = 1
      for j,char2 in enumerate(line[i+1:]):
        if char == char2:
          count += 1
      if count == 2:
        two_rv = True
      elif count == 3:
        three_rv = True

  return two_rv, three_rv

twice = 0
thrice = 0
with open("../input.txt", "r") as f:
  for line in f:
    is_twice, is_thrice = count(line)
    twice  = twice+1 if is_twice else twice
    thrice = thrice+1 if is_thrice else thrice

print(twice*thrice)
