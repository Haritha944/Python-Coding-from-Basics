# 31 Write a program to find the number of occurrences of elements from list1 to list2.
def occur_count(list1,list2):
    count=0
    for i in list1:
        if i in list2:
            count+=1
    return count

list1=[2,3,6,7,8]
list2=[2,4,5,8,0]
result=occur_count(list1,list2)
print(result)

#or using dictionary
def occur_count(list1,list2):
    occur={ element:0 for element in list1}
    for items in list2:
        if items in occur:
            occur[items]+=1
    return occur

list1 = [1, 2, 3,5]
list2 = [1, 2, 2, 3, 3, 3, 4, 5]
result = occur_count(list1, list2)
print(result)

