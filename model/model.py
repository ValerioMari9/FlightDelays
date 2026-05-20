from database.DAO import DAO
import networkx as nx

from model.airport import Airport


class Model:
    def __init__(self):
        self._airports=DAO.getAllAirports()
        self._idMapAirports: dict[int, Airport]={i.ID: i for i in self._airports}
        self._grafo: nx.Graph = nx.Graph()

    def buildGraph(self, n: int):
        self._grafo.clear()
        n=DAO.getAirportsbyAirlines(n)
        for i in n:
            self._grafo.add_node(self._idMapAirports[i])
        e=DAO.getFlights()
        for i in e:
            o=self._idMapAirports[i["orig"]]
            d=self._idMapAirports[i["dest"]]
            if self._grafo.has_node(o) and self._grafo.has_node(d):
                if self._grafo.has_edge(o,d):
                    self._grafo[o][d]["weight"]+=i["n"]
                else:
                    self._grafo.add_edge(o,d, weight=i["n"])
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges(), self._grafo.nodes

    def aeroportiConnessi(self, idA: int):
       #archi = list(G.edges(nodo))
        l=[]
        for i in list(self._grafo.edges(self._idMapAirports[idA], data=True)):
            l.append((i[1], i[2]['weight']))
        l.sort(key=lambda x: x[1], reverse=True)
        return l
