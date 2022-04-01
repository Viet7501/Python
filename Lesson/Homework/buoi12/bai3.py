def hoan_function():
    try:
        print('Monday')
    finally:
        print('Sunday')
hoan_function()

try:
    print("throw")
except:
    print("except")
finally:
    print("finally")