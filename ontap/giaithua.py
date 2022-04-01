def giaithua(n):
    if n <= 1:
        return 1
    else:
        return n * giaithua(n-1)

print(giaithua(10))