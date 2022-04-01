'''
Viết chương trình để sinh ra dict mới
từ list các dict có dạng như trong ví dụ
Ví dụ:
Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Output: {'item1': 1150, 'item2': 300}
'''


my_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

new_dict = {}

for i in my_list:
    if i['item'] not in new_dict:
        new_dict[i['item']] = i['amount']
    else:
        new_dict[i['item']] += i['amount']


print(new_dict)

