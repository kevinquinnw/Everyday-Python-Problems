def PrimeFactorization(k):
    primeFactor = 1
    q = 2 

    while q <= k / q:
        if  k % q == 0:
            primeFactor = q
            k /= q
        else:
            q += 1

    if primeFactor < k:
        primeFactor = k
    return primeFactor

print(PrimeFactorization(300))
print(PrimeFactorization(4854545))
print(PrimeFactorization(947584385))

        



    