#44.highest value in dict
my_dict = {'c': 3, 'a': 1, 'b': 2}
update=max(my_dict,key=lambda k:my_dict[k])
value_max=my_dict[update]
print(update)

#next method
my_dict = {'c': 3, 'a': 1, 'b': 2}
max_value=max(my_dict.values())
print("The highest value is:", max_value)

#45 Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('No Key is present in the dictionary')

is_key_present(5)

#46 Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x).

dict1={}
n = int(input("Input a number "))
for x in range(1,n+1):
    dict1[x]=x*x
print(dict1)

#using dict comprehension
d={k:k*k for k in range(1,6) if k%2==0}
print(d)
