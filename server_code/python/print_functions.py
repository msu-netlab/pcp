def print_graph(g):
    print "Graph: "
    print "  Vertices("+str(len(g.vertices()))+"): "
    for v in g.vertices():
        print "    "+v
    print "  Edges("+str(len(g.edges()))+"): "
    for e in g.edges():
        print "    "+str(e) + " : " + str(g.edge(e))

def print_path(start, dest, graph, path):
	print "Path from start to end nodes: "
	v1 = path.pop()
	v2 = path.pop()
	print v1 + " --("+str(graph.edge(frozenset([v1, v2])))+")-> ", 
	while len(path) != 0:
	    v1 = v2
	    v2 = path.pop()
	    print v1 + " --("+str(graph.edge(frozenset([v1, v2])))+")-> ", 
	print dest    

def get_path(start, dest, prev):
    path = [dest]
    v = prev[dest]
    path.append(v)
    while v != start:
        v = prev[v]
        path.append(v)
    return path