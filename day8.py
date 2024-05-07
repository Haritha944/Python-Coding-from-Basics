# Question 26: Given a list of words,count the words having more thean 5 characters
def count_words(my_list):
    count=0
    for x in my_list:
        if len(x)>=5:
            count+=1
    return count

my_list=['ga','radhika','elephant','haritha','lion']
result=count_words(my_list)
print(result)

#Question 27:Sum of integer value

def sum_number(number):
    number_string=str(number)
    sum_num=0
    for x in number_string:
        sum_num+=int(x)
    return sum_num

number =int(input("Enter the number\n"))
value=sum_number(number)
print(value)


#quesstion 27: squares of the list
def square_list(my_list):
    sq_list=[x**2 for x in my_list]
    return sq_list

my_list=[2,5,9,8,1,7]
result=square_list(my_list)
print(result)


#Question 28: remove vowels from a string

def remove_vowel(string1):
     vowels = "aeiouAEIOU"
     return ''.join(char for char in string1 if char not in vowels)

string1='elephant'
result=remove_vowel(string1)
print(result)


#Question 28: Take a sentence and reverse each word in that sentence

def rev_sentence(my_string):
    value=my_string.split()
    return ''.join(x[::-1] for x in value)


string1='elephant is crying'
result=rev_sentence(string1)
print(result)

#Question 29: Take a list of names and return list contain names startswith vowel


def add_list(names):
    value=[]
    vowels='AEIOUSaeiou'
    for name in names:
        if name[0] in vowels:
            value.append(name)
    return value

names=['APPLE','GNM','GRAPES']
result=add_list(names)
print(result)

