"""
Programme testant si une date, saisie par l'utilisateur, est valide ou non.
Données : Une date saisie par l'utilisateur
Indications:
        Pour pouvoir déterminer si une année est bissextile :       
        	- Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        	- Si elle est multiple de 4, on regarde si elle est multiple de 100.
            	- Si c'est le cas, on regarde si elle est multiple de 400.
      		- Si c'est le cas, l'année est bissextile.
                        		- Sinon, elle n'est pas bissextile.
- Sinon, elle est bissextile.

Résultats : Un message spécifiant si la date entrée est valide.

"""

### Déclaration et initialisation des variables
MESSAGE1: str = "Cette date est valide"
MESSAGE2: str = "Cette date n'est pas valide"
MOIS_31: list = [1, 3, 5, 7, 8, 10, 12]
MOIS_MAX: int = 13
JOURS_MAX: int = 31
FEVRIER: int = 2
JOURS_MAX_FEVRIER: int = 29
ANNEE_BISS: list = [4, 100, 400]
jour_uti: int = None
mois_uti: int = None
annee_uti: int = None

### Séquence d'opération
# On demande à l'utilisateur de rentrer une date
jour_uti = int(input("Saisissez un jour: "))
mois_uti = int(input("Sasissez un mois: "))
annee_uti = int(input("Saisissez une année: "))
### Si les mois sont supérieur à 13 ou les jours supérieur à 31, on affiche le message d'erreur.
### Par soucis d'efficacité, la vérification pour les années bisextiles est exécutée en même temps
if mois_uti > MOIS_MAX or jour_uti > JOURS_MAX or (jour_uti == JOURS_MAX and mois_uti not in list(MOIS_31)) or (mois_uti == FEVRIER and (jour_uti > JOURS_MAX_FEVRIER or not(jour_uti == JOURS_MAX_FEVRIER and ((annee_uti % ANNEE_BISS[0] == 0 and annee_uti % ANNEE_BISS[1] != 0) or annee_uti % ANNEE_BISS[2] == 0)))):
    print(MESSAGE2)
else:
    print(MESSAGE1)
