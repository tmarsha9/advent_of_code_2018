#!/usr/bin/env python3

#only 1 line
lines = []
with open("../input.txt", "r") as f:
  for line in f:
    lines.append(line.strip())

reaction_diff = abs(ord('A') - ord('a'))
reacted = True
while reacted:
  reacted = False
  for i in range(len(lines[0])-1):
    if abs(ord(lines[0][i]) - ord(lines[0][i+1])) == reaction_diff:
      lines[0] = lines[0][:i] + lines[0][i+2:]
      reacted = True
      break #line changed, just start again
print(len(lines[0]))
