import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        answer = x + y
        attempts = 0

        while attempts < 3:
            try:
                response = int(input(f"{x} + {y} = "))
                if response == answer:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError as e:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
