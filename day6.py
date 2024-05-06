#Quesion 19: Create a program to find maximum number in a list

def max_numbers(my_list):
    my_list.sort(reverse=True)
    return my_list[0]

n=int(input("Enter the limit"))
my_list=[]
for x in range(n):
    my_list.append(int(input("Enter the number")))

result=max_numbers(my_list)
print(result)


#Question 20: Fibonacci series

def fibonacci_series(number):
    first_num=0
    second_num=1
    my_list=[]
    my_list.append(first_num)
    my_list.append(second_num)
    for x in range(number):
        third_num=first_num+second_num
        my_list.append(third_num)
        first_num=second_num
        second_num=third_num
    return my_list
number=int(input("Enter the number\n"))
result=fibonacci_series(number)
print(result)


# 21 Question: Print names startswith 'A'
def name_sort(name):
    value=[]
    for x in name:
        if x.startswith('A'):
            value.append(x)
    return value

name=['Sadasivan','Haritha','Sreevedh','Aparna']
result=name_sort(name)
print(result)


#22.Multiplication table

def multiply_table(number,limit):
    for x in range(1,limit+1):
        prod=x*number
        value=print("{} * {} = {} ".format(x,number,prod))
    return value

number=int(input("Enter the number\n"))
limit=int(input('eNTER THE LIMIT'))
result=multiply_table(number,limit)
print(result)

