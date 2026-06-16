def keyValue(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")



keyValue(name="Rinkesh",city="FBD",pincode="12005")