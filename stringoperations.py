#string functions
str = '     "Hello World"          '
print(str)
#function to remove space from left side
print(str.lstrip())
#function to remove space from right side
print(str.rstrip())
#function to remove space from both sides
print(str.strip())

str_1 = 'This part was concatinated(Without any space in frozenset)'
#for string concatination
print("\n\n" + str + str_1)


#Function to find the string length
length = len(str_1)
print(str_1 + "\nLength of this string : " + length)

#Function to find position of a character in string
print(str)
print("\nPosition of W : " + str.find('W')
