#!/usr/bin/env python3

num = 0
with open("../input.txt", "r") as f:
  for line in f:
    exec("num = num " + line)
  print(num)
