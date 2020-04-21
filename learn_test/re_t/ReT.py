from re import compile, match, search
def main():
    reComplie = compile("a.b")

    string1 = 'a_ba4ba3cakdhkbkjsdka8ba b'
    regexReturn = match('a.b', string1)
    if regexReturn is not None:
        print(regexReturn.groups())

if __name__ == '__main__':
    main()
