Fraction = input("Fraction:").strip()
while True:
    try:
        x, y = Fraction.split("/", 1)
        if x.isdigit() and y.isdigit():
            if int(x) <= int(y) and int(y) != 0:
                percent = (int(x) / int(y)) * 100
                if percent >= 99:
                    print("F")
                    break
                elif percent <= 1:
                    print("E")
                    break
                else:
                    print(f"{percent:.0f}%")
                    break
    except(ValueError, ZeroDivisionError):
        pass
    else:
        pass

