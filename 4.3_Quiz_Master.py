'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print ("Hello welcome to my random facts quiz! ")
answer = input("are you ready for the test?")
if answer == ("no").lower() or answer == ("n").lower():
    print("Welp... too bad :)! ")
elif answer == ("yes").lower() or answer == ("y").lower():
    print("Good for you! Now lets start. ")
else:
    print("no matter what your answer is we're starting.")
score = 0
print("-------------------------------------/----------------------------------------------------")
answer = input("(Question number 1) What day is cinco de mayo? ")
if answer == (" May 5th ") or answer == ("may 5th") or answer == ("5/5") or answer == ("5-5"):
    print("CORRECT! (not really that hard though if you speak spanish...)")
    score+=1
else:
    print("Incorrect. the answer is May 5th (would've known the answer if you paid attention in spanish) ")


print("-----------------------------------------------------------------------------------------")
answer = input("(Question number 2)What level is earth currently at on the kardashev scale? (A: 2) (B: 2.7)  (C: 0.29)  (D: 0.73)")

if answer == ("A") or answer == ("B") or answer == ("C"):
    print("Incorrect. the answer is 0.73 (maybe you should've known more weird facts).")
elif answer == ("D"):
    print("CORRECT! I see your a man of culture (or you just never leave the basement). ")
    score+=1
else:
    print("You didn't even enter a proper answer so, no points... horray")


print("-----------------------------------------------------------------------------------------")
answer = input("(Question number 3)What is the largest insect in the world?  (A: titan beetle)  (B: Stick bug)  (C: Hercules Beetle)  (D: Hunstman Spider)")
if answer == ("A") or answer == ("C"):
    print("Incorrect. its a stick bug (you'd know that if you were an entomologist)")
elif answer == ("D"):
    print("Incorrect. Spiders arent bugs NERD!")
elif answer == ("B"):
    print("CORRECT! you must be a proper entomologist! (or a weird bug lady)")
    score+=1
else:
    print("thats not a proper answer so no points.")


print("-----------------------------------------------------------------------------------------")
answer = input("(Question number 4)How many countries are in the world?")
if answer == ("195"):
    print("CORRECT! Now can you name them all? (dont actually.)")
    score+=1
else:
    print("incorrect.The answer was 195 so not even close... unless you were (you probably weren't)")


print("-----------------------------------------------------------------------------------------")
answer = input("(Question number 5)How many planets are in our solar system?")
if answer == ("8"):
    print("CORRECT. Looks like someone past 5th grade, want a cookie! (Spoiler, you don't get a cookie.)")
    score+=1
else:
    print("Incorrect.The answer was 8 Looks like someones not smarter than a 5th grader.")


print("-----------------------------------------------------------------------------------------")
answer = input("(Question number 6)How many people have eaten a plane?")
if answer == ("2"):
    print("CORRECT! Also weird right? (its pretty weird)")
    score+=1
else:
    print("Incorrect. it would be weird if you knew that. (also pretty weird that you dont.)")


print("-----------------------------------------------------------------------------------------")
answer = input("(Question number 7)What is the fastest animal on earth? (A:Cheetah)  (B:Antelope)  (C:Dragonfly)  (D:Falcon)")
if answer == ("A") or answer == ("B") or answer == ("C"):
    print("Incorrect. the answer was a falcon.(I bet you thought it was a cheetah NERD.")
if answer == ("D"):
    print("CORRECT! glad your not one of those people that thought it was a cheetah.")
    score+=1


print("-----------------------------------------------------------------------------------------")
answer = input("Welp its finally over, how do you think you did?")
if answer == ("good").lower() or answer == ("okay"):
    print("Well ill be the judge of that")
elif answer == ("bad"):
    print("yeah probably")
print("Your final score was",score,"out of 7.")
if score == 7:
    print("It was a pretty easy test so thats expected, but I guess you've earned a congradulations. Anyways I've got stuff to do so goodbye.")
elif score == 6 or score == 5:
    print("It was close to a pefect score... to bad close only counts in horse shoes and hand grenades. Anyways we're done now so goodbye.")
elif score == 4 or score == 3 or score == 2 or score == 1 or score == 0:
    print("Not a very good score for a simple quiz, but atleast you tried... too bad trying doesn't get you points.")


