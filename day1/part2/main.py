#!/usr/bin/env python3

import sys

num = 0
past = set()
lines = []

def process_line(line):
  exec("num = num " + line,globals())
  if num in past:
    print(num)
    sys.exit(0)
  else:
    past.add(num)


with open("../input.txt", "r") as f:
  #read lines from file
  for line in f:
    #save each line as it is read for first time
    lines.append(line)
    #also process it
    process_line(line)

#continually process lines until freq is reached 2nd time
while True:
  for line in lines:
    process_line(line)
