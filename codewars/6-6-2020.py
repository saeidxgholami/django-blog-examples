def get_middle(s):
    i = len(s) // 2

    if len(s) % 2 == 0:
        return s[i-1]+s[i]
    return s[i]
def get_middle(s):
    return s[len(s)//2 - 1:len(s)//2 + 1] if len(s) % 2 == 0 else s[len(s) // 2]

# assert get_middle("test") == "es"
# assert get_middle("testing") == "t"
# assert get_middle("A") == "A"


def high_and_low(numbers):
    nums_str = numbers.split()
    nums = [int(n) for n in nums_str]
    mx = max(nums)
    mn = min(nums)
    return '{} {}'.format(mx, mn)



def high_and_low(numbers):
    nums = [int(n) for n in numbers.split()]
    return '{} {}'.format(max(nums), min(nums))


def high_and_low(numbers):
    nums = [int(n) for n in numbers.split()]
    return '{} {}'.format(sorted(nums)[-1], sorted(nums)[0])



# assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
# # high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") #"542 -214"


def square_digits(num):
    res = ''
    for ch in str(num):
        n = int(ch)
        res += str(n ** 2)

    return int(res)

def square_digits(num):
    res = ''
    for ch in str(num):
        res += str(int(ch) ** 2)

    return int(res)

assert square_digits(9119) == 811181


# my own thing for testing purpose
def reverse_num(number):
    digits = []
    i = 0
    while number > 0:
        digits.append(number % 10)
        number //= 10
    
    print(digits)


