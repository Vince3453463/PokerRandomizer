import random

while(True):
    x =  input("Whats the frequency % of your play? [type end to stop] \n")
    try:
        y = random.randint(1,100)
        if( y <= int(x)):
            print("Yes go for it! RNG says " + str(y) + " \n")
        else:
            print("No, let it go. RNG says " + str(y) + " \n")
    except ValueError:
        if (x != "end"):
            print("type something else \n")
        else:
            break
