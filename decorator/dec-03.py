def outer_func(cb):
    def inner_fun(*args):
        cb(args)
        print(cb.__name__)
        
    return inner_fun    
        
        
       
       
     
     
@outer_func
def print_name_arguments(arguments):
        print(arguments)  
        
        
print_name_arguments(1,2,3,4,5)        
        
        
        