while True:
    epsilon = float(input("Nhập epsilon = "))
    if epsilon < 1 and epsilon > 0:
        break

fact_max = 1/epsilon
i = 1
factorial = 1
value_e = 1
while factorial <= fact_max:
    value_e += 1 / factorial
    i += 1
    factorial *= i
print('Giá trị của e = ', round(value_e,3))