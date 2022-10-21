'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''

test = float(input("Insert a number you would like to have analyzed:"))

if test in range(-200000,2000001,2):
    test_1 = "even"
    print("Test 1:", test_1, )
elif test in range(-200000,2000001,1):
    test_1 = "odd"
    print("Test 1:", test_1, )
if test in range(-200000,0):
    test_2 = "negative"
    print("Test 2:",test_2,)
elif test in range(0,2000001):
    test_2 = "positive"
    print("Test 2:", test_2, )
if test in range(-20000,-101) or test in range(101, 2000001):
    test_3 = "Exlusive"
    print("Test 3:", test_3, )
elif test in range(-100,101):
    test_3 = " "
