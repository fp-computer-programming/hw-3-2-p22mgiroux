# Author: MOG 9/29/21

height = input("How tall are you in centimeters? ")
weight = input("How much do you weigh in kilograms? ")

bmi = (float(weight) / float(height) ** 2) * 10000

if bmi < 19:
    print("You are underweight with a bmi of " + str(bmi))
elif bmi < 25:
    print("You are healthy with a bmi of " + str(bmi))
elif bmi < 30:
    print("You are overweight with a bmi of " + str(bmi))
elif bmi < 35:
    print("You are obese with a bmi of " + str(bmi))
else:
    print("You are extremely obese with a bmi of " + str(bmi))