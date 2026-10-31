print("Welcome to GradeTracker !")

from notes import calculer_moyenne, creer_notes 
notes = [ ]

note = float(input("Saisir la note :"))
bareme = float(input("Saisir le barème : "))
coefficient = float(input("Saisir le coefficient : "))

nouvelle_note = creer_notes(note, bareme, coefficient)
notes.append(nouvelle_note)

continuer = input("Saisir oui si tu veux continuer et non si tu veux arrêter : ")

while continuer == "oui":
    note = float(input("Saisir la note : "))
    bareme = float(input("Saisir le barème : "))
    coefficient = float(input("Saisir le coefficient : "))

    nouvelle_note = creer_notes(note, bareme, coefficient)
    notes.append(nouvelle_note)
    continuer = input("Saisir oui si tu veux continuer et non si tu veux arrêter : ")

moyenne = calculer_moyenne(notes)
print("Votre moyenne est : ", moyenne)


