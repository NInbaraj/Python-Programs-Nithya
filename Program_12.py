#Repeating program11 using Def to minimize the number of in program
#Adding values in a list. Create multiple lists with string, float and interger values
my_list = []
my_string_list = []
my_float_list = []
my_integer_list =[]

def add_values_in_list():
    for i in range(5):
        my_value = input('Enter the value')
        my_list.append(my_value)
    return my_list

my_new_string = add_values_in_list()
print(my_new_string)
my_new_float = add_values_in_list()
print(my_new_float)
my_new_integer = add_values_in_list()
print(my_new_integer)




