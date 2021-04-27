nb_joueurs = 3
somme_initiale = 1000
jetons=[ 1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000 ]
porte_monaie = [somme_initiale for i in range(nb_joueurs)]
mise = [0 for i in range(nb_joueurs)]
tableau_de_resultat = []

def mise_jeton(joueur, jeton):
    global mise
    #le porte monaie perd la valeur du jeton
    porte_monaie[joueur] = porte_monaie[joueur] - jeton
    #ajoute le jeton à la mise
    mise[joueur] += jeton
    return

def afficher_jetons(joueur):
    sous = porte_monaie[joueur]
    jetons_a_jouer = []
    for i in jetons:
        if i<=sous:
            jetons_a_jouer.append(i)
    return jetons_a_jouer

def peut_miser_jeton(joueur, jeton):
    #si le jeton est disponible à la mise -> vrai, faux sinon
    if jeton in afficher_jetons(joueur):
        return True
    else:
        return False

def résultat(somme_carte_croupier,somme_carte_joueur,joueur):
    resultat=""
    if somme_carte_croupier>somme_carte_joueur and somme_carte_croupier<=21 or somme_carte_joueur>21 :
        resultat="Défaite"
    elif somme_carte_croupier<somme_carte_joueur and somme_carte_joueur<=21 or somme_carte_croupier>21 :
        #si victoire on ajoute par défaut 2x la mise au porte monaie du joueur
        porte_monaie[joueur] += 2*mise[joueur]
        resultat="Victoire"
    elif somme_carte_croupier==somme_carte_joueur :
        #si push on re-ajoute par la mise au porte monaie du joueur
        porte_monaie[joueur] += mise[joueur]
        resultat="Push"
    #La mise est vidée (quoi qu'il arrive)
    mise[joueur] = 0
    #On persiste le résultat dans le tableau de resultats
    tableau_de_resultat.append([joueur,resultat,porte_monaie[joueur]])
    return resultat 
        