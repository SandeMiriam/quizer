print("welcome to quizer")
username = input("Username? ")
print("hey",username,"\nlet's get started for every good answer you get one point!")

playing = True
while playing == True:
    points =0

    print("what football/soccer player is known as CR?")
    Answer_1 = input("Fill in here: ")
    if Answer_1 == "Ronaldo" or Answer_1 =="ronaldo":  
        print("Correct")
        points +=1
    else:
        print("Wrong!")

    print("what is the capital city of Italy?")
    Answer_2=input ("Fill in here: ")
    if Answer_2 == "rome" or Answer_2 =="Rome":
        print("Correct")
        points +=1
    else:
        print("Wrong!")

    print("In what continent Turkmenistan located? ")
    Answer_3 = input("Fill in here: ")
    if Answer_3 == "asia" or Answer_3 =="Asia":
        print("Correct")
        points +=1
    else:
        print("Wrong!")

    final_Question =input("Do you want to play again?")
    if final_Question == "Yes" or final_Question =="yes":
     playing = True
    else:
     break
    print("Thanks for playing,your final points are",points)

