def if_palindrome(data):
    if type(data) != str:
        print("Wrong data")
    elif " " in data:
        print("Wrong data")
    elif data.isnumeric() == True :
        print("Wrong data")
    else:
        result = data[::-1].lower() == data.lower()
        print(result)

if_palindrome("kajak")
if_palindrome("kanapka")
if_palindrome("Kajak")
if_palindrome("kebab")
if_palindrome("cIViC")
if_palindrome(10)
list = ("kajak", "kanapka")
if_palindrome(list)
if_palindrome("Kajak spada z przyczepy")
if_palindrome("123")
