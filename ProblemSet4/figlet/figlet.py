from pyfiglet import Figlet
import random, sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
            text = input("Input: ").strip()
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()