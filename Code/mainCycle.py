import sys, os

sys.setrecursionlimit(10_000)

from atlasCycle import AtlasCycle
from util import Util


class Main:
    @staticmethod
    def main(args):
        util = Util()
        folder_path = "test_instances/DRPP_Instances_Campos"
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            graph = util.toGraphCampos(file_path)
            atlas = AtlasCycle()
            testSuite, totalCost = atlas.run(graph)
            # print(f"{totalCost}")
            # print("atlas: ", len(testSuite))
            t_c=0
            for i in range(len(testSuite)):
                # print(f"{graph.getEdge(testSuite[i]).source}-{graph.getEdge(testSuite[i]).destination}", end="|")
                t_c += graph.getEdge(testSuite[i]).weightForDi
            print(f"{t_c}")
            # break
        


if __name__ == '__main__':
    Main.main(sys.argv)


