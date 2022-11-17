import os
import re
import scripts


def get_loose_ends(
    directory_or_file_path,
    do_search_recursively = True
):
    file_paths = get_file_paths(directory_or_file_path, do_search_recursively)

    for file_path in file_paths:
        get_functions(file_path)

    return(file_paths)



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


def get_functions(file_path):
    print(file_path)
    with open(file_path) as f:
        lines = f.read()
    
    func_defs = scripts.func_def_compiler.findall(lines)

    # print(func_defs)

    for func_def in func_defs:
        print(func_def)

        # Parse called function
        called_functions = scripts.called_func_compiler.findall(func_def)
        calling_function = called_functions[0]
        print((calling_function, called_functions[1:]))