def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    periodcent = periodcent_to_float(input("What periodcentage would you like to tip? "))
    tip = dollars * periodcent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    return float(dollars.strip("$"))


def periodcent_to_float(periodcent):
    return float(periodcent.strip("%")) / 100


main()