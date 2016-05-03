def calcBMI(weight,height):
    bmi = weight / (height*2)
    print("BMI value is: {:.2f}".format(bmi))

weight = float(input("Enter your weight(in kg): "))
height = float(input("Enter your height(in m): "))
result = calcBMI(weight,height)