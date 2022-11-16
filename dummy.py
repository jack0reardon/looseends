def my_function():
  print("Hello from a function")


def another_function():
    my_function1()
    my_function()


def yet_another_function():
  another_function()
  my_function()
  yet_another_function()


def my_last_function():
  yet_another_function()
  another_function()
  my_function()
  my_function1()

def an_unused_function():
  print()