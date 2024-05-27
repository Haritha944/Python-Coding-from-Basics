#32.Implement a program to find all permutations of a string.

def find_permutations(my_string):
    if len(my_string) == 1:
        return [my_string]

    perms = []
    for i in range(len(my_string)):
        first_char = my_string[i]
        rem_chars = my_string[:i] + my_string[i+1:]
        for perm in find_permutations(rem_chars):
            perms.append(first_char + perm)
    return perms

my_strings = 'abc'
result = find_permutations(my_strings)
print(result)


#33.Common letters in between two string

def common_string(string1,string2):
    s1=set(string1)
    s2=set(string2)
    lst=s1&s2
    return lst

string1=input("Enter the string1\n")
string2=input("Enter the string2\n")
result=common_string(string1,string2)
print(result)
