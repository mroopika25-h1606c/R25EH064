1.Write a program for the following problem

Let’s consider a rectangle of length 11 and breadth 13.
Output the following on separate lines:
Area of the rectangle having sides as 11 and 13
Perimeter of the rectangle having sides as 11 and 13
For any rectangle, the formula for area is length * breadth.
The formula for perimeter is 2 * (length + breadth)


code:print(11*13)          # Area of the rectangle

print(2 * (11 + 13))    # Perimeter of the rectangle
o/p:143
48

2.t("My favorite number is", 10)
The code will output:

My favorite number is 10
Task
You have to output the text:
7 plus 3 equals 10

code:
print(7 "plus" 3 "equals" 10)
o/p:7 plus 3 equals 10

3.What will be the output of this code?

print("Add", 2, "and", 3, "to get ", 5)
Option 1:

Add 2 and 3 to get 5
Option 2:

"Add" 2 "and" 3 "to get " 5
Option 3:

Add 2 and 3 to get  5
 o/p:3 option

 4.rint("\n3. What is the output of print(2 + 3)?")
print("A. 5")
print("B. 6")
print("C. 23")
print("D. 2 + 3")

answer = input("Enter your answer: ")

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is A. 5")

# Final score
print("\n===== RESULT =====")
print("Your score is:", score, "/ 3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job!")
else:
    print("Keep practicing!")

5.A variable is like a labelled box where you can store data. Imagine you have a box labeled "age" and you put the number 25 in it. In Python, you would do this by writing:

age = 25
When you write this, python creates a box(variable) with name 
a
g
e
age and stores 25 in that box(variable).

This process of creating a variable to store a value is called Declaration and
The process of setting its value for the first time is called Initialization.
Here's the cool part: whenever you use age in your code, Python will remember it is 25. For example, if you write print(age), Python will show 25.

code:print(age) 
Output: 25

6.Write a program which does the following

There is a variable named number having value 20 in the editor.
Use the print command to output the value of (number - 1).
 code:
 number=20
 print(number - 1)
o/p:19

7.There is some code written in the editor to print Code Chef.
But the variable names are not following the rule. Can you spot the mistake and fix it?

code:lst_name = "Code"
last_name = "Chef"
print(lst_name, last_name)


o/p:Code Chef

8.Write a program which does the following:

Declare two variables 
a
a and 
b
b.
Assign the value 
23
23 to 
a
a and 
20
20 to 
b
b.
Output the sum of 
a
a and 
b
b to the console

code:a=23
b=20
print(a+b)
o/p:43

9.Write a program which does the following

Find out and display the area of a rectangle of sides 45 and 76 respectively.
Declare variables length, width and area and assign the relevant values to them
Output the value of variable area
code:length=45
width=76
area=length*width
print(area)
o/p:3420

10.Write a program which does the following:

Find the area of a circle whose radius is 8.9. Take pi = 3.14
Declare variables radius , pi and area and assign the relevant values to them
Output the area, you don't need to output any other text.
Note: Formula for the area of a circle is 
area=pi*radius*radius

code:radius=8.9
pi=3.14
area=pi*radius*radius
print(area)

o/p:248.71940000000004

