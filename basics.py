def hello_world_task():
    my_string = 'Hello, World!'
    return my_string


def variables_and_types_task():
    mystring = "hello"
    myfloat = 10.0
    myint = 20
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)


def lists_task():
    numbers = []
    strings = []
    names = ["John", "Eric", "Jessica"]
    # write your code here
    [numbers.append(x) for x in range(1, 4)]
    [strings.append(y) for y in hello_world_task().split()]
    second_name = names[1]
    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)


def basic_operators_task():
    # TODO: fill this function
    pass


def string_formatting_task():
    # TODO: fill this function
    pass


def basic_string_operations_task():
    # TODO: fill this function
    pass


def conditions_task():
    # TODO: fill this function
    pass


def loops_task():
    # TODO: fill this function
    pass


def functions_task():
    # TODO: fill this function
    pass


def docstrings_task():
    # TODO: fill this function
    pass


def dictionaries_task():
    # TODO: fill this function
    pass


if __name__ == '__main__':
    hello_world_task()
    variables_and_types_task()
    lists_task()
    basic_operators_task()
    string_formatting_task()
    basic_string_operations_task()
    conditions_task()
    loops_task()
    functions_task()
    docstrings_task()
    dictionaries_task()
