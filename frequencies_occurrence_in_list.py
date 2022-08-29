#Write a Python script to print distinct elements along with their frequencies of occurrence in the list

list_1=[10,10,20,30,30,'kk','rahul','kk']
list_2=[]

for x in list_1:
    if x in list_2:
        continue
    list_2.append(x)
for x in list_2:
    print(x,'Frequencies of Occurrence :',list_1.count(x))