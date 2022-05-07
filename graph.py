class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_direct={}
        for start, end in self.edges:
            if start in self.graph_direct:
                self.graph_direct[start].append(end)
            else:
                self.graph_direct[start]=[end]
        print(f"Graph Dict: {self.graph_direct}")

    def getPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_direct:
            return []

        paths = []
        for node in self.graph_direct[start]:
            if node not in path:
                newPaths = self.getPaths(start=node, end=end, path=path)
                for p in newPaths:
                    paths.append(p)

        return paths

    # def getShortestPath(self, start, end, path=[]):
    #     path = path + [start]

    #     if start == end:
    #         return path

    #     if start not in self.graph_direct:
    #         return None

    #     shortestPath = None
    #     for node in self.graph_direct[start]:
    #         if node not in path:
    #             sp = self.getShortestPath(start=node, end=end, path=path)
    #             if sp:
    #                 if shortestPath is None or len(sp) < len(shortestPath):
    #                     shortestPath = sp

    #     return shortestPath

    def getShortestPath(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_direct:
            return []
       
        paths=[]
        for index,node in enumerate(self.graph_direct[start]):
            if node not in path:
                newPath=self.getShortestPath(start=node,end=end,path=path)
                if newPath:
                    lengthOfNewPath=len(newPath[0])
                else:
                    lengthOfNewPath=0

                if not paths:
                    minLengthinPaths=0
                else:
                    minLengthinPaths=len(paths[0])

                if minLengthinPaths and lengthOfNewPath:
                    if lengthOfNewPath<minLengthinPaths:
                        paths=[]
                        for p in newPath:
                            paths.append(p)
                else:
                    for p in newPath:
                        paths.append(p)
        return paths            


if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris",),
        ("Mumbai", "Dubai",),
        ("Paris", "Dubai",),
        ("Paris", "New York",),
        ("Dubai", "New York",),
        ("Dubai", "Yumthang",),
        ("New York", "Toronto",),
        ("New York", "Yumthang")
    ]

    route_graph = Graph(edges=routes)

    print(route_graph.getPaths(start="Paris", end="Yumthang"))