from utils import *
from kruskal import *

city_name = 'nice'

nodes_file = 'instances/' + city_name + '/nodes.csv'
distances_file = 'instances/' + city_name + '/distances.csv'

full_tab, n, n_distr, n_term = read_nodes_csv2(nodes_file)
distances_matrix = read_distances_csv(distances_file, n)

#On sépare le graphe en n_distr parties
term_full_tab = full_tab[n_distr+1:]
distr_full_tab = full_tab[0:n_distr]
term_tab_sep = separate(distr_full_tab, term_full_tab, distances_matrix)


# # Kruskal
# g = Graph(n)
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             g.addEdge(i, j, distances_matrix[i][j])
#
# krusk_tree = g.KruskalMST()
#
# #Euler
# g2 = Graph2(n)
# for e in krusk_tree:
#     g2.addEdge(e[0], e[1])
#     g2.addEdge(e[1], e[0])
#
# g2.printEulerTour()
# euler_tour = g2.tour
#
# #Hamiltonien

krusk_tree_separate = []
eul_path_separate = []
ham_path_separate = []

for partition in term_tab_sep:
    n_partition = len(partition)
    # Kruskal
    krusk_tree = kruskal_tree(n, partition, distances_matrix)
    krusk_tree_separate.append(krusk_tree)

    # Euler
    eul_path = eulerian_path(krusk_tree, n_partition)
    eul_path_separate.append(eul_path)

    # Hamiltonien
    ham_path = hamiltonian_path(eul_path)
    ham_path_separate.append(ham_path)
    ham_path_separate_reg = regularize(ham_path_separate)
