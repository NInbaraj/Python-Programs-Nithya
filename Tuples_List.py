'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')
'''
num_list = []

def add_numbers():
    for i in range(6):
        numbers = str(input('Enter the number '))
        num_list.append(numbers)
        num_tuple = tuple(num_list)
    return num_tuple

num_tuple = add_numbers()
print('numbers')

print(num_list)
print(num_tuple)



