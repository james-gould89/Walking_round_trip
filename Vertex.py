class Vertex:
  def __init__(self, name):
    self.name = name
    self.edges = {}
    self.return_time=0

  def add_edge(self, vertex, weight=0):
    self.edges[vertex] = weight

  def get_interest(self):
    return self.interest

  def get_edges(self):
    return list(self.edges.keys())

  def get_edge_weight(self, edge): 
    return self.edges[edge]
  
  def set_return_time(self, return_time):
    self.return_time = return_time

  def get_return_time(self):
    return self.return_time
  
  def get_return_time(self):
    return self.return_time
