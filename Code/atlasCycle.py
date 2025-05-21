from sys import maxsize
import heapq
from graph import Graph

class AtlasCycle:
    
    def _dijkstra(self, graph: Graph, source: int, target: int):
        """Return (shortest_distance, [edge_label, ...]) from source → target
        using current edge weights (binary‑heap implementation)."""
        dist = {v: maxsize for v in graph.getNodes().keys()}
        prev_edge = {}                     
        dist[source] = 0
        pq = [(0, source)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue                   
            if u == target:
                break                      
            for e_lbl in graph.edgeLabels(u):
                edge = graph.getEdge(e_lbl)
                v   = edge.destination
                w   = edge.weightForDi
                new_d = d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    prev_edge[v] = e_lbl
                    heapq.heappush(pq, (new_d, v))
        if source != target and target not in prev_edge:
            raise ValueError("No path from %d to %d" % (source, target))
        
        edge_path = []
        v = target
        while v != source:
            e_lbl = prev_edge[v]
            edge_path.append(e_lbl)
            v = graph.getEdge(e_lbl).source
        edge_path.reverse()
        return dist[target], edge_path

    def topological_sort(self, graph: Graph, edge, visited, stack):
        visited[edge.getLabel()] = True
        for neighborEdgeLabel in graph.edgeLabels(edge.destination):
            if not visited[neighborEdgeLabel]:
                self.topological_sort(graph, graph.getEdge(neighborEdgeLabel), visited, stack)
        stack.append(edge)

    def longestPath(self, graph: Graph):
        totalCost = 0
        path      = []                       
        path.append(next(iter(graph.getStarts())))

        while len(graph.getReqEdges()) != 0:
            start = path.pop()               
            stack = []
            currentPathLong = -1
            n = len(graph.getEdges())
            pathLong = [0] * n
            cost     = [0] * n
            comeFrom = [-maxsize - 1] * n
            contained = [False] * n
            visited   = [False] * n
            current   = -1

            self.topological_sort(graph, graph.getEdge(start), visited, stack)

            for edge_lbl in graph.getEdgeLabels():
                cost[edge_lbl]     = maxsize
                pathLong[edge_lbl] = -maxsize - 1
            pathLong[start] = 0
            cost[start]     = 0

            while stack:
                edge = stack.pop()
                contained[edge.getLabel()] = True
                for neighborEdgeLabel in graph.edgeLabels(edge.destination):
                    if not contained[neighborEdgeLabel]:
                        newPathLong = pathLong[edge.getLabel()] + graph.getEdge(neighborEdgeLabel).getValue()
                        newCost     = cost[edge.getLabel()]     + graph.getEdge(neighborEdgeLabel).weight
                        if (pathLong[neighborEdgeLabel] < newPathLong or
                                (pathLong[neighborEdgeLabel] == newPathLong and newCost < cost[neighborEdgeLabel])):
                            pathLong[neighborEdgeLabel] = newPathLong
                            comeFrom[neighborEdgeLabel] = edge.getLabel()
                            cost[neighborEdgeLabel]     = newCost
                            if currentPathLong < pathLong[neighborEdgeLabel]:
                                currentPathLong = pathLong[neighborEdgeLabel]
                                current = neighborEdgeLabel
            insert_pos = len(path)
            path.append(current)                       
            totalCost += graph.getEdge(current).weight
            graph.getEdge(current).weight = 0          
            graph.getReqEdges().remove(current)
            while comeFrom[current] >= 0:              
                current = comeFrom[current]
                path.insert(insert_pos, current)
                totalCost += graph.getEdge(current).weight
                graph.getEdge(current).weight = 0
                graph.getReqEdges().discard(current)

        if path:                                       
            last_edge_lbl = path[-1]
            last_vertex   = graph.getEdge(last_edge_lbl).destination
            depot_vertex  = 1
            if last_vertex != depot_vertex:
                
                extra_cost, extra_edge_path = self._dijkstra(graph, last_vertex, depot_vertex)
                path.extend(extra_edge_path)           
                totalCost += extra_cost

        return path, totalCost


    def printPath(self, graph: Graph, path):
        for edge in path:
            print(str(graph.getEdge(edge).source) + "_" + str(graph.getEdge(edge).destination) + " , ", end="")
        print()

    def run(self, graph: Graph):
        return self.longestPath(graph)



















































# from sys import maxsize
# import heapq
# from graph import Graph

# class AtlasCycle:
#     # binary‑heap Dijkstra ----------
#     def _dijkstra(self, graph: Graph, source: int, target: int):
#         """Return (shortest_distance, [edge_label, ...]) from source → target
#         using current edge weights (binary‑heap implementation)."""
#         dist = {v: maxsize for v in graph.getNodes().keys()}
#         prev_edge = {}                      # key = vertex, value = incoming edge label
#         dist[source] = 0
#         pq = [(0, source)]
#         while pq:
#             d, u = heapq.heappop(pq)
#             if d != dist[u]:
#                 continue                    # stale entry
#             if u == target:
#                 break                       # early exit
#             for e_lbl in graph.edgeLabels(u):
#                 edge = graph.getEdge(e_lbl)
#                 v   = edge.destination
#                 w   = edge.weightForDi
#                 new_d = d + w
#                 if new_d < dist[v]:
#                     dist[v] = new_d
#                     prev_edge[v] = e_lbl
#                     heapq.heappush(pq, (new_d, v))
#         if source != target and target not in prev_edge:
#             raise ValueError("No path from %d to %d" % (source, target))
#         # ---------- reconstruct edge‑label path ----------
#         edge_path = []
#         v = target
#         while v != source:
#             e_lbl = prev_edge[v]
#             edge_path.append(e_lbl)
#             v = graph.getEdge(e_lbl).source
#         edge_path.reverse()
#         return dist[target], edge_path

#     # ---------- longest‑path sweep heuristic ----------
#     def topological_sort(self, graph: Graph, edge, visited, stack):
#         visited[edge.getLabel()] = True
#         for neighborEdgeLabel in graph.edgeLabels(edge.destination):
#             if not visited[neighborEdgeLabel]:
#                 self.topological_sort(graph, graph.getEdge(neighborEdgeLabel), visited, stack)
#         stack.append(edge)

#     def longestPath(self, graph: Graph):
#         totalCost = 0
#         path      = []                       # list of edge labels in traversal order
#         # --- start at the first depot edge (source vertex is assumed to be 1) ---
#         path.append(next(iter(graph.getStarts())))

#         # -------- main sweep loop --------
#         while len(graph.getReqEdges()) != 0:
#             start = path.pop()               # last edge label becomes new sweep start
#             stack = []
#             currentPathLong = -1
#             n = len(graph.getEdges())
#             pathLong = [0] * n
#             cost     = [0] * n
#             comeFrom = [-maxsize - 1] * n
#             contained = [False] * n
#             visited   = [False] * n
#             current   = -1

#             self.topological_sort(graph, graph.getEdge(start), visited, stack)

#             for edge_lbl in graph.getEdgeLabels():
#                 cost[edge_lbl]     = maxsize
#                 pathLong[edge_lbl] = -maxsize - 1
#             pathLong[start] = 0
#             cost[start]     = 0

#             while stack:
#                 edge = stack.pop()
#                 contained[edge.getLabel()] = True
#                 for neighborEdgeLabel in graph.edgeLabels(edge.destination):
#                     if not contained[neighborEdgeLabel]:
#                         newPathLong = pathLong[edge.getLabel()] + graph.getEdge(neighborEdgeLabel).getValue()
#                         newCost     = cost[edge.getLabel()]     + graph.getEdge(neighborEdgeLabel).weight
#                         if (pathLong[neighborEdgeLabel] < newPathLong or
#                                 (pathLong[neighborEdgeLabel] == newPathLong and newCost < cost[neighborEdgeLabel])):
#                             pathLong[neighborEdgeLabel] = newPathLong
#                             comeFrom[neighborEdgeLabel] = edge.getLabel()
#                             cost[neighborEdgeLabel]     = newCost
#                             if currentPathLong < pathLong[neighborEdgeLabel]:
#                                 currentPathLong = pathLong[neighborEdgeLabel]
#                                 current = neighborEdgeLabel
#             insert_pos = len(path)
#             path.append(current)                       # forward sweep edges
#             totalCost += graph.getEdge(current).weight
#             graph.getEdge(current).weight = 0          # mark as served
#             graph.getReqEdges().remove(current)
#             while comeFrom[current] >= 0:              # backtrack through predecessor edges
#                 current = comeFrom[current]
#                 path.insert(insert_pos, current)
#                 totalCost += graph.getEdge(current).weight
#                 graph.getEdge(current).weight = 0
#                 graph.getReqEdges().discard(current)

#         # --------- NEW: close the walk back to vertex 1 ---------
#         if path:                                       # safeguard: non‑empty route
#             last_edge_lbl = path[-1]
#             last_vertex   = graph.getEdge(last_edge_lbl).destination
#             depot_vertex  = 1
#             if last_vertex != depot_vertex:
#                 # print("Getting the shortest path to the Route to perform a cycle")
#                 extra_cost, extra_edge_path = self._dijkstra(graph, last_vertex, depot_vertex)
#                 path.extend(extra_edge_path)           # dead‑heading segment (travel only)
#                 totalCost += extra_cost

#         return path, totalCost


#     def printPath(self, graph: Graph, path):
#         for edge in path:
#             print(str(graph.getEdge(edge).source) + "_" + str(graph.getEdge(edge).destination) + " , ", end="")
#         print()

#     def run(self, graph: Graph):
#         return self.longestPath(graph)
