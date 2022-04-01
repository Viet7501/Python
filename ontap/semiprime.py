import math
#
# def isSemiPrime(n):
#     l = []
#     i = 2
#     while n > 1:
#         if n % i == 0:
#             n = int(n / i)
#             l.append(i)
#         else:
#             i += 1
#     if len(l) == 0:
#         l.append(n)
#
#     them = []
#     for i in l:
#         if i > 2:
#             for j in range(2, i):
#                 if i % j == 0:
#                     return 0
#         them.append(i)
#
#     if len(them) == 2:
#         return True
#     else:
#         return False
#
# while True:
#     n = abs(int(input()))
#     if n <= 1000000000:
#         break
# print(isSemiPrime(n))
#

def isSemiPrime(num):
    num = math.fabs(num)
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break
    if(num > 1):
        cnt += 1
    return cnt == 2

n = int(input())
print(isSemiPrime(n))