'''
Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu
từ dict ban đầu theo tập các key cho trước
Ví dụ:
dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
Output: {'name': 'Kelly', 'salary': 8000}
'''
sample = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
result = {k: sample[k] for k in keys}
print(f'Kết quả của bài toán {result}')


'Cách này không tổng quát'
# person_dict = {
#     'Name': 'Jason',
#     'Age': 27,
#     'Salary': 5000,
#     'City': 'Iowa City'
# }
#
# my_dict = {
#     'Name': '',
#     'Age': ''
# }
#
# my_dict['Name'] = person_dict['Name']
# my_dict['Age'] = person_dict['Age']
#
# print('dict mới sau trích xuất key "Name" và "Age" là: ')
# print(my_dict)