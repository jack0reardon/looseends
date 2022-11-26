import re
import matplotlib.pyplot as plt

python_file_name_compiler = re.compile(r"""
    [\w_]+\.py$
""", re.MULTILINE | re.VERBOSE)


func_def_compiler = re.compile(r'(?=(^def[\s\S]*?^def))', re.MULTILINE)

called_func_compiler = re.compile(r'([a-zA-Z_][\w_]*)\(')

options_for_graph = {
    # 'font_size': 10,
    # 'node_size': 10,
    # 'node_color': 'white',
    # 'edgecolors': 'black',
    'alpha': 0.7,
    # 'linewidths': 1,
    # 'width': 3,
    'cmap': plt.cm.Blues
}

# nx.draw_networkx(G, node_size = node_size, 
    #              node_color = node_color, alpha = 0.7,
    #              with_labels = True, width = edge_width,
    #              edge_color ='.4', cmap = plt.cm.Blues)