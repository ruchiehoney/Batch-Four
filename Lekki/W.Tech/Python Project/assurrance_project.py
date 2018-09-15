print('NAME = Okongwu Cherechukwu Assurance')
print('EMAIL = ocherechukw@gmail.com')
print('My Codelagos Project')

print('ClASS QUIZ\n')
print('Choose the best Option for the below Questions\n')
score = 0
name="Prince"
course='Python'
question1=input('How many males are there in pytthon class \na>4\nb>2\nc>7\n::> ')
if question1 == 'c'or question1 == '4':
    print('Correct\n')
    score += 1
else:
    print('Wrong\n')

question2=input('How many female are there in pytthon class \na>4\nb>2\nc>7\n::> ')
if question2 == 'b'or question2 == '7':
    print('Correct\n')
    score += 1
else:
    print('Wrong\n')

question3=input('How many female are there in pytthon class \na>9\nb>2\nc>7n: ')
if question3 == 'a'or question3 == '9':
    print('Correct\n')
    score += 1
else:
    print('Wrong\n')

print(name,'youy total is scored',course,score, '/3')

print('Grade Report')
print("Your total score is :", score)
if score == 3:
    print('Excellent')
elif score == 2:
    print('Pass')
elif score == 1:
    print('Fail')
else:
    print('You Failed, Please Quit Codelagos!')
