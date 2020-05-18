from collections import Counter



def scramble(s1, s2):
    for ch in s2:
        if ch not in s1:
            return False
    return True

def scramble(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    inter = s1.intersection(s2)
    print(inter)
    return inter == s2

def scramble(s1, s2):
    r = ''
    for ch in s2:
        if ch not in s1:
            return False
        else:
            r += ch
    print(r)
    return r == s1

# Solved but performance issue
def scramble(s1, s2):
    if len(s1) < len(s2): return False
    s1 = list(s1)
    for ch in s2:
        if ch not in s1:
            return False
        s1.remove(ch)
    return True

def scramble(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)

    for ch, count in c2.items():
        if ch not in c1:
            return False
        elif c1.get(ch) < count:
            return False
    return True

# Test area
print("Start testing ... ")
assert scramble('rkqodlw', 'world') ==  True
assert scramble('cedewaraaossoqqyt', 'codewars') == True
assert scramble('katas', 'steak') == False
assert scramble('scriptjava', 'javascript') == True
assert scramble('scriptingjava', 'javascript') == True
assert scramble('scriptjavx', 'javascript') == False
assert scramble('mgyycrnopbi', 'hmwvhfiuxaiqrnelcdq') == False
print("Pass all test")

print(
        scramble('rkqodlw', 'world'),
        scramble('mgyycrnopbi', 'hmwvhfiuxaiqrnelcdq'),
    )

