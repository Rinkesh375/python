def outer(cb):
    cached_square_of_arguments = {}
    
    def inner(a):
        print(cached_square_of_arguments)
        if (a in cached_square_of_arguments):
            return f"value from cached {cached_square_of_arguments}"
        else:
            result =  cb(a)
            cached_square_of_arguments[a] = result
            return f"Value from {cb.__name__} {result}"
        
    return inner





@outer
def square_calculator(a):
    return a**2


print(square_calculator(1))
print(square_calculator(2))

print(square_calculator(3))

print(square_calculator(4))
print(square_calculator(3))
print(square_calculator(2))
print(square_calculator(5))

