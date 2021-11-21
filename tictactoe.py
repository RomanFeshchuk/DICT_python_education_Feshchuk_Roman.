c = list("_" * 9)
cx = c.count("x")
co = c.count("o")
c_ = c.count("_")
win = 0


#The game board
def play():
    print("---------")
    print("| ", end="")
    for a in c[:3]:
        print(a, end=" ")
    print("|")
    print("| ", end="")
    for a in c[3:6]:
        print(a, end=" ")
    print("|")
    print("| ", end="")
    for a in c[6:9]:
        print(a, end=" ")
    print("|")
    print("---------")



