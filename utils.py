import csv
from kruskal import *


def read_nodes_csv(nodes_file):
    with open(nodes_file, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=';')
        nodes_tab = []
        i = 0
        for row in spam_reader:
            if i == 0:
                pass
            i += 1
            nodes_tab.append(row)
    distribution_tab = []
    for e in nodes_tab:
        if e[2] == 'distribution':
            l = []
            for i in e[:2]:
                l.append(float(i))
            distribution_tab.append(l)
    terminal_tab = []
    for e in nodes_tab:
        if e[2] == 'terminal':
            l = []
            for i in e[:2]:
                l.append(float(i))
            terminal_tab.append(l)
    n = len(distribution_tab) + len(terminal_tab)
    return distribution_tab, terminal_tab, n


def read_distances_csv(distances_file, n):
    with open(distances_file, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=';')
        distances_tab = []
        i = 0
        for row in spam_reader:
            if i == 0:
                pass
            i += 1
            distances_tab.append(row)
        distances_matrix = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                distances_matrix[i].append(int(distances_tab[i*n+j][0]))
    return distances_matrix


def create_output(list_b, list_c, nom):
    nom = nom+".txt"
    with open(nom, 'w') as txt_file:
        for list_bi in list_b:
            txt_file.write("b")
            for i in list_bi:
                txt_file.write(" "+str(i))
            txt_file.write("\n")
        for list_ci in list_c:
            txt_file.write("c")
            for i in list_ci:
                txt_file.write(" "+str(i))
            txt_file.write("\n")


def read_nodes_csv2(nodes_file):
    with open(nodes_file, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=';')
        nodes_tab = []
        i = 0
        for row in spam_reader:
            if i == 0:
                pass
            i += 1
            nodes_tab.append(row)
    full_tab = []
    n_distr = 0
    n_term = 0
    for e in nodes_tab:
        if e[2] == 'distribution':
            l = []
            for i in e[:2]:
                l.append(float(i))
            l.append(0)
            l.append(nodes_tab.index(e))
            full_tab.append(l)
            n_distr += 1
        if e[2] == 'terminal':
            l = []
            for i in e[:2]:
                l.append(float(i))
            l.append(1)
            l.append(nodes_tab.index(e))
            full_tab.append(l)
            n_term += 1

    n = len(full_tab)
    return full_tab, n, n_distr, n_term

# def readSolution(filename): # UNUSED
#     try:
#         with open(filename, 'r') as solu:
#             return solu
#     except:
#         print("Erreur d'ouverture de solution !")


def separate(distr_full_tab, term_full_tab, distances_matrix):
    term_tab_sep = [[] for i in range(len(distr_full_tab))]

    for d in distr_full_tab:
        term_tab_sep[d[3]-1].append(d)

    for t in term_full_tab:
        min = 100000
        for d in distr_full_tab:
            if distances_matrix[t[3]-1][d[3]-1] < min:
                min = distances_matrix[t[3]-1][d[3]-1]
                min_d = d
        term_tab_sep[min_d[3]-1].append(t)
    return term_tab_sep


def kruskal_tree(n, partition, distances_matrix, corresp):
    g = Graph(n)
    for i in range(len(partition)):
        for j in range(len(partition)):
            if partition[i] != partition[j]:
                g.addEdge(partition[i], partition[j], distances_matrix[corresp[i]-1][corresp[j]-1])

    return g.KruskalMST()


def demapping(appendices_separate, corresp):
    for i in range(len(appendices_separate)):
        for j in range(len(appendices_separate[i])):
            for k in range(len(appendices_separate[i][j])):
                appendices_separate[i][j][k] = corresp[i][k]


def demapping2(appendices_separate, corresp):
    for i in range(len(appendices_separate)):
        for j in range(len(appendices_separate[i])):
            appendices_separate[i][j] = corresp[i][j]


def get_missing(ham_path, appendices, corresp, distances_matrix):
    for i in range(max(ham_path)):
        if i not in ham_path:
            appendices.append([i, nearest_vertice(i, corresp, distances_matrix, ham_path)])


def eulerian_path(krusk_tree, n):
    g2 = Graph2(n)
    for e in krusk_tree:
        g2.addEdge(e[0], e[1])
        g2.addEdge(e[1], e[0])

    g2.printEulerTour()
    return g2.tour


def hamiltonian_path(eul_path):
    H = []

    for e in eul_path:
        if e[0] not in H:
            H.append(e[0])
    return H

# def rearrange(ham_path_separate_reg, distances_matrix):
#     list_appendices = []
#     for element in ham_path_separate_reg:
#         node_i = 0
#         while node_i < len(element):
#             min = 50000
#             for k in range(5):
#                 if distances_matrix[element[node_i]][]:


def regularize(ham_path, corresp, distances_matrix):
    i = 0
    appendices = []

    while i < len(ham_path):
        k_min = 1
        d_min = 100000
        k = 1
        while k + i < len(ham_path) and k < 5:
            if distances_matrix[corresp[ham_path[i]]-1][corresp[ham_path[i+k]]-1] < d_min:
                k_min = k
                d_min = distances_matrix[corresp[ham_path[i]]-1][corresp[ham_path[i+k]]-1]
            k += 1

        if k_min != 1:
            appendices.append(ham_path[i:i+k_min])

        i += k_min
    print(appendices)

    for e in appendices:
        print(e)
        for m in e[1:]:
            print(m)
            print(ham_path)
            ham_path.remove(m)

    return appendices


def mapping(tab_sep):
    mapped_tab_sep = [[] for i in range(len(tab_sep))]
    corresp = [[] for i in range(len(tab_sep))]

    for group_i in range(len(tab_sep)):
        for i in tab_sep[group_i]:
            corresp[group_i].append(i[3])

    for group_i in range(len(tab_sep)):
        for i in range(len(tab_sep[group_i])):
            mapped_tab_sep[group_i].append(i)

    return mapped_tab_sep, corresp


def nearest_vertice(i, corresp, distances_matrix, ham_path):
    min = distances_matrix[corresp[ham_path[0]]-1][corresp[i]-1]
    result = 0
    for j in ham_path:
        if distances_matrix[corresp[j]-1][corresp[i]-1] <= min:
            result = j
            min = distances_matrix[corresp[j]-1][corresp[i]-1]
    return result


def destruct(appendices_separate):
    sol = []
    for i in appendices_separate:
        for j in i:
            sol.append(j)
    return sol