# Hash Generator


def generate_hashtag(s):
	s = s.strip()
	result = ''
	if s != '' and len(s) < 140:
		words = s.strip().split(' ')
		for word in words:
			if word != '':
				word = word.lower()
				word = word[0].upper() + word[1:]
				result += word
		return '#' + result
	return False


def generate_hashtag(s):
	

print(
	generate_hashtag(''),   # -> False
	generate_hashtag('Codewars      '), #-> '#Codewars'
	generate_hashtag('Codewars Is  Nice'), #-> '#Codewars'
	generate_hashtag('c i n'), #-> '#Codewars'
	generate_hashtag('CodeWars is   nice'), #-> '#Codewars'
)


