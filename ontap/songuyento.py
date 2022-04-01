def songuyento(n):

    count = 0
    if n <= 0:
        return 'Khong phai so nguyen to'
    else:
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
    if count <= 2:
        return 'So nguyen to'
    else:
        return 'Khong phai so nguyen to'

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

print(songuyento(10))
print(songuyento(7))