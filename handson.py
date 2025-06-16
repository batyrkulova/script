inp = int(input("please enter number 1"))
inp2 = int(input("please enter number 2"))
print(inp * inp2)
print(inp / inp2)
upper(inp, inp2)# print(inp + inp2)
print(inp - inp2)

sentence = "Python programming is fun!"
reversed_string = "" .join(reversed(sentence))
print(reversed_string)

sentence = "Python programming is fun!"
print(sentence[::-1])

inp = int(input("How old are you: "))
if inp < 13: 
    print("Child")
elif inp >= 13 and inp <=19:
    print("Teen")
elif inp >=20 and inp <=64:
    print("Adult")
else:
    print("Senior")

vowel = [ 'a', 'e', 'i', 'o', 'i', 'A', 'E', 'I', 'O', 'U' ]
count = 0
inp = input("Enter a word: ")
for i in inp:
    if i in vowel:
        count += 1
print(count)
    

inp = int(input("Please enter a number: "))
for i in range(1,11):
    print(f"{inp} * {i}")

inp = int(input("please enter a number: "))
if inp < 0 and inp % 2 == 0:
    print("It's negative and even")
elif inp < 0 and inp % 2 != 0:
    print("It's nagative and odd")
if inp > 0 and inp % 2 == 0:
    print("It's possitive and even")
elif inp > 0 and inp % 2 != 0:
    print("It's possitive and odd ")

