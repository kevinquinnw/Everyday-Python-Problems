k, q = 1, 1 
total = 0 
while k <= 4000000:
    if k % 2 == 0:
        total += k
    k, q = q, k + q
print (total)