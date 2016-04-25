LOWER = 10
UPPER = 80

def get_number():
    while True:
        low = input("Enter a number({}-{}):".format(LOWER, UPPER)).strip()
        if low.isdecimal():
            int1 = int(low)
            if LOWER <= int1 <= UPPER:
                break
            else:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")
    int1 = int(low)
    while True:
        upp = input("Enter a number({}-{}):".format(LOWER, UPPER)).strip()
        if upp.isdecimal():
            int2 = int(upp)
            if int1 <= int2 <= UPPER:
                break
            else:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")
    int2 = int(upp)
    return int1, int2


low, upp = get_number()
for i in range(low, upp):
    print("{} {}".format(i, chr(i)))


