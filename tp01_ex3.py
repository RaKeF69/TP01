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
risk: int = 0
age_uti: int = None
sexe_uti: str = None
fume: str = None
sport: str = None
sucre: str = None
### Séquence d'opération

fume = input("Etes-vous fumeur ? (oui ou non)")
sport = input("Faits -vous du sport ? (oui ou non)")
sexe_uti = input("Quel est votre sexe ? (h ou f)")
age_uti = int(input("Quel est votre age ? "))
sucre = input("Consommez-vous beaucoup d'aliments sucrés ? (oui ou non)")
if fume == "oui":
    risk += 2
if sport == "oui":
    risk -= 1
if (age_uti > 50 and sexe_uti == "h") or (age_uti > 60 and sexe_uti == "f"):
    risk += 1
if sucre == "oui":
    risk += 2
if risk <= 1:
    print("Le niveau de risque est faible ({})".format(risk))
elif risk <= 3:
    print("Le niveau de risque est élevé ({})".format(risk))
else:
    print("Le niveau de risque est très élevé ({})".format(risk))
