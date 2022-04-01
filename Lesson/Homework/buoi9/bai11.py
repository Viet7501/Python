"""
Thực hiện code lại hàm sau và cho biết ý nghĩa của nó
def enter_data():
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")
"""


def enter_data():
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")


enter_data()
''' Kiểm tra xem chuỗi vừa nhập có phải ký tự số và là số nguyên dương hay không
    -   Nhập n từ bàn phím
    -   Do nhập dưới <class 'str'> -> check xem dữ liệu đã nhập có phải số không
        n.isnumeric() : kiểm tra xem trong chuỗi chỉ chứa ký tự số hay không, nếu đúng trả True, sai thì False
    -   nếu n.isnumeric() trả giá trị True
            -> ép kiểu n thành <class 'int'>
            -> kiểm tra nếu n > 0: print("Đã nhập số dương")
            -> return n  #Bỏ qua print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
    -  Nếu n.isnumeric() trả giá trị False
            -> print("Dữ liệu đã nhập không phải số nguyên")
    
    Ví dụ:
    nhập n = 5 -> n.isnumeric() True -> n > 0 True -> print("Đã nhập số dương") -> return n
    nhập n = -5 -> n.isnumeric() False -> print("Dữ liệu đã nhập không phải số nguyên")
'''
