# Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.



n = int(input("Enter a number: "))

for x in range(1, 11):
    if x != 5:
        print(f"{n} x {x} = {n * x}")

