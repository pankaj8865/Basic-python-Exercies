import random

def remove_dup_set(c):
    d = list(set(c))
    print(d)

def remove_dup_loop(c):
    d = []
    for i in c:
        if i not in d:
            d.append(i)
    print(sorted(d))


a = random.sample(range(1,10),5)
b = random.sample(range(1,10),5)
c = a+b
print(c) 
remove_dup_set(c)
remove_dup_loop(c)
