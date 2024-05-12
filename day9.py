#30 .Python program to interchange first and last elements in a list

def swap_list(my_list):
    my_list[0],my_list[-1] = my_list[-1],my_list[0]
    return my_list

my_list = [12,89,45,100]
result = swap_list(my_list)
print(result)
