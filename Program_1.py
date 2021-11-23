#Calculate the BMI of a Person

#Give the appropriate message for BMI values

height = float(input('Your height in inches: '))
weight = float(input('Your weight in pounds: '))
bmi = float(weight/(height*height))*703
if bmi <= 16.0:
    print('Your BMI is: ', bmi, 'You are Severely Underweight')
elif bmi <= 18.4:
    print('Your BMI is: ', bmi, 'You are Underweight')
elif bmi <= 24.9:
    print('Your BMI is: ', bmi, 'You are Normal')
elif bmi <= 29.9:
    print('Your BMI is: ', bmi, 'You are Overweight')
elif bmi <= 34.9:
    print('Your BMI is: ', bmi, 'You are Moderately Obese')
elif bmi <= 39.9:
    print('Your BMI is: ', bmi, 'You are Severely Obese')
elif bmi > 39.9:
    print('Your BMI is: ', bmi, 'You are Morbidly Obese')
    





 

