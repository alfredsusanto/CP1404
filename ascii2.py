lower = 10
upper = 80

def get_number(lower,upper):
    first=int(input("Enter first number( {0} --- {1}): \n>>>".format(lower,upper).strip()))
    second=int(input("Enter second number( {0} --- {1}): \n>>>".format(lower,upper).strip()))
    while True:
        if first < second:
            break
        print("Second number is too low")
        second=int(input("Enter second number( {0} --- {1}): \n>>>".format(lower,upper).strip()))

    for i in range(first, second):
        print("{} {}".format(i,chr(i)))


    return first, second

result = get_number(lower,upper)


