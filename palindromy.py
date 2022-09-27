def if_palindrome(data):
    if type(data) != str:
        return(False)
    elif " " in data:
        return(False)
    elif data.isnumeric() == True :
        return(False)
    else:
        result = data[::-1].lower() == data.lower()
        return(result)

assert if_palindrome("kajak")
assert not if_palindrome("kanapka")
assert not if_palindrome("kebab")
assert if_palindrome("cIViC")
assert not if_palindrome(10)
assert not if_palindrome("Kajak spada z przyczepy")
list = ("kajak", "kanapka")
assert not if_palindrome(list)
assert not if_palindrome("123")

