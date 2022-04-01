"""
Viết hàm
        def body_mass_index(m, h)
để tính toán chỉ số bmi của một người với cân nặng m (kg), chiều cao h (m)
Viết hàm
        def bmi_information(m, h)
để đưa ra thông tin về chỉ số bmi cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
"""


def body_mass_index(m, h):
    return m / h ** 2


def bmi_information(m, h):
    bmi = body_mass_index(m, h)
    if bmi < 18.5:
        print('Gầy')
    elif 18.5 <= bmi <= 24.9:
        print('Bình thường')
    elif 25 <= bmi <= 29.9:
        print('Thừa cân')
    else:
        print('Béo phì')


bmi_information(40, 1.60)
bmi_information(71, 1.71)
bmi_information(100, 1.70)
bmi_information(80, 1.71)
