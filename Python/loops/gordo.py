primes = []
for num in range(1, 101):
    if num == 1:
        print(num)
    elif num == 2 or num == 3 or num == 5 or num == 7:
        print('Primo')
        primes.append(num)
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        print('Primo')
        primes.append(num)
    elif num % 3 == 0 and num % 5 == 0:
        print('TriCin')
    elif num % 3 == 0:
        print('Tri')
    elif num % 5 == 0:
        print('Cin')
    else:
        print(num)

# this is only to check if the primes printed above are correct and are complete
print(primes)
