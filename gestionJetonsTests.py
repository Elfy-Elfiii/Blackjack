from gestionJetons import *

#Ceci est un fichier permettant de tester les fonctions de gestion des jetons

#afficher_jetons(10000)
print (afficher_jetons(0))
#print (mise)

### Mise de 50 pour le joueur n°0
mise_jeton(0,50)
print (mise)
print (afficher_jetons(0))
#print (peut_miser_jeton(0,5000))
#print (peut_miser_jeton(0,500))
#print (porte_monaie)

###Resultat croupier = 20, joueur = 20, pour le joueur n°0
print (résultat(20,20,2,2,0))

### Mise de 50 pour le joueur 1
mise_jeton(1,50)
###Resultat croupier = 21, joueur = 19, pour le joueur n°1
print (résultat(21,19,2,2,1))

### Mise de 50 pour le joueur 2
mise_jeton(2,50)
###Resultat croupier = 15, joueur = 20, pour le joueur n°2
print (résultat(15,20,2,2,2))

print (porte_monaie)
print (tableau_de_resultat)
#tableau_de_résultat = [n° du joueur,résultat(Victoire,Défaite,Push),somme disponible dans le porte monnaie]

### Mise de 50 pour le joueur 0
mise_jeton(0,50)
###Resultat croupier = 20, joueur = 20, pour le joueur n°0
print (résultat(21,20,2,2,0))

### Mise de 50 pour le joueur 1
mise_jeton(1,50)
assurer(1)
###Resultat croupier = 21, joueur = 19, pour le joueur n°1
print (résultat(21,19,2,2,1))

### Mise de 50 pour le joueur 2
mise_jeton(2,50)
assurer(2)
###Resultat croupier = 15, joueur = 20, pour le joueur n°2
print (résultat(15,20,2,2,2))

print (tableau_de_resultat)

### Mise de 50 pour le joueur 0
mise_jeton(0,50)
###Resultat croupier = 21, joueur = 21, pour le joueur n°0
print (résultat(21,21,3,2,0))

### Mise de 50 pour le joueur 1
mise_jeton(1,50)
###Resultat croupier = 21, joueur = 21, pour le joueur n°1
print (résultat(21,21,2,3,1))

### Mise de 50 pour le joueur 2
mise_jeton(2,50)
###Resultat croupier = 15, joueur = 20, pour le joueur n°2
print (résultat(21,21,3,3,2))

### Mise de 50 pour le joueur 2
mise_jeton(2,50)
###Resultat croupier = 15, joueur = 20, pour le joueur n°2
print (résultat(20,20,3,2,2))
print (tableau_de_resultat)