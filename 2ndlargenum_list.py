'''
Write a python program to acceot numbers as input and find the 2nd largest number in a list
'''


num_list = []

#Adding numbers to a list
def add_num_list():
    for i in range(5):
        number = int(input('Enter number: '))
        num_list.append(number)
    return num_list

#Sorting the numbers in ascending order
def sort_list(my_list):

    for i in range(len(my_list)):

        for j in range(i+1, len(my_list)):

            if (my_list[i] > my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list


#Print the input list
num_list = add_num_list()
print(num_list)

#Print list sorted ascending
my_list = sort_list(num_list)
print('List sorted by Ascending number: ', my_list)

#Print the 2nd largest number in the list
number_2 = my_list[3]
print('The second largest number is: ', number_2)

