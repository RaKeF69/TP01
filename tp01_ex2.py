"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Fanta orange à 2.90
           - Coca cola à 2.90
           - Coca cola light à 2.70
           - Henniez à 2.30
           - Ice Tea à 2.20
           - Limonade à 1.90
           
 Résultats : - Un message d’annulation de la transaction
                 (« Produit inconnu / Monnaie insuffisante »)
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant "santé"

"""

### Déclaration et initialisation des variables
PRIX_FANTA: float = 2.9
PRIX_COCA: float = 2.9
PRIX_COCA_L: float = 2.7
PRIX_HENNIEZ: float = 2.3
PRIX_IT: float = 2.2
PRIX_LIMONADE: float = 1.9
nom_boisson: str = None
thune: float = None
choix_boisson: int = None
change: float = 0
### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Fanta Orange")
print("2. Coca cola")
print("3. Coca cola light")
print("4. Henniez")
print("5. Ice tea")
print("6. Limonade")

thune = float(input("Veuillez introduire votre monnaie : "))
choix_boisson = int(input("Veuillez sélectionner un produit : "))
#On demande les données à l'utilisateur
#Pour chaque choix de boisson possible, on enregistre le change et le nom de la boisson
if choix_boisson == 1:
    nom_boisson = "Fanta Orange"
    change = thune - PRIX_FANTA
elif choix_boisson == 2:
    nom_boisson = "Coca cola"
    change = thune - PRIX_COCA
elif choix_boisson == 3:
    nom_boisson = "Coca cola light"
    change = thune - PRIX_COCA_L
elif choix_boisson == 4:
    nom_boisson = "Henniez"
    change = thune - PRIX_HENNIEZ
elif choix_boisson == 5:
    nom_boisson = "Ice tea"
    change = thune - PRIX_IT
elif choix_boisson == 6:
    nom_boisson = "Limonade"
    change = thune - PRIX_LIMONADE
#afin d'optimiser, on commence avec le message d'erreur parce qu'il n'y en qu'un
if change < 0 or choix_boisson > 6:
    print("Produit inconnu ou monnaie insuffisante")
#On affiche le message d'erreur
else:
    if change > 0:
        print("\tMonnaie à rendre {}".format(change))
    print("{} servi ! Santé !".format(nom_boisson))
#On affiche le résultat demandé
