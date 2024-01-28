

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, vertex):
    self.graph_dict[vertex.name] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    self.graph_dict[from_vertex].add_edge(to_vertex, weight)
    self.graph_dict[to_vertex].add_edge(from_vertex, weight)

  def get_vertex(self,name):
    return self.graph_dict[name]

  def get_interest(self,name):
    return self.graph_dict[name].interest

  def get_edges(self, name):
    return list(self.graph_dict[name].edges.keys())

  def get_edge_weight(self, name, edge): 
    return self.graph_dict[name].edges[edge]
  
  def get_return_time(self, name):
    return self.graph_dict[name].return_time

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False
