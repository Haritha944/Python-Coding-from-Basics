#41 Dictionaries
# add a key to dict
dict1={'a':10,'b':20}
print("Current dict is",dict1)
dict1['c']=80
print(dict1)

# add a key using update

dict1={'a':10,'b':20,'c':30}
dict2={'d':50,'e':60}
dict1.update(dict2)
print(dict1)

# add a key using dict comprehension
dict1={'a':10,'b':20,'d':30}
key='e'
value=87
update_dict={**dict1,key:value}
print(update_dict)
