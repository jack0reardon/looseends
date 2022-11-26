import re
import matplotlib.pyplot as plt

python_file_name_compiler = re.compile(r"""
    [\w_]+\.py$
""", re.MULTILINE | re.VERBOSE)


func_def_compiler = re.compile(r'(?=(^def[\s\S]*?^def))', re.MULTILINE)

called_func_compiler = re.compile(r'([a-zA-Z_][\w_]*)\(')

# options_for_graph = {
#     # 'font_size': 10,
#     # 'node_size': 10,
#     # 'node_color': 'white',
#     # 'edgecolors': 'black',
#     'alpha': 0.7,
#     # 'linewidths': 1,
#     # 'width': 3,
# }

options_for_graph = {
    'alpha': 0.7,
    'arrowsize': 15,
    'edgecolors': '.4',
    'with_labels': True,
    'cmap': plt.cm.Blues
}