# Stripe comments
def solution(string,markers):
    r = ''
    for line in string.split('\n'):
        for ch in line:
            if ch not in markers:
                r += ch
            # found a marker, we need to skip marker position until the end of lien.
            else:
                break
        r = r.strip()
        r += '\n'
    if r == '': 
        return '\n'
    return r[:-1]


print('Test case\n------------\n')

# -> "apples, pears\ngrapes\nbananas"
# solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) 
# assert solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas"
# solution("a #b\nc\nd $e f g", ["#", "$"]) # -> "a\nc\nd"
x = solution('apples lemons avocados apples avocados\n# lemons\n- oranges strawberries\noranges bananas @ pears bananas apples', ['#', '=', '@'])
# 'apples lemons avocados apples avocados\n\n- oranges strawberries\noranges bananas'
print(x.__repr__())