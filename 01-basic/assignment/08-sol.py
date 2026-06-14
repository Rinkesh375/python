#  Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


dic = {}
string = input("Give string=")

for ch in string:
    if (ch in dic):
        dic[ch] += 1
    else:
        dic[ch] = 1


for key in dic:
    if (dic[key] == 1):
        print(key)
        exit()


print("No non-repeated character found.")        





for ch in string:
    if (string.count(ch) == 1):
        print(f"First repeated charact={ch}")
        exit()


print("No non-repeated character found.")  








charCount = {}

# Count occurrences of each character
for ch in string:
    charCount[ch] = charCount.get(ch, 0) + 1

# Find the first character that appears only once
for ch in string:
    if charCount[ch] == 1:
        print("First non-repeated character =", ch)
        break
else:
    print("No non-repeated character found.")
    


    

