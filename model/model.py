import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.DiGraph()
        self._grado_vertici = {}
        self._n_componenticonnesse = 0

    def build_graph(self, anno_max):
        self._grafo.clear()
        #self._grafo.add_nodes_from(DAO.get_all_countries())
        for e in DAO.get_confini(anno_max):
            if e.conntype == 1:
                self._grafo.add_edge(e.country1, e.country2)
            else:
                self._grafo.add_node(e.country1)
                self._grafo.add_node(e.country2)
                self._grado_vertici[e.country1] = 0
                self._grado_vertici[e.country2] = 0
        self.grado_vertici()
        self.componenti_connesse()


    def grado_vertici(self):
        for v in self._grafo.edges.keys():
            if v[0] not in self._grado_vertici.keys() or self._grado_vertici[v[0]] == 0:
                self._grado_vertici[v[0]] = 1
            else:
                self._grado_vertici[v[0]] += 1
            if v[1] not in self._grado_vertici.keys() or self._grado_vertici[v[1]] == 0:
                self._grado_vertici[v[1]] = 1
            else:
                self._grado_vertici[v[1]] += 1

    def componenti_connesse(self):
        temp_grafo = self._grafo.copy()
        n_componenti = 0
        for n in self._grafo.nodes:
            if n in temp_grafo:
                n_componenti += 1
                temp_grafo.remove_nodes_from(self.getDFSNodes(n))
                temp_grafo.remove_node(n)
        self._n_componenticonnesse = n_componenti


    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    @property
    def get_nodes(self):
        return self._grafo.nodes

    def get_edges(self):
        return self._grafo.edges

    def get_grado_vertici(self):
        return self._grado_vertici

    def get_n_componenticonnesse(self):
        return self._n_componenticonnesse

