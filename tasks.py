inp = int(input("please enter a number: "))
for inp in range(inp):
    if inp % 2 == 0 :
        print(inp)


inp = input("Please enter a word: ")
print(inp[::-1])

inp = input("Please enter a word: ")
reverse =  []
for i in inp:
    if inp not in reverse:
        reverse.append(i)
        reversed(reverse)
print(reverse) 


count = 0
inp = input("Please enter a word: ")
inp2 = input("Please enter a character: ")

for i in inp:
    if i == inp2:
        count += 1
print(count)

count = 0  
num = int(input("Please enter a numer: "))
for i in range(num):
    count += i
print(count)

count = 0  
num = int(input("Please enter a numer: "))
sm = 1
while sm <= num:
    count += sm
    sm += 1
print(count)

Start counting: 0, 1, 2, 3, 4, 5

When you reach 6, the break is triggered

So 6 and anything after it is not printed

m = 1
count = 0
inp = int(input("Please enter a number: "))
br = int(input("Please enter a breack point: "))
while br < inp:
    if br == inp:
        break
    count += 1
    print(br)
    

