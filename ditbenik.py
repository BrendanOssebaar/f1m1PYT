print("Hello you")
print("My name is Brendan")
print("I am 24 years old")
print("What's your name?: ")
b=input()
print("Hello " + b)
print("I am a newcomer to this school and to get you to know me better, I have a few questions about me that you can answer")
while True:
    print("Before I went to this school I did what?:")

    print("A: I worked as a grocerie deliverer with a boxcar")
    print("B: I studied the same study but on HBO")
    print("C: I traveled around the world")

    i = input()

    if i == "A":
        print("That's correct! I worked for AH home delivery")
        break
    elif i == "B": 
        print("I studied Aplied Biology on HBO before, not Software Developer")
    elif i == "C":
        print("I only traveled to Honk Kong once for a week, but thats pretty much all")

print("I like playing games a lot")
print("")