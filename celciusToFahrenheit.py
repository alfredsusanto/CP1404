def celciusToFahrenheit(celciusValue):
    fahrenheitValue = celciusValue * 9/5 + 32
    print("Temperature today: {}, Fahrenheit: {}".format(celciusValue,fahrenheitValue))

celciusValue=float(input("Enter the temperature today: "))
result=celciusToFahrenheit(celciusValue)