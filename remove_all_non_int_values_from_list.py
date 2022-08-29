#Write a Python script to remove all non int values from a list.

list_1=[10,20,3.14,True,'kk',4+8j]
print('Original List :',list_1)

list_1=[x for x in list_1 if type(x)==int]
print('After Removing All-Non Int Values From List :',list_1)