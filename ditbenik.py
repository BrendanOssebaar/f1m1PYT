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

while True:
    print("I like playing games a lot")
    print("But which genre do I like the most?")
    print("A: Open World")
    print("B: Real Time Strategy")
    print("C: First-person shooters")

    i = input()

    if i == "B":
        print("That's correct! I love big army battles with base building")
        break
    elif i == "A":
        print("I really love traveling through gigantic worlds, but it's not my favourite")
    elif i == "C":
        print("I loved playing Call of Duty Black Ops when I was 16, but not as much anymore")

while True:
    print("I live in a city near Amsterdam")
    print("But which one?")
    print("A: Purmerend")
    print("B: Zaandam")
    print("C: Haarlem")

    i = input()

    if i == "A":
        print("That's correct! It takes 1 hour to travel between home and school")
        break
    elif i == "B":
        print("Not correct, although it's not too far away")
    elif i == "C":
        print("I work there a lot but it's not where I live")

print("I hope you learned something new about me today and I hope to learn something new about you as well! See you next time!")