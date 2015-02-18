undirectedKautzGraph = { 'a': set(['b','c','d']), 'b':set(['a','c','e']), 'c':set(['f','a','b']),
						 'd': set(['e','f','a']), 'e':set(['d','f','b']), 'f':set(['d','e','c'])
						}


class GraphSearch(object):
	'''
	This class provides a set of methods that can be used on Graphs.

	remark:  Our definition of a Graph is a dictionary whose keys are the vertices of the graphs and associated values are sets of vertices.  
	Any two vertices, 'i' and 'j', are said to be adjacent if and only if 'i' is contained in the associated set of 'j' and 'j' is contained in the associated set of 'i'.
	e.g. {'i':set(['j']),'j':set(['i'])}
	'''
	@staticmethod
	def DepthFirstSearchIterative(graph, start):
		'''
		This performs depth first search iteratively.
		
		Input:
		graph ->   a dictionary of vertices and corresponding set of adjacent vertices
		start -> a vertex in graph.

		return -> a set of vertices that were traversed.

		Assumptions, the returned set of traversed vertices is the set of vertices within the graph should the graph be connected
		'''
		if start not in graph:
			raise Exception("vertex is not in graph")
		visitedVertices = set()
		stack = [start]
		while stack:
			vertex = stack.pop()
			if vertex not in visitedVertices:
				visitedVertices.add(vertex)
				unvisted = graph[vertex] - visitedVertices
				stack.extend(unvisted)
		return visitedVertices
	@staticmethod
	def DepthFirstSearchRecursive(graph, start, visitedVertices=None):
		'''
		This performs depth first search recursively.
		
		Input:
		graph ->   a dictionary of vertices and corresponding set of adjacent vertices
		start -> a vertex in graph.

		return -> a set of vertices that were traversed.

		Assumptions, the returned set of traversed vertices is the set of vertices within the graph should the graph be connected
		'''
		if start not in graph:
			raise Exception("vertex is not in graph")
		if visitedVertices is None:
			visitedVertices = set()
		visitedVertices.add(start)
		for vertex in graph[start]:
			if vertex not in visitedVertices:
				GraphSearch.DepthFirstSearchRecursive(graph,vertex,visitedVertices)
		return visitedVertices
	@staticmethod
	def BFS(graph,start):
		'''
		This performs breadth first search iteratively.
		
		Input:
		graph ->   a dictionary of vertices and corresponding set of adjacent vertices
		start -> a vertex in graph.

		return -> a set of vertices that were traversed.

		Assumptions, the returned set of traversed vertices is the set of vertices within the graph should the graph be connected
		'''
		if start not in graph:
			raise Exception("vertex is not in graph")
		visitedVertices = set()
		queue = [start]
		while queue:
			vertex = queue.pop(0)
			if vertex not in visitedVertices:
				visitedVertices.add(vertex)
				unvistedVertices = graph[vertex] - visitedVertices
				queue.extend(unvistedVertices)
		return visitedVertices


if __name__ == "__main__":
	undirectedKautzGraph = { 'a': set(['b','c','d']), 'b':set(['a','c','e']), 'c':set(['f','a','b']), 'd': set(['e','f','a']), 'e':set(['d','f','b']), 'f':set(['d','e','c'])}#http://en.wikipedia.org/wiki/Kautz_graph
	print "DFS Iterative \n"
	print GraphSearch.DepthFirstSearchIterative(undirectedKautzGraph, 'a')
	print "DFS Recursive \n"
	print GraphSearch.DepthFirstSearchRecursive(undirectedKautzGraph, 'a')
	print "BFS Iterative \n"
	print GraphSearch.BFS(undirectedKautzGraph,'a')
