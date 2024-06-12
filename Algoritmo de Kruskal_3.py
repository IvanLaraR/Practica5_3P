# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:46:16 2024

@author: IvanL
"""
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class GrafoKruskal2:
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
        for peso, desde, hacia in self.aristas:
            G.add_edge(desde, hacia, weight=peso)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title('Grafo Original')
        plt.show()

        mst_G = nx.Graph()
        mst_G.add_edges_from([(u, v, {'weight': w}) for u, v, w in mst])
        plt.figure(figsize=(10, 7))
        nx.draw(mst_G, pos, with_labels=True, node_color='lightgreen', node_size=700, edge_color='red', width=2)
        edge_labels_mst = {(u, v): f'{d["weight"]}' for u, v, d in mst_G.edges(data=True)}
        nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=edge_labels_mst, font_color='red')
        plt.title('Árbol de Expansión Mínima')
        plt.show()

# Ejemplo de uso
grafo = GrafoKruskal2()
grafo.agregar_vertice('Servidor1')
grafo.agregar_vertice('Servidor2')
grafo.agregar_vertice('Servidor3')
grafo.agregar_vertice('Servidor4')
grafo.agregar_vertice('Servidor5')

grafo.agregar_arista('Servidor1', 'Servidor2', 1)
grafo.agregar_arista('Servidor1', 'Servidor3', 3)
grafo.agregar_arista('Servidor2', 'Servidor3', 1)
grafo.agregar_arista('Servidor2', 'Servidor4', 6)
grafo.agregar_arista('Servidor3', 'Servidor4', 4)
grafo.agregar_arista('Servidor3', 'Servidor5', 2)
grafo.agregar_arista('Servidor4', 'Servidor5', 5)

mst = grafo.kruskal()
print("Árbol de Expansión Mínima:", mst)

grafo.graficar_mst(mst)
