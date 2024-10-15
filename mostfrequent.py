def mostfrequent(array):
    count = {}
    for i in range(len(array)):
        
        if array[i] not in count:
            count[array[i]] = 1
        else :
             count[array[i]]+=1
    return [k for k,v in count.items() if v==max(count.values())]

print(mostfrequent([2,2,4,4,4,4,5,1,6,6,6,6,6,6,6,6,6,6,6,6,6,7,8,-1]))