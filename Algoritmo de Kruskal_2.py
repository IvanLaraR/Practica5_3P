# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:46:16 2024

@author: IvanL
"""
import matplotlib.pyplot as plt
import networkx as nx

class GrafoKruskal1:
    def __init__(self):
        self.vertices = set()
        self.aristas = []

    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)

    def agregar_arista(self, desde, hacia, peso):
        self.aristas.append((peso, desde, hacia))

    def kruskal(self):
        mst = []
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            root1 = find(v1)
            root2 = find(v2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        self.aristas.sort()
        for peso, desde, hacia in self.aristas:
            if find(desde) != find(hacia):
                union(desde, hacia)
                mst.append((desde, hacia, peso))

        return mst

    def graficar_mst(self, mst):
        G = nx.Graph()
        G.add_edges_from([(u, v, {'weight': w}) for u, v, w in mst])

        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, edge_color='green', width=2)
        edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
        plt.title('Árbol de Expansión Mínima')
        plt.show()

# Ejemplo de uso
grafo = GrafoKruskal1()
grafo.agregar_vertice('Localidad1')
grafo.agregar_vertice('Localidad2')
grafo.agregar_vertice('Localidad3')
grafo.agregar_vertice('Localidad4')
grafo.agregar_vertice('Localidad5')

grafo.agregar_arista('Localidad1', 'Localidad2', 1)
grafo.agregar_arista('Localidad1', 'Localidad3', 4)
grafo.agregar_arista('Localidad2', 'Localidad3', 2)
grafo.agregar_arista('Localidad2', 'Localidad4', 5)
grafo.agregar_arista('Localidad3', 'Localidad4', 1)
grafo.agregar_arista('Localidad4', 'Localidad5', 3)

mst = grafo.kruskal()
print("Árbol de Expansión Mínima:", mst)

grafo.graficar_mst(mst)
