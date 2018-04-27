import numpy as np
import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized verison:" + str(1000*(toc - tic)) +"ms")

c = 0
tic = time.time()
for i in range (1000000)
  c += a[i]*b[i]
toc = time.time()

print(c)
print("For loop:" + str(1000*(toc - tic)) +"ms")

u = np.exp(v)
u = np.log(v)
dw = np.zeros((n_x,1))
# n_x by 1

