def read_data():
  # Read in the data
  print("I read the data")
  the_data = 1
  return(the_data)


def analyse_data(the_data):
  get_recusive_metric(the_data)
  perform_analysis(the_data)


def get_recusive_metric(the_data):
  if len(the_data) > 0:
    get_recusive_metric(the_data[1:])
  else:
    get_split_data(the_data)

def get_split_data(the_data):
  left_side = get_recusive_metric(the_data[0:(len(the_data) - 1)])
  right_side = get_recusive_metric(the_data[1:len(the_data)])
  the_result = set(left_side).intersection(right_side)
  return(the_result)

def perform_analysis(the_data):
  perform_minimal_analysis(the_data)
  perform_superfluous_analysis(the_data)

def perform_minimal_analysis(the_data):
  # Perform it
  print('Performed!')

def perform_superfluous_analysis(the_data):
  # Perform it
  print('Performed!')