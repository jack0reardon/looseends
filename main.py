import scripts.ancillary_functions as af

function_dependencies = af.get_loose_ends('./scripts/')
# function_dependencies = af.get_loose_ends('./recursive_project_example/')
# function_dependencies = af.get_loose_ends('.')

print(function_dependencies)