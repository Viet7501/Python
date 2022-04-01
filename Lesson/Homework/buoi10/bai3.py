"""
Hãy nghĩ ra một đối tượng trong thực tế, tìm thuộc tính và
các hành vi của nó rồi xây dựng một class cho các đối tượng vừa nghĩ ra.
"""


class Vehicle:

    def __init__(self, loai_xe, nam_san_xuat, mau_xe, toc_do):
        self.loai_xe = loai_xe
        self.nam_san_xuat = nam_san_xuat
        self.mau_xe = mau_xe
        self.toc_do = toc_do
    def khoi_dong_xe(self):
        print(f'Bạn đang khởi động xe {self.loai_xe} {self.nam_san_xuat} - màu {self.mau_xe}')

    def di_chuyen(self):
        print(f'Xe {self.loai_xe} đang di chuyển')

    def dung_lai(self):
        print(f'Xe {self.loai_xe} đang không đi chuyển')

    def toc_do_hien_tai(self):
        print(f'Xe đang đi chuyển với tốc độ {self.toc_do} km/h')

    def tang_toc(self):
        print(f'Xe {self.loai_xe} đang tăng tốc')

    def giam_toc(self):
        print(f'Xe {self.loai_xe} đang giảm tốc')


car1 = Vehicle('Ferrari', 2020, 'đỏ', 50)
car1.khoi_dong_xe()
car1.tang_toc()
car1.toc_do_hien_tai()
car1.giam_toc()
car1.dung_lai()

print('')
car2 = Vehicle('Mercedes', 2018, 'xanh', 60)
car2.dung_lai()
car2.toc_do_hien_tai()