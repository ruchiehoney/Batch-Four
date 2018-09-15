#python cbt exam
print('NAME: SAMUEL AKINTUNDE \nEmail: samakintunde1@gmail.com \nthis is my project for python(code lagos)')
print()
print()
name=input('please enter your name to proceed to your python cbt exam \n:')
print(name, 'you are welcome to python quiz')
print()
print("Please choose a difficulty:")
difficulty = input("A) Hard   B)Easy\n: ").upper()
if difficulty == 'A' or difficulty == 'HARD':
    
    score = 0
    print("")
    print("You chose the hard difficulty")
    print()
    answer1 = input("1.Where is the Great Victoria lake located? \nA) Canada   B)West Africa   C)Australia   D)North America\n: ").upper()

    if answer1 == "C" or answer1 == 'AUSTRALIA':
        print("Correct")
        score += 1
    else:
        print("wrong")
    print()
        
    answer2 = input("2.Who is most responsible for cracking the Enigma Code? \nA) Alan Turing   B) Jeff Bezos   C) George Boole   D) Charles   Babbage\n: ").upper()
    if answer2 == "A" or answer2 == "ALAN TURING":
        print("Correct")
        score += 1
    else: 
        print("wrong")
    print()
    answer3 = input("3.What is the art and science of designing and constructing of structures? \nA) civil engineering   B)structural engineering   C)Architecture   D)building management\n: ").upper()

    if answer1 == "C" or answer1 == 'ARCHITECTURE':
        print("Correct")
        score += 1
    else:
        print("wrong")
    print()
    print('your total score is', score, '/3')
    if score == 3:
        print('EXCELLENT')
        print(name,'you did a nice work')
    elif score == 2:
        print('PASS')
    elif score == 1:
        print('FAIL')
    else:
        print('GO AND STUDY HARDER, AND COME BACK NEXT YEAR TO RETAKE THE EXAM \nYOU ARE ALWAYS WELCOME', name) 


elif difficulty == 'B' or difficulty == 'EASY':
    print()
    score = 0
    print("You chose the easy difficulty")
    print()
    answer3 = input("1.What is the capital of Lagos State? \nA) Lekki   B) Ikeja   C)Ajah \n:").upper()
    if answer3 == "B" or answer3 == "IKEJA":
        print("Correct")
        score += 1
    else:
        print("wrong")
    print()
        

    
    answer4 = input("2.how old is Nigeria? \nA) 55  B) 56   C)58 \n:").upper()
    if answer4 == "C" or answer4 == "58":
        print("Correct")
        score += 1
    else:
        print("wrong")
    print()
    answer4 = input("3.1000 metres how many kilometre? \nA) 10km   B) 1km   C)100km \n:").upper()
    if answer4 == "B" or answer4 == "1KM":
        print("Correct")
        score += 1
    else:
        print("wrong")
    print()
    print('your total score is', score, '/3')
    if score == 3:
        print('EXCELLENT')
        print(name,'you did a nice work')
    elif score == 2:
        print('PASS')
    elif score == 1:
        print('FAIL')
    else:
        print('GO AND STUDY HARDER, AND COME BACK NEXT YEAR TO RETAKE THE EXAM \nYOU ARE ALWAYS WELCOME', name)             

