import random
import string

def generate_password(size):
	
	alphabets = string.ascii_letters
	digits = string.digits
	symbol = string.punctuation

	password = alphabets+digits+symbol
	gen_pass = "".join(random.sample(password,size))
	return gen_pass

size = int(input("Enter size of the password: "))
print(generate_password(size))
