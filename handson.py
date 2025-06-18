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


passwd = input("Please enter a password: ")
if (len(passwd)) >= 8 and "@" in passwd and " " not in passwd:
    print("password strong")
else:
    print("Weak password")



pl1 = input("player1: ")
pl2 = input("player2: ")
if pl1 == "rock" and pl2 == "scissors" or pl1 == "paper" and pl2 == "rock " or pl2 == "scissors" and pl1 == "paper" :
    print("player 1 wins")
elif pl2 == "rock" and pl1 == "scissors" or pl2 == "paper" and pl1 == "rock " or pl2 == "scissors" and pl1 == "paper" :
    print("Player 2 wins")
elif pl1 == pl2 :
    print("Its a tie")
else:
    print("please enter a correct input")

inp = int(input("please enter number 1"))
inp2 = int(input("please enter number 2"))
print(inp * inp2)
print(inp / inp2)
upper(inp, inp2)# print(inp + inp2)
print(inp - inp2)




