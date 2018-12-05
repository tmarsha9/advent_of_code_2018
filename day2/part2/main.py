#!/usr/bin/env python3

import sys

def get_difference(line1,line2):
  assert len(line1) == len(line2)

  count = 0
  pos = None
  for i,char in enumerate(line1):
    if char != line2[i]:
      if count:
        return 2, None #we only care if they have 1 difference. Exit as soon as we know this pair won't work
      else:
        count = 1
        pos = i
  return count, pos

lines = []
with open("../input.txt", "r") as f:
  for line in f:
    lines.append(line.strip())
#looking for 1 char difference, so they will be close lexicographically
lines = sorted(lines)

for i,line in enumerate(lines):
  num_diff, pos = get_difference(lines[i],lines[i+1])
  if num_diff == 1:
    #this is the string pair, get common chars
    #all chars are same except for where 1 char differs
    #print(''.join(sorted(set(lines[i][:pos] + lines[i][pos+1:]))))
    print(lines[i][:pos] + lines[i][pos+1:])
    sys.exit(0)
