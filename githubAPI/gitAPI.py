class DirectedGraph(object):

    def __init__(self):
        self.graph_dict = {}
        self.checked = []

    def addEdge(self, nodeA, nodeB):
        if nodeA in self.graph_dict and nodeB in self.graph_dict:
            self.graph_dict[nodeA].append(nodeB)
        elif not nodeA in self.graph_dict and nodeB in self.graph_dict:
            self.graph_dict[nodeA] = [nodeB]
        elif nodeA in self.graph_dict and not nodeB in self.graph_dict:
            self.graph_dict[nodeA].append(nodeB)
            self.graph_dict[nodeB] = []
        elif not nodeA in self.graph_dict and not nodeB in self.graph_dict:
            self.graph_dict[nodeA] = [nodeB]
            self.graph_dict[nodeB] = []

    def getNeighborsFor(self, node):
        return self.graph_dict[node]

    def pathBetween(self, nodeA, nodeB):
        if nodeB in self.graph_dict[nodeA]:
            return True
        else:
            self.checked.append(nodeA)
            for pointedByPrevios in self.graph_dict[nodeA]:
                if not pointedByPrevios in self.checked:
                    if self.pathBetween(pointedByPrevios, nodeB):
                        return True
        return False

    def toString(self):
        #for key in self.graph_dict:
            #print(key + ": "),(self.graph_dict[key])
        return self.graph_dict


graph = DirectedGraph()
graph.addEdge("Ivan", "Dragan")
graph.addEdge("Pesho", "Marto")
graph.addEdge("Pesho", "Dragan")
graph.addEdge("Sasho", "Dragan")
graph.addEdge("Dragan", "Ivan")
#print(graph.getNeighborsFor("Ivan"))
print(graph.pathBetween("Pesho", "Ivan"))
print(graph.pathBetween("Dragan", "Pesho"))
print(graph.toString())
