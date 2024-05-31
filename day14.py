# 38. From a dictionary, print only the items with an odd value of less than 45.
def dict_items(dict1):
    for i,j in dict1.items():
        if j%2!=0 and j<45:
            return (i,":",j)

dict1={'Sweta': 45, 'Mausam': 31, 'Pratik':312, 'Pari': 400}
result=dict_items(dict1)
print(result)


#39 Write a program to count pairs of elements of a list with a given sum

def count_elements(list1,sum1):
    count=0
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j]==sum1:
                count+=1
    return count




list1=[1,2,3,4,5,4,3,2,1]
sum1=6
result=count_elements(list1,sum1)
print(result)

# 40 Write a python program to find the common characters from two input strings.

a1="Shiva"
b1="Shewetha"
list1=list(set(a1)& set(b1))
print(list1)
