# Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
#        Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
# Input: A - mảng chứa id của mỗi bài hát
# Output: Độ dài cần tìm
# Example:
#     Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
#     => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]

A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
temp = []
for item in A:
    if item not in temp:
        temp.append(item)
print(f"Chuỗi dài nhất là {len(temp)} các bài hát liên tiếp")