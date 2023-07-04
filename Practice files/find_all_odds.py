def find_all_odds(lst):
    # Write your code here.
    odd_lst = []
    for i in lst:
        if lst[i] % 2 == 1:
            odd_lst.append(lst[i])
        return odd_lst

lst = [1, 2, 3, 4, 5, 6, 5, 5, 3, 2]
finallist = find_all_odds(lst)
print(finallist)
