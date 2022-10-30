Physics = int(input("What is your score in Physics\n\n"))
Chemistry = int(input("What is your score in Chemistry\n\n"))
Biology = int(input("What is your score in Biology\n\n"))
Maths = int(input("What is your score in Maths\n\n"))
Geology = int(input("What is your score in Geology\n\n"))
average_score = int((Physics + Chemistry + Biology + Maths + Geology) / 5)

if average_score > 90 or average_score == 90:
    print("Congratulations!!!, you have an A grade")
elif average_score > 80 or average_score ==80:
    print("Congratulations!!!, you have a B grade")
elif average_score > 70 or average_score == 70:
    print("Congratulations!!!, you have a C grade")
elif average_score > 60 or average_score == 60:
    print("Sorry, you failed with a D grade")
else:
    print("Sorry, You flunged with an F grade")




