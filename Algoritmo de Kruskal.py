# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:14:53 2024

@author: IvanL
"""
import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self):
        self.aristas = []

    def agregar_arista(self, desde, hacia, peso):
        self.aristas.append((peso, desde, hacia))

    def encontrar(self, padre, vertice):
        if padre[vertice] != vertice:
            padre[vertice] = self.encontrar(padre, padre[vertice])
        return padre[vertice]

    def unir(self, padre, rango, vertice1, vertice2):
        raiz1 = self.encontrar(padre, vertice1)
        raiz2 = self.encontrar(padre, vertice2)
        if rango[raiz1] < rango[raiz2]:
            padre[raiz1] = raiz2
        elif rango[raiz1] > rango[raiz2]:
            padre[raiz2] = raiz1
        else:
            padre[raiz2] = raiz1
            rango[raiz1] += 1

    def kruskal(self, maximo=False):
        self.aristas.sort(key=lambda item: item[0], reverse=maximo)
        padre, rango = {}, {}
        for peso, desde, hacia in self.aristas:
            padre[desde] = desde
            padre[hacia] = hacia
            rango[desde] = 0
            rango[hacia] = 0
        mst = []
        for peso, desde, hacia in self.aristas:
            raiz1 = self.encontrar(padre, desde)
            raiz2 = self.encontrar(padre, hacia)
            if raiz1 != raiz2:
                mst.append((peso, desde, hacia))
                self.unir(padre, rango, raiz1, raiz2)
        return mst

    def graficar_resultado(self, mst, titulo):
        G = nx.Graph()
        for peso, desde, hacia in self.aristas:
            G.add_edge(desde, hacia, weight=peso)
        
        pos = nx.spring_layout(G)

        # Dibujar el grafo original
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title('Grafo Original')
        plt.show()

        # Dibujar el MST o MaxST
        mst_G = nx.Graph()
        for peso, desde, hacia in mst:
            mst_G.add_edge(desde, hacia, weight=peso)
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, alpha=0.3)
        nx.draw(mst_G, pos, with_labels=True, node_color='lightgreen', node_size=700, edge_color='red')
        edge_labels = {(desde, hacia): f'{peso}' for peso, desde, hacia in mst}
        nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=edge_labels, font_color='red')
        plt.title(titulo)
        plt.show()

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 3)
grafo.agregar_arista('B', 'C', 1)
grafo.agregar_arista('B', 'D', 6)
grafo.agregar_arista('C', 'D', 4)
grafo.agregar_arista('C', 'E', 2)
grafo.agregar_arista('D', 'E', 5)

mst = grafo.kruskal()
print("Árbol de Expansión Mínima:", mst)
grafo.graficar_resultado(mst, "Árbol de Expansión Mínima")

maxst = grafo.kruskal(maximo=True)
print("Árbol de Expansión Máxima:", maxst)
grafo.graficar_resultado(maxst, "Árbol de Expansión Máxima")

