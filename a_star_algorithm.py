# To create the oft-used algorithm you:
#
# Modified Dijkstra’s algorithm to include a path and target.
# Added the Manhattan heuristic to use for estimating distance on a grid.
# Changed the Manhattan heuristic to the Euclidean heuristic to estimate distances between cities.
#
# Manhattan Heuristic : x_distance + y_distance
#
# Euclidean Heuristic : sqrt(x_distance * x_distance + y_distance * y_distance)

from math import inf
from heapq import heappop, heappush

def a_star(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + heuristic(neighbor, target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]


def heuristic(start, target):
	x_distance = abs(start.position[0] - target.position[0])
	y_distance = abs(start.position[1] - target.position[1])
	return sqrt(x_distance * x_distance + y_distance * y_distance)