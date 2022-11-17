import re

python_file_name_compiler = re.compile(r"""
    [\w_]+\.py$
""", re.MULTILINE | re.VERBOSE)


func_def_compiler = re.compile(r'(?=(def[\s\S]*?def))', re.MULTILINE)

called_func_compiler = re.compile(r'([a-zA-Z_][\w_]*)\([[a-zA-Z_][\w_]*,\s*]*\)')