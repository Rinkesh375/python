"""
========================================
DECORATORS - EXECUTION TIMER NOTES
========================================

1. What does @timer do?

@timer is a decorator.

Python converts:

    @timer
    def example_function():
        pass

into:

    def example_function():
        pass

    example_function = timer(example_function)

The original function is passed to timer() and
the returned wrapper function replaces the original function.

------------------------------------------------

2. What is func?

When Python executes:

    timer(example_function)

The original function is received in:

    def timer(func):

So:

    func = original example_function

------------------------------------------------

3. What is wrapper?

wrapper() is a new function created inside timer().

    def wrapper(*args, **kwargs):

It adds extra functionality before and after
the original function execution.

------------------------------------------------

4. Why use *args and **kwargs?

They allow wrapper() to accept any number of:

    *args   -> positional arguments
    **kwargs -> keyword arguments

Example:

    func(10)
    func(10, name="John")

Both work without changing wrapper code.

------------------------------------------------

5. Execution Flow

Code:

    @timer
    def example_function(n):
        time.sleep(n)

    example_function(5)

Actual Flow:

    example_function = timer(example_function)

    example_function(5)
            ↓
        wrapper(5)
            ↓
    start = time.time()
            ↓
    func(5)   # original function
            ↓
    time.sleep(5)
            ↓
    end = time.time()
            ↓
    print execution time

------------------------------------------------

6. What does time.time() return?

Returns current timestamp in seconds.

Example:

    start = 1000.25
    end   = 1005.25

Difference:

    end - start

Result:

    5.0 seconds

------------------------------------------------

7. What is func.__name__ ?

Returns the name of the original function.

Example:

    func.__name__

Output:

    "example_function"

------------------------------------------------

8. Why is output not exactly 5?

Output:

    example_function ran in 5.000374794006348 time

Because Python also takes a tiny amount of time
to execute instructions before and after sleep().

Therefore execution time is slightly more than 5 seconds.

------------------------------------------------

9. Final Output Explanation

    example_function ran in 5.000374794006348 time

example_function  -> function name
5.000374794006348 -> total execution time in seconds

------------------------------------------------

10. Decorator Memory View

Before decorator:

    example_function
            │
            ▼
    Original Function

After decorator:

    func
      │
      ▼
    Original Function

    example_function
            │
            ▼
        Wrapper Function

Calling:

    example_function()

actually calls:

    wrapper()

and wrapper internally calls:

    func()

------------------------------------------------

11. Common Uses of Decorators

✓ Measure execution time
✓ Logging
✓ Authentication
✓ Authorization
✓ Caching
✓ Input validation
✓ Retry mechanism
✓ Rate limiting

========================================
SHORT REVISION
========================================

@decorator
def my_func():
    pass

Internally:

    my_func = decorator(my_func)

- func = original function
- wrapper = new function
- wrapper replaces original function
- func(*args, **kwargs) executes original function
- Decorators add functionality without modifying original code

========================================
"""




import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper



@timer
def example_function(n):
    time.sleep(n)
    return "I am example function returned value"
    
    
#example_function = timer(example_function) return value will be example_function = wrappper
    
    
    
example_function(5) 
# now when I called this example_function(5)  internally wrapper got called with arguments 5,{}

print(example_function(5))

 