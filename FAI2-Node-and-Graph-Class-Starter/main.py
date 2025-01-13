#Node Class 
class Node:

  def __init__(self, key):
    self.key = key
    self.neighbors = []

  def add_neighbor(self, node):
    self.neighbors.append(node)
    
  def __str__(self):
    s = "ID: " + self.key + "\nNeighbors: "
    for n in self.neighbors:
      s += n.key + "  "
    return s





# Define a Graph class that represents an undirected, unweighted Graph containing nodes and edges using the following steps

#DEFINE CLASS HERE


  
  #Write an __init__() method for the Graph class. The class should only have one instance attribute called graph (a dictionary mapping the keys to nodes in the graph to the Node object) and it should be set to a default value.


  
  #Write an instance method called add_node() that takes in a Node object and adds it to the Graph.
  

  
  #Write an instance method called add_edge() that takes in two Node objects that should have an edge between them and adds each Node as a neighbor of the other (if both nodes are in the Graph).


  
  #Write a __str__() method that prints out each Node in the graph.



#Make an instance of the Graph class. Create 4 Nodes and add them to your Graph. Add some edges in between the Nodes in the Graph. Print out the entire Graph.