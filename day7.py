#23 factorial of number using recursion

def factorial_num(number):
    for x in range(number):
        if number == 1:
             return 1
        else:
            return number * factorial_num(number-1)
number=int(input("Enter the number\n"))
result=factorial_num(number)
print(result)


#24 Question factorial of number
def factorial_num(number):
    result=1
    for x in range(1,number+1):
        result*=x
    return result

number=int(input("Enter the number\n"))
value=factorial_num(number)
print(value)


#25 Print all prime numbers from 1 to 50

def prime_numbers(limit):
    primes = []
    for x in range(2, limit + 1):
        is_prime=True
        for j in range(2, x):
            if x % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

limit = int(input("Enter the limit: "))
result = prime_numbers(limit)
print("Prime numbers up to", limit, "are:", result)
