#Get 2 persons salary and calculate the sum of the salaries

person1 = int(input('Enter the salary of person 1 ='))
person2 = int(input('Enter the salary of person 2 ='))
print('The salary of Person 1 and Person 2 is', person1, person2)
sum = int(person1) + int(person2)
print('The total salary is', sum)
if sum>2500:
    print('It is a good salary')
