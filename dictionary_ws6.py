dictionary = {}
text = input("Enter text: ")

listings = text.strip().split()

for each in listings:
    if each in dictionary:
        dictionary[each] += 1
    else:
        dictionary[each] = 1

sorted_keys = sorted(dictionary, key=dictionary.__getitem__, reverse= True)

for key in sorted_keys:
    print("{} : {:<5d}".format(key, dictionary[key]))
