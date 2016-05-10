from programmingLanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(vb)

    listing = [ruby, python, vb]
    print("The dynamically typed languages are:")
    for each in listing:
        if each.is_dynamic():
            print(each.name)

main()


