#!/usr/bin/env python
import cPickle as pickle, graph, sys
try:
  new_ip = sys.argv[1] 
  new_cdn = sys.argv[2]
  rtt = sys.argv[3]

  with open("python/edges.pickle", "rb") as input_file:
    e = pickle.load(input_file)
  with open("python/vertices.pickle", "rb") as input_file:
    v = pickle.load(input_file)

  g = graph.UndirectedGraph()
  g.newEdges(e)
  g.newVertices(v)

  #g.print_graph()
  g.addVertex(new_ip)
  g.addVertex(new_cdn)
  g.addEdge(new_ip, new_cdn, rtt)

  with open("python/edges.pickle", "wb") as output_file:
    pickle.dump(g.saveEdges(), output_file)
  with open("python/vertices.pickle", "wb") as output_file:
    pickle.dump(g.saveVertices(), output_file)
  print "Finished updating graph"
except Exception, e:
  print "ERROR IN PYTHON: "+str(e)


