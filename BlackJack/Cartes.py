import random

def prends_carte(cartes_utilisées) :
  nv_tirage = True
  y = 0
  while nv_tirage == True :
    y = 0
    chiffre = random.randint(1,104)
    for i in range (0,len(cartes_utilisées)):
      if chiffre == cartes_utilisées[i]:
        y = y + 1
    if y == 0 :
      ctrs_carte = carte(chiffre)
      nv_tirage = False

  if nv_tirage == False :
    return(chiffre,ctrs_carte)

def carte(chiffre) :
  couleur_carte = 1
  if chiffre < 53 :
    if chiffre  < 13 :
      valeur_carte = chiffre
    else :
      if chiffre < 27 :
        couleur_carte = couleur_carte * 2
        valeur_carte = chiffre - 13
      else :
          if chiffre < 40 :
            couleur_carte = couleur_carte * 3
            valeur_carte = chiffre - 26
          else :
            couleur_carte = couleur_carte * 4
            valeur_carte = chiffre - 39
  else :
    if chiffre < 66 :
      valeur_carte = chiffre - 53
    else:
      if chiffre < 79 :
        couleur_carte = couleur_carte * 2
        valeur_carte = chiffre - 65
      else:
        if chiffre < 92 :
          couleur_carte = couleur_carte * 3
          valeur_carte = chiffre - 78
        else:
          couleur_carte = couleur_carte * 4
          valeur_carte = chiffre - 91
  if couleur_carte == 1 :
    couleur_carte = "coeur"
  if couleur_carte == 2 :
    couleur_carte = "carreaux" 
  if couleur_carte == 3:
    couleur_carte = "trèfle"
  if couleur_carte == 4 :
    couleur_carte = "pique"
  return (valeur_carte,couleur_carte)

def spéciale(chiffre,num_carte):

  if chiffre == 1 or chiffre == 14 or chiffre == 27 or chiffre == 40 or chiffre == 53 or chiffre == 66 or chiffre == 79 or chiffre == 92 :
    signe = "as"

  if chiffre == 11 or chiffre == 24 or chiffre == 37 or chiffre == 50 or chiffre == 63 or chiffre == 76 or chiffre == 89 or chiffre == 102 :
    signe = "valet"

  if chiffre == 12 or chiffre == 25 or chiffre == 38 or chiffre == 51 or chiffre == 64 or chiffre == 77 or chiffre == 90 or chiffre == 103 :
    signe = "dame"

  if chiffre == 13 or chiffre == 26 or chiffre == 39 or chiffre == 52 or chiffre == 65 or chiffre == 78 or chiffre == 91 or chiffre == 104 :
    signe = "roi"

  if chiffre != 1 and chiffre != 14 and chiffre != 27 and chiffre != 40 and chiffre != 53 and chiffre != 66 and chiffre != 79 and chiffre != 92 and chiffre != 11 and chiffre != 24 and chiffre != 37 and chiffre != 50 and chiffre != 63 and chiffre != 76 and chiffre != 89 and chiffre != 102 and chiffre != 12 and chiffre != 25 and chiffre != 38 and chiffre != 51 and chiffre != 64 and chiffre != 77 and chiffre != 90 and chiffre != 103 and chiffre != 13 and chiffre != 26 and chiffre != 39 and chiffre != 52 and chiffre != 65 and chiffre != 78 and chiffre != 91 and chiffre != 104:
    signe = "normal"
  
  
  if num_carte == 2:
    if signe == "as" :
      print("La deuxième carte du croupier est l'as de",carte(chiffre)[1])
    if signe == "valet" :
      print("La deuxième carte du croupier est le valet de",carte(chiffre)[1])
    if signe == "dame" :
      print("La deuxième carte du croupier est la dame de",carte(chiffre)[1])
    if signe == "roi" :
      print("La deuxième carte du croupier est le roi de",carte(chiffre)[1])
    if signe == "normal" :
      print("La deuxième carte du croupier est le",carte(chiffre)[0],"de",carte(chiffre)[1])


  if num_carte == 3 :
    if signe == "as" :
      print("La première carte du joueur 1 est l'as de",carte(chiffre)[1])
    if signe == "valet" :
      print("La première carte du joueur 1 est le valet de",carte(chiffre)[1])
    if signe == "dame" :
      print("La première carte du joueur 1 est la dame de",carte(chiffre)[1])
    if signe == "roi" :
      print("La première carte du joueur 1 est le roi de",carte(chiffre)[1])
    if signe == "normal" :
      print("La première carte du Joueur 1 est le",carte(chiffre)[0],"de",carte(chiffre)[1])

  if num_carte == 4:
    if signe == "as" :
      print("La deuxième carte du joueur 1 est l'as de",carte(chiffre)[1])
    if signe == "valet" :
      print("La deuxième carte du joueur 1 est le valet de",carte(chiffre)[1])
    if signe == "dame" :
      print("La deuxième carte du joueur 1 est la dame de",carte(chiffre)[1])
    if signe == "roi" :
      print("La deuxième carte du joueur 1 est le roi de",carte(chiffre)[1])
    if signe == "normal" :
      print("La deuxième carte du Joueur 1 est le",carte(chiffre)[0],"de",carte(chiffre)[1])


def gestion_joueur(num_joueur):
  if num_joueur == 1 :
    joueur1 = input("Choix du nom de Joueur 1 : (10 caractères max.) ") or "Joueur 1"
    if len(joueur1) < 11 :
      print("Le joueur 1 s'appelle", joueur1)
    else:
      print("Nombre de caractères dépassé")