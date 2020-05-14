# Find anagram

def anagrams(word, words):
	set_word = set(word)

	flag = False
	res = []

	for w in words:
		for ch in set(w):
			if ch not in set_word:
				flag = False
				break
			else:
				flag = True
		if flag and len(w) == len(word):
			res.append(w)

	return set(res)

def anagrams(word, words):
	r = []
	for w in words:
		if set(word) == set(w):
			r.append(w)
	return r


def anagrams(word, words):
	return [w for w in words if set(word) == set(w)]
# 'abcd', 'bbaa', 'dada'
x = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) #['aabb', 'bbaa']
y = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) # -> ['carer', 'racer'])
print(x, '\n', y)
