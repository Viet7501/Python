def extract_characters(*file):

    with open("file3.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(c)

extract_characters('file3.txt')