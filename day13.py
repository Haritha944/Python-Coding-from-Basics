# 36.Write a program that accepts input in this form: s3t1z5. Here any character is followed by a number. The program should return a string
#where the character is repeated for the corresponding number of times.
def repeat_chara(my_string):
    result=''
    i=0
    while i< len(my_string):
        char=input_string[i]
        if char.isalpha():
            if i+1 <len(my_string) and my_string[i+1].isdigit():
                repeat_count = int(my_string[i + 1])
                result += char * repeat_count
                i+=2
            else:
                result+=char
                i+=1
    return result



input_string = "s3t1z5"
output_string = repeat_chara(input_string)
print(output_string)


# 37.Take a sentence as input and print only the words that start with “s” in the sentence.
def string_occur(string2):
    string1=string2.split()
    for i in string1:
        if i.lower().startswith('s'):
            print(i,end=' ')

string2='sailor sends a signal'
result=string_occur(string2)
print(result)
