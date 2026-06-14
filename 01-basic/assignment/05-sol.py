# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a number: "))

sumEven = 0

for num in range(2, n + 1, 2):
    sumEven += num

print("Sum of even numbers:", sumEven)     
