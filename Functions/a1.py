def GCD(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
              
    return gcd

GCD(48,72)

'''Output
24
'''