q) what are the two values of boolean data type?
ans) true and fals

q) three boolean operators?
ans) not, and, or

q)write out the tables for each boolean operator

not true = true
not false true

true or true = true
true or false = true
false or false = false

true and true = true
true and false = false
false and false = false

q)what do the following expressions evaluate to?

1, (5>4) and (3==5)
ans) false

2, not(5 > 4)
ans) false

3, (5>4) or (3==5)
ans) true

4, not((5 > 4) or (3==5))
ans) false

5, (True and True) and (True == False)
ans) false

6, (not False) or (not True)
ans) true


q) What are the six comparison operators?
ans) <,>,==,<=,=>,!=

q) what is the difference between the equal to operator and the assignment?
ans) assignment operator (=) is used to assign values to variables
while the the equal to operator (==) is used to compare two values. which returns a boolean value depending on whether the two values are equal or not

7) Explain what a condition is and where do we use it?
ans) A condition is a statement that returns true or false, it can be used in if or elif statements to conditionally run a block of code.
or it can be used to run a "while" loop while that condition holds true.

8 identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

1st block after 2nd line (if spam == 10:)
2nd block after 4th line (if spam > 5:)
3rd block after 6th line (else:)

9) write code that print Hello if 1 is stored in spam prints Howdy if 2 is strored in spam and prints Greetings! if anything else is stored in spam
ans)
spam = int(input())
if spam == 1:
	print("Hello")
if spam == 2:
	print("Howdy")
else:
	print("Greetings!")
	
	
10) what keys can you press if your program is stuck in an infinite loop?
ctrl + c

11) what is the difference between break and continue?
ans) break breaks out of the loop and moves onto the next line of code
continue moves on to the next iteration of the loop


12)what is the difference between  range(10),range(0,10) and rang(0,10,1) in a for loop
ans) there is no difference

13) write a shhort program that prints the numebrs 1 to 10 using a for loop then write an equivalent program that prints the numbers 1 to 10 using a while loop:

for i in range(1,11):
	print(i)
	
i = 1:
while i != 11:
	print(i)
	i+= 1

14) if you had a function named bacon() inside a module named spam, how would you call it after importing spam

spam.bacon()





