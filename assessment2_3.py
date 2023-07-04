"""
Assessment 2.3 - Sort Employees

Write a function that accepts a list of lists that contains the name, age and salary of specific employees and also accepts a string
representing the key to sort employees by. Your function should return a new list that contains the lists representing each employee 
sorted in ascending order by the given key.

The string parameter named "sort_by" will always be equal to one of the following values: "names", "age" or "salary".

Sample input:
employees = 
[
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_by = "age"

Sample output:
employees =
[
    ["Sarah", 24, 75000],
    ["Connor", 25, 110000],
    ["Jason", 26, 55000],
    ["Josie", 29, 100000],
    ["John", 33, 65000]
]
"""

def sort_employees(lst, keyword):
    def sort_by_name(item):
        return item[0]
    
    def sort_by_age(item):
        return item[1]
    
    def sort_by_salary(item):
        return item[2]
    
    if keyword == "name":
        sorted_list = sorted(lst, key = sort_by_name)
    elif keyword == "age":
        sorted_list = sorted(lst, key = sort_by_age)
    elif keyword == "salary":
        sorted_list = sorted(lst, key = sort_by_salary)
    
    return sorted_list

employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_by = "salary"

print(sort_employees(employees, sort_by))