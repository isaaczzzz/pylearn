# 斐波那契数列 UTF-8
import sys
n = int(input())
if n < 3:
    print("Input error!")
    sys.exit(0)
a = 1
b = 1
print(a)
print(b)
for i in range(3, n + 1):
    tmp = a
    a = b
    b = tmp + a
    print(b)

