# 34 Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd.


def check_numbers(number_1,number_2):
    if number_1%2==0 and number_2%2==0:
        return min(number_1,number_2)
    return max(number_1,number_2)

number_1=int(input("Enter the number\n"))
number_2=int(input("Enter the number\n"))
result=check_numbers(number_1,number_2)
print(result)

# 35 .Write a python function that
# accepts a string and calculates the number of upper case letters and lower case letters.

def count_string(my_string):
    count_upper=0
    count_lower=0
    for i in my_string:
        if i.isupper():
            count_upper+=1
        elif i=='':
            pass
        else:
            count_lower+=1
    return count_upper,count_lower

my_string='HarithA M s'
result=count_string(my_string)
print(result)
