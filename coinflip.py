import random

running1 = True
while running1:
    ask1 = input('start? (yes or no)\n')
    if ask1 == 'yes':
        running1 = False
        running2 = True
        while running2:
            value = random.randrange(100)
            if value < 50:
                print('\nheads\n')
            else:
                print('\ntails\n')

            askrun = True
            while askrun:
                ask2 = input('continue? (yes or no)\n')
                if ask2 == 'no':
                    askrun = False
                    running2 = False
                elif ask2 == 'yes':
                    askrun = False
                else:
                    print('INVALID INPUT TRY AGAIN')

    elif ask1 == 'no':
        running1 = False
        print('ok')

    else:
        print('INVALID INPUT TRY AGAIN')
