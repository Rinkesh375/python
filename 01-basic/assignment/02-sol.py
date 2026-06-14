weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

todayDay = input("Give me today's day = ").capitalize()

age = int(input("Your age in numbers = "))

if age < 0:
    print("Invalid age")

elif todayDay not in weekDays:
    print("Please provide a valid day")

else:
    #age 18 or above price 12 else 8
    price = 12 if age >= 18 else 8

    # Wednesday discount
    if todayDay == "Wednesday":
        price -= 2

    print("Price = ${}".format(price))

