name=int=(input("What is your name? "))
print(f"\nHello, {name}. Be polite.")
def checkguess(guess, answer):
    #saves score as a global variable
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        #I used the lower() command :)
        if guess.lower() == answer.lower():
            print("correct")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Incorrect. Try again.")
            attempt = attempt + 1
        if attempt == 3:
            print("The right answer is", answer)
        #I also used the upper() command :P
        if guess.lower() == answer.lower():
            print(" ")
score = 0
print("Quiz")
guess1 = input("Which bear lives at the North Pole? ")
checkguess(guess1, "polar bear")
guess2 = input("What color is #4287f5? ")
checkguess(guess2, "Blue")
guess3 = input("Which is the largest animal? ")
checkguess(guess3, "Blue Whale")
guess4 = input("Who was the first president of the US? ")
checkguess(guess4, "George Washington")
guess5 = input("What language is this written in? ")
checkguess(guess5, "python")
guess6 = input("Origin of a coordinate plane? ")
checkguess(guess6, "0,0")
guess7 = input("What powers a cell? ")
checkguess(guess7, "mitochondria")
guess8 = input("Toughest rock? ")
checkguess(guess8, "diamond")
guess9 = input("What year did WW1 end? ")
checkguess(guess9, "1918")
guess10 = input("When did WW2 end? ")
checkguess(guess10, "1945")
print("You got "+ str(score) +" out of 10")
if score < 10:
    print(f"\n{name}, do it again until you get a 100!")
