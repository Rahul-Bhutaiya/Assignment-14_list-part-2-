#Write a Python script to print indices of all occurrences of a given element in a given list.

list1=[11,22,11,33,33]
print('list1 = ',list1)
list2=[]
for x in list1:
    if list1.count(x)>1:
        if x in list2:
            continue
        for y in range(len(list1)):
            if list1[y]==x:
                print(x,':[',y,']')
                list2.append(x)
    else:
        print(x,':[',list1.index(x),']')    
