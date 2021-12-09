'''
1. Write a python Program to accept values in a listG
2. Get the difference between the maximum value and minimum value
'''

# Finding the Max number
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

def sort_list(my_list):

    for i in range(len(my_list)):

        for j in range(i+1, len(my_list)):

            if (my_list[i] > my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list



num_list = add_num_list()
print(num_list)

max_number = find_max_number()
print('The highest number is: ', max_number)

my_list = sort_list(num_list)
print('List sorted by Ascending number: ', my_list)

#Calculating the difference between the largest and least
diff = my_list[4]-my_list[0]

print('The smallest number is: ', *my_list[:1]) 
print('The difference is: ', diff)

