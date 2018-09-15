print('\nMY CODE LAGOS PROJECT\n')
print('NAME - ['+ ' '*4,'Taiwo Adeleke'+ ' ' * 4,' ]')
print('Email- [christyadeleke@gmail.com]\n')
print('Apply For Debit Card Through An Automated Card Machine (ACM)\n')
request = 0
pin = 1227
acount_number = 9876543210
print('\tInsert your card\n')
while True:
    pin=int(input('Please enter your secret number: '))
    if pin == 1227:
        print('\nWelcome, Taiwo Adeleke\n')
        acount_number=int(input('Please enter your account number: '))
        if acount_number == 9876543210:
            print ('\nOkay, follow these process to apply for a new card')
            select=input('Make a request: \n\t.1. Naira card \n\t.2. Dollar card\n\t>> ')
            if select=='1':
                request = input('\nSelect type of card:\n\t.1. Master Card \n\t.2. Visa Card \n\t.3. Verve Card\n\t>> ')
                location = input('Enter your location\n\t>> ')
                if request=='1':
                    print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                    break
                elif request=='2':
                    print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                    break
                elif request=='3':
                    print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                    break
            elif select == '2':
                location = input('\nEnter collection area/city\n>> ')
                print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service ")    
                break  
            else:
                print('Invalid Entry, Re-choose\n')
                continue
                select=input('Make a request: \n\t.1. Naira card \n\t.2. Dollar card\n\t>> ')
                if select=='1':
                    request = input('\nSelect type of card:\n\t.1. Master Card \n\t.2. Visa Card \n\t.3. Verve Card\n\t>> ')
                    location = input('Enter your location\n\t>> ')
                    if request=='1':
                        print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                        break
                    elif request=='2':
                        print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                        break
                    elif request=='3':
                        print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                        break
                    else:
                        print('Invalid Entry.\n Try Next Time')
                        break
        else:
            print('Invalid Entry, Re-choose\n')
            acount_number=int(input('Please enter your account number: '))
            if acount_number == 9876543210:
                print ('\nOkay, follow these process to apply for a new card')
                select=input('Make a request: \n\t.1. Naira card \n\t.2. Dollar card\n\t>> ')
                if select=='1':
                    request = input('\nSelect type of card:\n\t.1. Master Card \n\t.2. Visa Card \n\t.3. Verve Card\n\t>> ')
                    location = input('Enter your location\n\t>> ')
                    if request=='1':
                        print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                        break
                    elif request=='2':
                        print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                        break
                    elif request=='3':
                        print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service")  
                        break
                elif select == '2':
                    location = input('\nEnter collection area/city\n>> ')
                    print("\nTransaction successful, ready in 48hrs and you'll receive a text message of the branch for pickup in "+ location+".Else visit any of our branch for complains\nThanks for using our service ")    
                    break
                else:
                    print('Invalid Entry.\nTry Next Time')
                    break
            else:
                print('Invalid Entry.\nTry Next Time')
                break
    else:
        print('Invalid Entry, Try Again!\n')
