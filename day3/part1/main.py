#!/usr/bin/env python3

import sys

fabric = [['.'] * 1000 for i in range(1000)]

def mark_area(pos, size):
  for col in range(size[0]):
    for row in range(size[1]):
      if fabric[pos[0]+col][pos[1]+row] != '.':
        fabric[pos[0]+col][pos[1]+row] = 'X' #multiple claims
      else:
        fabric[pos[0]+col][pos[1]+row] = '1' #1 claim
      

with open("../input.txt", "r") as f:
  for line in f:
    line = line.strip().split()
    pos  = [int(thing) for thing in line[2][:-1].split(',')]
    size = [int(thing) for thing in line[3].split('x')]
    mark_area(pos,size)

count = 0
for line in fabric:
  for char in line:
    if char == 'X':
      count += 1
print(count)
