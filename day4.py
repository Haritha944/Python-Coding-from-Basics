#Question 12:Create a list of fruits and access elements using index
list_1=['apple','orange','banana']
print("Fruits 1st is ",list_1[0])
print("Fruits 2nd is ",list_1[1])
print("Fruits 3rd is ",list_1[2])

# Question 11: Create a function to reverse a string
def reverse_string(my_string):
    value =''.join(reversed(my_string))
    return value

my_string = "Haritha"
result = reverse_string(my_string)
print(result)

#Question 12: Given a list of names,we have to concatinate to single string

def concate_string(my_list):
    value = " ,".join(my_list)
    return value

my_list=[]
n=int(input("Enter the limit"))
for x in range(0,n):
    my_list.append(input("Enter names here"))
result=concate_string(my_list)
print(result)

# Question 13 Create a function to check whether all the letters in string is anagram

def check_anagram(my_list1,my_list2):
    for x in my_list1:
        if x in my_list2:
            return True
    return False

my_list1='bdaa'
my_list2='dbaa'
result=check_anagram(my_list1,my_list2)
print(result)

