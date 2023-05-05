def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    evaluate = ''
#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha:
            for character in s:
                if character not in [' ', ',', '.', ';', '?', '!']:
                    if character.isnumeric() and i == 0 and character != '0':
                        i += 1
                        evaluate += character
                    elif character.isnumeric() and i > 0:
                        i += 1
                        evaluate += character
                    elif character.isalpha() and i < 1:
                        evaluate += character
    if evaluate == s:
        return True
    else:
        return False


main()