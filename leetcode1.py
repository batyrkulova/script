nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Pleae enter a number: "))
print([nums])

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Bizz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
larg = []
sec = []
num = 0
inp = list(map(int,input("Please enter a list of number").split()))
for i in inp:
    if i > num:
        larg == i
        sec == larg
        
print(sec)


inp =input("Please enter a word: ")
if inp[::-1] == inp:
    print("POlidtone")
else:
    print("It's not polidrone: ")


num = 48
inp = int(input("Please enter a number: "))
if inp > num:
    print("too high")
elif inp < num:
    print("too low")
else:
    print("Correct")

inp = list(map(int,input("Please enter numbets seperated by spaces: ").split()))
uniqu = []
for i in inp:
    if i not in uniqu:
        uniqu.append(i)
print(uniqu)