def descending_order(num):
    x = int(''.join(sorted(str(num), reverse=True)))
    print(x)
    return x

# assert descending_order(21445) == 54421
# assert descending_order(123456789) == 987654321
# descending_order(21445)# == 54421
# descending_order(123456789)# == 987654321

def disemvowel(string):
    result = ''
    for ch in string:
        if ch in 'aeiouAEIOU':
            continue
        result += ch
    return result

def disemvowel(string):
    return ''.join(ch for ch in string if ch not in "aeiouAEIOU")
    
assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"

x = disemvowel('hello world')
print(x)