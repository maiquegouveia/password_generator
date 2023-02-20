import random


# A function to shuffle all the characters of the password
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# A function to generate a random uppercase letter
def generateRandomUppercaseLetter():
    return chr(random.randint(65, 90))

# A function to generate a random lowercase letter
def generateRandomLowercaseLetter():
    return chr(random.randint(97, 122))

# A function to generate a random number from 0 to 9
def generateRandomNumber():
    return str(random.randint(0, 9))

# A function to generate a random punctuation sign
def generatePunctuationSign():
    # Choose the signs you want
    # https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf
    signs = [35, 36, 38, 64]
    return chr(random.choice(signs))

password = ''
for i in range(5):
    password += generateRandomUppercaseLetter()
    password += generateRandomLowercaseLetter()
    password += generateRandomNumber()
    password += generatePunctuationSign()

# Input
password = shuffle(password)

# Output
print(password)