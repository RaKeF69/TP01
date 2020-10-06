"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.

1J  =  0.738 ft-lb  =  0.239 cal  =  6.24*10^18 eV

Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variables
RATIO_J_FT_LB: float = 0.738
RATIO_J_CAL: float = 0.239
RATIO_J_EV: float = 6.24*10**18
MESSAGE: str = """Valeur en entrée : {} {}
        ---------Conversion---------
        en ft-lb : {} ft-lb
        en calories : {} cal
        en eV : {} eV"""
magnitude_uti: float = None
unit_uti: str = None
conversion_ft_lb: float = None
conversion_cal: float = None
conversion_ev: float = None
conversion_j: float = None
### Séquence d'opération
magnitude_uti = float(input("Quantité d'énergie à convertir: "))
unit_uti = input("Unité (J, ft-lb, cal ou eV): ")
if unit_uti == "J":
    conversion_ft_lb = magnitude_uti * RATIO_J_FT_LB
    conversion_cal = magnitude_uti * RATIO_J_CAL
    conversion_ev = magnitude_uti * RATIO_J_EV
    #conversion des données de l'utilisateur: J à ft-lb, J à cal, J à eV
    print(MESSAGE.format(magnitude_uti, unit_uti, conversion_ft_lb, conversion_cal, conversion_ev))
    # Affichage des données converties
elif unit_uti == "ft-lb":
    conversion_j = magnitude_uti / RATIO_J_FT_LB
    conversion_cal = magnitude_uti / RATIO_J_FT_LB * RATIO_J_CAL
    conversion_ev = magnitude_uti / RATIO_J_FT_LB * RATIO_J_EV
    #conversion des données de l'utilisateur: ft-lb à J, ft-lb à cal, cal à eV
    print(MESSAGE.format(magnitude_uti, unit_uti, conversion_j, conversion_cal, conversion_ev))
    # Affichage des données converties
elif unit_uti == "cal":
    conversion_j = magnitude_uti / RATIO_J_CAL
    conversion_ft_lb = magnitude_uti / RATIO_J_CAL * RATIO_J_FT_LB
    conversion_ev = magnitude_uti / RATIO_J_CAL * RATIO_J_EV
    #conversion des données de l'utilisateur: cal à ft-lb, cal à J, cal à eV
     print(MESSAGE.format(magnitude_uti, unit_uti, conversion_ft_lb, conversion_j, conversion_ev))
    # Affichage des données converties
else:
    conversion_j = magnitude_uti / RATIO_J_EV
    conversion_ft_lb = magnitude_uti / RATIO_J_EV * RATIO_J_FT_LB
    conversion_cal = magnitude_uti / RATIO_J_EV * RATIO_J_CAL
    # Conversion des données de l'utilisateur: eV à J, eV à ft-lb, J à cal
    print(MESSAGE.format(magnitude_uti, unit_uti, conversion_ft_lb, conversion_cal, conversion_j))
    # Affichage des données converties
