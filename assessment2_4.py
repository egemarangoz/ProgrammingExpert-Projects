"""
Assessment 4 - Longest Unique Words

Write a function that accepts a list of strings that represent words and a positive integer n, representing the number of words to return. 
Your function should return a new list containing the n longest unique words from the input list. Words are unique if they only appear
one time in the input list.

There will always be exactly n words to return and you may return the words in any order.

Note: all strings in the input list should not contain any special characters or spaces.

Sample input:
words = [
'Longer',
'Whatever',
'Longer',
'Ball',
'Rock',
'Rocky',
'Rocky'
]
n = 3

Sample output:
[
'Whatever',
'Ball',
'Rock'
]
"""
def get_n_longest_unique_words(words, n):
    unique_words = []
    for element in words:
        if words.count(element) == 1:
            unique_words.append(element)
    
    unique_words.sort(key = len, reverse = True)
    n_unique_words = unique_words[0:n]
    
    return n_unique_words

words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
n = 3

print(get_n_longest_unique_words(words, n))
