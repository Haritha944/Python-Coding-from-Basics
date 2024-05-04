#Question 4:Calculate the area of rectangle

def area_function(len,bre):
    area=len*bre
    return area

len=int(input("Enter the length \n"))
bre=int(input("Enter the breadth\n"))
value=area_function(len,bre)
print("The area of rectangle:", value)

#5:Print A greeting message by taking input as name and age

def greeting(name1,age1):
   value="Good Morning {} and your age is {} right".format(name1,age1)
   return value
name1=input("Enter your name")
age1=input("Enter your age")
result=greeting(name1,age1)
print(result)

#6.Check a number is odd or even

def check_odd_or_even(number_1):
    if number_1 % 2 == 0:
        value="It is even"
    else:
        value="It is odd"
    return value

number_1=int(input("Enter a number:\n"))
value1=check_odd_or_even(number_1)
print(value1)
