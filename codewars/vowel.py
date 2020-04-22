test_str = 'abraciiadabra'
t = 0
for vowel_ch in ['a', 'e', 'i', 'o', 'u']:
	t += test_str.count(vowel_ch)

print(t)