def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


result = even_generator(50)
print(result)
for num in result:
    print(num)