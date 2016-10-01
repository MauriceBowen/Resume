class GraphMethods:
    @staticmethod
    def DepthFirstSearch(dictionary, root, query):
        S = []
        S.append((root,False))
        while len(S) > 0:
            v = S.pop()
            if v[1] is False:
                v[1] = True
                for v[0].getNextNodes()
