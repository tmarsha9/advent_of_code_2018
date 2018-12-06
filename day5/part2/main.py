#!/usr/bin/env python3

#only 1 line
line = None
with open("../input.txt", "r") as f:
  for thing in f:
    line = thing.strip()

reaction_diff = abs(ord('A') - ord('a'))
already_removed = []

#from part1
def compact_polymer(s):
  reacted = True
  while reacted:
    reacted = False
    i = 0
    while i < len(s)-1:
      if abs(ord(s[i]) - ord(s[i+1])) == reaction_diff:
        s = s[:i] + s[i+2:]
        reacted = True
      else:
        i += 1
  return len(s)

min_size = len(line) #init to length of whole line, no reacting
for char in line:
  if char not in already_removed: #don't try same char twice
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
      #char is lowercase
      char_complement = chr(ord(char)-ord('a')+ord('A'))
    else:
      #char is uppercase
      char_complement = chr(ord(char)-ord('A')+ord('a'))
    already_removed.append(char)
    already_removed.append(char_complement)
    min_size = min(min_size, compact_polymer(line.replace(char,"").replace(char_complement,"")))

print(min_size)
