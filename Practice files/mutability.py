def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        if lst[idx] == target:
            lst[idx] = swap_value

lst = ["tim", "is", "great", "tim", "tim", "tim"]
replace(lst, "tim", "tim")
print(lst)