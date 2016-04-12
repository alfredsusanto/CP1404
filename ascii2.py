lower = 10
upper = 50

def get_number(lower,upper):
    first=int(input("Enter a number( {0} --- {1}): \n>>>".format(lower,upper).strip()))
    second=int(input("Enter a number( {0} --- {1}): \n>>>".format(lower,upper).strip()))
    return first, second

