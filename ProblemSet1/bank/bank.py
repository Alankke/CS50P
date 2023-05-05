def main():
    greeting = input("Greeting:").lower().strip()
    print(money(greeting))

def money(greeting):
    if greeting.startswith('hello') == True:
        return "$0"
    elif greeting.startswith('h') == True:
        return "$20"
    else:
        return "$100"

main()

