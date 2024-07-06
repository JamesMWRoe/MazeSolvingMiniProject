class Graph:
    '''This class represents a graph data structure. This graph contains nodes, and methods for accessing
       and modifying these nodes.'''
    def __init__(self, V):
        self.numberOfVertices = V
        self.numberOfEdges = 0
        self.nodeList = []

        for i in range(V):
            self.nodeList.append(Node(i))

    def getOrder(self):
        '''returns the number of vertices in the graph as an integer'''
        return self.numberOfVertices

    def getSize(self):
        '''returns the number of edges in a graph as an integer'''
        return self.numberOfEdges

    def addEdge(self, v, w):
        '''Takes integer values v and w which correspond to indexes of nodes within the graph and adds 
        an edge between these vertices. Note that multiple edges between the same two vertices can be made'''

        nodeV = self.nodeList[v]
        nodeW = self.nodeList[w]

        nodeV.addAdjacentNode(nodeW)
        nodeW.addAdjacentNode(nodeV)
        
        self.numberOfEdges += 1

    def getNode(self, nodeIndex):
        '''Returns the node object with index nodeIndex.'''
        return self.nodeList[nodeIndex]

    def getNodeAdjacencyList(self, node):
        '''returns the adjacency list of the node "node"'''
        return node.getAdjacencyList()
    
    def getNodeAdjacencyListAsIndexes(self, nodeIndex):
        '''returns the indexes of the nodes connected to the node with index nodeIndex'''
        node = self.nodeList[nodeIndex]
        indexList = []
        for adjacentNode in node.getAdjacencyList():
            indexList.append(adjacentNode.getIndex())
        
        return indexList
    
    def setNodeCoordinates(self, nodeIndex, coordinates):
        '''Sets the coordinates of the node with index nodeIndex to coordinates. 
           coordinates should be given as 2 integers packed in a tuple'''
        node = self.getNode(nodeIndex)
        node.setCoordinates(coordinates)
    
    def getNodeCoordinates(self, nodeName):
        '''returns a 2-tuple of integers that are coordinates corresponding to the node with index nodeIndex'''
        node = self.getNode(nodeName)
        return node.getCoordinates()


class Node:
    def __init__(self, i):
        self.adjacencyList = []
        self.index = i
        self.coordinates = ()

    def getIndex(self):
        '''returns the integer index, which acts as the name of the node.'''
        return self.index

    def getAdjacencyList(self):
        '''returns the adjacency list of this node, which is a list of all the nodes connected to this node
           by an edge'''
        return self.adjacencyList

    def getCoordinates(self):
        '''returns a 2 tuple of integers which correspond to this node's coordinates.'''
        return self.coordinates

    def addAdjacentNode(self, otherNode):
        '''This method should only be used by the graph daa structure to create edges between
           nodes. Adds a node to this node's adjacency list.'''
        self.adjacencyList.append(otherNode)
    
    def setCoordinates(self, coordinates):
        '''This method should only be used by the graph data structure to set the coordinates
        of the node. Sets this node's coordinates to the value coordinates'''
        self.coordinates = coordinates

if __name__ == '__main__':
    testGraph = Graph(5)
    testGraph.addEdge(0, 3)
    testGraph.addEdge(0, 1)
    testGraph.addEdge(1, 4)
    testGraph.addEdge(2, 3)
    testGraph.addEdge(0, 4)

    adjacencyListByIndex = []
    for node in testGraph.getNodeAdjacencyList(testGraph.getNode(0)):
        nodeIndex = node.getIndex()
        adjacencyListByIndex.append(nodeIndex)
    
    print(adjacencyListByIndex)
    
    adjacencyListByIndex = []

    for node in testGraph.getNodeAdjacencyList(testGraph.getNode(1)):
        nodeIndex = node.getIndex()
        adjacencyListByIndex.append(nodeIndex)

    print(adjacencyListByIndex)