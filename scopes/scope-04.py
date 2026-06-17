x = 100

def test():
    global x
    print(x)
    x = 40

test()
print(x)