
class Edge:
    def __init__(self, label: int, source: int, destination: int, weight: int, req: bool, weightForDi: int):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.label = label
        self.req = req
        self.weightForDi = weightForDi

    def getValue(self) -> int:
        return 1 if self.req and self.weight > 0 else 0

    def getLabel(self) -> int:
        return self.label
