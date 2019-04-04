#!/usr/bin/env python3

data = []

def get_size(index):
  rv = 2 #header always at least 2

  for i in range(data[index]): #include size of all my children
    rv += get_size(index+rv)

  rv += data[index+1] #include size of metadata

  return rv

def get_immediate_children(index):
  rv = []

  child_count = data[index]


  offset = 2
  while child_count > 0:
    rv.append(index+offset)
    offset += get_size(index+offset)
    child_count -= 1

  return rv

def get_metadata(index):
  #number of metadata entries
  num = data[index+1]

  if data[index] > 0:
    #metadata is just after last child
    last_child = get_immediate_children(index)[-1]
    last_child_size = get_size(last_child)
    metadata_start = last_child+last_child_size
  else:
    metadata_start = index+2

  return data[metadata_start:metadata_start+num]

def sum_metadata(index):
  total = 0
  
  for child in get_immediate_children(index):
    total += sum_metadata(child)

  for metadata in get_metadata(index):
    total += metadata

  return total


with open("../input.txt", "r") as f:
  for line in f:
   data += [int(thing) for thing in line.split() ]

print(sum_metadata(0)) #print sum of metadata for root node
