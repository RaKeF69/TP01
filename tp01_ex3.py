"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
            - Si l’utilisateur possède une alimentation trop sucrée
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            - Si l’utilisateur consomme trop de sucre, le niveau de risque augmente de 2
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1, le niveau de risque est faible.
            - Si le niveau de risque est de 2 à 3, le niveau de risque est élevé
            - Sinon il est très élevé.

"""
### Déclaration et initialisation des variables
VIEUX: int = 50
VIEILLE: int = 60
COEFF_FUME: int = 2
COEFF_SUCRE: int = 2
COEFF_AGE: int = 1
COEFF_SPORT: int = 1
RISK_LOW: int = 1
RISK_HIGH: int = 3
risk: int = 0
age_uti: int = None
sexe_uti: str = None
fume: str = None
sport: str = None
sucre: str = None
### Séquence d'opération
# On demande les informations à l'utilisateur
fume = input("Etes-vous fumeur ? (oui ou non)")
sport = input("Faits -vous du sport ? (oui ou non)")
sexe_uti = input("Quel est votre sexe ? (h ou f)")
age_uti = int(input("Quel est votre age ? "))
sucre = input("Consommez-vous beaucoup d'aliments sucrés ? (oui ou non)")
# Pour chaque cas, on ajoute ou enlève les valeurs correspondante aux cas
if fume == "oui":
    risk += COEFF_FUME
if sport == "oui":
    risk -= COEFF_SPORT
if (age_uti > VIEUX and sexe_uti == "h") or (age_uti > VIEILLE and sexe_uti == "f"):
    risk += COEFF_AGE
if sucre == "oui":
    risk += COEFF_SUCRE
# On affiche le résultat final
if risk <= RISK_LOW:
    print("Le niveau de risque est faible ({})".format(risk))
elif risk <= RISK_HIGH:
    print("Le niveau de risque est élevé ({})".format(risk))
else:
    print("Le niveau de risque est très élevé ({})".format(risk))
