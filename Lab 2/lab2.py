"""
This function gets the input of a filename from a user abd returns filename. 
"""

def getInputFile():
    filename = input("Enter the input filename: ")
    while filename[-4:] != ".txt":
        filename = input("Invalid filename extension. Please re-enter the input filename: ")
    return filename

"""
This function uses ascii to shift each letter to the right by 5. It decrypts the message.
It uses the paramater filename to decrypt each message.
"""

def decrypt(filename):
    file = open(filename, "r")
    alpha = int(file.readline().strip()) # Reads the first line of the txt file
    encrypted = file.readline().strip() # Reads the second line of the txt file
    file.close()
    words = encrypted.strip()
    decrypted_msg = ""
    alpha = alpha % 26
    for word in words:
        for character in word.lower():
            if "a" <= character <= "z":
                ascii = ord(character) - alpha
                if ascii < ord("a"):
                    ascii = ord("z") - (ord("a") - ascii - 1)
                character = chr(ascii)
            decrypted_msg += character
        decrypted_msg += ""
    return decrypted_msg.strip()

def main():
    filename = getInputFile()
    decrypted_msg = decrypt(filename)
    print(decrypted_msg)

main()