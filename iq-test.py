import random


print("Welcome to the IQ Test!")
input("Press Enter to start..")


points = 0

#Which number logically follows this series?
print("\n1. Which number logically follows this series?")

log1 = random.randint(1,2)
if log1 == 1:
    while True:
        q1 = input("\n2, 5, 8, 11, ?\
\n\n1) 8\n2) 10\n3) 11\n4) 13\n\nAnswer: ")
        if q1 in ["1", "2", "3", "4"]:
            if q1 == "3":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log1 == 2:
    while True:
        q2 = input("\n121, 144, 169, 196, ?\
\n\n1) 225\n2) 230\n3) 275\n4) 221\n\nAnswer: ")
        if q2 in ["1", "2", "3", "4"]:
            if q2 == "1":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

log2 = random.randint(3,4)
if log2 == 3:
    while True:
        q3 = input("\n4, 6, 9, 6, 14, 6, ?\
\n\n1) 14\n2) 9\n3) 16\n4) 19\n\nAnswer: ")
        if q3 in ["1", "2", "3", "4"]:
            if q3 == "4":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log2 == 4:
    while True:
        q4 = input("\n2, 3, 5, 9, 17, 33, 65, ?\
\n\n1) 104\n2) 129\n3) 97\n4) 135\n\nAnswer: ")
        if q4 in ["1", "2", "3", "4"]:
            if q4 == "2":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

log3 = random.randint(5,7)
if log3 == 5:
    while True:
        q5 = input("\n1, 3, 12, 52, 265, ?\
\n\n1) 1188\n2) 1390\n3) 1489\n4) 1596\n\nAnswer: ")
        if q5 in ["1", "2", "3", "4"]:
            if q5 == "4":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log3 == 6:
    while True:
        q6 = input("\n13, 17, 19, 23, 29, ?\
\n\n1) 30\n2) 31\n3) 33\n4) 34\n\nAnswer: ")
        if q6 in ["1", "2", "3", "4"]:
            if q6 == "2":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log3 == 7:
    while True:
        q7 = input("\n2, 3, 6, 11, 18, 27, ?\
\n\n1) 21\n2) 28\n3) 38\n4) 41\n\nAnswer: ")
        if q7 in ["1", "2", "3", "4"]:
            if q7 == "3":
                points += 1
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")


#Which number is missing?
print("\n2. Which number is missing?")

log4 = random.randint(8,9)
if log4 == 8:
    while True:
        q8 = input("\n144, ?, 206, 240\
\n\n1) 155\n2) 167\n3) 170\n4) 174\n\nAnswer: ")
        if q8 in ["1", "2", "3", "4"]:
            if q8 == "4":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log4 == 9:
    while True:
        q9 = input("\n16, 64, ?, 1024, 4096\
\n\n1) 98\n2) 156\n3) 256\n4) 298\n\nAnswer: ")
        if q9 in ["1", "2", "3", "4"]:
            if q9 == "3":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
            
log5 = random.randint(10,11)
if log5 == 10:
    while True:
        q10 = input("\n56, 75, 94, ? , 132\
\n\n1) 113\n2) 128\n3) 130\n4) 131\n\nAnswer: ")
        if q10 in ["1", "2", "3", "4"]:
            if q10 == "1":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log5 == 11:
    while True:
        q11 = input("\n19, 57, ?, 513\
\n\n1) 88\n2) 171\n3) 333\n4) 467\n\nAnswer: ")
        if q11 in ["1", "2", "3", "4"]:
            if q11 == "2":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

log6 = random.randint(12,14)
if log6 == 12:
    while True:
        q12 = input("\n-9, -6, -3, ?, 3\
\n\n1) 3\n2) 4\n3) 5\n4) 0\n\nAnswer: ")
        if q12 in ["1", "2", "3", "4"]:
            if q12 == "4":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log6 == 13:
    while True:
        q13 = input("\n78, 184, ?, 396, 502\
\n\n1) 290\n2) 1345\n3) 1266\n4) 1456\n\nAnswer: ")
        if q13 in ["1", "2", "3", "4"]:
            if q13 == "1":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log6 == 14:
    while True:
        q14 = input("\n83, ?, 332, 664\
\n\n1) 166\n2) 178\n3) 266\n4) 567\n\nAnswer: ")
        if q14 in ["1", "2", "3", "4"]:
            if q14 == "1":
                points += 2
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")


