'''
Viết chương trình tạo ra dict với lớn hơn 3 phần tử,
value của mỗi phần tử là một list có lớn hơn 5 phần tử. Truy cập
và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
'''

our_dict = {
    'ten' : ['Nam', 'Viet', 'Hung', 'Duy', 'Duc', 'Dung', 'Trang', 'Linh' ],
    'tuoi': [15, 16, 17, 18, 19, 20, 21, 22],
    'Dia chi': [56, 86, 454, 123, 345, 678, 333, 349],
    'so thich': ['hoc', 'choi', 'lam viec', 'bong ro', 'cau long', 'chup anh', 'bong da', 'game']
}

for i in our_dict:
    print(f'{i} : {our_dict[i][5]}')
