name=input("Enter name: ")
print(" (H)ello\n","(G)oodbye\n","(Q)uit\n")

choice=input().upper()
while choice !='Q':
    if choice == 'H':
        print("Hello",name)
    elif choice == 'G':
        print("Goodbye",name)
    else:
        print("Invalid Choice")
    print(" (H)ello\n","(G)oodbye\n","(Q)uit\n")
    choice=input().upper()
print("Finished")
