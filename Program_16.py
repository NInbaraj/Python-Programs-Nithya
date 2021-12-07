#Program to find all numbers between 2000 & 3200 that are divisible by 7 and not multiples of 5

output = []

def numbers():
    for i in range(2000,3200):
        if i%7==0 and i%5!=0:
            output.append(i)
    return output

output = numbers()
print(output)
