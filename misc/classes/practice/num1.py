def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

print num([1,2,3])
