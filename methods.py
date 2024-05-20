import math

# pythagoras theorem
number1 = input('number 1:\n')
number2 = input('number 2:\n')
result = math.sqrt(pow(int(number1), 2) + pow(int(number2), 2))
print('Result:\n' + str(result))