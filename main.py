from utils import *
from kruskal import *

city_name = 'nice'

nodes_file = 'instances/' + city_name + '/nodes.csv'
distances_file = 'instances/' + city_name + '/distances.csv'

full_tab, n, n_distr, n_term = read_nodes_csv2(nodes_file)
distances_matrix = read_distances_csv(distances_file, n)

# Kruskal
g = Graph(n)
for i in range(n):
    for j in range(n):
        if i != j:
            g.addEdge(i, j, distances_matrix[i][j])

kruk_tree = g.KruskalMST()

#Euler

