class Vertex:
    def __init__(self,weight = 0, adjacents=None):
        self.weight = weight
        self.adjacentNoddes = None
        if adjacents is None:
            self.adjacentNodes = {}
        else:
            self.adjacentNodes = adjacents
    def