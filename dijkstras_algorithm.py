# Understanding Heapq
# Remember that Dijkstra’s Algorithm works like the following:

# Instantiate a dictionary that will eventually map vertices to their distance from their start vertex
# Assign the start vertex a distance of 0 in a min heap
# Assign every other vertex a distance of infinity in a min heap
# Remove the vertex with the smallest distance from the min heap and set that to the current vertex
# For the current vertex, consider all of it’s adjacent vertices and calculate the distance to them by 
# (distance to the current vertex) + (edge weight of current vertex to adjacent vertex). If this new distance
# is less than its current distance, replace the distance.
# 
# Repeat 4 and 5 until the heap is empty
# After the heap is empty, return the distances
####################################################################################################################
# In order to keep track of all the distances for Dijkstra’s Algorithm, we will be using a heap! Using a heap 
# will allow removing the minimum from the heap to be efficient. In python, there is a library called heapq 
# which we will use to do all of our dirty work for us!
#
# The heapq method has two critical methods we will use in Dijkstra’s Algorithm: heappush and heappop.
#
# heappush will add a value to the heap and adjust the heap accordingly
# heappop will remove and return the smallest value from the heap
####################################################################################################################
# Define the function with a start vertex and a graph.
# 
# Instantiate a distances dictionary that will eventually map vertices to their distance from their start vertex.
# Assign the start vertex a distance of 0.
# Assign every other vertex a distance of infinity.
# Set up a vertices_to_explore min-heap list that keeps track of neighboring vertices left to explore.
#
# First, we’ll traverse the vertices_to_explore heap until it is empty, popping off the vertex 
# with the minimum distance from start. Inside our while loop, we’ll iterate over the neighboring 
# vertices of current_vertex and add each neighbor (and its distance from start) to the vertices_to_explore min-heap.
#
# In each neighbor iteration, we will do the following:
#
# Identify neighbor‘s distance from start.
# Make sure the new distance found for neighbor is less than the distance currently set for distances[neighbor].
# Update distances[neighbor] if the new distance is smaller than the currently recorded distance.
# Add neighbor and its distance to the vertices_to_explore min-heap.
####################################################################################################################
# Pseudo Code:
#
# create dictionary to map vertices to their distance from start vertex
#
# assign start vertex a distance of 0 in min heap
#
# assign every other vertex a distance of infinity in min heap
#
# remove the vertex with the minimum distance from the min heap and set it to the current vertex
#
# while min heap is not empty:
#   for each current vertex:
#     for each neighbor in neighbors:
#     new distance = (distance to current vertex) + (edge weight of current vertex to neighbor)
#
#     if new distance is less than its current distance:
#       current distance = new distance
#
# return distances
###################################################################################################################

from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
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
        
  return distances
        
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
