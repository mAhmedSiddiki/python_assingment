def get_indices(nums_list, n):
	return [idx for idx, i in enumerate(nums_list) if i == n]


print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices([1, 5, 5, 2, 7], 5))
print(get_indices([1, 5, 5, 2, 7], 8))
