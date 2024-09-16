print("Welcome to my computer quiz!")
playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("what does CPU stand for? ").lower()
if answer == "centeral processing unit":
    print("correctd!")
    score++
else:
    print("incorrect!")
    
answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correctd!")
    score++
else:
    print("incorrect!")
    
answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("correctd!")
    score++
else:
    print("incorrect!")
    
answer = input("what does psu stand for? ").lower()
if answer == "power supplay":
    print("correctd!")
    score++

else:
    print("incorrect!")
    
answer = input("what does CPU stand for? ").lower()
if answer == "centeral processing unit":
    print("correctd!")
    score++

else:
    print("incorrect!")
    
answer = input("what does CPU stand for? ").lower()
if answer == "centeral processing unit":
    print("correctd!")
    score++
else:
    print("incorrect!")
print("you got" + str(score) + "questions correct!")
