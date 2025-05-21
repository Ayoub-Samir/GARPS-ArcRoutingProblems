import re
from graph import Graph


class Util:
    def toGraphCampos(self, fileName: str) -> Graph:
        graph = Graph()
        with open(fileName, 'r') as br:
            label = 0
            for line in br:
                # Compile the regular expression as defined in Java:
                # Pattern regex = Pattern.compile("^\\s+(\\d*),\\s+(\\d*),\\s*(\\d*)\\s+,(\\d*)");
                regex = re.compile(r"\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*")
                regexMatcher = regex.finditer(line)
                for match in regexMatcher:
                    state_ = int(match.group(1))
                    nextState_ = int(match.group(2))
                    weight = int(match.group(3))
                    req = (match.group(4) == "1")
                    graph.addEdge(label, state_, nextState_, weight, req)
                    if req:
                        graph.addReqEdge(label)
                    if state_ == 1:
                        graph.addStart(label)
                    label += 1
        return graph

    def toGraph(self, fileName: str) -> Graph:
        graph = Graph()
        with open(fileName, 'r') as br:
            req = True
            label = 0
            for line in br:
                if line.strip() == "LIST OF NO REQUIRED ARCS:":
                    req = False
                # Compile the regular expression as defined in Java:
                # Pattern regex = Pattern.compile("\\((\\d*),(\\d*)\\)\\scoste\\s(\\d*)");
                regex = re.compile(r"\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*")
                regexMatcher = regex.finditer(line)
                for match in regexMatcher:
                    state_ = int(match.group(1))
                    nextState_ = int(match.group(2))
                    weight = int(match.group(3))
                    graph.addEdge(label, state_, nextState_, weight, req)
                    if req:
                        graph.addReqEdge(label)
                    if state_ == 1:
                        graph.addStart(label)
                    label += 1
        return graph
