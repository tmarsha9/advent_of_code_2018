#!/usr/bin/env python3

rules = {} # pattern -> next generation output

with open('../input.txt', 'r') as f:
  pots = f.readline().split(':')[1].strip()
  f.readline() # skip blank

  for line in f:
    line = [item.strip() for item in line.split('=>')]
    rules[line[0]] = line[1]

first_pot_index = 0
for generation in range(20):

  # pad front in case there are not at least two empty pots in front
  while pots[0] != '.' or pots[1] != '.' or pots[2] != '.': # only need to pad three because all rules go at most 2 to the left
    pots = '.' + pots
    first_pot_index += 1

  while pots[-1] != '.' or pots[-2] != '.' or pots[-3] != '.':
    pots = pots + '.'

  #print("generation: {}".format(generation))
  #print(pots)

  new_pots = [pot for pot in pots] # for easier changing of values

  # attempt to pattern match
  for i in range(len(pots)-5+1):
  # attempt to match rules at this position
    for rule in rules:
      if rule == pots[i:i+5]:
        #print("{} matches at index {}".format(rule,i))
        # rule matches, so pot at position i + 2 will change next generation
        new_pots[i+2] = rules[rule]
        break # two rules can't apply

  # update pots
  pots = ''.join(new_pots)

print("generation: {}\nfirst_pot: {}".format(20,first_pot_index))
print(pots)

total = 0
for i,char in enumerate(pots):
  if char == '#':
    total += (i-first_pot_index)
print(total)
