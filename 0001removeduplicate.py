def remove_duplicate(list):
    for ele in list:
        count=0
        temp=ele
        for j,i in enumerate(list):
            if temp==i:
                count+=1
                if count>1:
                    del list[j]
    return list

list=[1,1,2,3,6,3,6,2,4]
print(remove_duplicate(list))                
