from MySearch import my_search


def main():
    file = "input.txt"
    user_num = int(input("Enter a number: "))
    value = my_search(file, user_num)

    print("Element " + str(user_num) + " is at index: " + str(value))


if __name__ == "__main__":
    main()
