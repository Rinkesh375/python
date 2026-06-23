def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        print(
            f"calling: {func.__name__} with args {args_value} "
            f"and kwargs {kwargs_value}"
        )

        return func(*args, **kwargs)

    return wrapper



@debug
def example_func1():
    return


@debug
def example_func2(name,city,add,pincode):
    return 
    
    
example_func1()    
    
    
example_func2("Rinkesh","FBD",add="698",pincode=121005)    
    
    
    
    
    