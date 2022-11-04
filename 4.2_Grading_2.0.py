'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semester_grade = int(input("What was your semester grade?: "))
final_grade = int(input("What was your final exam grade?: "))
final_worth = float(input("What was your final exam worth in decimal form?: "))
overall_grade = final_grade*final_worth+((1-final_worth)*semester_grade)
print(" Your overall final grade is:",overall_grade,"%")
if overall_grade >=97:
    print("Your letter grade is A+")
elif overall_grade>=93:
    print("Your letter grade is A")
elif overall_grade>=90:
    print("Your letter grade is A-")
elif overall_grade in range(87,89):
    print("Your letter grade is B+")
elif overall_grade in range(83,86):
    print("Your letter grade is B- ")
elif overall_grade in range(80,82):
    print("Your letter grade is C+ ")
elif overall_grade in range(77,79):
    print("Your letter grade is C ")
elif overall_grade in range(73,76):
    print("Your letter grade is C-")
elif overall_grade in range(70,72):
    print("Your letter grade is D+")
elif overall_grade in range(67,69):
    print("Your letter grade is D")
elif overall_grade in range(65,66):
    print("Your letter grade is D-")
else:
    print(" You Failed, Go to Johnston")
