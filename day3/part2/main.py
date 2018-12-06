#!/usr/bin/env python3

import sys

fabric = [['.'] * 1000 for i in range(1000)]

past_areas = {}

def mark_new_area(pos, size, id):
  has_overlap = False

  for col in range(size[0]):
    for row in range(size[1]):
      if fabric[pos[0]+col][pos[1]+row] != '.':
        has_overlap = True
        if fabric[pos[0]+col][pos[1]+row] != 'X':
          #invalidate other claim
          mark_area_as_overlap(fabric[pos[0]+col][pos[1]+row])
      else:
        fabric[pos[0]+col][pos[1]+row] = id
  past_areas[id] = (pos, size)
  if has_overlap:
    mark_area_as_overlap(id)

def mark_area_as_overlap(id):
  pos, size = past_areas[id]
  for col in range(size[0]):
    for row in range(size[1]):
      fabric[pos[0]+col][pos[1]+row] = 'X'
      

with open("../input.txt", "r") as f:
  for line in f:
    line = line.strip().split()
    id = int(line[0][1:])
    pos  = [int(thing) for thing in line[2][:-1].split(',')]
    size = [int(thing) for thing in line[3].split('x')]
    mark_new_area(pos,size,id)

for col in range(len(fabric)):
  for row in range(len(fabric[col])):
    if fabric[row][col] != '.' and fabric[row][col] != 'X':
      print(fabric[row][col])
      sys.exit(0)
