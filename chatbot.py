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
# stage 5
print("How many file extensions does python have?")
print("""
1.Python has only 5 types of file extensions
2.Python has only 9 types of file extensions
3.Python has only 11 types of file extensions
4.Python has only 12 types of file extensions
""")
def answers(new_answer):
    answer = int(input())
    if answer == 2:
        print("Congratulations, have a nice day!")
    else:
        print("Wrong answer! Please, try again.")
        answers("1")
answers("3")
answers("4")