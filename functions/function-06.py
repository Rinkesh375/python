def greet(name="Guest"):
    if name is None:
        name = "Guest"
    return f"Hello {name}"

print(greet("Rinkesh"))
print(greet(None))
print(greet())