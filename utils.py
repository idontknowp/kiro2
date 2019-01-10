import csv


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

readSolution("mai")

def separate(distr_full_tab, term_full_tab, distances_matrix):
    term_tab_sep = [[] for i in range(len(distr_full_tab))]

    for d in distr_full_tab:
        term_tab_sep[d[3]].append(d)

    for t in term_full_tab:
        min = 100000
        for d in distr_full_tab:
            if distances_matrix[t[3]][d[3]] < min:
                min = distances_matrix[t[3]][d[3]]
                min_d = d
        term_full_tab[min_d[3]].append(d)
    return term_tab_sep

def kruskal_tree(n, partition, distances_matrix):
    g = Graph(n+1)
    for i in partition:
        for j in partition:
            if i != j:
                g.addEdge(i, j, distances_matrix[i][j])

    return g.KruskalMST()


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


def plot_separate_network(data, links=0):
    for i in range(len(data)):
        l_x, l_y = [], []
        for e in data[i]:
            if e[2] == 1:
                l_x.append(e[0])
                l_y.append(e[1])
        plt.scatter(l_x, l_y, marker='o')
        l_x, l_y = [], []
        for e in data[i]:
            if e[2] == 0:
                l_x.append(e[0])
                l_y.append(e[1])
        plt.scatter(l_x, l_y, marker='^')

        # l_x, l_y = [], []

    plt.show()


def regularize(ham_path_separate):
    for i in range(1, len(ham_path_separate)):
        for j in range(len(ham_path_separate[i])):
            ham_path_separate[i][j] += len(ham_path_separate[i-1])
    return ham_path_separate


# def rearrange(ham_path_separate_reg, distances_matrix):
#     list_appendices = []
#     for element in ham_path_separate_reg:
#         node_i = 0
#         while node_i < len(element):
#             min = 50000
#             for k in range(5):
#                 if distances_matrix[element[node_i]][]:
