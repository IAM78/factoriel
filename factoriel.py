number = int(input('Enter the number you want: '))
incr = fact = 1

while fact < number:

    incr += 1
    fact *= incr

if number == fact:


    
    print('Yes')
else:
    print('No')