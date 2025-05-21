import re
from graph import Graph
# =====================================================================================
# ========================== for DRPP_Instances_Campos ================================
# =====================================================================================
class Util:
    def toGraphCampos(self, fileName: str) -> Graph:
        graph = Graph()
        with open(fileName, 'r') as br:
            label = 0
            for line in br:
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

# ===================================================================================
# ========================= for MCPP_Instances_Corberan =============================
# ===================================================================================
# class Util:
#     # def toGraphCampos(self, fileName: str) -> Graph:
#     #     graph = Graph()
#     #     with open(fileName, 'r') as br:
#     #         label = 0
#     #         for line in br:
#     #             regex = re.compile(r"^\s+(\d+),\s+(\d+),\s*(\d+)\s+,\s*(\d+)")
#     #             regexMatcher = regex.finditer(line)
#     #             for match in regexMatcher:
#     #                 state_ = int(match.group(1))
#     #                 nextState_ = int(match.group(2))
#     #                 weight = int(match.group(3))
#     #                 req = True
#     #                 graph.addEdge(label, state_, nextState_, weight, req)
#     #                 graph.addReqEdge(label)
#     #                 if state_ == 1:
#     #                     graph.addStart(label)
#     #                 label += 1
#     #     return graph


#     def toGraph(self, fileName: str) -> Graph:
#         graph = Graph()
#         x=0
#         with open(fileName, 'r') as br:
#             label = 0
#             for line in br:
#                 regex = re.compile(
#                     r"""
#                     ^\(\s*        
#                     (\d+)         
#                     \s*,\s*       
#                     (\d+)         
#                     \s*\)\s+      
#                     coste\s+      
#                     (\d+)         
#                     \s+           
#                     (\d+)        
#                     $           
#                     """,
#                     re.VERBOSE,
#                 )
#                 regexMatcher = regex.finditer(line)
#                 for match in regexMatcher:
#                     from_node = int(match.group(1))
#                     to_node = int(match.group(2))
#                     cost_forward = int(match.group(3))
#                     cost_backward = int(match.group(4))
                    
                 
#                     if cost_backward > 999999:
#                         graph.addEdge(label, from_node, to_node, cost_forward, req=True)
#                         graph.addReqEdge(label)
#                         if from_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x+=cost_forward

#                     elif cost_forward > 999999:
#                         graph.addEdge(label, to_node, from_node, cost_backward, req=True)
#                         graph.addReqEdge(label)
#                         if to_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x+=cost_backward
                        
#                     elif cost_backward == cost_forward and cost_backward < 999999:    
#                         graph.addEdge(label, from_node, to_node, cost_forward, req=True)
#                         graph.addReqEdge(label)
#                         if from_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         graph.addEdge(label, to_node, from_node, cost_backward, req=True)
#                         graph.addReqEdge(label)
#                         if to_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x+=cost_forward*2
            
#         return graph




# ===================================================================================
# ==================== for MCPP_Instances_YaoyuenyongInstances ======================
# ===================================================================================

# class Util:
#     # def toGraphCampos(self, fileName: str) -> Graph:
#     #     graph = Graph()
#     #     with open(fileName, 'r') as br:
#     #         label = 0
#     #         for line in br:
#     #             regex = re.compile(r"^\s+(\d+),\s+(\d+),\s*(\d+)\s+,\s*(\d+)")
#     #             regexMatcher = regex.finditer(line)
#     #             for match in regexMatcher:
#     #                 state_ = int(match.group(1))
#     #                 nextState_ = int(match.group(2))
#     #                 weight = int(match.group(3))
#     #                 req = True
#     #                 graph.addEdge(label, state_, nextState_, weight, req)
#     #                 graph.addReqEdge(label)
#     #                 if state_ == 1:
#     #                     graph.addStart(label)
#     #                 label += 1
#     #     return graph


#     def toGraph(self, fileName: str) -> Graph:
#         graph = Graph()
#         x=0
#         with open(fileName, 'r') as br:
#             label = 0
#             for line in br:
#                 regex = re.compile(r'^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*,\s*(\d)\s*,\s*(\d)\s*$')
#                 regexMatcher = regex.finditer(line)
#                 for match in regexMatcher:
#                     from_node = int(match.group(1))
#                     to_node = int(match.group(2))
#                     cost = int(match.group(3))
#                     one_way_flag = int(match.group(5))
                    
                    
#                     if one_way_flag == 1:
#                         graph.addEdge(label, from_node, to_node, cost, req=True)
#                         graph.addReqEdge(label)
#                         if from_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x+=cost
                        
#                     else:    
#                         graph.addEdge(label, from_node, to_node, cost, req=True)
#                         graph.addReqEdge(label)
#                         if from_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         graph.addEdge(label, to_node, from_node, cost, req=True)
#                         graph.addReqEdge(label)
#                         if to_node == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x+=cost
            
#         return graph






# ===================================================================================
# ========================== for WRPP_Instances_Corberan ============================
# ===================================================================================
# class Util:
#     def toGraph(self, fileName: str) -> Graph:
#         graph = Graph()
#         x=0
#         with open(fileName, 'r') as br:
#             label = 0
#             required = True
#             for line in br:
            
#                 line = line.strip()
#                 if line.startswith("LISTA_ARISTAS_NOREQ"):
#                     required = False
#                     continue
#                 regex = re.compile(r'^\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)\s+coste\s+(\d+)\s+(\d+)\s*$')
#                 match = regex.match(line)
                
#                 if match:
#                     u = int(match.group(1))
#                     v = int(match.group(2))
#                     cost_uv = int(match.group(3))
#                     cost_vu = int(match.group(4))
#                     if cost_uv < 999999:
#                         graph.addEdge(label, u, v, cost_uv, required)
#                         if required:
#                             graph.addReqEdge(label)
#                         if u == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x += cost_uv
#                     if cost_vu < 999999:
#                         graph.addEdge(label, v, u, cost_vu, required)
#                         if required:
#                             graph.addReqEdge(label)
#                         if v == 1:
#                             graph.addStart(label)
#                         label += 1
#                         x += cost_vu
#         return graph
            

