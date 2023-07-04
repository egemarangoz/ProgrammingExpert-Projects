"""
Assessment 2.2 - Caesar Cipher

Write a function that accepts a string and returns the caesar cipher encoding of a string according to a secondary input parameter named "offset".

The cipher encoding of a string involves shifting each character in the string a set number of position previous in the alphabet.
For example, if you were performing a caesar cipher of the string "tim" with "offset" = 2 you would get "rgk". "t" is shifted 
two positions to "r", "i" is shifted two positions to "g" and "m" is shifted two positions to "k".

In the situation where the shift of a character results in it being a position before "a", the positions wrap and the next character should be "z". 
For example, the caesar cipher of "ab" with "offset" = 2 would be "yz".

"offset" will always be a positive integer that is no greater  than 26 and the input string will only contain lowercase letters.

Sample input:
string = "hello"
offset = 3

Sample output:
"ebiil"

Sample input: 
string = "apple"
offset = 5

Sample output: 
"vkkgz"
"""

def caesar_cipher(string, offset):
    encoded_string = ""

    for character in string:
        diff = ord(character) - offset
        if diff  < 97:
            character = chr(122 - (97 - diff) + 1)
            encoded_string = encoded_string + character
        else:
            character = chr(ord(character) - offset)
            encoded_string = encoded_string + character
    
    return encoded_string

print(caesar_cipher("hello", 3))
print(caesar_cipher("apple", 5))
