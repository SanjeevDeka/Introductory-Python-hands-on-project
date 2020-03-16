def cCipher(string, shift):
    encryptedMsg = ""
    if type(string) != str:
        return 'The input is not a string.'
    for character in string:
        if character.isalpha() == True:
            if character == character.lower():
                x = ord(character) - 97 
                x += shift
                x = x % 26
                encryptedMsg += chr(x + 97)                
            else:
                x = ord(character) - 65
                x += shift
                x = x % 26
                encryptedMsg += chr(x + 65)                
        else:
            x = ord(character)
            x += shift
            encryptedMsg += chr(x)           
    return encryptedMsg
print(cCipher("AbCd 1234 !@#$", 1))
print(cCipher('abc', 1))
print(cCipher('123', 3))
print(cCipher(44, 3))
print(cCipher('143Hg!)>#', 2))
print(cCipher("Here's 2 U MRS Robinson", 1))
