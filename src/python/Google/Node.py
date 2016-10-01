class Node:
    '''
    This is a basic Node
    '''
    def __init__(self, data,children=None):
        self.data = data
        self.nextNodes = children

    def next(self):
        if self.nextNode is not None:
            return self.nextNode
        else:
            raise StopIteration

    def getData(self):
        return self.data

    def getNextNodes(self):
        return self.nextNodes

    def setData(self,datum):
        self.data = datum

    def setNextNodes(self,nextnode):
        self.nextNodes = nextnode