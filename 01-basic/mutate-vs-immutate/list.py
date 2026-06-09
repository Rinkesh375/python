# #  Array is called list in python

# mylist = [1,2,3,["a","b"],]


# # print(mylist)

# # print(mylist[3])

# # print(mylist[3][1])


# # print(len(mylist))


# print(mylist[len(mylist)-1])

# # see the output
# # print(mylist[len(mylist)])









# # "------------------------------------------------------------"

# list1 = [1,2]
# list2 = list1


# list1[0] = 101

# print(list1,list2)



# "------------------------------------------------------------"

# list1 = [1,2]
# list2 = list1


# list2[0] = 101

# print(list1,list2)



# # "------------------------------------------------------------"

# list1 = [1,2,3,4,5]


# # this will create a copy of all value in list2 from list1 it will be copy not reference
# list2 = list1[:]


# list1[0] = 101
# print(list1,list2)



# "------------------------------------------------------------"
import copy
list1 = [1,2,3,4,5]

# this is also inbulit method to create a copy
list2 =  copy.copy(list1)
list3 =  copy.deepcopy(list1)
list4 =  list1

list1[0] = 101
print(list1,list2)
print(list1 is list2, list1 == list2)

print(list1 is list4, list1 == list4)