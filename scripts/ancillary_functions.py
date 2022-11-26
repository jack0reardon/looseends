import os
import re
import scripts
import networkx as nx
import matplotlib.pyplot as plt


def get_loose_ends(
    directory_or_file_path,
    do_search_recursively = True,
    do_show_graph = True
):
    file_paths = get_file_paths(directory_or_file_path, do_search_recursively)

    defined_funcs_and_dependencies = {}

    for file_path in file_paths:
        defined_funcs_and_dependencies.update(get_defined_funcs_and_dependencies(file_path))

    only_defined_funcs_and_dependencies = get_only_defined_funcs_and_dependencies(defined_funcs_and_dependencies)

    if do_show_graph:
        get_loose_ends_graph(only_defined_funcs_and_dependencies)

    return(only_defined_funcs_and_dependencies)



def get_file_paths(
    directory_or_file_path,
    do_search_recursively,
    file_paths = []
):
    if os.path.isfile(directory_or_file_path):
        if scripts.python_file_name_compiler.search(directory_or_file_path) is not None:
            file_paths.append(directory_or_file_path)
        return(file_paths)

    elif os.path.isdir(directory_or_file_path):
        standard_directory_path = get_standard_directory_path(directory_or_file_path)
        directories_or_files_to_search = [standard_directory_path + file_name \
            for file_name in os.listdir(directory_or_file_path) \
            if file_name[0] != '.']

        if do_search_recursively and len(directories_or_files_to_search) > 0:
            for directory_or_file in directories_or_files_to_search:
                get_file_paths(directory_or_file, do_search_recursively, file_paths)
        
        return(file_paths)

    else:
        raise Exception("Neither directory nor file provided")


def get_standard_directory_path(directory_path):
    last_character = directory_path[(len(directory_path) - 1):]
    if last_character == '/':
        return(directory_path)
    elif directory_path == '.':
        return('')
    else:
        return(directory_path + '/')


def get_defined_funcs_and_dependencies(file_path):
    with open(file_path) as f:
        lines = f.read()
    
    func_defs = scripts.func_def_compiler.findall(lines)

    defined_funcs_and_dependencies = {}

    for func_def in func_defs:
        # Parse called function
        called_functions = scripts.called_func_compiler.findall(func_def)
        calling_function = called_functions[0] + '()'
        defined_funcs_and_dependencies[calling_function] = [called_function + '()' for called_function in called_functions[1:]]

    return(defined_funcs_and_dependencies)


def get_only_defined_funcs_and_dependencies(defined_funcs_and_dependencies):
    defined_funcs = list(defined_funcs_and_dependencies.keys())

    # Only retain dependent functions that are one of the defined funcs
    for defined_func in defined_funcs:
        dependencies_to_retain = set(defined_funcs_and_dependencies[defined_func]).intersection(defined_funcs)
        if len(dependencies_to_retain) == 0:
            defined_funcs_and_dependencies.pop(defined_func, None)
        else:
            defined_funcs_and_dependencies[defined_func] = dependencies_to_retain

    return(defined_funcs_and_dependencies)


def get_loose_ends_graph(defined_funcs_and_dependencies):
    directed_graph = nx.DiGraph()
    for defined_func in defined_funcs_and_dependencies:
        directed_graph.add_node(defined_func)
        for dependency in defined_funcs_and_dependencies[defined_func]:
            directed_graph.add_edge(dependency, defined_func)

    pos = nx.circular_layout(directed_graph)
    nx.draw_networkx(directed_graph, pos, **scripts.options_for_graph)
    nx.draw(directed_graph, pos)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis('off')
    plt.show()