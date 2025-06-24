str = int(input("Please provide numder: " ))
str2 = int(input("Plese provide number2: "))
print(str+str2)
print(str-str2)
print(str*str2)
print(str/str2)

str = "Python programing is fun! "
print(str[6:18])
print(str[::2])
print(str[::-1])

name = "elsu"
last = "loda"
upcase = name.upper()
upcasel = last.upper()
print(name+last)
print(name, last)
print(upcase, upcasel)
print(name ,last, end='\n', sep=' by the way my last name is ') 

str = input("Please enter a sentence: ") 
print(len(str))

one = float(input("Please provide integer1: "))
two = float(input("Please provide integer2: "))
print(one//two)
print(one%two)

inp = float(input("Please provide celsious:"))
print((inp*9/5) + 32)

base = int(input("Please provide base number: "))
expodent = int(input("Please provide expondent number: "))
print(base**expodent)
print(base%expodent)

age = 28
new_age = age + 5
print(new_age)
print('hey ' * 5)

name = input('What is your name')
print("Hell0 ", name )

inp = float(input("How many hours did you work last month "))
inp2 = float(input("What is your hourly rate? "))
print(f"last month you earned:{inp2 * inp} ")

var1 = 1
var2 = 0

age = int(input("Enter your age: "))
if age < 13 :
    print("You are a child")
elif age <= 19 and age >= 13 :
    print("YOu are a teenager")
elif age >= 20 and age <= 64 :
    print("You are an adult")
else :
    print("You are a senior")

inp = input("Enter a sentence: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(inp.count(v) for v in set(inp) & vowels)
print("Number of vowels:", c)

inp = int(input("Enter the numer : "))
print(inp * 1 )
print(inp * 2 )
print(inp * 3 )
print(inp * 4 )
print(inp * 5 )
print(inp * 6 )
print(inp * 7 )
print(inp * 8 )
print(inp * 9 )
print(inp * 10 )

inp = int(input("Enter the numer : "))
for i in range(1, 11):
    print(inp * i)

num1 = int(input("Enter fisrt number: "))
num2 = int(input("Enter second numer: "))
opr = input("Chosose an operator such us /;*;-;+ : ")
if opr == "*" :
    print(num1 * num2)
elif opr == "/" :
    print(num1 / num2 )
elif opr == "-" :
    print(num1 - num2 )
elif  opr == "+" :
    print(num1 + num2 )
else: 
    print("Incorrect operator")

inp = int(input("please enter a number: "))
if inp % 3 == 0 and inp %  5 == 0 :
    print("The number is multile my both 3 and 5 ")
elif inp % 3 == 0 :
    print("The number is multiple by 3 ")
elif inp % 5 == 0 :
    print("The number is multiple by 5 ")
else:
    print("The number is not multiple by 3 or 5 ") 
inp = int(input("please enter a month: "))

days_31 =1, 3, 5, 7, 8, 10, 12 
days_28 = 2
days_30 = 4, 6, 9, 11
if inp in days_31 :
    print("31 days")
elif inp in days_30 :
    print("30 days")
elif inp == days_28 :
    print("28 or 29 days")
else: 
    print("incorect input")
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

inp = int(input("Please enter a number: "))
if is_prime(inp) :
    print("It'ax prime number")
else:
    print("It's not a prime")

age = int(input("whst id your age: "))
if age > 30 :
    print("You are old ")

passw = input('Passwd: ')
if passw != 'secret':
    print('not correct')
else:
    print('correct passwd')

ans = input("Do you like to travel: ")
if ans == 'y':
    print('GOod')
    ansb = input('Do you like asia?')
    if ansb == 'y':
        print("awesome")
    else: 
        print("Lol")
else:
    print("sorry")

inp1 = int(input("How many days ago you purschased: "))
inp2 = input("Have you used the item at all[y/n]: ")
inp3 = input("Has the item broken down on its own[y/n]: ")

if inp1 <= 10 and inp2 == 'n' or  inp3 == 'y':
    print("you can get a refund")
else:
    print("You can not get a refund")


counter = 1
while counter <  23:
    print(counter)
    counter += 3
print('Finished')

for i in range(11):
    pass

year = 1994 
inp = int(input("What year was python released: "))
if inp == year :
    print("Correct")
    while inp < year : 
        print("It was later than that")


i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        break
    print('*')
    
    a = 5
b = 1
c = a > b or b < a and a == 1
print(c)

inp = int(input("Please enter a number: "))
count = 0
while inp > 1 :
    if inp % 2 == 0 :
    print(inp)
    count+=1

inp = (input("Enter a word: "))
for i in inp: 
    print(reverse(inp))

emty list = []
top_cities = [ 'Chi' ,'Philly', 'New-York', 'Boston']
print(top_cities[0:2])

top_cities = [ 'Chi' ,'Philly', 'New-York', 'Boston', 'Berlin']
del top_cities[-1]
print(top_cities)

num = [ 2, 4 , 5 , 6 ]
num.insert(0, 234)
print(num)

top_cities = [ 'Chi' ,'Philly', 'New-York', 'Boston', 'Berlin']
for city in top_cities:
    print("Current city: " , city)
spendings = [ 32.45, 18.76, 78.32, 5.32]
sum = 0
for spending in spendings:
    sum+= spending
print("Money spent: ", sum)

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
high = 0
low = 0
norm = 0

for spending in spendings:
    if spending < 1000.0 : 
        low+=1
    elif spending >= 1000 and spending <= 2500:
        norm+=1  
    elif spending > 2500:
        high+=1
print("High" + str(high) + "Low" + str(low)  + "Norm" + str(norm))

top_cities = [ 'Chi' ,'Philly', 'New-York', 'Boston', 'Berlin']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

numbers = [2, 4 ,5 ,65,765, 56,4543 ]
numbers.sort()
print(numbers)


numbers = [2, 4 ,5 ,65,765, 56,4543 ]
numbers.sort(reverse=True)
print(numbers)
g = [ 'Elsu', 'Ana', 'Denise', 'Inti']
name = input("What is your name: ")
if name in g:
    print("welcome!")
else:
    print("You are not invited")

name = "jon snow"
name_new = "name"

num = [1,2,3,4]
num = []
for i in range(1,101):
    num.append(i)
print(num)

num = [ i for i in range (1, 101)]
print(num)

num = [ i for i in range(1,101) if i % 3 != 0]
print(num)

num = [1,2,2,4]
con = [ 'UK', 'America', 'USA']
cells = [['a1', 'a2', 'a3'],['b1','b2','b3'] ]
for x in cells:
    print('Element:', x)

cells = [['a1', 'a2', 'a3'],['b1','b2','b3'] ]
for x in cells:
    for y in x:
        print("element:", y)

table = [['a1', 'a2', 'a3'],['b1','b2','b3'] ]
for row in table:
    for cell in row:
        print("element:", cell)


table = [['a1', 'a2', 'a3'],['b1','b2','b3'] ]
for row in table:
    for cell in row:
        print(cell, '',end='')


table = [[i for i in range(1,6)] for j in range(2)]
print(table)

us = ['New-York', 'Austin', 'Chi', 'Philly']
uk = [ 'London', 'Bristol']
all = us + uk
print(all)

num = [0,1] * 10
print(num)

band = "Green Day"
print(band[:6])

text = 'please capitalize'
textc = text.upper()
print(textc)

tupl = ()
one = (1,)
b = 1,
c = 1, 2, 3
print(type(c))

us = ('New-York', 'Austin', 'Chi', 'Philly')
print(len(us))
city_1 = ('London', 'UK', 8.98)
city_2 = ('Bishkek', 'KG', 1.1)
city_3 = ('WD', 'USA', 2.3)
capitals= [('London', 'UK', 8.98),('Bishkek', 'KG', 1.1),('WD', 'USA', 2.3) ]
for i in capitals:
    print('Name', i[0], 'country', i[1], 'pop', i[2])

user = ( 'Jonh', 'American')


connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
counter = 0
sum = 0.0
for con in connections: 
    if con[1] == "Rome":
        counter +=0
        sum+= con[2]
print(counter, sum /print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')counter)


sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True: 
    inp = input("Please enter a wordl in English or EXIT: ")
    if inp == "EXIT" :
        break
    if inp in sample_dict:
        print('The translation of the word you entered is: ', sample_dict[inp])
    else:
        print("No match, try again")
print("Bye")


list_a = [1, 2, 3]
list_b = list_a[-2:-1]
list_c = list_a[-1:-2]
print(list_a, list_b, list_c)

ratings = [3.0, 4.5, 6.3, 4.5, 6.7]
print(ratings[-4:-2])

my_list = [0, 1, 2] * 3 + [0]
print(len(my_list)) 



students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
tar = 50
for key, value in students.items():
    if value >= tar :
        print(key,value)


inp = input("Enter a word: ")
def sliced(inp):
    new = {}
    for ch in inp:
        if ch in new:
            new[ch] += 1
        else:
            new[ch] = 1
    return new
print(sliced(inp))    




dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"banana": 2, "orange": 4, "grape": 6}
for key,value in dict1.items():
    if key not in dict2:
        print(key,value, "#Only in dic1:" )
    if key in dict1 and key in dict2:
        dict2[key] += value
        print(key, dict2[key], f"# {dict1.get(key)} (from dict1)  {dict2.get(key)} (from dict2)")
for key,value in dict2.items():
    if key not in dict1:
        print(key,value, "#Only in dict2")
for i in range (1,3)
    print(I)



inp = list(map(int,input("Please enter numbets seperated by spaces: ").split()))
uniqu = []
for i in inp:
    if i not in uniqu:
        uniqu.append(i)
print(uniqu)