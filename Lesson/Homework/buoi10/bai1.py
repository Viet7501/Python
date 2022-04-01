"""
Mô phỏng lại trò chơi sau:
- Người chơi tung 2 con xúc xắc 6 mặt, các mặt có số chấm là: 1, 2, 3, 4, 5, 6
- Quan sát kết quả, tính tổng các mặt hướng lên sau khi 2 con xúc xắc đứng yên
- Lần đầu tiên,
    - Nếu tổng là 7 hoặc 11 => Người chơi THẮNG
    - Nếu tổng là 2, 3 hoặc 12 => Người chơi THUA
    - Nếu tổng là 4, 5, 6, 8, 9 hoặc 10 => Đây sẽ là ĐIỂM của người chơi, và sang vòng tiếp theo
- Để giành được THẮNG, người chơi tiếp tục tung 2 con xúc xắc cho đến khi ra được tổng = ĐIỂM trong lần đầu tiên;
 nếu tung ra được tổng = 7 => Người chơi THUA
"""

import random


class xuc_xac:

    def __init__(self):
        """
            Tung xúc xắc
        """
        self.xuc_xac1 = random.randrange(1, 7)
        self.xuc_xac2 = random.randrange(1, 7)
        self.total = self.xuc_xac1 + self.xuc_xac2

    def kiem_tra(self):
        """
            Kiểm tra tổng 2 xúc xắc
        """
        if self.total == 7 or self.total == 11:
            print(self.total)
            print('Bạn đã thắng')
        elif self.total == 2 or self.total == 3 or self.total == 12:
            print(self.total)
            print('Bạn đã thua')
        else:
            total = self.total
            print(total)
            print('Tiếp tục tung')
            while True:
                self.__init__()
                print(self.total)
                if total == self.total:
                    print('Bạn đã thắng')
                    break
                elif self.total == 7:
                    print('Bạn đã thua')
                    break


obj = xuc_xac()
obj.kiem_tra()
