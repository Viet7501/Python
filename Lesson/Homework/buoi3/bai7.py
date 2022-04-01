'''
    Người dùng nhập vào số n - số hàng để in
    mô hình kim tự tháp số dạng dọc như ví dụ sau
'''

n = int(input("Nhập n: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print("")

for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print("")