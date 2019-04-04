#!/usr/bin/env python3

nodes = {} #maps node id -> {refcount:int, prereq:list of nodeids}

def get_node(id):
  try:
    return nodes[id]
  except KeyError:
    node = {"incident_refs":0, "prereq_to":[], "id":id}
    nodes[id] = node
    return node

with open("../input.txt", "r") as f:
  for line in f:
    line = line.split()
    
    node1 = get_node(line[1])
    node2 = get_node(line[7])
    
    #line says node1 -> node2
    #add node 2 to node1's prereq list
    node1["prereq_to"].append(node2["id"])
    #increment node2 incident ref count
    node2["incident_refs"] += 1

  output = ''
  while len(nodes) > 0:
    #sort by incident_refs, then by id
    next_node = sorted(nodes.items(), key=lambda k: (k[1]["incident_refs"], k[0]))[0][1]
    
    #do this step next
    output += next_node["id"]
    
    #update remaining steps
    for other_node in next_node["prereq_to"]:
      nodes[other_node]["incident_refs"] -= 1
    
    #decrease size so this loop may end
    del nodes[next_node["id"]]

  print(output)
