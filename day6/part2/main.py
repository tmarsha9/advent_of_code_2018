#!/usr/bin/env python3

#does

min_x = None
max_x = None

min_y = None
max_y = None

def get_dist(p1, p2):
  """manhattan distance"""
  return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def add_to_grid(grid, point):
  while len(grid) <= point[0]:
    grid.append(grid[0][:])

  while len(grid[0]) <= point[1]:
    for row in grid:
      row.append('.')

  grid[point[0]][point[2]] = point[2]

with open("../input.txt", "r") as f:
  points = []
  grid = [['.']]
  id = 0

  for thing in f:
    line = thing.strip().split(', ')

    point = (int(line[1]), int(line[0]), id) #points are (row, col, id)
    id += 1

    if min_y is None or point[0] < min_y:
      min_y = point[0]
    if max_y is None or point[0] > max_y:
      max_y = point[0]

    if min_x is None or point[1] < min_x:
      min_x = point[1]
    if max_x is None or point[1] > max_x:
      max_x = point[1]

    add_to_grid(grid, point)
    points.append(point)

  region_size = 0
  for row in range(min_y,max_y+1):
    for col in range(min_x,max_x+1):
      distance = 0
      for point in points:
        distance += get_dist((row,col),point)
      if distance < 10000:
        region_size += 1

  print(region_size)
