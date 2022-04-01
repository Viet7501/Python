file1 = ""
file2 = ""

with open('Hello.txt') as f:
    file1 = f.read()

with open('Hi.txt') as f:
    file2 = f.read()

file1 += "\n"
file1 += file2

with open('file3.txt', 'w') as f:
    f.write(file1)