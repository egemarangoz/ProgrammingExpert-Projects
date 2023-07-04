"""
Assessment 2.5 - Pairs Sum to Target

Write a function that accepts two lists(list1 and list2) of integers and a target integer named "target".
Your function should return all pairs of indices in the form [x, y] where
list1[x] + list2[y] == "target". In other words, return the pairs of indices where the sum of their
values equals "target".

list1 and list2 will always have the same number of elements and you may return the pairs in any order.
"""

def pairs_sum_to_target(list1, list2, target):
    list_of_pairs = []
    for elm1 in range(len(list1)):
        for elm2 in range(len(list2)):
            if list1[elm1] + list2[elm2] == target:
                list_of_pairs.append([elm1, elm2])
    
    return list_of_pairs

list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5

print(pairs_sum_to_target(list1, list2, target))