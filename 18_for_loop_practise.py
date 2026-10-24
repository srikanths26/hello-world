for number in 1,2,3,4,5:
    print('The number is:', number)
for number in range(6):  # only one number is given, so it will be considered as end value and start value will be 0 by default
    print('The number is:', number)
for number in range(1, 6):  # two numbers are given, so first one will be considered as start value and second one will be considered as end value
    print('The number is:', number)
for number in range(1, 10, 2):  # three numbers are given, so first one will be considered as start value, second one will be considered as end value and third one will be considered as step value
    print('The number is:', number)
