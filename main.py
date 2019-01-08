from utils import *

city_name = 'grenoble'

nodes_file = 'instances/' + city_name + '/nodes.csv'
distances_file = 'instances/' + city_name + '/distances.csv'

distribution_tab, terminal_tab, n = read_nodes_csv(nodes_file)
distances_matrix = read_distances_csv(distances_file, n)


