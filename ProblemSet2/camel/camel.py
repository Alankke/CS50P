def main():
    user_input = input("camelCase: ").strip()
    print(f"snake_case: {snake(user_input)}")



def snake(input):
    space = ""
    for character in input:
        if character.isupper():
            space += "_"
            space += character.lower()
        else:
            space += character
    return space



main()