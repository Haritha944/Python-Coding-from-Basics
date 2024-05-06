# Question 15:Count number of vowels in a string

def count_vowel(my_string):
    count=0
    for x in my_string:
        if x in "aeiouAEIOU":
            count+=1
    return count


my_string="APPLE"
value=count_vowel(my_string)
print(value)


#Quetsion 16: Covert given minutes to hours and minutes

def convert_time(value):
    hour =  value // 60
    minutes= value % 60
    return hour,minutes

value=int(input("Enter the time\n"))
result=convert_time(value)
print(result)

# Question 17: Check whether the number is prime or not

def check_prime(value):
    n=value
    for x in range(2,n):
        if n%x ==0:
            return False
    return True

value=int(input("Enter the number\n"))
result=check_prime(value)
print(result)


# Question 18:List with print first 10 even numbers

def check_even(number):
    list_2=[]
    for x in range(1,number+1):
        if x % 2==0:
            list_2.append(x)
    return list_2

number=int(input("Enter a number\n"))
result=check_even(number)
print(result)




