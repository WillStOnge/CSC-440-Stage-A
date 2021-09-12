def my_search(input_file, value):
    input_list = []
    with open(input_file, "r") as in_file:
        for line in in_file:
            input_list.append(int(line))
    try:
        return input_list.index(value)
    except ValueError:
        return -1
