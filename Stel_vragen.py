print("Hey you, what's your name?")
a = input()
print("alright, hi " + a)
print("How old are you?")
b =int(input())
print("Nice, you are " + str(b) + " years old")
if b < 24: 
    print("You are younger than me!")
elif b > 24: 
    print("You are older than me!")
elif b == 24: 
    print("You are just as old as me!")
print("Do you live in Amsterdam? Y/N")
c = input()
if c == "N": 
    print("Oh, then I reckon you make use of public transit a lot")
elif c == "Y":
    print("Ah, so you most likely have less traveltime than I do")