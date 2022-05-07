import string
import random


def createPassword():
    possibleChars = ""
    passwordLength = int(input("Length of Password? "))
    includeLetters = int(input("Include Letters? (1 for yes, 0 for no): "))
    includeNumbers = int(input("Include Numbers? (1 for yes, 0 for no): "))
    includeSpecialChars = int(input("Include Special Characters? (1 for yes, 0 for no): "))

    if includeLetters == 1:
        possibleChars = string.ascii_letters
    if includeNumbers == 1:
        possibleChars += string.digits
    if includeSpecialChars == 1:
        possibleChars += string.punctuation

    
    password = random.sample(possibleChars, passwordLength)
    return "".join(password)
    
    


print(createPassword())
