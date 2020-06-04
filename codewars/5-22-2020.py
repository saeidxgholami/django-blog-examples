# Strings Mix
from collections import Counter

# counte each latter of the strings
# print string:biggest number/=:chars
# 2:yyyy/1:nnn/=:mm

def mix(s1, s2):
	c1 = Counter(s1)
	c2 = Counter(s2)
	print(c1)
	print(c2)
	d = {}
	r = ''
	for k, v in c1.items():
		if k in c2:
			if v > c2[k]:
				d[k] = v
				r += 
			elif v < c2[k]:
				d[k] = c2[k]
			else:
				d[k] = v

	d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
	d.pop(' ')
	print(d)


mix("Are they here", "yes, they are here")  # "2:eeeee/2:yy/=:hh/=:rr"