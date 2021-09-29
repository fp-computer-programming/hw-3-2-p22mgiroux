# Author: MOG 9/29/21

grade = input("What is your grade for the quarter? ")

if float(grade) < 60:
    print("You get an F")
elif float(grade) < 65:
    print("You get a D")
elif float(grade) < 70:
    print("You get a D+")
elif float(grade) < 73:
    print("You get a C-")
elif float(grade) < 77:
    print("You get a C")
elif float(grade) < 80:
    print("You get a C+")
elif float(grade) < 83:
    print("You get a B-")
elif float(grade) < 87:
    print("You get a B")
elif float(grade) < 90:
    print("You get a B+")
elif float(grade) < 93:
    print("You get a A-")
else:
    print("You get an A!")
