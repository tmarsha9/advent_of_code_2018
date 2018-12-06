#!/usr/bin/env python3

#only 1 line
line = None
with open("../input.txt", "r") as f:
  for thing in f:
    line = thing.strip()

reaction_diff = abs(ord('A') - ord('a'))
reacted = True
while reacted:
  reacted = False
  i = 0
  while i < len(line)-1:
    if abs(ord(line[i]) - ord(line[i+1])) == reaction_diff:
      line = line[:i] + line[i+2:]
      reacted = True
    else:
      i += 1
print(len(line))
