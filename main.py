import random

MIN_NUMBER = 1
MAX_NUMBER = 10
QUESTION_NUMBER = 4

def question():
    a, b = random.randint(MIN_NUMBER, MAX_NUMBER), random.randint(MIN_NUMBER, MAX_NUMBER)
    _som = a + b
    calculate = input(f"Calcule : {a} + {b} = ")
    int_calculate = int(calculate)
    if int_calculate == _som:
        return True
    return False


points = 0
for i in range(0, QUESTION_NUMBER):
    print(f"Question N°: {i + 1} sur {QUESTION_NUMBER}")
    if question():
        print("Réponse correcte ! Bravo.")
        points += 1
    else:
        print("Réponse incorrecte !")
    print("______________------------_______________")

moy = QUESTION_NUMBER/2
print(f"Ta note est de: {points}/{QUESTION_NUMBER}")
if points == 0:
    print("Tu devrais apprendre tes maths !")
elif points == QUESTION_NUMBER:
    print("Bravo le genie !")
elif points >= moy:
    print("Pas mal !")
else:
    print("Tu peux mieux faire !")
