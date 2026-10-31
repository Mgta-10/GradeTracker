def creer_notes(note, bareme, coefficient):
    
    notes = {
    "valeur": note,
    "bareme": bareme,
    "coefficient": coefficient
}
    return notes

def calculer_moyenne(notes) :
    if len(notes) == 0 :
        return None
    
    total_notes = 0
    total_coefficients = 0
    
    for note in notes:
        total_notes += note["valeur"] * note["coefficient"]
        total_coefficients += note["coefficient"]
    moyenne = total_notes / total_coefficients
    return moyenne
