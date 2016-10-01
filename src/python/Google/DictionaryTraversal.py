graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def path_search(graph, start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newPath = path_search(graph,node, end, path)
            if newPath:
                return newPath
    return None

def paths(graph, start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newPaths = paths(graph,start,end, path=[])
            for p in newPaths:
                path.append(p)


def search(graph,start,end):
    if start not in graph:
        return None
    

print path_search(graph,"A","D")
print "A" in graph