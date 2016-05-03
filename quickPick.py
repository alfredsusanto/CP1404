import random

user_input = int(input("How many quick picks to generate?\n >>>"))

for i in range(user_input):
    data = []
    for i in range(6):
        while True:
            pick = random.randint(1,46)
            if pick in data:
                continue
            else:
                data.append(pick)
            break
    data.sort()
    print("{:3d} {:3d} {:3d} {:3d} {:3d} {:3d}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
