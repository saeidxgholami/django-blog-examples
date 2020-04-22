def get_vowel(s):
	t = 0
	for ch in ['a', 'e', 'i', 'o', 'u']:
		t += s.count(ch)



def longest2(s1, s2):
	# Make s1 and s2 unique
	u_s1 = ''
	u_s2 = ''

	for ch1 in set(s1):
		u_s1 += ch1
	for ch2 in set(s2):
		u_s2 += ch2

	# Concatinate s1 and s2 and make them unique
	ss = u_s1 + u_s2
	u_ss = ''
	for ch3 in set(ss):
		u_ss += ch3
	
	return u_ss
	# Sort whole string.
	sorted_ss = sorted(u_ss)
	return ''.join(sorted_ss)


def longest(s1, s2):
	u_s = set(s1) | set(s2)
	ss = ''
	for c in u_s:
		ss += c
	sorted_ss = sorted(ss)
	return ''.join(sorted_ss)



# ab -> A-Bb
# xnz -> X-Nn-Zzz
def accum2(s):
	i = 0
	ss = ''
	while i < len(s):
		ss += ( s[i] * (i+1) ) + '-'
		ss = ss.title()

		i += 1

	print(ss[:-1])



def accum3(s):
	return '-'.join(c*(s.index(c)+1) for c in s).title()

# 853 M
def accum(s):
	return '-'.join(char*index for index, char in enumerate(s, 1)).title()


def find_it(seq):
    d = {}
    for n in seq:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    for item, number in d.items():
    	if number % 2 != 0:
    		return item


def tribonacci2(sig, n):
	r = [*sig]
	t = sig[:]
	for i in range(n-3):
		r.append(sum(t))
		t = r[-3:]
		
	return r


def tribonacci(sig, n):
	x = [*sig]
	r = [sum(x[-3:]) for i in range(n-3)]
	return r

print(tribonacci([1, 1, 1], 10))

def tribonacci(sig, n):
	r = [*sig]    
	t = sig[:]
	for i in range(n-3):
		r.append(sum(t))
		t = r[-3:]
		
	return r


