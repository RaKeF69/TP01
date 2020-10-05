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
jour_uti: int = None
mois_uti: int = None
annee_uti: int = None

### Séquence d'opération
jour_uti = int(input("Saisissez un jour: "))
mois_uti = int(input("Sasissez un mois: "))
annee_uti = int(input("Saisissez une année: "))
if mois_uti > 13 or jour_uti > 31:
    print(MESSAGE2)
elif jour_uti == 31:
    if mois_uti in list(MOIS_31):
        print(MESSAGE1)
elif mois_uti == 2:
    if jour_uti > 28
