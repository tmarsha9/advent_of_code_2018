#!/usr/bin/env python3

import sys

events = {} #maps time -> event to be processed
nodes = {} #maps node id -> {refcount:int, prereq:list of nodeids}

NUM_WORKERS = 5
active_workers = 0

def get_node(id):
  try:
    return nodes[id]
  except KeyError:
    node = {"incident_refs":0, "prereq_to":[], "id":id, "in_queue":False}
    nodes[id] = node
    return node

with open("../input.txt", "r") as f:

  #build graph
  for line in f:
    line = line.split()
    
    node1 = get_node(line[1])
    node2 = get_node(line[7])
    
    #line says node1 -> node2
    #add node 2 to node1's prereq list
    node1["prereq_to"].append(node2["id"])
    #increment node2 incident ref count
    node2["incident_refs"] += 1

  #immediately start work on all tasks with no prereqs
  current_time = 0
  events[current_time] = []
  first_nodes = [node for node in nodes if nodes[node]["incident_refs"] == 0]
  for nodeId in first_nodes:
    events[0].append(("start", nodeId))
    #print(0,("start", nodeId))
    nodes[nodeId]["in_queue"] = True

  while len(events) > 0: #while something to do

    #find next time step something actually occurs at
    current_time = sorted(events.items())[0][0]
    
    #process finished events first so workers can immediately start new ones
    i = 0
    while i < len(events[current_time]): 
      event = events[current_time][i]

      if event[0] == "finish":
        active_workers-=1 #free up worker

        #remove dependency from other nodes
        for other_node in nodes[event[1]]["prereq_to"]:
          nodes[other_node]["incident_refs"] -= 1
        
        #mark node as complete
        del events[current_time][i]
      else:
        i+=1

    #get updated list of nodes which have no dependencies
    ready_nodes = [node for node in nodes if nodes[node]["incident_refs"] == 0]

    #add those to list of available start jobs
    for nodeId in ready_nodes:
      if not nodes[nodeId]["in_queue"]: #don't add nodes that already have an event created for them
        events[current_time].append(("start", nodeId))
        #print(current_time,("start", nodeId))
        nodes[nodeId]["in_queue"] = True
    
    #start as many jobs as possible
    start_events = [e for e in sorted(events[current_time], key=lambda k: k[1]) if e[0] == "start"]
    
    i = 0
    while i < len(start_events):
      if active_workers < NUM_WORKERS:
        event = start_events[i]

        #starting a job simply means creating the finish event at the time the job would be over
        time_to_complete = ord(event[1]) - ord('A') + 61 #+1 because that is time when worker is actually free and not still working on job
        #time_to_complete = ord(event[1]) - ord('A') + 1
        try:
          events[current_time+time_to_complete].append(("finish",event[1]))
          #print(current_time+time_to_complete,(("finish",event[1])))
        except KeyError as e:
          events[current_time+time_to_complete] = []
          events[current_time+time_to_complete].append(("finish",event[1]))
          #print(current_time+time_to_complete,(("finish",event[1])))
        active_workers+=1
        i+=1
      else:
        break
    
    #move any events that couldn't be processed to next time step
    while i < len(start_events):
      event = start_events[i]
      #print("moved event", event)
      try:
        events[current_time+1].append(event)
      except KeyError as e:
        events[current_time+1] = []
        events[current_time+1].append(event)
      i+=1

    del events[current_time]

  # end while len(events) > 0

  print(current_time) 
