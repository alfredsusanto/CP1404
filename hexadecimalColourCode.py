color = {"Aliceblue":"#f0f8ff", "Antiquewhite":"#faebd7", "beige":"#f5f5dc", "black":"#000000", "Blanched/almond":"#ffebcd", "brown":"#a52a2a", "Blueviolet":"#8a2be2", "Cornflowerblue": "#6495ed"}
name = input("Enter a name: ").capitalize()

for key,value in color.items():
    if name == key:
        print(value)
if name not in color.keys():
    print("No hexadecimal color code detected")