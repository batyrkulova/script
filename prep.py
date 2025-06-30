
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
!/bin/bash 

Session 1 tasks

# create a file called /var/www/html/ouput.txt
# write the message "This is a test output" into the file using output redirection
echo "This is a test output" > /var/www/html/output.txt

appends the current date and time to the file called /var/www/html/logs.txt using >> (append redirection)
run sctipt multiple times to see the log grow with each run 
date >> /var/www/html/logs.txt

Prints the values of predefined environment variables: PATH, HOME, and USER.
Creates a custom environment variable MY_VAR and prints its value.

MY_VAR="This is a custom environment" 
echo "$PATH"
echo "$HOME"
echo "$USER"
echo "$MY_VAR"

Retrives and logs the current status of the Apache web server 
Use ans envirenmonet variable to store the Apache service name9e.g apache 2 or httpd 
logs the status and date to a file called /var/www/html/apache_status.log each time the script is run 


# $(systemctl status httpd | head -n 3 | tail -n 1 | awk -F: '{ print $1 }') > /var/www/html/apache_status.log

Session 2 tasks.
read -p "Please provide your name, age and city where you live: " arg1 arg2 arg3
if [[ -n "$arg1" && -n "$arg2" && -n "$arg3" ]]; then  
echo "Thanks for the info"
echo " $arg1 $arg2 $arg3 "
else 
echo "provide more info"
fi  

echo " The proccess ID of this script is : $$" >> /var/www/html/process_log.txt
echo "The number of argumets passed the script is $#" >> /var/www/html/process_log.txt 

read -p "Please enter a directory that you want to check: " dir
if [ -d "$dir" ]; then 
echo "The directory exist" 
else 
echo "the directory does not exist"
fi 
echo "The exit status of the script is $? " 

session 3 
if [ -f "report.txt" ]; then 
echo "file exits" 
else
echo "Report created" > report.txt 
fi 

cat << option
Choose an option: 
1)Show date
2)List files
3)Show user
4)Exit
option

read -p "Enter your choice: " num

case $num in 
1) date ;;
2) ls -la ;;
3) id ;; 
4) echo "Bye" && exit ;;
*) echo "please enter the chosen numbers" 
esac 

for file in *.txt ; do 
mv $file backup$file
done 

read -p "enter a number" num
while (( num > 0 )); do
  echo $num
  ((num--))
done
echo "Times up" 
 Not accurate
read -p "Please enter a file name" name
if [ -f $name ] && [ -r $name ] && [ -w $name ] ; then
echo "file exist , its has r and w permissions" 
elif [ -f $name ] && ([ ! -r $name ] && [ ! -w $name ]); then
echo "file exist , nut not readible or writble" 
else 
echo "file doesn't exists"
fi  

cat << opt
Select an option:
1.Delete all .tmp files
2.Back up all .tmp files
3.Exit 
opt
read -p "Enter your choice: "

case $file in
   1) for file in *.tmp; do 
   if [ -f $file ]; then 
   rm -r $file 
   fi 
   done ;;
   2) for file in *.tmp ; do 
   if [ -f $file ]; then 
   mv $file backup_$file
   fi 
   done ;;
   3) for file in *.tpm ; do 
      if [ -f $file ]; then 
      echo "file exist" | exit
      fi 
      done ;;
esac









