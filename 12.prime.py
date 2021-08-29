def check_prime(num):
    half = (num//2)+1
    flag = 0
    i=2
    while i<=half:
        if num%i==0:
            flag =1
        i+=1

    if flag==1:
        print("number is not Prime")
    else:
        print("number is prime")

number = int(input("Enter a Number: "))
check_prime(number)
