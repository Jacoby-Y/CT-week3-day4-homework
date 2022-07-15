# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.
# array1 = [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

# array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
# Output:
# [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

def move_zeroes(arr):
	zeroes = []
	nums = []
	for n in arr:
		if n == 0:
			zeroes.append(0)
		else:
			nums.append(n)

	return nums + zeroes
	# return [*nums, *zeroes]

print(move_zeroes([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]))
print([1, 7, 8, 10, 12, 4, 0, 0, 0, 0])