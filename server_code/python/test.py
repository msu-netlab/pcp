import graph, cPickle as pickle, pprint, print_functions

def main():
	g = graph.UndirectedGraph()
	g.addVertex("1.1.1.1")
	g.addVertex("1.1.1.2")
	g.addVertex("1.1.2.3")
	g.addVertex("1.4.4.4")
	g.addVertex("0.0.0.0")
	g.addVertex("0.1.1.1")
	g.addVertex("0.0.1.1")
	g.addEdge("1.1.1.1", "1.1.1.2", 5)
	g.addEdge("1.1.1.1", "1.1.2.3", 7)
	g.addEdge("1.4.4.4", "1.1.1.1", 12)
	g.addEdge("1.4.4.4", "1.1.1.2", 2)
	g.addEdge("1.1.1.1", "0.0.0.0", 1)
	g.addEdge("0.0.0.0", "0.1.1.1", 1)
	g.addEdge("0.1.1.1", "0.0.1.1", 1)
	g.addEdge("0.0.1.1", "1.4.4.4", 1)

	# f = open("graph.pkl", "rb")
	# g = pickle.load(f)
	# f.close()

	g.print_graph()
	start = "1.1.1.1"
	dest = "1.4.4.4"
	res = graph.dijsktra(g, start)
	distances = res[0]
	print "DIST: "+str(distances[dest])
	paths = res[1]
	# print "Distances: "
	# print distances
	path = graph.get_path(start, dest, paths)
	graph.print_path(start, dest, g, path)
	# g.print_graph()

	f = open(r"graph.pickle", "wb")
	pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)
	f.close()

	stored_obj = open(r"graph.pickle", "rb")
	g2 = pickle.load(stored_obj)
	stored_obj.close()
	print "Printing g2 loaded from pickled file"
	g2.print_graph()


if __name__ == '__main__':main()
