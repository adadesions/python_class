n = int(input('Pleses select you range:'))
def prime(x):
    if x > 1:
        x = n // 2
        for i in range(2, x + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False
if prime(n):
    print (n," is a prime number")
else:
    print (n," is a composite number")
