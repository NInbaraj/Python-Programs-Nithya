#Calculate the BMI of a Person USING FUNCTION
#Give the appropriate message for BMI values
# Calculated the BMI
#You have catogrized

#One function should get the input(height and weight)
#one function should calculate the bmi
#one function should tell me in which category the person comes under
def bmi_input():
    height = float(input('Your height in inches: '))
    weight = float(input('Your weight in pounds: '))
    return height,weight

def calculate_bmi(height,weight):
    bmi = float(weight/(height*height))*703
    bmi_index(bmi)
    print('Your BMI is: ', bmi)

def bmi_index(bmi):
    if bmi <= 16.0:
        print('You are Severely Underweight')
    elif bmi <= 18.4:
        print('You are Underweight')
    elif bmi <= 24.9:
        print('You are Normal')
    elif bmi <= 29.9:
        print('You are Overweight')
    elif bmi <= 34.9:
        print('You are Moderately Obese')
    elif bmi <= 39.9:
        print('You are Severely Obese')
    elif bmi >= 40:
        print('You are Morbidly Obese')
user_height,user_weight=bmi_input()
calculate_bmi(user_height,user_weight)
    



