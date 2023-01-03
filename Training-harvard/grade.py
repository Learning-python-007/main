score = int(input("Score: "))
# aproach 1
if score >= 90 and score <= 100:
    print("Grade : A")
elif score >= 80 and score < 90:
    print("Grade : B")
elif score >= 70 and score < 80:
    print("Grade : C")
elif score >= 60 and score < 70:
    print("Grade : D")
else:
    print("Grade : F")

# aproach 2
score2 = int(input("Score2: "))
if score2 >= 90:
    print("Grade : A")
elif score2 >= 80:
    print("Grade : B")
elif score2 >= 70:
    print("Grade : C")
elif score2 >= 60:
    print("Grade : D")
else:
    print("Grade : F")