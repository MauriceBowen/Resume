class Node(object):
    def CheckType(self, input):
        if type(input) is type(Node) or next is None:
            return True
        else:
            raise Exception("next must be None or a Node")

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.SetNext(nextNode)

    def GetNext(self):
        return self.nextNode

    def SetNext(self, input):
        if self.CheckType(input):
            self.nextNode = input

    def GetData(self):
        return self.data

    def SetData(self, d):
        self.data = d
