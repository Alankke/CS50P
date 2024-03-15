def main():
    dict = []
    while True:
        try:
            item = input().lower().strip()
            dict.append(item)
        except (EOFError, KeyError):
            list = sorted(set(dict))
            for i in list:
                print(f"{dict.count(i)} {i.upper()}")
            quit()
            
main()

