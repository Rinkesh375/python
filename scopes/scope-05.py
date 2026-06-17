def chaicoder(num):
    def actual (x):
        return x ** num
    return actual


print(chaicoder(3)(4))