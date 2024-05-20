import math

# pythagoras theorem

def hypotenuse_calc(side_a, side_b):
    result = math.sqrt(pow(int(side_a), 2) + pow(int(side_b), 2))
    return result

number1 = input('number 1:\n')
number2 = input('number 2:\n')

print('Result:\n', round(hypotenuse_calc(number1, number2), 2))