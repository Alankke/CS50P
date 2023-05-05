def main():
    user_input = convert(input("Write a text with a smiling face or a frowning face: "))
    print(user_input)


def convert(user_input):
    user_input_converted = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return user_input_converted

main()