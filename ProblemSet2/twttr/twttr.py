def main():
    text = input("Input: ").strip()
    text = text.replace('a', "").replace('e',"").replace('i',"").replace('o',"").replace('u',"")
    print(text)
    if text.isupper():
        text = text.replace('A', "").replace('E',"").replace('I',"").replace('O',"").replace('U',"")
        print(text)




main()