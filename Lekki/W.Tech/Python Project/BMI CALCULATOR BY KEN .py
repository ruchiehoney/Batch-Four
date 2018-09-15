print('Enter your height units:\n')
height = float(input('please enter your height input in meters(decimals):'))
print('Enter your weight units:\n')
weight = int(input('please enter your weight input in kg:'))
bmi = weight/height**2
print("bmi:")
print(bmi)
if (input == 'bmi'):
    
 if (bmi < 18.5):
    print('your BMI is', bmi, 'which means you are underweight.')

elif bmi > 18.5 or bmi < 25:
    print('your BMI is', bmi, 'which means you are normal.')

elif bmi > 25 or bmi < 30:
    print('your BMI is', bmi, 'which means you are overweight.')

elif bmi > 30:
    print('your BMI is', bmi, 'which means you are obese')

else:
    print('there is an error in your input, try again.')

