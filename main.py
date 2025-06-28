from addition import addition
from soustraction import soustraction
from multiplication import multiplication
from division import division

def afficher_menu():
    print("=== Calculatrice Python ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

while True:
    afficher_menu()
    choix = input("Choisissez une opération (1-5) : ")

    if choix == '5':
        print("Au revoir !")
        break

    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))

        if choix == '1':
            print(f"Résultat : {addition(a, b)}")
        elif choix == '2':
            print(f"Résultat : {soustraction(a, b)}")
        elif choix == '3':
            print(f"Résultat : {multiplication(a, b)}")
        elif choix == '4':
            print(f"Résultat : {division(a, b)}")
        else:
            print("Choix invalide.")
    except Exception as e:
        print(f"Erreur : {e}")
