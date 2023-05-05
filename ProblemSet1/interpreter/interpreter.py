def main():
    x, y, z = input("Expression: ").strip().split(" ")
    print(f"{interpreter(int(x), str(y), int(z)):.1f}")

def interpreter(x, y, z):
    if y == "+":
        return x + z
    elif y == "*":
        return x * z
    elif y == "-":
        return x - z
    elif y == "/" and z != 0:
        return x / z
    
main()