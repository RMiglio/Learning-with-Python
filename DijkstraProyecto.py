# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:34:54 2022

@author: Rmiglio
"""

import math

#establecer grafo y recibir los vertices como arg de entrada
def Graph(vertices):
    #matriz para el grafo
    matriz = [[math.inf for columna in range(vertices)] for fila in range(vertices)]
    return matriz

#Imprimir matriz o algo dijsktra
def PrintGraph(matriz):
    print(matriz)
    
#Conectar los routers con sus pesos respectivos
def ConectRouters(matriz):
    v_Inicial = int(input("Inicio: "))
    v_Final = int(input("Final: "))
    peso = int(input("Peso: "))    
    matriz[v_Inicial] [v_Final] = peso
    matriz[v_Final] [v_Inicial] = peso
    return matriz

#Menor distancia entre los bordes del grafo
def main():
    vertices = int(input("N°Routers: "))
    matriz = Graph(vertices)
    Arcos = int(input("N°conexiones: "))
    for i in range(Arcos):
        matriz = ConectRouters(matriz)
    dest = int(input("To Destiny: "))
    print("\n")
    PrintGraph(matriz)
    print("\n")
    l = dijkstra(matriz, vertices, dest)
main()
def MenorDist(longs, vertices, vex):
    minVal = math.inf
    for i in range(vertices):
        if longs[i]< minVal and vex[i] == False:
             minVal = longs[i]
             minVal2 = i
    return  minVal2

def dijkstra(matriz, vertices, dest):    
    vex = []
    longs = []

    for i in range(vertices):
        vex.append(False)
        longs.append(math.inf)        
    longs[dest] = 0
    
    for i in range(vertices):
        x = MenorDist(longs, vertices, vex)
        vex[x] = True
        for j in range(vertices):
            if matriz[x][j] > 0 and vex[j] == False:
                if longs[j] > longs[x] + matriz[x][j]:
                    longs[j] = longs[x] + matriz[x][j]
                    
    print("From Source: ")
    for i in range(vertices):
        print("Desde r",i, ":", longs[i])
    return 0

