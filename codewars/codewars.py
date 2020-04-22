def number2(bus_stops):
    enters = 0
    outs = 0
    for enter, out in bus_stops:
        enters += enter
        outs += out

    return enters - outs


def number(bus_stops):
    return sum(enter - out for enter, out in bus_stops)


def printer_error2(s):
    err = 0
    for ch in s:
        if ord(ch) not in range(ord('a'), ord('n')):
            err += 1
    return '{1}/{0}'.format(len(s), err)

def printer_error(s):
    err = sum([1 for ch in s if ord(ch) not in range(ord('a'), ord('n'))])
    return '{}/{}'.format(err, len(s))

def create_phone_number(n):
    r = ''.join(str(i) for i in n)
    a = r[:3]
    b = r[3:-3]
    c = r[-3:]
    return '({}) {}-{}'.format(a, b, c)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))