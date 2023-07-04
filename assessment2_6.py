"""
Assessment 2.6 - Create Strings from Characters

Write a function that accepts a dictionary called "frequencies" and two strings named "string1" and "string2". 
The "frequencies" dictionary contains character keys and integer values, the value associated with each character represents its frequency. 
Your function should return  0, 1 or 2 according to the cases below.

- Your function should return 2 if the frequency of characters in the dictionary is sufficient to create both string1 and string2 
without reusing any characters.

- Your function should return 1 if the frequency of characters in the dictionary is sufficient to create either string1 or string2 
without reusing any characters.

- Your function should return 0 if the frequency of characters in the dictionary is not sufficient to create either string1 or string2 
without reusing any characters.

Sample input:
frequencies = {
"h": 2,
"e": 1,
"l": 1,
"r": 1,
"a": 3,
"o": 2,
"d": 1,
"w", 1
}
string1 = "hello"
string2 = "world"

Sample Output:
# The string "world" can be created but "hello" cannot be.

Sample input #2:
frequencies = {
"h": 2,
"e": 1,
"l": 2,
"r": 4,
"a": 3,
"o": 2,
"d": 1,
"w", 1
}
string1 = "hello"
string2 = "world"

Sample output #2:
# The string "world" and "hello" can be created but they cannot both be created without reusing any characters.
# This is because there is not enough "l"s.
"""

#def create_strings_from_characters(frequencies, string1, string2):
#    for key in frequencies:
#       for character in string1:  
 