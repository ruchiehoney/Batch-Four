import time
print('\nA Python Project By;\n')
print('NAME: Uzuana_Dumebi')
print('E-MAIL: duzuana@gmail.com')
print('08135324473\n')
#A countdown timer in python
#firstly, we need to import time
#importing time will enable us make use of time functions like sleep() function
#input the state of the meal to determine the maximum time for that state selected
#A ranged loop is used to count down
#if frozen, timer doesn't exit 540seconds
#if cold, timer doesn't exit 300seconds
#if at room temperature, timer doesnt exit 120seconds
#we need to have python sleep for 1 second between each countdown
print ("\nMICROWAVE OPERATION IN SECONDS")
print (' ')
while True:
    option_1= input("What is the state of your meal? \n\t a). frozen \n\t b). cold \n\t c). room temperature \n\t >> ")
    if option_1 == ('a'):
        meal_type=input('\nWhat do you want to microwave? ')
        seconds=int(input("Enter number of seconds needed "))
        for i in range(seconds):
            time.sleep(1)
            if seconds <= 540:
                print(str(seconds - i) + "seconds left ")
        print('your ', meal_type, 'is ready!!!\n')
        break
    
    
    elif option_1 == ('b'):
        meal_type=input('\nWhat do you want to microwave? ')
        seconds=int(input("Enter number of seconds needed "))
        for i in range(seconds):
            time.sleep(1)
            if seconds <= 300:
                print(str(seconds - i) + "seconds left")
        print('your ',meal_type, 'is ready!!!\n')
        break
    
    
    elif option_1 == ('c'):
        meal_type=input('\nWhat do you want to microwave? ')
        seconds=int(input("Enter number of seconds needed "))
        for i in range(seconds):
            time.sleep(1)
            if seconds <= 300:
                print(str(seconds - i) + "seconds left")
        print('your ',meal_type, 'is ready!!!')
        break
    else: print('Invalid Entry, Re-choose')
    
