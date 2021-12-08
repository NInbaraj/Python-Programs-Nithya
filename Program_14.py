'''
Writing a program for
1. Accepting values into a list
2. Printing the list
3. Finding the max value
'''

num_list = []

def add_num_list():
    for i in range(5):
        number = int(input('Enter number: '))
        num_list.append(number)
    return num_list

def find_max_number():
    max_number = 0
    for number in num_list:
        if number > max_number:
            max_number = number
    return max_number
  
num_list = add_num_list()
print(num_list)

max_number = find_max_number()
print('The max number is: ', max_number)


