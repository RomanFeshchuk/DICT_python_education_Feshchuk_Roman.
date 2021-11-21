c = list(input("Enter cells: "))
cx = c.count("x")
co = c.count("o")
c_ = c.count("_")
print("---------")
print("| ", end="")
for x in c[:3]:
    print(x, end=" ")
for a in c[:3]:
    print(a, end=" ")
print("|")
print("| ", end="")
for y in c[3:6]:
    print(y, end=" ")
print("|", end="")
for a in c[3:6]:
    print(a, end=" ")
print("|")
print("| ", end="")
for z in c[6:]:
    print(z, end=" ")
print("|", end="")
for a in c[6:9]:
    print(a, end=" ")
print("|")
print("|", end="")
print(a, end=" ")
print("|")
print("---------")
winner = 0



def put():
    global  winner
    if c[0] == c[1] == c[2] != "_":
        winner += 1
    if c[3] == c[4] == c[5] != "_":
        winner += 1
    if c[6] == c[7] == c[8] != "_":
        winner += 1
    if c[0] == c[3] == c[6] != "_":
        winner += 1
    if c[0] == c[4] == c[8] != "_":
        winner += 1
    if c[2] == c[5] == c[8] != "_":
        winner += 1
    if c[1] == c[4] == c[7] != "_":
        winner += 1
    if c[2] == c[4] == c[6] != "_":
        winner += 1



put()
if winner == 0 or winner == 1:
    if cx == co + 1 or cx == co - 1 or cx == co:
        if c[0] == c[1] == c[2] != "_":
            print(c[0, + " wins"])
        elif c[3] == c[4] == c[5] != "_":
            print(c[3] + " wins")
        elif c[6] == c[7] == c[8] != "_":
            print(c[6] + " wins")
        elif c[0] == c[4] == c[8] != "_":
            print(c[0] + " wins")
        elif c[2] == c[4] == c[6] != "_":
            print(c[2] + " wins")
        elif c[1] == c[4] == c[7] != "_":
            print(c[4] + " wins")
        elif c[2] == c[5] == c[8] != "_":
            print(c[5] + " wins")
        elif c[0] == c[3] == c[6] != "_":
            print(c[3] + " wins")
        elif c_ > 0:
            print("You don't finish game!")
        else:
            print("Draw!")
    else:
        print("Impossible!")
else:
    print("Impossible!")