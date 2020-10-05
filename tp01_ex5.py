"""
Programme de calcul du prix d'un billet de transport journalier selon plusieurs rabais possibles.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais demi-tarif : 5chf
    Rabais groupe : 2 chf par billet acheté à partir de 4.
    Carte mensuelle : Billet gratuit

Indications :
    - Il est possible de bénéficier d'un rabais demi-tarif et étudiant
    - Le rabais groupe n’est cumulable avec aucun autre rabais
    - Il est possible d'avoir une carte mensuelle permettant d’avoir ce billet gratuitement

Contrainte : 
- Si la personne possède la carte mensuelle, il ne faut pas lui demander
d'autres informations.

"""
### Déclaration et initialisation des variables
PRIX_BILLET: int = 10
RABAIS_ETU: int = 2
RABAIS_DEMI: int = 5
RABAIS_GROUPE: int = 2
TAILLE_GROUPE_MIN: int = 4
MESSAGE: str = "Le prix à payer est: {}CHF"
total: int = 0
carte_mensuelle: str = None
carte_demi: str = None
carte_etu: str = None
nbr_ticket: int = None

### Séquence d'opération
### Si l'utilisateur à la carte mensuelle, on arrète le programme. Sinon on pose les questions supplémentaires
carte_mensuelle = input("Possédez-vous la carte mensuelle ? (oui non) ")
if carte_mensuelle == "oui":
    print(MESSAGE.format(total))
else:
    carte_demi = input("Possédez-vous la carte demi tarif ? (oui non) ")
    carte_etu = input("Possédez-vous la carte étudiante ? (oui non) ")
### Pour chaque cas de figure différent, on éffectue les calculs correspondant
    if carte_etu == "oui" and carte_demi == "oui":
        total = PRIX_BILLET - RABAIS_DEMI - RABAIS_ETU
    elif carte_etu == "oui" and carte_demi == "non":
        total = PRIX_BILLET - RABAIS_ETU
    elif carte_etu == "non" and carte_demi == "oui":
        total = PRIX_BILLET - RABAIS_DEMI
    elif carte_etu == "non" and carte_demi == "non":
        nbr_ticket = int(input("Combien de billets voulez-vous ? "))
# On vérifie que le groupe soit de minimum 4 personnes
        if nbr_ticket >= TAILLE_GROUPE_MIN:
            total = nbr_ticket * (PRIX_BILLET - RABAIS_GROUPE)
        else:
            total = nbr_ticket * PRIX_BILLET
### On affiche le total à payer
    print(MESSAGE.format(total))
