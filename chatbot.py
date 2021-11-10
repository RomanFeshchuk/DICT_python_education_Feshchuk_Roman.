# First stage
print("Hello! My name is Firstbot.")
print("I was created in 2021")
# Second stage
print("Please, remind me your name.")
str_name = str(input())
print("What a great name you have, " + str_name +"!")
# Third stage
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
a = int(input())
b = int(input())
c = int(input())
int_age = (a*70+b*21+c*15)%105
print("Your age is " + str(int_age) + " that's a good time to start programming")
# stage 4
print("Now I will prove to you that I can count to any number you want.")
str_num = int(input())
x = int()
while x <= str_num:
    print("" + str(x) + "!")
    x += 1
print("Completed, have a nice day!")