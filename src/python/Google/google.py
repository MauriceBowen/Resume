def toString(root, path=None):
    if path is None:
        string = ""
    else:
        string = path
    if root.left is not None:
        string = toString(root.left, path=string+root.left.value)#traverse left child
        if root.right is not None:
            string = toString(root.right, path=string+root.right.value)
    else:
        if root.right is not None:
                string = toString(root.right,path=string+root.value+root.right.value)
    return string


class Node:
    def __init__(self,val,l=None,r=None):
        self.left = l
        self.right = r
        self.value = val

F = Node('F')
D = Node('D',r=F)
B = Node('B',l=D)
E = Node('E')
C = Node('C',r=E)
A = Node('A',r=C,l=B)
print toString(A)