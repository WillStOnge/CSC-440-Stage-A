def my_search(input_file, value):
    try:
        with open(input_file, "r") as in_file:
            return [int(i) for i in in_file.read().splitlines()].index(value)
    except ValueError:
        return -1
    except FileNotFoundError:
        print("File does not exist")