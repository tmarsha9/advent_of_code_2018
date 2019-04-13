#!/usr/bin/env python3

import sys

class Grid:
  class Point:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
      self.pos_x = pos_x
      self.pos_y = pos_y
      self.vel_x = vel_x
      self.vel_y = vel_y

  def __init__(self, points):
    self.points = {}

    for point in points:
      self.points['{},{}'.format(point[0][0], point[0][1])] = self.Point(point[0][0], point[0][1],point[1][0], point[1][1])

    self.boundaries = None
    self.set_boundaries()
    self.smallest_area = self.width*self.height

  def forward_tick(self):
    for pos, point in self.points.items():
      point.pos_x += point.vel_x
      point.pos_y += point.vel_y
    self.set_boundaries()

  def backward_tick(self):
    for pos, point in self.points.items():
      point.pos_x -= point.vel_x
      point.pos_y -= point.vel_y
    self.set_boundaries()

  def set_boundaries(self):
    init_point = self.points[next(iter(self.points))]
    min_x = init_point.pos_x
    max_x = init_point.pos_x
    min_y = init_point.pos_y
    max_y = init_point.pos_y
    for pos, point in self.points.items():
      if point.pos_x > max_x:
        max_x = point.pos_x
      elif point.pos_x < min_x:
        min_x = point.pos_x

      if point.pos_y > max_y:
        max_y = point.pos_y
      elif point.pos_y < min_y:
        min_y = point.pos_y

    self.boundaries = (min_x, min_y, max_x, max_y)
    self.width = max_x-min_x+1
    self.height = max_y-min_y+1

  def print_points(self):
    # create grid
    grid = [['.'] * self.width for i in range(self.height)]
    for pos, point in self.points.items():
      # translate each point by the smallest x and y value
      point.pos_x -= self.boundaries[0]
      point.pos_y -= self.boundaries[1]
      grid[point.pos_y][point.pos_x] = '#'

    # actually print it
    for row in range(len(grid)):
      for col in range(len(grid[row])):
        sys.stdout.write(grid[row][col])
      sys.stdout.write('\n')
    sys.stdout.write('\n')

  def find_message(self):
    while True:
      self.forward_tick()

      current_area = self.width * self.height
      if current_area < self.smallest_area:
        self.smallest_area = current_area
      elif current_area > self.smallest_area:
        # increase in area means that points are diverging. assume time to stop
        break
      # else do nothing if equal

    # current point in time is when area increased, so go back one
    self.backward_tick()
    self.print_points()

points = []
with open('../input.txt', 'r') as f:
  for line in f:
    line = line.split('>')
    pos_text = line[0].split('=')[1][1:].split(',')
    vel_text = line[1].split('=')[1][1:].split(',')

    points.append(((int(pos_text[0]),int(pos_text[1])),(int(vel_text[0]),int(vel_text[1]))))

Grid(points).find_message()
