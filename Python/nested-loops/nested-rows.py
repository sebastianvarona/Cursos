rows = int(input('Digit the # of rows: '))
collums = int(input('Digit the # of collums: '))


def tiktaktoe(rows, collums):
    if rows <= 30 and collums <= 108:
        for r in range(1, rows+1):
            if r % 2 != 0:
                for c in range(1, collums+1):
                    if c < collums:
                        if c % 2 != 0:
                            print(' ', end="")
                        else:
                            print('|', end="")
                    else:
                        if c % 2 != 0:
                            print(' ')
                        else:
                            print('|')
            else:
                print('-'*collums)
        return True
    else:
        for r in range(1, rows+1):
            if r % 2 != 0:
                for c in range(1, collums+1):
                    if c < collums:
                        if c % 2 != 0:
                            print(' ', end="")
                        else:
                            print('|', end="")
                    else:
                        if c % 2 != 0:
                            print(' ')
                        else:
                            print('|')
            else:
                print('-'*collums)
        return False


tiktaktoe(rows, collums)
print(tiktaktoe(rows, collums))
