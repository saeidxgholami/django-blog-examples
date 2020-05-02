def array_diff(a, b):
	r = []
	for i in a:
		for j in set(b):
			if i != j:
				r.append(i)

	print(r)


def array_diff(a, b):
	for i in set(b):
		c = a.count(i)
		for _ in range(c):
			a.remove(i)
	print(a)


def duplicate_count2(text):
	# count each char
	# if char number is bigger than one inc num of duplicate
	x = []
	text = text.lower()
	uniq = set(text)
	for ch in uniq:
		x.append(text.count(ch))
	print(x)
	
	number_of_duplicate = 0
	for i in x:
		if i > 1:
			number_of_duplicate += 1
	print(number_of_duplicate)


def duplicate_count(text):
	chars_count = {}
	text = text.lower()

	for ch in text:
		if ch in chars_count:
			chars_count[ch] += 1
		else:
			chars_count[ch] = 1
	print(chars_count)

	num_of_dup = 0
	for count in chars_count.values():
		if count > 1:
			num_of_dup += 1

	print(num_of_dup)


def duplicate_count(text):
	n = 0
	for ch in set(text.lower()):
		if text.lower().count(ch) > 1:
			n += 1
	print(n)


def delete_nth(nums, mx):
	set_nums = set(nums)
	r = []
	for n in set_nums:
		count = nums.count(n)
		print(n, count)
		if count > mx:  # find a number occurence bigger than m
			# keep the n mx-1 times
			pass
		else:
			pass

def delete_nth(nums, mx):
	from collections import Counter
	r = []
	for n in nums:
		if r.count(n) < mx:
			r.append(n)
	print(r)

def delete_nth(nums, mx):
	pass
delete_nth([1,2,3,2,3,2,1,1,2], 2)  # [1, 2, 3, 2, 3, 1]
delete_nth([1,1,3,3,7,2,2,2,2], 3) # [1, 1, 3, 3, 7, 2, 2, 2]

def delete_nth(nums, mx):
	r = []
	for n in nums:
		if r.count(n) < mx:
			r.append(n)
	return r