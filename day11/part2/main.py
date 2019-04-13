#!/usr/bin/env python3

GRID_SERIAL_NUMBER = 3031 # puzzle input

grid = [[0] * 300 for i in range(300)]
sum_grid = [[0] * 300 for i in range(300)] # used to compute submatrix sums

for row in range(len(grid)):
  for col in range(len(grid[row])):
    rack_id = (col+1)+10 # +1 because 0-indexed
    power = rack_id * (row+1) + GRID_SERIAL_NUMBER
    power *= rack_id
    power = (power//100) % 10
    power -= 5
    grid[row][col] = power

# compute first row
total = 0
for col in range(len(sum_grid[0])):
  total += grid[0][col]
  sum_grid[0][col] = total

#compute first col
total = 0
for row in range(len(sum_grid)):
  total += grid[row][0]
  sum_grid[row][0] = total

#compute rest of sum grid
for row in range(1,len(sum_grid)):
  for col in range(1,len(sum_grid[row])):
    sum_grid[row][col] = sum_grid[row][col-1] + sum_grid[row-1][col] - sum_grid[row-1][col-1] + grid[row][col]


def find_block_value(sum_grid, row, col, size):
  top_left_row = row
  top_left_col = col
  bottom_right_row = row+size-1
  bottom_right_col = col+size-1

  total = sum_grid[bottom_right_row][bottom_right_col]

  if top_left_row > 0:
    total -= sum_grid[top_left_row-1][bottom_right_col]

  if top_left_col > 0:
    total -= sum_grid[bottom_right_row][top_left_col-1]

  if top_left_row > 0 and top_left_col>0:
    total += sum_grid[top_left_row-1][top_left_col-1]

  return total

max_power = find_block_value(sum_grid,0,0,1)
max_coord = (1,1)
max_size = 1

for size in range(1,301):
  for row in range(300-size+1):
    for col in range(300-size+1):
      block_value = find_block_value(sum_grid,row,col,size)
      if block_value > max_power:
        max_power = block_value
        max_coord = (col+1,row+1)
        max_size = size

print('{},{},{}'.format(max_coord[0],max_coord[1],max_size))
