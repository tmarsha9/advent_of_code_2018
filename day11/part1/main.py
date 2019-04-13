#!/usr/bin/env python3

GRID_SERIAL_NUMBER = 3031

def get_power(col, row):
  rack_id = (col+1)+10 # +1 because 0-indexed
  power = rack_id * (row+1) + GRID_SERIAL_NUMBER
  power *= rack_id
  power = (power//100) % 10
  power -= 5
  return power

def find_block_value(row, col):
  total = 0
  for i in range(row,row+3):
    for j in range(col,col+3):
      total += get_power(j,i)
  return total

max_power = find_block_value(0,0)
max_coord = (1,1)

for row in range(300-2):
  for col in range(300-2):
    block_value = find_block_value(row,col)
    if block_value > max_power:
      max_power = block_value
      max_coord = (col+1,row+1)

print('{},{}'.format(max_coord[0],max_coord[1]))
