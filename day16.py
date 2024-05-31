# 42. Write a Python script to sort (ascending and descending) a dictionary by keys.

dict1={'r':11,'d':2,'c':5}
update_dict1=dict(sorted(dict1.items()))
print(update_dict1)

# 43. Write a Python script to sort (ascending and descending) a dictionary by values.
dict2={'r':11,'d':2,'c':5}
update=dict(sorted(dict2.items(), key=lambda item:item[1]))
print(update)

#descending
dict3={'d':40,'t':20,'e':80}
update_dict=dict(sorted(dict3.items(),key=lambda item:item[1],reverse=True))
print(update_dict)

#custom sorted order
dict4 = {'d': 50, 't': 200, 'e': 10}
dict5 = {'t': 0, 'd': 1, 'e': 2}

sorted_dict4 = dict(sorted(dict4.items(), key=lambda item: dict5[item[0]]))
print("newdict",sorted_dict4)


# 44  Write a Python script to concatenate the following dictionaries to create a new one.

dict1={'a':10,'b':20}
dict2={'c':40,'d':60}
dict3={'e':50,'f':80}
dict4={}
for d in (dict1,dict2,dict3):
    dict4.update(d)

print(dict4)
