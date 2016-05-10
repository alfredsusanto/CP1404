dictionary = {}
text = input("Enter text: ")

listings = text.strip().split()

for each in listings:
    if each in dictionary:
        dictionary[each] += 1
    else:
        dictionary[each] = 1

sorted_keys = sorted(dictionary)

for each in sorted_keys:
    print("{} : {:<5d}".format(each, dictionary[each]))
