import random

a = random.sample(range(1,30),12)
b = random.sample(range(1,30),16)
print("a: "+str(a))
print("b: "+str(b))
result = [i for i in a if i in b]
print(result)
