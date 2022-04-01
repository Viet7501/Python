'Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi'

s = input('Nhập chuỗi s: ')
chuoimoi=""

for i in range(0,len(s)):
    if s[i].isupper():
        chuoimoi += s[i].lower()
    else:
        chuoimoi += s[i].upper()
print(chuoimoi)

