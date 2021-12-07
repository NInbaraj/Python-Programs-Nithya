'''
BMI program using Class and Objects
'''
class bmi:
    "Calculating BMI"

    def bmi_input(self):
        self.height = float(input('Your height in inches: '))
        self.weight = float(input('Your weight in pounds: '))

    def calculate_bmi(self):
        try:
            self.my_bmi = float(self.weight/(self.height*self.height))*703
            return self.my_bmi
        except Exception as e:
            print(e)

    def bmi_index(self):
        if self.my_bmi <= 16.0:
            print('You are Severely Underweight')

        elif self.my_bmi <= 18.4:
            print('You are Underweight')

        elif self.my_bmi <= 24.9:
            print('You are Normal')

        elif self.my_bmi <= 29.9:
            print('You are Overweight')

        elif self.my_bmi <= 34.9:
            print('You are Moderately Obese')

        elif self.my_bmi <= 39.9:
            print('You are Severely Obese')

        elif self.my_bmi > 39.9:
            print('You are Morbidly Obese')

bmi_object = bmi()
bmi_object.bmi_input()
bmi_object.calculate_bmi
bmi_object.bmi_index()

