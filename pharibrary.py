## Objets
# Joueur (a introduire avec joueur1 = Joueur(pseudo, pv de base, att de base, def de base)
class Joueur:
    def __init__(self, name, health, atk, defense, mp, potion, defplus, mpboost):
        self.name = name
        self.health = health
        self.atk = atk
        self.defense = defense
        self.mp = mp
        self.potion = potion
        self.defplus = defplus
        self.mpboost = mpboost

    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def get_atk(self):
        return self.atk
    def get_defense(self):
        return self.defense
    def get_mp(self):
        return self.mp
    def get_potion(self):
        return self.potion
    def get_defplus(self):
        return self.defplus
    def get_mpboost(self):
        return self.mpboost
    def attack(self, target):  # target -> cible de l'attaue Ex: attack(zombie.health) par exemple
        target -= self.atk
    def attacked(self, degat):  # Utiliser joueur1.degat(nombre de dégats subis)
        self.health -= (degat - self.get_defense())
    def use_potion(self, potion):  # Utiliser joueur1.use_potion(joueur1.get_potion())
        self.health += 5
        potion -= 1
    def use_attplus(self):
        self.atk += 3
    def use_defplus(self):
        self.defense += 1
    def use_mpboost(self):
        self.mp += 20
    def gain_health(self, health):
        self.health += health
    def gain_atk(self, atk):
        self.atk += atk
    def gain_mp(self, mp):
        self.mp += mp

#Adversair
class Adversair:
    def __init__(self, name, health, atk):
        self.name = name
        self.health = health
        self.atk = atk

    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def get_atk(self):
        return self.atk
    def gain_health(self, health):
        self.health += health

## Fonctions
# Système de combat
#joueur1.nomal, joueur1.alvie, joueur1.alatt, joueur1.aldef, zombie.advie, zombie.adatt, joueur1.potion, joueur1.defplus, joueur1.pmpboost

def fight():
    action = ""
    en_vie = 1
    from sys import exit
    aldefcombat = joueur1.get_defense()
    adviecombat = zombie.health
    for loop in range(9999):
        if joueur1.get_health() > 0:
            if adviecombat > 0:
                print()
                print(joueur1.get_name(), ":", joueur1.get_health(), "PV  Potion:", joueur1.get_potion(), "   ", zombie.get_name(), ":", adviecombat, "PV")
                print()
                print("Quelle action veux tu faire ?  ")
                print("[attaque] [sac] [fuite]")
                action = input("")
                print()
                if action == "attaque":
                    print("""Quelle attaque veux tu utiliser ?
   -Attaque faible (1DG -5 PM)           -> faible
   -Attaque intermédiaire (3DG -10 PM)   -> intermédiaire
   -Attaque forte (9DG -30 PM)           -> forte
   -Attaque spéciale (20DG -70 PM)       -> spéciale""")
                    choixattaque = input("Nom de l'attaque : ")
                    if choixattaque == "faible":
                        adviecombat -= joueur1.get_atk()
                    if choixattaque == "intermédiaire":
                        adviecombat -= joueur1.get_atk()
                    if choixattaque == "forte":
                        adviecombat -= joueur1.get_atk()
                    if choixattaque == "spéciale":
                        adviecombat -= joueur1.get_atk()
                    for loop3 in range(20):
                        print()

                elif action == "sac":
                    print("""Sac :
    -potion de soin
    -def+
    -mpboost""")
                    sac = input()
                    if sac == "potion":
                        if joueur1.get_potion() == 0:
                            print("Tu n'as pas de potions de soin.")
                        elif joueur1.get_potion() > 0:
                            print("Vous utilisez la potion et gagnez +5pv.")
                            joueur1.health += 5
                    elif sac == "def+":
                        if joueur1.get_defplus() == 0:
                            print("Tu n'as pas de potions de défense.")
                        elif joueur1.get_defplus() > 0:
                            aldefcombat += 1
                    elif sac == "MPboost":
                        if joueur1.get_mpboost() == 0:
                            print("Tu n'as pas de MPboost.")
                        elif joueur1.get_mpboost() > 0:
                            joueur1.mp += 20

                elif action == "suicide" or "devexit":
                    joueur1.health = 0

                else:
                    print("-----------[ Erreur 002 ]-----------")
                    print()

                # mettre le coup de l'enemi en dessous en gardant cette indentation (pas oublier de retirer la def)
                joueur1.health -= (zombie.get_atk() - aldefcombat)
                print("L'enemi vous a mis un coup de", zombie.get_atk(), "points de dégat.")
        else:
            en_vie = 0

    if en_vie == 0:
        print("Vous êtes mort.")
        if action != "devexit":
            exit()
        if action == "devexit":
            print("\n")

