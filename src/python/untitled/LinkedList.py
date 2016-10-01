from Node import Node
class LinkedList(Node):
    def __init__(self, val):
        super.__init__(data=val,next=None)

    def appendToTail(self,val):
        end = LinkedList(data=val)
        node = self
        while node.GetNext() is not None:
            node = node.GetNext()
        node.nextNode = end
    @staticmethod
    def deleteNode(head, val):
        n = head
        if n.GetData() is val:
            return head.GetNext()
        while n.GetNext() is not None:
            if n.GetNext().GetData() is val:
                n.SetNext(n.GetNext().GetNext())
                return head
            n = n.GetNext()
        return head