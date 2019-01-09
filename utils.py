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

def readSolution(filename):
    try:
        with open(filename, 'r') as solu:
            return solu
    except:
        print("Erreur d'ouverture de solution !")

def judgeSolution(solution):
    return 0

<<<<<<< HEAD
def costSolution(solution):
    return 800000

readSolution("mai")
=======

def separate(distr_full_tab, term_full_tab, distances_matrix):
    term_tab_sep = [[]*len(distr_full_tab)]
    for e in distr_full_tab:
        min = 100000
        for i in range(len(distr_full_tab))
            if distances_matrix[e[3]][term_full_tab[i]] < min:
                min = distances_matrix[e[3]][term_full_tab[i]]

>>>>>>> 804a6b0fc28c77fc8c0a36de47772a0d3b33db93
