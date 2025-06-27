
inp = int(input("please enter 1 side lengh: "))
inp2 = int(input("please enter 2 side lengh: "))
inp3 = int(input("please enter 3 side lengh: "))

if inp + inp2 < inp3 or inp2 + inp3 < inp or inp+inp3 < inp2:
    print("Not a triangle")
elif inp == inp2 and inp2 == inp3:
    print("Equilateral")
elif inp == inp2 and inp2 != inp3 or inp3 == inp2 and inp != inp3:
    print("Isocales")
elif inp != inp2 and inp2 != inp3:
    print("Scalene")


inp = (input("please enter a list seperated by spaces: ")).split()
reverse = []
for i in reversed(inp):
    if i not in reverse:
        reverse.append(i)
print(reverse)

inp = input("Enter a words: ").split()
dup = []
for i in inp:
    if i not in dup:
        dup.append(i) 
print(dup)

inp = input("please enter a list").split()
max = 0
lonf = ""
for i in inp:
    if (len(i)) > max:
        max = len(i)
        lonf = i
print(lonf)


numbers = list(map(int, input("Enter numbers: ").split()))
larg = 0
secd = 0
for i in numbers: 
    if i > larg:
        secd = larg
        larg = i
    elif i > secd and i != larg:
        secd = i
print(secd)

students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
for keys,values in students.items():
    if values >= 50:
        print(keys, values, end=" ")



inp = input("Please enter an input: ")
char_count = {}

for char in inp:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Output:", char_count)

num = int(input("please enter a list of number"))
lists = []
for i in num:
    if i in lists:
        lists(i) += 1
    else:
        lists(i) = 1
print(lists)

cube = [ [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ] ]

cube[1][1][0] = 99

print(cube)

L = [1,2,3,4,5]

L*2

print(L)


for i in range(2, -1, -1):
    print(i, end=' ')


for i in range(3):
    print(i, end=" ")
else:
    print('FINISHED')

for i in range(1,1):
    print(i, end=' ')
else:
    print('FINISHED')

for i in range(3):
    if i == 2:
        break
    print(i, end=' ')
else:
    print('FINISHED')

i = 1
while True:
    print(i, end=' ')
    i += 1
    if i == 3:
        break    
else:
    print('FINISHED')

pl = 1 + 1 // 2 * 3
if pl > 0 :
    print("#")
elif pl > 1:
    print("**")
else:
    print("***")


power = 1
while power != 10:
    power *= 2
    if power == 5:
        continue
    print("@")
else:
    print("@")


ang = 0
for i in range(5):
    if i % 2 == 1:
        ang += 1
else:
    ang -= 1
print(ang )

others = 0 
for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others += 1
print(others)

others = -1 
for i in range(1,3):
    for j in range(1,2):
        if i == j:
            others += 1
else:
    others += 1
print(others)


the_list = ['a', 'b', 'c']
counter = 0
for ix in range(len(the_list)):
    print(the_list[ix], end=' ')
    the_list[ix] = counter
    counter += 1
for ix in range(len(the_list)):
    print(the_list[ix], end=' ')

planets = 1 + 1 // 2 * 3
if planets > 0 :
    print("#")
elif planets > 1:
    print("##")
else:
    print("###")










