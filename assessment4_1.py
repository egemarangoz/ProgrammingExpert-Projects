"""
Assessment 4.1 - Positive Even Squares

Write a function that accepts any number of positional arguments, all of which you may assume will be lists of integers.
Your function should filter all of these lists such thatthey only contain even positive integers and combine all of the lists
into one list of integers. Your function should then modify the combined list such that it contains the squares of all the elements
and return that list.

Use a combination of "map", "filter" and "lambda" functions/keywords to modify the lists.
"""

def positive_even_squares(*args):
    positive_even_nums = []

    for lst in args:
        filtered_list = filter(lambda x: x > 0 and x % 2 == 0, lst)
        positive_even_nums.extend(filtered_list)

    squares = map(lambda x: x ** 2, positive_even_nums)
    return list(squares)