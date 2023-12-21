import random
import math

def generador_matriz_10x10():
    matriz = []
    
    for num in range(0, 10):
        fila_de_ceros = []
        for num in range(0, 10):
            fila_de_ceros.append(0)
        matriz.append(fila_de_ceros)
    
    return matriz

def generador_matriz_minas():
    matriz_minas = generador_matriz_10x10()

    for num in range(0, 10):
        random_num = random.randint(0, 99)
        fila_mina = math.trunc(random_num / 10)
        columna_mina = random_num - fila_mina * 10
    
        while matriz_minas[fila_mina][columna_mina] == 9:
            random_num = random.randint(0, 99)
            fila_mina = math.trunc(random_num / 10)
            columna_mina = random_num - fila_mina * 10
            
        matriz_minas[fila_mina][columna_mina] = 9
    
    return matriz_minas

def imprimir_matriz(matriz:list):
    for fila in matriz:
        print(fila)