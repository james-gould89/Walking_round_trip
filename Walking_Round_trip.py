from Graph import Graph
from Vertex import Vertex
from heapq import heappop, heappush
from math import inf
from Locations_and_Distances import locations, values, connections
from operator import itemgetter
import random 

## build vertex graph based on graph module and vertex module and information stored in Locations_and_Distances
def build_graph():
  print("Building Graph!/n./n../n...")
  graph = Graph()
  for location in locations:
    vertex = Vertex(location)
    graph.add_vertex(vertex)

  for connection in connections:
    graph.add_edge(connection[0],connection[1],connection[2])

  ##for location in graph.graph_dict:
    ##print ("{} is connected to {}".format(location, graph.get_vertex(location).get_edges()))
  return graph

## build heap graph using a vertex for use with calculating return times 
def build_heap_graph(graph):
  heap_graph = {}
  for location in graph.graph_dict:
    heap_graph[location]=[]
    for edge in graph.get_vertex(location).get_edges():
      heap_graph[location].append(tuple((edge, graph.get_vertex(location).get_edge_weight(edge))))
  return heap_graph
  ##print(heap_graph)

## return_time function will add the return times to all vertex set up inside the heap graph based on the minimum return time from that vertex back to the "office" vertex
def return_time(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = inf
    
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))

  for location in vertex_graph.graph_dict:
    vertex_graph.get_vertex(location).set_return_time(distances[location])
    ##print("setting return time of {} to {}".format((location), distances[location]))
  ##print(distances)      
  ##print("\n\nreturn time from {} to {} is {} minutes".format(start, end, distances[end]))


vertex_graph = build_graph()
heap_graph = build_heap_graph(vertex_graph)
return_time(heap_graph, "office")

possible_journeys = []

def find_journey(time):
  min_time = time*0.8
  max_time = time*1.2
  journey_search(vertex_graph, min_time, max_time)
  print(possible_journeys)

def within_range(min, max, time):
  if min <= time <= max:
    return True
  else: 
    return False

def journey_search_bfs(graph, desired_time,  start_vertex = "office", target_value = "office"):
  min_time = desired_time*0.8
  max_time = desired_time*1.2
  path = [start_vertex]
  time_spent=0
  score=0
  vertex_path_and_time = [start_vertex, path,time_spent,score]
  #print("vertex_path_and_time:\n",vertex_path_and_time)
  bfs_queue = [vertex_path_and_time]
  #print("bfs_queue:\n",bfs_queue)
  #visited = {k:0 for k in locations}
  count_proccessed = 0
  count_too_long = 0
  count_visited_twice = 0
  count_found = 0
  while bfs_queue:
    current_vertex, path, time_spent, score = bfs_queue.pop(0)
    #print("path, bfs_queue:\n", path,".. ", bfs_queue)
    #visited[current_vertex]=+1
    #print("visited:\n",visited)
    for neighbor, edge_weight in graph[current_vertex]:
      count_proccessed += 1
      if path.count(neighbor) < 2: # and neighbor != target_value) or (path.count(neighbor) < 3 and neighbor == target_value):
        if time_spent + edge_weight + vertex_graph.get_vertex(neighbor).get_return_time() < max_time:
          if neighbor is target_value and within_range(min_time, max_time, time_spent):
            result_journey = str(path + [neighbor])
            possible_journeys.append([result_journey , time_spent + edge_weight , score])
            count_found +=1
            #print("Path found")
          else:
            if neighbor in path:
              bfs_queue.append([neighbor, path + [neighbor], time_spent + edge_weight, score])
            else:
              bfs_queue.append([neighbor, path + [neighbor], time_spent + edge_weight, score+values[neighbor]])
        else: 
          #print("Spent too long {}".format(neighbor))
          count_too_long += 1
      else: 
        #print("visited {} twice allready".format(neighbor))
        count_visited_twice += 1
  random.shuffle(possible_journeys)
  possible_journeys.sort(key=lambda x: x[2])
  for journey in possible_journeys[-3:]:
    print(journey)
  print("proccessed {}/nSpent too long {}/n visited twice {}/n found {}".format(count_proccessed, count_too_long, count_visited_twice, count_found))
  print("Done")

def journey_search(v_graph, min_time, max_time, vertex = "office", path = [], time_spent = 0, destination = "office"):
  path.append(vertex)
  print("Exploring {}".format(path)) ##check
  print("time Spent {}".format(time_spent))
  if vertex == destination and within_range(min_time, max_time, time_spent):
    possible_journeys.appends([path, time_spent])
    print("Path found")
  else:
    if path.count(vertex)>=3:
      print("Visited {} 3 times".format(vertex))
    else:
      potentials = v_graph.get_vertex(vertex).get_edges()
      for potential in potentials:
        print("potential = {}".format(potential))
        if time_spent + v_graph.get_vertex(vertex).get_edge_weight(potential) + v_graph.get_vertex(potential).get_return_time() > max_time:
          print("Gone to far")
        else:
          journey_search(v_graph, min_time, max_time, potential, path, time_spent+v_graph.get_vertex(vertex).get_edge_weight(potential), destination)

#find_journey(10)

journey_search_bfs(heap_graph, 27)
#print(vertex_graph.get_vertex('Fairlands Valley park').get_return_time())



  
  


