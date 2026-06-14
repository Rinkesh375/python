# Reverse a String
# Problem: Reverse a string using a loop.


string = input("String to reverse string=")
length = len(string)-1
reverseStr = ""
for i in range(length,-1,-1):
    reverseStr += string[i]


print(reverseStr)
print(string[::-1])

# string[start:stop:step]
# string[::-1]

