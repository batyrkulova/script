# 1. Write a function to greet a person
# Task: Create a function called greet_user that takes a name and prints:
# Hello, <name>!
def greeting(inp):
    return("Hello", inp )
print(greeting("Elsu"))




# 2. Write a function to calculate the square of a number
# Task: Create a function square_number(num) that returns the square of the given number.

def square(num):
    return(num ** 2)
print(square(5))



# 3. Write a function to check if a number is even
# Task: Write is_even(num) that returns True if the number is even, False otherwise.
def is_even(num):
    if num % 2 == 0:
        return("It's even")
    elif num % 2 != 0:
        return("It's odd")
    else:
        return("there is some error")
print(is_even(6))

# 4. Write a function that returns the sum of two numbers
# Task: Create add(a, b) that returns the sum of a and b.

def plus(a,b):
    return( a + b)
print(plus(2,3))

# 5. Write a function that checks if a word is a palindrome
# Task: Create is_palindrome(word) that returns True if the word is the same forwards and backwards.
def pali(inp):
    if inp[::-1] == inp:
        return("It's a palidrone")
    else:
        return("It's not a palidrone")
print(pali("deed"))

# 6. Write a function to find the maximum of three numbers
# Task: Write find_max(a, b, c) that returns the largest number.

def larg(a,b,c):
    if a > b and a > c :
        return(a)
    elif b > a and b > c:
        return(b)
    elif c > a and c > b:
        return(c)
print(larg(12,19,8))


# 7. Write a function to count how many vowels are in a string
# Task: Create count_vowels(text) that returns the number of vowels in the string.

def vowels(inp):
    lst = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for i in inp:
        if i in lst:
            count += 1
            return(count)
        else: 
            return("There is no vowels")
print(vowels("Hello"))


# 8. Write a function to convert Celsius to Fahrenheit
# Task: Write to_fahrenheit(celsius) to convert and return the Fahrenheit equivalent.



# 9. Write a function to reverse a list
# Task: Create reverse_list(my_list) that returns the reversed list.

def conv(inp):
    return(inp[::-1])
print(conv("hello there"))



# 10. Write a function that prints numbers from 1 to n
# Task: Write print_numbers(n) that prints numbers from 1 to n.
def prn(n):
    return(n in range(1, n))
print(prn(10))
