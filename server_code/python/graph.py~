import heapq
INF = 999999999.0
class UndirectedGraph(object):
    adjList = {}
    edgeList = {}
    
    def newEdges(self, edges):
      self.edgeList = edges
    def newVertices(self, vertices):
      self.adjList = vertices
    def addVertex(self, v):
        self.adjList.setdefault(v, set())
    def addEdge(self, v1, v2, value):
        self.addVertex(v1)
        self.adjList[v1].add(v2)
        self.addVertex(v2)
        self.adjList[v2].add(v1)
        edge = frozenset([v1, v2])
        if edge not in self.edgeList or self.edgeList[edge] > value:
            self.edgeList[frozenset([v1, v2])] = value
    def removeVertex(self, v):
        if v in self.adjList:
            for n in self.neighbors(v):
                self.removeEdge(v, n)
            del self.adjList[v]
    def removeEdge(self, v1, v2):
        self.adjList.get(v2, set()).discard(v1)
        self.adjList.get(v1, set()).discard(v2)
        self.edgeList.pop(frozenset([v1, v2]), None)
    def saveVertices(self):
      return self.adjList
    def saveEdges(self):
      return self.edgeList
    def vertices(self):
        return set(self.adjList.keys())
    def edges(self):
        return set(self.edgeList.keys())
    def neighbors(self, v):
        return self.adjList.get(v, None)
    def edge(self, v1, v2):
        return self.edge(frozenset([v1, v2]))
    def edge(self, edge):
        return self.edgeList.get(edge, None)
    def print_graph(self):
        print "Graph: "
        print "  Vertices("+str(len(self.vertices()))+"): "
        for v in self.vertices():
            print "    "+v
        print "  Edges("+str(len(self.edges()))+"): "
        for e in self.edges():
            print "    "+str(e) + " : " + str(self.edge(e))

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

def dijsktra(Graph, start):
    unvisited = []
    dist = {}
    prev = {}
    for v in Graph.vertices():
        if v != start:
            heapq.heappush(unvisited, [INF, v])
        else:
            heapq.heappush(unvisited, [0.0, v])
        prev[v] = ""
        dist[v] = INF
    dist[start] = 0.0

    while len(unvisited) != 0:
        u = heapq.heappop(unvisited)[1]
        for n in Graph.neighbors(u):
            curr_edge = frozenset([u, n])
            alt_dist = float(dist.get(u)) + float(Graph.edge(curr_edge))
            if alt_dist < dist[n]:
                dist[n] = alt_dist
                prev[n] = u
        new_heap = []
        for i in range(0, len(unvisited)):
            curr_v = unvisited[i][1]
            heapq.heappush(new_heap, [dist[curr_v], curr_v])
        unvisited = new_heap
    return [dist, prev]

