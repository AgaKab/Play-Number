from art import logo
import random
print(logo)
print("Welcome to the 'Play Numbers' game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
#print(f"pssst, the correct answer is {number}")


easy_trials = 10
def easy():
  global easy_trials
  if easy_trials > 0:
    print(f"You have {easy_trials} attepmts remaining to guess the number.")
    easy_trials -=1
    guess = int(input("Make a guess: "))
    if guess > number:
      print ("Too high")
      if easy_trials>1:
        print ("Guess again")
      easy()
    elif guess < number:
      print ("Too low")
      if easy_trials>1:
        print ("Guess again")
      easy()
    else:
      print (f"You got it! The answer was {number}")
      False
  else:
    print("You've run out of guesses, you lose.")
    False

hard_trials = 5
def hard():
  global hard_trials
  if hard_trials > 0:
    print(f"You have {hard_trials} attepmts remaining to guess the number.")
    hard_trials -=1
    guess = int(input("Make a guess: "))
    if guess > number:
      print ("Too high")
      if hard_trials>1:
        print ("Guess again")
      hard()
    elif guess < number:
      print ("Too low")
      if hard_trials>1:
        print ("Guess again")
      hard()
    else:
      print (f"You got it! The answer was {number}")
      False
  else:
    print("You've run out of guesses, you lose.")
    False



choose = input("Choose difficulty. Type 'easy' or 'hard': ")
if choose == 'easy':
  easy()

else:
  hard()