# Système de coffre
def coffre(money):
    def pieces(argent, pieces):
        print("Vous avez gagné", pieces, "pièces !")
        argent += pieces
        print()
        continuer(1)
        return argent

    from random import choice
    raretee = ("classique", "classique", "classique", "classique", "classique", "peu commun", "peu commun", "peu commun", "peu commun", "rare", "rare", "rare", "épic", "épic", "légendaire")
    raretee = choice(raretee)
    print("Ceci est un coffre", raretee, "!")

    if raretee == "classique":
        money = pieces(money, 10)
    elif raretee == "peu commun":
        money = pieces(money, 20)
    elif raretee == "rare":
        money = pieces(money, 30)
    elif raretee == "épic":
        money = pieces(money, 50)
    elif raretee == "légendaire":
        money = pieces(money, 100)
    for loop in range(20):
        print()
    return money

# Système de boutique
def boutique(thune):
    pxepee = 20
    pxlance = 30
    pxbouclier = 50
    print("La boutique est en cours de dev... revenez plus tard ^^")
    print("""-Épée       2att     20pieces
-Lance      3att     30pieces
-bouclier   1def     50pieces""")
    shop=int(input())
    if shop == 1:
        if thune >= pxepee:
            print("Vous avez acheté l'épée !")
            thune = thune - pxepee
            joueur1.atk += 2
        else:
            print("T'as pas assez de pièces")
    elif shop == 2:
        if thune >= pxlance:
            print("Vous avez acheté la lance !")
            thune -= pxlance
            joueur1.atk += 2
        else:
            print("T'as pas assez de pièces")
    elif shop == 3:
        if thune >= pxbouclier:
            print("Vous avez acheté le bouclier !")
            thune -= pxbouclier
            joueur1.defense += 1
        else:
            print("T'as pas assez de pièces")
    continuer(0)

    retour = [thune, joueur1.atk]
    return retour


## Micro fonction:
# Appellez la fonction continuer avec pour unouzero = 1 pour sans les sauts de ligne et unouzero = 0 pour avec
def continuer(unouzero):
    if unouzero == 1:
        input("\n[Appui sur Entrer pour continuer !]")
    elif unouzero == 0:
        input("\n[Appui sur Entrer pour continuer !]")
        for loop in range(200):
            print()

#Initialisation du perso :
#   -Chevalier
#   -Mage
#   - ???
print("""Quelle classe choisies tu ?
    -Le "chevalier", possedant une armure le rendant plus résistant que la moyenne (défense 1)
    -Le "mage" armé de son scèptre et de sont sac à potion (1x potion de soin et 1x potion de MPboost""")
print()
classe = input("Classe : ")
if classe == "chevalier" or classe == "Chevalier" or classe == "C":
    print()
    nom = input("Bien. Mais au fait, quel est ton nom ? ")
    joueur1 = Joueur(nom, 25, 3, 0, 20, 0, 0, 0)
elif classe == "mage" or classe == "Mage" or classe == "m":
    print()
    nom = input("Bien. Mais au fait, quel est ton nom ? ")
    joueur1 = Joueur(nom, 20, 2, 0, 20, 1, 0, 1)
    ok_ide = joueur1
    """### Anti frustration de l'IDE ###
    if ok_ide == joueur1:
        ok_ide = 0"""
else:
    print("Vous n'avez pas entré le nom d'une classe.")
    print("Veullez redéramer de jeu. (Vous pouvez continuer a jouer mais avec les stats minimum)")
    joueur1 = Joueur("Erreur,", 1, 0, 0, 0, 0, 0, 0)
    input()

zombie = Adversair("zombie", 20, 3)
