import random 
from Cartes import *
from gestionJetons import *

fin_code = False
étape = 0

while fin_code == False :
  if étape == 0 :
    interface = input("Choix de l'interface texte. (\"texte\" ou \"graphique\") ") or "texte"

    if interface == "texte" :
      étape = étape + 1
      print("En interface texte")

    if interface == "graphique" :
      étape = étape + 1
      print("en interface graphique")

    if interface != "texte" and interface != "graphique" :
      suite_inter = False
      étape = 0
      print("Merci de donner une réponse en minuscules comme les exemples ci-dessus")


  if étape == 1 :
    nbr_joueurs = int(input("Nombre de joueurs : (max 5) ") or "1")
    if nbr_joueurs != 1 and nbr_joueurs != 2 and nbr_joueurs != 3 and nbr_joueurs != 4 and nbr_joueurs != 5 :
      print("merci de choisir un nombre entre 1 et 5")
    else :
      print("Le nombre de Joueurs est", nbr_joueurs)
      étape = étape + 1

  if étape == 2:
    nbr_étapes_noms = 0
    étapeJ1 = False
    étapeJ2 = False
    étapeJ3 = False
    étapeJ4 = False
    étapeJ5 = False
    while étapeJ1 == False :
      joueur1 = input("Choix du nom de Joueur 1 : (10 caractères max.) ") or "Joueur 1"
      if  len(joueur1) < 11 :
        print("Le joueur 1 s'appelle", joueur1)
        étapeJ1 = True
        nbr_étapes_noms = nbr_étapes_noms + 1
      else:
        print("Nombre de caractères dépassé")

    if étapeJ1 == True :
      if nbr_joueurs < 2 :
        étapeJ2 = True
      else :
        while étapeJ2 == False :
            joueur2 = input("Choix du nom de Joueur 2 : (10 caractères max.) ") or "Joueur 2"
            if  len(joueur2) > 9 :
              print("Nombre de caractères dépassé")
            else:
              if joueur2 == joueur1 :
                print(joueur2, "est déja utilisé.")
              else :
                print("Le joueur 2 s'appelle", joueur2)
                nbr_étapes_noms = nbr_étapes_noms + 1
                étapeJ2 = True

      if étapeJ2 == True :
        if nbr_joueurs < 3 :
          étapeJ3 = True
        else:
          while étapeJ3 == False :
            joueur3 = input("Choix du nom de Joueur 3 : (10 caractères max.) ") or "Joueur 3"
            if  len(joueur3) > 9 :
              print("Nombre de caractères dépassé")
            else:
              if joueur3 == joueur1 or joueur3 == joueur2:
                print(joueur3, "est déja utilisé.")
              else :
                print("Le joueur 3 s'appelle", joueur3)
                étapeJ3 = True
                nbr_étapes_noms = nbr_étapes_noms + 1
            
        if étapeJ3 == True :
          if nbr_joueurs < 4 :
            étapeJ4 = True
          else:
            while étapeJ4 == False:
              joueur4 = input("Choix du nom de Joueur 4 : (10 caractères max.) ") or "Joueur 4"
              if  len(joueur4) > 9 :
                print("Nombre de caractères dépassé")
              else:
                 if joueur4 == joueur1 or joueur4 == joueur2 or joueur4 == joueur3 :
                   print(joueur4, "est déja utilisé.")
                 else :
                   print("Le joueur 4 s'appelle", joueur4)
                   étapeJ4 = True
                   nbr_étapes_noms = nbr_étapes_noms + 1

          if étapeJ4 == True :
            if nbr_joueurs < 5 :
              étapeJ5 = True
            else:
              while étapeJ5 == False :
                joueur5 = input("Choix du nom de Joueur 5 : (10 caractères max.) ") or "Joueur 5"
                if  len(joueur5) > 9 :
                  print("Le nombre de caractères est dépassé")
                else:
                  if joueur5 == joueur1 or joueur5 == joueur2 or joueur5 == joueur3 or joueur5 == joueur4 :
                    print(joueur5, "est déja utilisé.")
                  else :
                    print("Le joueur 5 s'appelle", joueur5)
                    étapeJ5 = True
                    nbr_étapes_noms = nbr_étapes_noms + 1
            if étapeJ5 == True :
              if nbr_étapes_noms == nbr_joueurs :
                étape = étape + 1
                print("Préparatifs terminés")

  if étape == 3 :
    
    nbr_jeton1 = mise_jeton(1,0)
    bonne_mise1 = False
    if nbr_joueurs > 1 :
      nbr_jeton2 = mise_jeton(2,0)
      bonne_mise2 = False
    if nbr_joueurs > 2 :
      nbr_jeton3 = mise_jeton(3,0)
      bonne_mise3 = False
    if nbr_joueurs > 3 :
      nbr_jeton4 = mise_jeton(4,0)
      bonne_mise4 = False
    if nbr_joueurs > 4 :
      nbr_jeton5 = mise_jeton(5,0)
      bonne_mise5 = False
    
    

    while bonne_mise1 == False :
      print (joueur1, ", vous avez", nbr_jeton1, "jetons.") 
      print ("Les jetons disponibles sont:", afficher_jetons(1))
      mise = int(input("Donnez votre mise : (parmi les choix ci-dessus) ") or afficher_jetons(1)[-2])
      if mise > nbr_jeton1 :
        print("Montant trop élévé")
      else :
        for a in range(0, len(afficher_jetons(1))):
          if mise == afficher_jetons(1)[a] :
            bonne_mise1 = True
        if bonne_mise1 == False :
          print ("Merci de choisir une mise proposéee")
        else :
          nbr_jeton1 = mise_jeton(1,mise)
          print(joueur1, ", Votre mise est de", mise)
          print(afficher_jetons(1))
          bonne_mise1 = True

    if bonne_mise1 == True :
      while bonne_mise2 == False :
        print (joueur2, ", vous avez", nbr_jeton2, "jetons.") 
        print ("Les jetons disponibles sont:", afficher_jetons(2))
        mise = int(input("Donnez votre mise : (parmi les choix ci-dessus) ") or afficher_jetons(2)[-2])
        if mise > nbr_jeton2 :
          print("Montant trop élévé")
        else :
          for a in range(0, len(afficher_jetons(2))):
            if mise == afficher_jetons(2)[a] :
              bonne_mise2 = True
              if bonne_mise2 == False :
                print ("Merci de choisir une mise proposéee")
              else :
                nbr_jeton2 = mise_jeton(2,mise)
                print(joueur2,", Votre mise est de", mise)
                print(afficher_jetons(2))
                bonne_mise2 = True
                print("mise 2 bonne")

  if étape == 4 :
    print("La partie commence !")

    cartes_utilisées = []

    prends_carte1 = prends_carte(cartes_utilisées)
    cartes_utilisées.append(prends_carte1[0])
    ctrs_carte1 = prends_carte1[1]
    print("La première carte du croupier est cachée.")

    prends_carte2 = prends_carte(cartes_utilisées)
    cartes_utilisées.append(prends_carte2[0])
    ctrs_carte2 = prends_carte2[1]
    spéciale(ctrs_carte2[0],2)

    prends_carte3 = prends_carte(cartes_utilisées)
    cartes_utilisées.append(prends_carte3[0])
    ctrs_carte3 = prends_carte3[1]
    spéciale(ctrs_carte3[0],3)
    
    prends_carte4 = prends_carte(cartes_utilisées)
    cartes_utilisées.append(prends_carte4[0])
    ctrs_carte4 = prends_carte4[1]
    spéciale(ctrs_carte4[0],4)

    valeur_cpr = ctrs_carte1[0] + ctrs_carte2[0]
    valeur_j1 = ctrs_carte3[0] + ctrs_carte4[0]
    if valeur_cpr == 21 :
      print("Le croupier")
    

  if étape == 4 :
    win = False 
    if valeur_cpr == 21:
      print ("Le croupier a un Blackjack")
      if valeur_j1 == 21 :
        win = "push"
      else :
        win = False
    else :
      if valeur_j1 == 21:
        print ("Le joueur 1 a un Blackjack")
        win = "blackjack"
      else :
        if prends_carte2[1][0] < 2:
          print ("Vous avez", jetons, "jetons.")
          if jetons == 0.5 * mise or jetons > 0.5 * mise:
            print ("vous pouvez \"assurer\"")
            assurer = input("Voulez-vous assurer ? (\"oui\", \"non\") ")
            if assurer == "oui" :
              jetons = jetons - (0.5 * mise)
              #je finirai ici plus tard
        print ("vous pouvez \"prendre une carte\"")
        if jetons == mise or jetons > mise :
          print ("vous pouvez \"doubler\"")
          print ("vous pouvez \"séparer\"")
        print ("vous pouvez \"rester\"")
        action_j1 = input("Que voulez vous faire ? (parmi les choix ci-dessus) ") or "rester"
        if action_j1 == "rester" :
          if valeur_j1 == valeur_cpr:
            win = "push"
          else : 
            if valeur_j1 > valeur_cpr:
              win = True
            else : 
              win = False
        if action_j1 == "prendre une carte":
          print ("prends une carte")
              
    print("étape :", étape)
    fin_code = True