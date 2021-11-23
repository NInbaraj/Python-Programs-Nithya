#Use Def to reduce the number of lines in the Program
#Adding values in a list. Create multiple lists with string, float and interger values

my_string_list = []
my_float_list = []
my_integer_list = []

for i in range(5):
    my_string_value = str(input('Enter the string: '))
    my_string_list.append(my_string_value)
    print('My string list is: ', my_string_list)

for i in range(5):
    my_float_value = float(input('Enter the float value: '))
    my_float_list.append(my_float_value)
    print('My float list is: ', my_float_list)

for i in range(5):
    my_interger_value = int(input('Enter the integer value: '))
    my_integer_list.append(my_interger_value)
    print('My integer list is: ', my_integer_list)
