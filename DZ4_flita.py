import networkx as nx
import numpy as np
import matplotlib.pyplot as plt



def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix

def sort_vertices_by_degree(matrix):
    degrees = [sum(row) for row in matrix]
    sorted_vertices = sorted(range(len(degrees)), key=lambda x: degrees[x], reverse=True)
    sorted_matrix = [matrix[vertex] for vertex in sorted_vertices]
    return sorted_matrix, sorted_vertices

input_file = 'matrix.txt'

# Чтение матрицы смежности
matrix = read_matrix(input_file)

# Сортировка вершин по убыванию степени
sorted_matrix, sorted_vertices = sort_vertices_by_degree(matrix)

# Построение графа с использованием предоставленного кода
G = nx.from_numpy_array(np.array(sorted_matrix) - np.eye(len(sorted_matrix)), create_using=nx.Graph)

pos = nx.spring_layout(G)
nx.draw(G, pos)
labels = {i: i for i in sorted_vertices}
nx.draw_networkx_labels(G, pos, labels)

plt.show()
