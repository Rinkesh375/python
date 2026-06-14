items = ["apple", "banana", "orange", "apple", "mango"]

seen = set()

for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break

    seen.add(item)
else:
    print("All elements are unique")









items = ["apple", "banana", "orange", "apple", "mango"]

visited = {}

for item in items:
    if item in visited:
        print("Duplicate found:", item)
        break

    visited[item] = True
else:
    print("All elements are unique")





items = ["apple", "banana", "orange", "apple", "mango"]

if len(items) == len(set(items)):
    print("All elements are unique")
else:
    print("Duplicate exists")    
        