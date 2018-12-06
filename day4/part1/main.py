#!/usr/bin/env python3

lines = []
with open("../input.txt", "r") as f:
  for line in f:
    line = line.strip()
    lines.append(line)
lines = sorted(lines) #chrono order

guard_asleep_time = {} #id -> dict minute -> time asleep at that minute

id = None
next_line = 0
while next_line < len(lines):
  line = lines[next_line].split()
  next_line += 1
  if line[2] == 'Guard':
    id = int(line[3][1:])
  elif line[2] == 'falls':
    #fall asleep start
    start = [int(thing) for thing in line[1][:-1].split(':')]
    if start[0] == 0:
      start[0] = 24
  else: #wakes
    end = [int(thing) for thing in line[1][:-1].split(':')]
    if end[0] == 0:
      end[0] = 24

    if id not in guard_asleep_time:
      guard_asleep_time[id] = {'total' : 0}

    while start[0] != end[0]: #while hours are not the same
      while start[1] < 60:
        if start[1] not in guard_asleep_time[id]:
          guard_asleep_time[id][start[1]] = 0
        guard_asleep_time[id][start[1]] += 1
        guard_asleep_time[id]['total'] += 1
        start[1] += 1
      #minutes now == 60
      start[1] = 0
      start[0] += 1
    
    while start[1] != end[1]: #while minutes are not same
      if start[1] not in guard_asleep_time[id]:
        guard_asleep_time[id][start[1]] = 0
      guard_asleep_time[id][start[1]] += 1
      guard_asleep_time[id]['total'] += 1
      start[1] += 1
        

#get id of guard asleep for longest
id = sorted(guard_asleep_time.items(), key=lambda kv: kv[1]['total'],reverse=True)[0][0]

#get minute guard was asleep for the longest
del guard_asleep_time[id]['total']
minute = sorted(guard_asleep_time[id].items(), key=lambda kv: kv[1],reverse=True)[0][0]

print(id*minute)
