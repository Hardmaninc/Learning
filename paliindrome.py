word_to_check = input("What word do you want to check? \n")
def palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

word_reversed = word_to_check[::-1]
print(f"{word_to_check} is a palindrome: {word_reversed == word_to_check}")
