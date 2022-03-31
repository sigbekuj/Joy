""" Program to decode and encode user inputs  """

# function to encode user input
def encode():
    string,s = input("Enter the string to be encoded: "),int(input("Enter the shift value: "))
    outcome = ""
    for i in range(len(string)):
        characters = string[i]
        if (characters.islower()):
            outcome += chr((ord(characters) + s - 97) % 26 + 97)
        else:
            outcome += characters        
    print("Your encrypted string: ",outcome)

#Function to decode user input           
def decode():
    message = input("Enter the string to be decoded: "), input("Enter the word from plainstring: ")
    string = input("Enter the word from plainstring: ")
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        if s in translated:
            break
    print('The encryption key is: %s\n Plainstring: %s' % (key, translated))

while(True):
    ch = input("\nEnter \n'e' to encrypt\n'd' to decrypt\n'q' to quit:\n") #displaying all the options
    if ch=='e' :
        encode()
    elif ch =='d':
        decode()
    elif ch =='q':
        break
    else:
        print("Try again: ")






