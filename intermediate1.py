numbers = []

for i in range(1,6):
    each = int(input("Number: "))
    numbers.append(each)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is ", sum(numbers) / len(numbers))
