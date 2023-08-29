# Tirage au sort d'un prix entre 1 et 10 (compris)
import random
cible = random.randint(1, 100)
essai = None
for i in range(1,6):
    # Choix du prix du joueur
    try:
        essai = int(input(f"essai n°{i} - prix ? "))
    except:
        print("Valeur incorecte ...")
        continue #redemarre a l'iteration suivante
    # Message "Bravo" si le prix est trouvé
    if cible == essai:
        print("Bravo !!!")
        break
    # Message "PAS ASSEZ" si le prix est trop bas
    elif cible > essai:
        print("Pas assez !!!")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("Trop eleve !!!")

 # Message "PERDUE" au bout de 5 essais
if cible != essai:
    print("Perdu...")

    # Fin au bout de 5 essais ou si le prix est trouve
