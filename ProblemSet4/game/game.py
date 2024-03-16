import random

def main():
    n = get_level()
    guess(n)

def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level > 0:
                return level
            else:
                continue
        except Exception:
            continue

def guess(level):
    rnd = random.randint(1, level)
    guessed = False
    while guessed == False:
        try:
            guess = int(input("Guess:"))
            if guess == rnd:
                print("Just right!")
                guessed = True
                break
            elif guess > rnd:
                print("Too large!")
                guessed = False
            elif guess < rnd:
                print("Too small!")
                guessed = False
        except Exception:
            continue

if __name__ == "__main__":
    main()
