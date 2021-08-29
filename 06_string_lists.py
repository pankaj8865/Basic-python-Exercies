string = input("Enter a String: ")
string = string.lower()
rev = string[::-1]
if string==rev:
    print("string is palindrome")
else:

    print("string is not palindrome")
