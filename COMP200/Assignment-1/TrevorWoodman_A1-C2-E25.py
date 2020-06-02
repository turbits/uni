print('''
\nTrevor Woodman
Athabasca University - COMP200
Assignment 1 - Chapter 2 - Exercise 25
->Program will loop. Type "q" and press enter to quit at any point.
->Program will output YES if there are a pair of adjacent values, otherwise it will print NO
''')
print('Input one integer at a time, greater than 0, and end the sequence by inputting -1.\nMust provide 2 or more numbers, not including -1.')

def check_adjacent_int():
    sequence = []
    result = False
    user_input = ''
    num = 0
    last_num = 0
    
    while num != -1:
        print('-----')
        user_input = input('> ')
        if user_input == 'q': exit()
        num = int(user_input)
        
        if num == -1:
            sequence.append(num)
            print('-----\nResults:')
            if len(sequence) < 3:
                print('Err: Sequence must have more than two numbers.\nSequence has been reset.')
                pass
            else:
                print(sequence)
                print('Does the sequence contain an adjacent number pair?')
                if (result):
                    print('YES')
                else:
                    print('NO')
                print('Sequence has been reset.')
            # Loop program
            check_adjacent_int()
        if num <= 0 and num != -1:
            print('Err: Number must be greater than 0.')
            print('Current Sequence:')
            print(sequence)
        else:
            sequence.append(num)
            print('Current Sequence:')
            print(sequence)
            
            if num == last_num:
                result = True
            last_num = num
                
# Initial call
check_adjacent_int()
