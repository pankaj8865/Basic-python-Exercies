number = int(input("Enter a Number: "))
L = range(2,number+1)

list_of_divisors = []

for i in L:
    if number%i==0:
        list_of_divisors.append(i)
print(list_of_divisors)
