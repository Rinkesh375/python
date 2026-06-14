# https://youtu.be/v9bOWjwdTlg?t=18898



age = int(input("What is your age = "))

if age < 0:
    print("Invalid age")
elif age >= 60:
    print("Senior")
elif age >= 20:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")