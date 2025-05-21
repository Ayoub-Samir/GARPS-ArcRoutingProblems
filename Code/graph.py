from typing import Dict, Set

from edge import Edge


class Graph:
    def __init__(self):
        self.nodes: Dict[int, Set[int]] = {}
        self.edges: Dict[int, Edge] = {}
        self.starts: Set[int] = set()
        self.req: Set[int] = set()

    def addVertex(self, s: int):
        self.nodes[s] = set()

    def addEdge(self, label: int, source: int, destination: int, weight: int, req: bool):
        if source not in self.nodes:
            self.addVertex(source)
        if destination not in self.nodes:
            self.addVertex(destination)
        edge = Edge(label, source, destination, weight, req, weight)
        self.nodes[source].add(label)
        self.edges[label] = edge

    def getEdge(self, label: int) -> Edge:
        return self.edges.get(label)

    def getEdgeLabels(self) -> Set[int]:
        return set(self.edges.keys())

    def edgeLabels(self, node: int) -> Set[int]:
        return self.nodes.get(node, set())

    def getStarts(self) -> Set[int]:
        return self.starts

    def addStart(self, root: int):
        self.starts.add(root)

    def addReqEdge(self, root: int):
        self.req.add(root)

    def getReqEdges(self) -> Set[int]:
        return self.req

    def getNodes(self) -> Dict[int, Set[int]]:
        return self.nodes

    def getEdges(self) -> Dict[int, Edge]:
        return self.edges
