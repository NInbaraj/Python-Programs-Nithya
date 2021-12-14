'''
Calculating the BMI using class
'''
class bmi:

    def bmi_input(self):
        self.height = float(input('Your height in inches: '))
        self.weight = float(input('Your weight in pounds: '))
    

    def calculate_bmi(self):
    
        self.bmi = float(self.weight/(self.height*self.height))*703
        print('Your BMI is:',self.bmi)
        return self.bmi

        
            
    def bmi_index(self):
        if self.bmi <= 16.0:
            print('You are Severely Underweight')
        elif self.bmi <= 18.4:
            print('You are Underweight')
        elif self.bmi <= 24.9:
            print('You are Normal')
        elif self.bmi <= 29.9:
            print('You are Overweight')
        elif self.bmi <= 34.9:
            print('You are Moderately Obese')
        elif self.bmi <= 39.9:
            print('You are Severely Obese')
        elif self.bmi > 39.9:
            print('You are Morbidly Obese')

bmi_object=bmi()
bmi_object.bmi_input()
bmi_object.calculate_bmi()
bmi_object.bmi_index()






