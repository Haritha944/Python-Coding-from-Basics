#Question 9: Program coverts a given number of days into year ,month and days
def days_convert(value):
    year=value//365
    remaining_days=value%365
    months=remaining_days//30
    days=remaining_days%30
    return year,months,days

value=int(input("Enter the days\n"))
result=days_convert(value)
print(result)


#Question 10: Program that find sum of numbers in a list

def sum_list_numbers(my_list):
    sum_list=0
    for x in my_list:
        sum_list+=x
    return sum_list

num = int(input("Enter the limit\n"))
my_list=[]
for x in range(num):
    my_list.append(int(input("Enter the numbers\n")))
result = sum_list_numbers(my_list)
print(result)


#qUESTION 11: Program to find number of words in sentence

def count_words(sentence):
    words=sentence.split()
    count_value=0
    for w in words:
        count_value+=1
    return count_value


sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print("Number of words:", word_count)
