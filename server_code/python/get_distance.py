import graph, cPickle as pickle, sys

try:
  ip1 = str(sys.argv[1])
  ip2 = str(sys.argv[2])
  with open("python/edges.pickle", "rb") as input_file:
    e = pickle.load(input_file)
  with open("python/vertices.pickle", "rb") as input_file:
    v = pickle.load(input_file)

  g = graph.UndirectedGraph()
  g.newEdges(e)
  g.newVertices(v)
  res = graph.dijsktra(g, ip1)  

  dist_ret = res[0]
  dist = dist_ret.get(ip2)

  print ip1+" -> "+ip2+": "+str(dist)+"(s)"


except Exception, e:
  print "Python Error: "+str(e)


