lines = []

while (line := input('> ')) != ':exit':
	lines.append(line+'\n')

f = open('mynote.txt', 'w')
f.writelines(lines)
f.close()