#Find the right answer to this question.
print("\n3. Find the right answer to this question.")

log7 = random.randint(15,17)
if log7 == 15:
    while True:
        q15 = input("\nMary is 16 years old. She is 4 times older than her brother. \
How old will Mary be when she is twice his age?\n\n1) That's impossible\n2) 20\n3) 24\n4) 28\n\nAnswer: ")
        if q15 in ["1", "2", "3", "4"]:
            if q15 == "3":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

if log7 == 16:
    while True:
        q16 = input("\nWhich fraction is the biggest?\
\n\n1) 3/5\n2) 5/8\n3) 1/2\n4) 4/7\n\nAnswer: ")
        if q16 in ["1", "2", "3", "4"]:
            if q16 == "2":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

if log7 == 17:
    while True:
        q17 = input("\nMUSIC: COMPOSE, DEVICE: ?\
\n\n1) USE\n2) CREATE\n3) CONSTRUCT\n4) INVENT\n\nAnswer: ")
        if q17 in ["1", "2", "3", "4"]:
            if q17 == "4":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")


log8 = random.randint(18,20)
if log8 == 18:
    while True:
        q18 = input("\nSunday, Monday, Wednesday, Saturday, Wednesday, ?\
\n\n1) Sunday\n2) Monday\n3) Wednesday\n4) Saturday\n\nAnswer: ")
        if q18 in ["1", "2", "3", "4"]:
            if q18 == "2":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log8 == 19:
    while True:
        q19 = input("\nHow many minutes is it before noon if 29 minutes ago \
it was six times as many minutes past 10 am?\
\n\n1) 13 minutes\n2) 15 minutes\n3) 10 minutes\n4) 16 minutes\n\nAnswer: ")
        if q19 in ["1", "2", "3", "4"]:
            if q19 == "1":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

if log8 == 20:
    while True:
        q20 = input("\nIf two people eat 2 slices of pizza in 2 minutes, \
how many people will it take to eat 18 pieces of pizza in 6 minutes?\
\n\n1) 9\n2) 3\n3) 6\n4) 8\n\nAnswer: ")
        if q20 in ["1", "2", "3", "4"]:
            if q20 == "3":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")

log9 = random.randint(21,23)
if log9 == 21:
    while True:
        q21 = input("\nIf you count from 1 to 100, how many numbers will you see that contain a 5?\
\n\n1) 20\n2) 19\n3) 10\n4) 9\n\nAnswer: ")
        if q21 in ["1", "2", "3", "4"]:
            if q21 == "2":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log9 == 22:
    while True:
        q22 = input("\nThere are 10 fingers on the feet. How many fingers are on 10 feet?\
\n\n1) 50\n2) 100\n3) 200\n4) 150\n\nAnswer: ")
        if q22 in ["1", "2", "3", "4"]:
            if q22 == "1":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")
if log9 == 23:
    while True:
        q23 = input("\nWhat is the most common digit in the range of numbers from 0 to 109?\
\n\n1) 9\n2) 8\n3) 5\n4) 1\n\nAnswer: ")
        if q23 in ["1", "2", "3", "4"]:
            if q23 == "4":
                points += 3
            break
        else:
            print("\nPlease, enter 1, 2, 3 or 4 as your answer!")



print(f"\nTotal score: {points}")




if points == 18:
    print("Your IQ is Very Superior! (130+)")
elif 16 <= points <= 17:
    print("Your IQ is Superior! (120-129)")
elif 13 <= points <= 15:
    print("Your IQ is High Average! (110-119)")
elif 7 <= points <= 12:
    print("Your IQ is Average! (90-109)")
elif 4 <= points <= 6:
    print("Your IQ is Low Average! (80-89)")
elif 2 <= points <= 3:
    print("Your IQ is Borderline! (70-79)")
elif 0 <= points <= 1:
    print("Your IQ is Extremely Low! (Less than 70)")
else:
    print("Something went wrong!")

input("\nPress Enter to exit..")
exit()
