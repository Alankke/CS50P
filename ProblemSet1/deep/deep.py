def main():
    user_input = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip())
    is_fortytwo(user_input)


def is_fortytwo(user_input):
    if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
        print("Yes")
    else:
        print("No")


main()