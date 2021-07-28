a = 1
b = 2
c = 0


def checker(a, b, c):
    if str(a) == str(b):
        return True
    elif str(a) == str(c):
        return True
    elif str(b) == str(c):
        return True
    else:
        return False


print(checker(a, b, c))
