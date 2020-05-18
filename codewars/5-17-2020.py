def make_readable(seconds):
    s = int(seconds % 60)
    seconds /= 60
    m = int(seconds % 60)
    seconds /= 60
    h = int(seconds)
    d = {'hour': h, 'minute': m, 'second': s}
    r = "{hour:0>2}:{minute:0>2}:{second:0>2}".format(**d)
    print(r)

make_readable(86399)  # "23:59:59"
make_readable(0)  # "23:59:59"
make_readable(359999)  # "23:59:59"