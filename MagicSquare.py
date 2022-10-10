import numpy as np


import numpy as np
N  = 7
magicsquare = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
    magicsquare[i, j] = n
    n += 1
    a, b = (i-1) % N, (j+1)% N
    if magicsquare[a, b]:
        i += 1
    else:
        i, j = a, b

print(magicsquare)