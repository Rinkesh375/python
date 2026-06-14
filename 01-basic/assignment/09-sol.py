number = int(input("Give in me the number in 1 to 10 or until I keep or asking number="))

while (not(number>=1 and number<=10)):
    number = int(input("Give in me the number in 1 to 10 or until I keep or asking number="))

else:
    print(f"Number={number}")






number = int(input("Enter a number (1-10): "))

while not (1 <= number <= 10):
    number = int(input("Invalid! Enter a number (1-10): "))

print(f"Number = {number}")