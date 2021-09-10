from MySearch import my_search


def main():
    input_file = "input.txt"
    user_num = int(input("Enter a number: "))
    value = my_search(input_file, user_num)

    print("Element " + str(user_num) + " is at index: " + str(value))


if __name__ == "__main__":
    main()
