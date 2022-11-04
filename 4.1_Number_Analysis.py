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

if test%2==0:
    print("test 1: even")
else:
    print("test 1: odd")

if test>0:
    print("Test 2: positive")
elif test<0:
    print("Test 2: negative")
else:
    print("Test 2: zero")

if test<=100 and test>=-100:
    print("Test 3: inclusive")
else:
    print("Test 3: exclusive")
