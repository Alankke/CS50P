import emoji

def main():
  alias = input("Input: ")
  print(emoji.emojize(f"Output: {alias}", language='alias'))

if __name__ == "__main__":
  main()
