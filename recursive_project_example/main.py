import analysis_functions as af

def my_main_function():
  the_data = af.read_data()
  analysed_data = af.analyse_data(the_data)
  plot_data(analysed_data)