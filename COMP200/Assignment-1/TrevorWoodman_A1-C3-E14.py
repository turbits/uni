print('''
\nTrevor Woodman
Athabasca University - COMP200
Assignment 1 - Chapter 3 - Exercise 14
->Program will run until it determines the correct answer.
''')

input('Press enter to start')

n = 1
a = 0
b = 0

while a <= b:
    a = 1.003*(n**2)
    b = 243*n
    n += 1
    print('Algorithm A: ' + str(a))
    print('Agorithm B: ' + str(b))
    print('Size: ' + str(n))
print('\n-----')
print('Algorithm A: ' + str(a))
print('Algorithm B: ' + str(b))
print('\nAlgorithm B became more efficient than Algorithm A at approximately ' + str(b) + ' instructions, n = ' + str(n))
