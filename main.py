#Introductionm set the stage
print("It is time for bed.") 
print("You can chose 1 of these 3 questions for your bed time question")
print()

#select a story
print("  A. Finish the ryhm?")
print("  B. What comes next?")
print("  C. Which way should I go?")
print()
myStory = input("Which story do you chose: A, B, or C: ")
print()
print()
#Story A Ryhm 
if(myStory == "A"):
  #Ryhm Question
  print("Finish the ryhm")
  print("Roses are Red")
  print("Violets are ____ ")
  print("  A. Weird")
  print("  B. Blue")
  print("  C. Dead")
  print()
  #Ryhm if statement to determine if the user is correct
  ryhmAnswer = input("What?  ")
  print()
  if(ryhmAnswer == "B"):
    print("Correct! I hope you have a wonderful nights sleep.")
  else:
    print("Wrong! What a terrible answer. Now go to bed.")
    
  print()
  print()

#Story B Logic
elif(myStory == "B"):
  #logic question
  print("What comes next?")
  print()
  print("Here are a series of letters")
  print()
  print("A, D, G, ___")
  print()
  logicAnswer = input("What letter should come next in the series? ")
  print()
  #logic if statement to determine if the user is correct
  if(logicAnswer == "J"):
    print("Correct! I hope you have a wonderful nights sleep.")
  else:
    print("Wrong! What a terrible answer. Now go to bed.")


  print()
  print()

#Story C Which way is home
elif(myStory == "C"):
  #intro to way home story
  print("You are traveling home from the South and come to a crossroads.")
  print()
  print("Only one way leads home.")
  print()
  #chose direction home
  wayHome = input("Do you go Left, Right, or Straight ahead?  ")
  print()
  #correct way home
  if(wayHome == "Left"):
    print("Correct! You made it home to your comfortable bed.") 
    print("I hope you have a wonderful nights sleep.")
  #wrong way to Bear
  elif(wayHome == "Right"):
    print("Wrong! You walk right into a Bear's den who has you for dinner.") 
  #wrong way to Tiger
  else:
    print("Wrong! You walk straight into a Tiger's den who has you for dinner.") 
    

  print()
  print()




#Wrong choice = No Question
else:
  print("That was not a choice, so no question for you.  Good Night")