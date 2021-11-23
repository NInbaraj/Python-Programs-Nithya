# Guess the number between 1 to 10
#Need to improve on this Program using While

num1 = int(input('Guess a number beween 1 to 10 '))
num2 =  int(input('Enter a number between 1 to 10 '))
if num1 == num2:
    print('You guessed the right number')
elif num1 > num2:
    print('Sorry! you guessed too low')
elif num1 < num2:
    print('Sorry! you guessed too high')

