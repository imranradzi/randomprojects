import random

running1 = True
while running1:
    ask1 = input('start? (yes or no)\n')
    if ask1 == 'yes':
        quantityrun = True
        while quantityrun:
            error = 'no'
            quantityask = input('how many things are we choosing from?\n')
            try:
                int(quantityask)
            except:
                print('INVALID INPUT TRY AGAIN\n')
                error = 'yes'
            if error == 'no':
                quantityrun = False
                quantity = int(quantityask)
        numberlist = [i for i in range(quantity)]
        nameassignrun = True
        while nameassignrun:
            nameassign = input('assign names?\n')
            if nameassign == 'yes':
                for i in numberlist:
                    numberlist[i] = input('enter name\n')
                nameassignrun = False
            elif nameassign == 'no':
                print('values will be printed in integers then\n')
                nameassignrun = False
            else:
                print('INVALID INPUT TRY AGAIN\n')
        running1 = False
        running2 = True
        while running2:
            value = random.randrange(quantity)
            if nameassign == 'yes':
                print(numberlist[value])
            else:
                print(numberlist[value] + 1)

            askrun = True
            while askrun:
                ask2 = input('continue? (yes or no)\n')
                if ask2 == 'no':
                    askrun = False
                    running2 = False
                elif ask2 == 'yes':
                    askrun = False
                else:
                    print('INVALID INPUT TRY AGAIN\n')

    elif ask1 == 'no':
        running1 = False
        print('ok')

    else:
        print('INVALID INPUT TRY AGAIN\n')