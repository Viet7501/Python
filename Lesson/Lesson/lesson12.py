"""
        Exception
           - Handling
           - Except clause
           - try-finally clause
"""

""" 
    Python errors và Built-in Exception
    
        - Syntax/Parsing errors: Lỗi do không tuân theo cú pháp của ngôn ngữ
        - Logical errors (Exceptions): Lỗi xảy ra trong thời gian chạy (sau khi qua kiểm tra cú pháp)
        
Ví dụ:
    -   Cố tình mở 1 file chưa có lên để đọc - FileNotFoundError
    -   Cố tình chia cho 0 - ZeroDivisionError
    -   Cố tình import module không tồn tại - ImportError
    -   Cố tình ép kiểu không đúng - ValueEError
"""

# x = 1/0
# print(x)

# a = int(input('Nhập số: '))
# print(a)


random_list = ['a', 0, 0.5, 1]
for item in random_list:
    try:
        print(f'Phần tử: {item}')
        r = 1 / int(item)
        print(f'Nghịch đảo của {item} là {r}')
    except:
        pass

try:
    # Code gì đó có thể gây exception
    pass

except ValueError:
    # Xử lý nếu như exception loại ValueError xảy ra
    pass

except (TypeError, ZeroDivisionError):
    # Xử lý nếu như gặp nhiều exceptions cùng lúc
    pass

except:
    # Xử lý tất cả các loại exceptions khác 3 loại trên
    pass

"Raising"

# try:
#     a = int(input('Nhập một số nguyên dương: '))
#     if a <= 0:
#         raise ValueError('Số vừa nhập không phải số nguyên dương!')
#
# except ValueError as ve:
#     print(ve)


"""     Câu lệnh: try-finally 
    - Câu lệnh try đi kèm với câu lệnh finally thì các câu lệnh trong khối finally
    sẽ luôn được thực thi dù có chuyện gì đi nữa!
    - Các câu lệnh trong finally thường dùng để giải phóng tài nguyên cho phần đang chạy
"""

try:
    a = int(input('Nhập một số nguyên dương: '))
    if a <= 0:
        raise ValueError('Số vừa nhập không phải số nguyên dương!')

except ValueError as ve:
    print(ve)
finally:
    print('Finally')

"""     File 
    - Open, Read, Write, Close File
"""

""" 
File
    Là nơi trên ổ cứng lưu trữ các thông tin liên quan nhau
    Dùng để lưu trữ vĩnh viễn dữ liệu trong bộ nhớ dài hạn
    RAM là bộ nhớ ngắn hạn, sẽ mất dữ liệu khi mất điện => Dùng file để lưu dữ liệu lại cho xử lý sau này
    Để thao tác vào file cần phải mở nó ra trước, sau khi thao tác (đọc hoặc ghi) thì cần đóng nó lại
    
Quy trình thao tác với file như sau:
    Bước 1. Mở file => Bước 2. Đọc hoặc ghi (thực hiện thao tác) => Bước 3. Đóng tệp
"""

""" 
Open file
    Python cung cấp hàm open(), hàm trả lại một file object
    Định nghĩa đầy đủ của hàm
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
"""

with open('G:/Python/Lesson/Hello.txt', mode='w', encoding='utf-8') as f:
    f.write('Hello\n')
    f.write('this line - 2')
    print(f.read)

with open('G:/Python/Lesson/Hello.txt', mode='r', encoding='utf-8') as f:
    print(f.read())