lower=10
upper=100
first=int(input("Enter a number( {0} --- {1}):".format(lower,upper).strip()))
second=int(input("Enter a number( {0} --- {1}):".format(lower,upper).strip()))
for i in range(first, second):
    print("{} {}".format(i,chr(i)))