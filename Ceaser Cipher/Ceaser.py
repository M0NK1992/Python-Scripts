"""
This script is used to perform the ceaser encryption by shifting to the right for encryption.

"""

def encryption(number, string):
    """This function will encrypt the string passed and send the encrypted string back.
    
    Arguments:
        number {str} -- The number used to shift.
        string {str} -- The plain text to be deencryptedcrypted.
    """
    encryptedstring= ''
    for char in string:
        # Check for valid characters
        if ord(char)>=65 or ord(char)<=122:
            asciivalue = ord(char) + number

            # Check to see if the value is within range 
            if asciivalue <= 122:
                newchar= chr(asciivalue)
                encryptedstring = encryptedstring + newchar
            
            elif asciivalue > 122:
                asciivalue = asciivalue - 58
                newchar= chr(asciivalue)
                encryptedstring = encryptedstring + newchar

    print("\n Encrypted string: ",encryptedstring)


def decryption(number, string):
    """[summary]
    
    Arguments:
        number {int} -- The number used to shift.
        string {str} -- The encrypted string to be decrypted.
    """

    decryptedstring = ''

    for char in string:
        #Check for valid characters
        if ord(char)>=65 or ord(char)<=122:
            asciivalue = ord(char) + number

            # Check to see if the value is within range
            if asciivalue >= 65:
                newchar= chr(asciivalue)
                decryptedstring = decryptedstring + newchar
            
            elif asciivalue < 65:
                asciivalue = asciivalue + 58
                newchar= chr(asciivalue)
                decryptedstring = decryptedstring + newchar

    print("\n Decrypted string: ",decryptedstring)


if __name__ == "__main__":
    number = 0
    eord = 'z'
    while (number > 9 or number <= 0 ):
        number= int(input("\n Enter the number between 1 to 9 inclusive:"))

    while (eord != 'e' or eord != 'd' or eord != 'q'):
        eord = input("\n Enter e for encryption, d for decryption and q to quit:")
        if eord == 'e':
            string = input("\n Enter the text to be encrypted:")
            encryption(number,string)
        
        elif eord == 'd':
            string = input("\n Enter the encrypted string:")
            decryption(number, string)

        elif eord == 'q':
            print("Quiting!")
            break
        