numString = input("Please enter a value in roman numbers : ")
romanNum = numString.lower()
print(romanNum)
value = 0
for digit in romanNum:
    if(digit == 'i'):
        value = value + 1
    elif(digit == 'v'):
        value = value + 5
    elif(digit == 'x'):
        value = value + 10
print(value)
