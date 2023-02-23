word = str(input("Please enter a word to check:"))
def is_it_palindrome(word):
    if(word == word[::-1]):
        return("Yes, it is palindrome")
    else:
        return("No, it is not palindrome")
print(is_it_palindrome(word))