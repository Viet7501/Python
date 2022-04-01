'''
Viết chương trình đếm số lần xuất
hiện các từ đơn trong một đoạn văn bản
'''

van_ban = "A short paragraph might be only two or three sentences long. Paragraph length, however, is relative to the surrounding paragraphs. If your document contains much longer paragraphs, a paragraph of five or six sentences might be considered short. Identify the main idea of your paragraph."
tach = van_ban.split()
so_lan_xuat_hien = {}

for i in tach:
    if i in so_lan_xuat_hien:
        so_lan_xuat_hien[i] += 1
    else:
        so_lan_xuat_hien[i] = 1

print(so_lan_xuat_hien)