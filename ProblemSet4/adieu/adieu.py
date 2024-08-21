import inflect, sys

names = []
def main():
  engine = inflect.engine()
  try:
    while True:
      name = input("Name: ")
      names.append(name)
  except EOFError:
    print(f"Adieu, adieu, to {engine.join(names)}")
    sys.exit(0)

if __name__ == "__main__":
  main()
