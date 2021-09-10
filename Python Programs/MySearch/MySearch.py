def my_search(input_file, value):
    input_list = []
    f = open(input_file, "r")
    for line in f:
        input_list.append(int(line))
    return linear_search(input_list, value)


def linear_search(array_of_values, value):
    for i in range(len(array_of_values)):
        if array_of_values[i] == value:
            return i
    return -1
