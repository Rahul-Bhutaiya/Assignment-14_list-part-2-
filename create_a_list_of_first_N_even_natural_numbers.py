#Write a Python script to create a list of first N even natural numbers.

"""
list_1=[]
for x in range(int(input('Enter N Value : '))):
    list_1.append((x+1)*2)

print('List of First N Even Natural Numbers :',list_1)
"""

list_1=[(x+1)*2 for x in range(int(input('Enter N Value : ')))]
print('List of First N Even Natural Numbers :',list_1)