#-*- coding: utf-8 -*-
# Pour s’assurer de la compatiblite entre correcteurs

#Bon courage et bonne lecture

import random
#afficher_grille permet d'afficher le plateau de jeu en fonction de la position des pions stockée dans grille
def afficher_grille(grille):
  print("Joueur blanc = ♘ ; Joueur noir = ♞  ")
  #permet à chaque joueur de repérer ses pions, s'affiche à chaque appel de afficher_grille
  print("")
  repere = ["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  #liste des chiffres à afficher, pour le reperage des cases dans le plateau
  print("| ", end="")
  for numero_ligne in repere:
      print(numero_ligne, " | ", sep="", end="")
  #permet d'afficher un ligne de chiffres pour mieux visualiser les emplacements des cases sur le plateau et faciliter la saisie des coordonnées par l'utilisateur
  print("")
  print("-----------------------------------------")
  chara = 65
  for ligne in grille:
    print("| ", chr(chara), " | ", sep="", end="")
    #permet d'afficher une colonne de lettres pour mieux visualiser les emplacements des cases sur le plateau et faciliter la saisie des coordonnées par les joueurs
    for element in ligne:
      if element == " ":
        print(element, " | ", sep="", end="")
      else:
        if element.couleur == "blanc":
          print("♘ | ", end="")
        else:
          print("♞ | ", end="")
    #permet d'afficher les cases vides et les pions des deux joueurs, en fonction de leur position et de leur couleur, sur le plateau
    print("")
    print("-----------------------------------------")
    #pour separer les cases
    chara += 1
    
  print("")
  return 0

#création de l'objet pion, qui permet d'obtenir la couleur d'un pion (stocker en parametre) et de l'inverser
class pion:
  def __init__(self, couleur):
    self.couleur = couleur
  def inverse_couleur(self) :
    if self.couleur=="blanc" :
      self.couleur="noir"
    else :
      self.couleur="blanc"

#est_dans_grille permet de verifier si les coordonnées entrées sont bien sur le plateau, renvoi un booleen 
def est_dans_grille(coordonnees):
  if len(coordonnees) != 2 or not ("A" <= coordonnees[0] <= "I") or not ("1" <= coordonnees[1] <= "9"):
    return False
  return True

#lecture_coordonnees transforme les coordonnées entrées en une liste de deux entiers, correspondant à la ligne puis à la colonne des coordonnées susnommées
#exemple : A1 devient [0,0]
def lecture_coordonnees(coordonnees):
  coordonnees_lues=[0,0]
  #initialisation
  liste_lettre=["A","B","C","D","E","F","G","H","I"]
  coordonnees_lues[0] = liste_lettre.index(coordonnees[0])
  #transforme la lettre en son indice dans la liste_lettre, donc A=0,B=1... ce qui correspond aussi à l'indice de la ligne dans grille
  coordonnees_lues[1]=int(coordonnees[1])-1
  #il n'y a pas de colonne 0 pour le joueur, mais bien une colonne à indice 0 dans grille
  return coordonnees_lues

#case_vide permet de verifier si une case est vide ou non, renvoi un booleen 
def case_vide(coordonnees, grille):
  ligne=coordonnees[0]
  colonne=coordonnees[1]
  if grille[ligne][colonne] == " ":
    return True
  #la case est vide si ses coordonnées renvoient une case contenant " "
  return False

#configuration_depart définit l'emplacement des pions pour le début du jeu
def configuration_depart():
  grille = []
  for ligne in range(9):
    grille.append([" ", " ", " ", " ", " ", " ", " ", " "," "])
  #on créée une grille vide
  for i in range(3) :
    for y in range(9) :
      grille[i][y]=pion("noir")
  #intègre 3 rangées de pion noir en haut du plateau
  for i in range(3) :
    for y in range(9) :
      grille[(-1)-i][y]=pion("blanc")
  #intègre 3 rangées de pion noir en haut du plateau
  return grille

#jeu_gagnant permet de verifier si un des joueurs a remporté la victoire, si le plateau présente une configuration gagnante pour l'un des joueurs, dans le but de stopper la boucle des tours de jeu, renvoi un booleen indiquant si un de joueurs a gagné
def jeu_gagnant(grille):
  if len([element for ligne in grille for element in ligne if (type(element) != str and element.couleur == "blanc")]) < 6:
    print("♛ Victoire du joueur noir ♛")
    return True
  #si le joueur blanc a moins de 6 pions, le joueur noir gagne
  #on affiche un message de victoire
  elif len([element for ligne in grille for element in ligne if (type(element) != str and element.couleur == "noir")]) < 6:
    print("♕ Victoire du joueur blanc ♕")
    return True
  #si le joueur noir a moins de 6 pions, le joueur blanc gagne
  #on affiche un message de victoire
  return False
  #si aucun joueur n'a gagné, renvoi un False

#la fonction deplacement va deplacer le pion joué en fonction du type de deplacment voulu par le joueur et du plateau, si cela est faisable
def deplacement(type_depla, grille, joueur) :
  coordonnees_depart = input("Saississez les coordonnées du pion que vous voulez déplacer, en commençant par la lettre :\n").upper()
  #saisie des coordonnées par le joueurs
  #le .upper permet au joueur de rentrer des majuscules et des minuscules pour la lettre correspondant à la ligne des coordonnées susnommées
        
  while not est_dans_grille(coordonnees_depart) or case_vide(lecture_coordonnees(coordonnees_depart),grille) or not grille[lecture_coordonnees(coordonnees_depart)[0]][lecture_coordonnees(coordonnees_depart)[1]].couleur==joueur :
    coordonnees_depart = input("Deplacement impossible. \n Saississez les coordonnées du pion que vous voulez déplacer, en commençant par la lettre :\n").upper()
  #verifie si les coordonnées entrées sont bien valides, correspondent à une position sur le plateau, que les coordonnées designent bien un pion de la couleur du joueur dont c'est le tour, et non une case vide.
  #sinon le joueur doit ressaisir de nouvelles coordonnées

  coordonnees_depart=lecture_coordonnees(coordonnees_depart)
  #lit les coordonnées, pour ensuite pouvoir les utiliser
  enchainer="Y"
  #pour pouvoir enchainer les sauts
  while enchainer=="Y":
    coordonnees_arrivee = input("Saississez la case d'arrivée du pion, en commençant par la lettre :").upper()
    while not est_dans_grille(coordonnees_arrivee) or coordonnees_depart==lecture_coordonnees(coordonnees_arrivee) :
      coordonnees_arrivee = input("Deplacement impossible.\n Saississez la case d'arrivée du pion, en commençant par la lettre :\n").upper()
    #verifie si les coordonnées entrées sont bien valides, correspondent à une position sur le plateau, que les coordonnées designent bien une case vide, puis qu'il n'y a pas d'autres pions sur le chemin
    
    coordonnees_arrivee=lecture_coordonnees(coordonnees_arrivee)
    #lit les coordonnées, pour ensuite pouvoir les utiliser

    #pour les deplacements simples
    if type_depla=="D":
      while not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille) and not case_vide(coordonnees_arrivee):
        coordonnees_arrivee = input("Deplacement impossible. \nSaississez la case d'arrivée du pion, en commençant par la lettre :\n").upper()
      grille[coordonnees_depart[0]][coordonnees_depart[1]] = " "
      #le pion disparait de la case de départ, qui devient une case vide
      grille[coordonnees_arrivee[0]][coordonnees_arrivee[1]] = pion(joueur)
      #la case vide d'arrivée devient un pion
      enchainer="N"
    
    #pour les eliminations
    elif type_depla=="E" :
      while not peut_eliminer(coordonnees_depart, coordonnees_arrivee, grille, joueur) :
        coordonnees_arrivee = input("Elimination impossible. \nSaississez la case d'arrivée du pion, en commençant par la lettre :\n").upper()
      grille[coordonnees_depart[0]][coordonnees_depart[1]] = " "
      #le pion disparait de la case de départ, qui devient une case vide
      grille[coordonnees_arrivee[0]][coordonnees_arrivee[1]] = pion(joueur)
      #la case vide d'arrivée devient un pion, en supprimant donc le pion adverse
      enchainer="N"

    #pour les sauts enchainés
    else :
      var_peut_sauter=peut_sauter(coordonnees_depart, coordonnees_arrivee, grille, joueur)
      while not var_peut_sauter[0] and not case_vide(coordonnees_arrivee,grille) :
        coordonnees_arrivee = input("Saut impossible. \nSaississez la case d'arrivée du pion, en commençant par la lettre : \n").upper()
        var_peut_sauter=peut_sauter(coordonnees_depart, coordonnees_arrivee, grille, joueur)
      
      grille[coordonnees_depart[0]][coordonnees_depart[1]] = " "
      #le pion disparait de la case de départ, qui devient une case vide
      grille[var_peut_sauter[1][0]][var_peut_sauter[1][1]].inverse_couleur()
      
      #le pion adverse sauté est retourné
      grille[coordonnees_arrivee[0]][coordonnees_arrivee[1]] = pion(joueur)
      #la case vide d'arrivée devient un pion
      afficher_grille(grille)
      enchainer=input("Voulez-vous enchainer ? Tapez Y pour oui.").upper()
      #on demande au joueur si i veut réaliser un autre saut
      if enchainer =="Y":
        coordonnees_depart=coordonnees_arrivee
        #les coordonnees d'arrivee du pion deviennent celle de départ de son prochain saut
  return grille

#peut_depla_simple va verifier qu'il n'y ai pas de pion sur le chemin entre les coordonnees de depart et d'arrivee, en cas de deplacement simple
def peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
  validation=True
  #on change cette variable si il y a un pion sur le chemin entre les coordonnees de départ et celles d'arrivee

  #vecteur de deplacement entre les coordonnees départ et les coordonnees d'arrivee 
  vecteur=[coordonnees_arrivee[0]-coordonnees_depart[0], coordonnees_arrivee[1]-coordonnees_depart[1]]

  #pour les deplacement à l'horizontale
  if coordonnees_depart[0]==coordonnees_arrivee[0] :
    for i in range(1,abs(vecteur[1])) :
      if type(grille[coordonnees_depart[0]][coordonnees_depart[1]+ ((vecteur[1] > 0) *2 - 1)*i  ])==pion :
        validation=False
  #pour les déplacement à la verticale
  elif coordonnees_depart[1]==coordonnees_arrivee[1] :
    for i in range(1,coordonnees_arrivee[1]-coordonnees_depart[1]) :
      if type(grille[coordonnees_depart[0]+ ((vecteur[0] > 0) *2 - 1)*i  ][coordonnees_depart[1]])==pion :
        validation=False
  #si diagonale partant de du coin en haut a gauche
  elif vecteur[0]==vecteur[1]:
    for i in range(1,abs(vecteur[0])):
      if type(grille[coordonnees_depart[0]+ ((vecteur[1] > 0) *2 - 1)*i  ][coordonnees_depart[1]+ ((vecteur[1] > 0) *2 - 1)*i])==pion :
          validation=False
  #si diagonale partant du coin en bas a gauche
  else :
    for i in range(1,abs(vecteur[0])):
      if type(grille[coordonnees_depart[0]+ ((vecteur[1] > 0) *2 - 1)*i  ][coordonnees_depart[1]-((vecteur[1] > 0) *2 - 1)*i ])==pion :
        validation=False
    
  return validation

#peut_eliminer verifie si on peut peux effectuer une elimination
def peut_eliminer(coordonnees_depart, coordonnees_arrivee, grille, joueur) :
  validation = True

  #verifie que la case contient bien un pion, et qu'il soit de la couleur de l'adversaire
  if type(grille[coordonnees_arrivee[0]][coordonnees_arrivee[1]])==pion and (grille[coordonnees_arrivee[0]][coordonnees_arrivee[1]].inverse_couleur == joueur) :
    validation=False

  vecteur=[coordonnees_arrivee[0]-coordonnees_depart[0], coordonnees_arrivee[1]-coordonnees_depart[1]]
  #on verifie si les coordonnees d'arrivee ne sont pas une case voisine a celle de départ, car c'est interdit par les regles de jeu
  if vecteur[0]==1 or vecteur[0]==-1 or vecteur[1]==1 or vecteur[0]==-1 :
    validation = False
  #vecteur de deplacement entre les coordonnees départ et les coordonnees d'arrivee  
  
  #deplacements horizontaux 
  if coordonnees_depart[0]==coordonnees_arrivee[0]:
    if vecteur[1]>0 :
      coordonnees_arrivee[1]=coordonnees_arrivee[1]-1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[1]=coordonnees_arrivee[1]+1
    else :
      coordonnees_arrivee[1]=coordonnees_arrivee[1]+1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[1]=coordonnees_arrivee[1]-1

  #deplacements verticaux
  elif coordonnees_depart[1]==coordonnees_arrivee[1]:
    if vecteur[0]>0 :
      coordonnees_arrivee[0]=coordonnees_arrivee[0]-1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[0]=coordonnees_arrivee[0]+1
    else :
      coordonnees_arrivee[0]=coordonnees_arrivee[0]+1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[0]=coordonnees_arrivee[0]-1
  
  #deplacements diagonale partant du coin haut gauche
  elif vecteur[1]==vecteur[0]:
    if vecteur[0]>0 :
      coordonnees_arrivee[0]=coordonnees_arrivee[0]-1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]-1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[0]=coordonnees_arrivee[0]+1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]+1
    else :
      coordonnees_arrivee[0]=coordonnees_arrivee[0]+1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]+1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[0]=coordonnees_arrivee[0]-1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]-1
  
  #deplacements diagonale partant du coin haut gauche
  elif vecteur[1]==-(vecteur[0]):
    if vecteur[0]>0 :
      coordonnees_arrivee[0]=coordonnees_arrivee[0]-1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]+1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[0]=coordonnees_arrivee[0]+1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]-1
    else :
      coordonnees_arrivee[0]=coordonnees_arrivee[0]+1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]-1
      if not peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
        validation=False
      coordonnees_arrivee[0]=coordonnees_arrivee[0]-1
      coordonnees_arrivee[1]=coordonnees_arrivee[1]+1
    
  
  return validation

#peut_sauter verifie si on peut effectuer un saut et un retournement
def peut_sauter(coordonnees_depart, coordonnees_arrivee, grille, joueur):
  validation=True
  coordonnees_pion_a_retourner=[0,0]
  #on change cette variable si il y a un pion sur le chemin entre les coordonnees de départ et celles d'arrivee

  #vecteur de deplacement entre les coordonnees départ et les coordonnees d'arrivee 
  vecteur=[coordonnees_arrivee[0]-coordonnees_depart[0], coordonnees_arrivee[1]-coordonnees_depart[1]]

  #pour les deplacement à l'horizontale
  if coordonnees_depart[0]==coordonnees_arrivee[0] :

    #on verfie  qu'il y a bien un pion a retourner, et qu'il est bien de la couleur de l'adversaire
    if (grille[coordonnees_arrivee[0]][coordonnees_arrivee[1]+ ((vecteur[1] > 0) *2 - 1)]==pion(joueur).couleur) or (grille[coordonnees_arrivee[0]+ ((vecteur[1] > 0) *2 - 1)][coordonnees_arrivee[1] + ((vecteur[1] > 0) *2 - 1)]==" ") :
      validation=False

    #on verifie si il n'y a aucun pion sur le chemin, jusqu'au pion a retourner
    elif validation:
      for i in range(1,abs(vecteur[1])) :
        if (type(grille[coordonnees_depart[0]][coordonnees_depart[1]+ ((vecteur[1] > 0) *2 - 1)*i + ((vecteur[1] > 0) *2 - 1)*2 ])==pion) :
          validation=False
    #si les deux conditions precedentes sont verifiées, le saut est correct, donc on recupere les coordonnees du piona retourner
    else :
      coordonnees_pion_a_retourner[0]=coordonnees_arrivee[0]
      coordonnees_pion_a_retourner[1]=coordonnees_arrivee[1] - ((vecteur[1] > 0) *2 - 1)

  #pour les déplacement à la verticale
  elif coordonnees_depart[1]==coordonnees_arrivee[1] :
    #on verfie  qu'il y a bien un pion a retourner, et qu'il est bien de la couleur de l'adversaire
    if (grille[coordonnees_arrivee[0] + ((vecteur[0] > 0) *2 - 1)][coordonnees_arrivee[1]]==pion(joueur).couleur) or (grille[coordonnees_depart[0]+ ((vecteur[0] > 0) *2 - 1)][coordonnees_depart[1]]==" "):
      validation=False
    
    #on verifie si il n'y a aucun pion sur le chemin, jusqu'au pion a retourner
    elif validation :
      for i in range(1,abs(vecteur[0])) :
        if (type(grille[coordonnees_depart[0]+ ((vecteur[1] > 0) *2 - 1)*i - ((vecteur[0] > 0) *2 - 1)*2 ][coordonnees_depart[1]])==pion) :
          validation=False

    #si les deux conditions precedentes sont verifiées, le saut est correct, donc on recupere les coordonnees du piona retourner
    else :
      coordonnees_pion_a_retourner[0]=coordonnees_arrivee[0]- ((vecteur[0] > 0) *2 - 1)
      coordonnees_pion_a_retourner[1]=coordonnees_arrivee[1] 
  #si diagonale partant du coin en haut a gauche
  elif vecteur[0]==vecteur[1]:
    #on verfie  qu'il y a bien un pion a retourner, et qu'il est bien de la couleur de l'adversaire
    if (grille[coordonnees_arrivee[0]+ ((vecteur[1] > 0) *2 - 1)][coordonnees_arrivee[1]+ ((vecteur[1] > 0) *2 - 1)]==pion(joueur).couleur) or (grille[coordonnees_depart[0]+ ((vecteur[1] > 0) *2 - 1)][coordonnees_depart[1] + ((vecteur[1] > 0) *2 - 1)]==" ") :
      validation=False

    #on verifie si il n'y a aucun pion sur le chemin, jusqu'au pion a retourner
    elif validation :  
      for i in range(1,abs(vecteur[0])):
        if type(grille[coordonnees_depart[0]+ ((vecteur[1] > 0) *2 - 1)*i - ((vecteur[1] > 0) *2 - 1)*2  ][coordonnees_depart[1]+ ((vecteur[1] > 0) *2 - 1)*i + ((vecteur[1] > 0) *2 - 1)*2])==pion :
            validation=False
    
    #si les deux conditions precedentes sont verifiées, le saut est correct, donc on recupere les coordonnees du piona retourner
    else :
      coordonnees_pion_a_retourner[0]=coordonnees_arrivee[0]- ((vecteur[1] > 0) *2 - 1)
      coordonnees_pion_a_retourner[1]=coordonnees_arrivee[1] - ((vecteur[1] > 0) *2 - 1)
  #si diagonale partant du coin en bas a gauche
  else :
    #on verfie  qu'il y a bien un pion a retourner, et qu'il est bien de la couleur de l'adversaire
    if (grille[coordonnees_arrivee[0] +((vecteur[1] > 0) *2 - 1)][coordonnees_arrivee[1] - ((vecteur[1] > 0) *2 - 1)]==pion(joueur).couleur) or (grille[coordonnees_depart[0]+ ((vecteur[1] > 0) *2 - 1)][coordonnees_depart[1] + ((vecteur[1] > 0) *2 - 1)]==" ") :
      validation=False
    
    #on verifie si il n'y a aucun pion sur le chemin, jusqu'au pion a retourner
    elif validation :
      for i in range(1,abs(vecteur[0])):
        if type(grille[coordonnees_depart[0]- ((vecteur[1] > 0) *2 - 1)*i + ((vecteur[1] > 0) *2 - 1)*2 ][coordonnees_depart[1]+((vecteur[1] > 0) *2 - 1)*i - ((vecteur[1] > 0) *2 - 1)*2 ])==pion :
          validation=False
    
    #si les deux conditions precedentes sont verifiées, le saut est correct, donc on recupere les coordonnees du piona retourner
    else :
      coordonnees_pion_a_retourner[0]=coordonnees_arrivee[0]+ ((vecteur[1] > 0) *2 - 1)
      coordonnees_pion_a_retourner[1]=coordonnees_arrivee[1] - ((vecteur[1] > 0) *2 - 1)

  return [validation, coordonnees_pion_a_retourner]

#depla_de_IA sert à lister les deplacements possibles de l'IA
def depla_poss_IA(grille, joueur):
  #on intialise la liste des deplacements possibles pour l'IA
  liste_depla_poss=[]
  #pour chaque pion noir dans chaque ligne de la grille
  for ligne in grille :
    for element in ligne :
      #on verifie que le pion est bien celui de l'IA
      if element == pion(joueur).couleur :
        coordonnees_depart=[grille.index(ligne), ligne.index(element)]
        #on definit les coordonnees de depart comme celle du pion étudié
        
        #on verifie les cases à l'horizontale pour savoir si le pion peut y aller
        for i in range(len(grille)-1) :
          coordonnees_arrivee=[coordonnees_depart[0], i]
          if coordonnees_arrivee!=coordonnees_depart :
            #on passe en revue toutes les cases du plateau pour voir quels deplacements sont possibles a partir du pion de départ
            liste_depla_poss=verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur)
        #on verifie les cases à la verticale pour savoir si le pion peut y aller
        for j in range(len(grille)-1) :
          coordonnees_arrivee=[j, coordonnees_depart[1]]
          if coordonnees_arrivee!=coordonnees_depart :
            #on passe en revue toutes les cases du plateau pour voir quels deplacements sont possibles a partir du pion de départ
            liste_depla_poss=verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur)

        coordonnees_arrivee=[0,0]
        #on verifie les cases sur la diagonale partant en haut a gauche pour savoir si le pion peut y aller
        for k in range(1, len(grille)-1) :
          #on passe en revue toutes les cases du plateau pour voir quels deplacements sont possibles a partir du pion de départ
          if len(grille)>coordonnees_arrivee[0]>=0 and len(grille)>coordonnees_arrivee[1]>=0 :
            coordonnees_arrivee=[coordonnees_depart[0]-k, coordonnees_depart[1]-k]
            liste_depla_poss=verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur)
            coordonnees_arrivee=[coordonnees_depart[0]+k, coordonnees_depart[1]+k]
            liste_depla_poss=verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur)

        coordonnees_arrivee=[0,0]
        #on verifie les cases sur la diagonale partant en bas a gauche pour savoir si le pion peut y aller  
        for l in range(1, len(grille)-1) :
          #on passe en revue toutes les cases du plateau pour voir quels deplacements sont possibles a partir du pion de départ
          if len(grille)>coordonnees_arrivee[0]>=0 and len(grille)>coordonnees_arrivee[1]>=0 :
            coordonnees_arrivee=[coordonnees_depart[0]-l, coordonnees_depart[1]+l]
            liste_depla_poss=verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur)
            coordonnees_arrivee=[coordonnees_depart[0]+l, coordonnees_depart[1]-l]
            liste_depla_poss=verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur)

  #on renvoie la liste des deplacements possibles
  return liste_depla_poss
  
#verif_depla_IA de sert a ajouter des deplacements possibles a la liste si ils sont valides
def verif_depl_IA(liste_depla_poss, coordonnees_depart, coordonnees_arrivee, grille, joueur):
  #on regarde si on peut acceder à la case par un deplacement simple
  if peut_depla_simple(coordonnees_depart, coordonnees_arrivee, grille):
    liste_depla_poss.append(["D", coordonnees_depart, coordonnees_arrivee])
  #on regarde si on peut acceder à la case par une elimination
  elif peut_eliminer(coordonnees_depart, coordonnees_arrivee, grille, joueur):
    liste_depla_poss.append(["E", coordonnees_depart, coordonnees_arrivee])
  #on regarde si on peut acceder à la case par un retournement sans enchainement
  elif peut_sauter(coordonnees_depart, coordonnees_arrivee, grille, joueur)[0] :
    liste_depla_poss.append(["R", coordonnees_depart, coordonnees_arrivee, peut_sauter(coordonnees_depart, coordonnees_arrivee, grille, joueur)[1]])
  return liste_depla_poss


#tour_de_IA sert a choisir un deplacement au hasard dans la liste de deplacement possible
def tour_de_IA(grille, joueur):
  #on recupere la liste des deplacements possibles
  liste_depla_poss=depla_poss_IA(grille, joueur)
  #on chosit un deplacement au hasard
  depla_IA=random.choice(liste_depla_poss)
  
  # en fonction du deplacment choisi, on effectue l'action de IA
  #si c'est deplacmement simple
  if depla_IA[0]=="D":
    grille[depla_IA[1][0]][depla_IA[1][1]] = " "
    #le pion disparait de la case de départ, qui devient une case vide
    grille[depla_IA[2][0]][depla_IA[2][1]] = pion(joueur)
    #la case vide d'arrivée devient un pion

  #si c'est une elimination
  elif depla_IA[0]=="E":
    grille[depla_IA[1][0]][depla_IA[1][1]] = " "
    #le pion disparait de la case de départ, qui devient une case vide
    grille[depla_IA[2][0]][depla_IA[2][1]] = pion(joueur)
    #la case vide d'arrivée devient un pion, en supprimant donc le pion adverse
  
  #si c'est un retournement 
  else :
    grille[depla_IA[1][0]][depla_IA[1][1]] = " "
    #le pion disparait de la case de départ, qui devient une case vide
    grille[depla_IA[3][0]][depla_IA[3][1]].inverse_couleur() 
    #le pion adverse sauté est retourné
    grille[depla_IA[2][0]][depla_IA[2][1]] = pion(joueur)
    #la case vide d'arrivée devient un pion
  
  #on renvoit la grille avec le pion déplacé
  return grille
    
def menu_jeu():
  #on demande à l'utilisateur de choisir son mode jeu
  mode_jeu=input("Voulez-vous jouer à deux joueurs ou un joueur contre IA ? \n Tapez J pour joueur contre joueur ou tapez A pour jouer contre IA.").upper()
  while (mode_jeu!="J" and mode_jeu!="A") :
    mode_jeu=input("Entrée incorrecte.\n Voulez-vous jouer à deux joueurs ou contre IA ? \n Tapez J pour joueur contre joueur, tapez A pour jouer contre IA.\n").upper()
    #si l'utilisateur n'entre pas un mode de jeu, il doit recommencer
  return mode_jeu 

def menu_grille():
  #on demande à l'utilisateur de choisir son mode jeu
  type_grille=input("Voulez-vous jouer en début, en milieu, ou en fin de partie? \n Tapez 1 pour debut, 2 pour milieu ou 3 pour fin de partie")
  while (type_grille!="1" and type_grille!="2" and type_grille!="3") :
    type_grille=input("Entrée incorrecte. \n Voulez-vous jouer en début, en milieu, ou en fin de partie? \n Tapez 1 pour debut, 2 pour milieu ou 3 pour fin de partie")
    #si l'utilisateur n'entre pas un mode de jeu, il doit recommencer
  return type_grille

def choix_grille():
  type_grille=menu_grille()

  if type_grille=="1" :
      #on importe la grille de départ
      grille=configuration_depart()
  elif type_grille=="2" :
      #on importe la grille de milieu
      grille=configuration_milieu()
  else : 
      #on importe la grille de fin
      grille=configuration_fin()
  
  return grille
  
#jeu, la fonction permettant de jouer
def jeu():
  mode_jeu=menu_jeu()
  grille=choix_grille()
  #pour le mode JcJ
  if mode_jeu=="J":
    #on affiche la grille de départ
    afficher_grille(grille)
    #permet d'alterner les joueurs
    liste_joueurs=["blanc","noir"]

    while not jeu_gagnant(grille) : #tant qu il n'y a pas victoire
      i=0
      #permet d'alterner les joueurs jusqu'à la victoire de l'un d'eux
      
      while i<2 :
        joueur=liste_joueurs[i]
        #pour l'alternance des joueurs

        print("C'est au tour du Joueur", joueur, ".")
        #On informe le joueur que c'est son tour
        type_depla= input("Saissisez le type de déplacement que vous voulez effectuez ; \n D pour faire un déplacement simple,\n E pour éliminer un pion inverse,\n R pour retourner un ou plusieurs pion(s) inverses : \n ").upper()
        while (type_depla!="R") and (type_depla!="D") and (type_depla!="E") :
          type_depla= input("Saisie inconnue. \n Saissisez le type de déplacement que vous voulez effectuez ;\n D pour faire un déplacement simple,\n E pour éliminer un pion inverse, \nR pour retourner un ou plusieurs pion(s) inverses : \n ").upper()

        grille=deplacement(type_depla, grille, joueur)
        afficher_grille(grille)
        #on affiche la plateau pour montrer aux joueurs le déplacmeent qui a été effectué et leurs conséquences
        if jeu_gagnant(grille):
          break
        #si un des joueurs a gagné, on sort de la boucle sans effectuer le tour de l'autre joueur
        i+=1
        #le tour passe à l'autre joueur
  else :
    #on affiche la grille de départ
    afficher_grille(grille)

    print("Vous jouez les pions blancs.")
    #permet d'alterner entre l'IA et le joueur
    while not jeu_gagnant(grille) : #tant qu il n'y a pas victoire
      joueur="blanc"
      print("C'est à vous de jouer.")
      #On informe le joueur que c'est son tour
      type_depla= input("Saissisez le type de déplacement que vous voulez effectuez ;\n D pour faire un déplacement simple,\n E pour éliminer un pion inverse, \n R pour retourner un ou plusieurs pion(s) inverses : \n ").upper()
      while (type_depla!="R") and (type_depla!="D") and (type_depla!="E") :
        type_depla= input("Saisie inconnue. \n Saissisez le type de déplacement que vous voulez effectuez ; \n D pour faire un déplacement simple, \n E pour éliminer un pion inverse, \n R pour retourner un ou plusieurs pion(s) inverses : \n ").upper()

      grille=deplacement(type_depla, grille, joueur)
      afficher_grille(grille)
      #on affiche la plateau pour montrer aux joueurs le déplacmeent qui a été effectué et leurs conséquences

      if jeu_gagnant(grille):
        break
      #si le joueur a gagné, on sort de la boucle sans effectuer le tour de IA

      joueur="noir"
      #on fait jouer le programme
      grille=tour_de_IA(grille, joueur)
      afficher_grille(grille)
      #on affiche la grille pour que le joueur voit le mouvement fait par IA
      if jeu_gagnant(grille):
        break
      #si IA a gagné, on sort de la boucle sans effectuer le tour du joueur


#configuration_milieu définit l'emplacement des pions pour visualiser une configuration de jeu en cours possible
def configuration_milieu():
  grille = []
  for ligne in range(9):
    grille.append([" ", " ", " ", " ", " ", " ", " ", " "," "])
  #on créée une grille vide

  for i in range(9) :
    grille[0][i]=pion("noir")
  grille[3][3]=pion("noir")
  grille[2][3]=pion("noir")
  grille[6][2]=pion("noir")
  grille[3][7]=pion("noir")

  for x in range(9) :
    grille[-1][x]=pion("blanc")
  grille[-3][3]=pion("blanc")
  grille[-2][3]=pion("blanc")
  grille[-6][2]=pion("blanc")
  grille[-3][6]=pion("blanc")
  return grille

#configuration_fin definit une possibilité de plateau clôturant le jeu par la victoire de l'un des joueurs
def configuration_fin():
  grille = []
  for ligne in range(9):
    grille.append([" ", " ", " ", " ", " ", " ", " ", " "," "])
  #on créée une grille vide
  for i in range(1) :
    for y in range(9) :
      grille[i][y]=pion("noir")
  grille[3][3]=pion("noir")
  grille[2][3]=pion("noir")
  grille[6][2]=pion("noir")
  grille[3][7]=pion("noir")
  grille[-3][3]=pion("blanc")
  grille[-2][3]=pion("blanc")
  grille[-6][2]=pion("blanc")
  grille[-3][6]=pion("blanc")
  grille[-3][5]=pion("blanc")
  return grille

#configuration_presque_fin definit une possibilité de plateau juste avant la clôture du jeu par la victoire de l'un des joueurs
def configuration_presque_fin():
  grille = []
  for ligne in range(9):
    grille.append([" ", " ", " ", " ", " ", " ", " ", " "," "])
  #on créée une grille vide
  for i in range(1) :
    for y in range(9) :
      grille[i][y]=pion("noir")
  grille[3][3]=pion("noir")
  grille[2][3]=pion("noir")
  grille[6][2]=pion("noir")
  grille[3][7]=pion("noir")
  grille[-3][3]=pion("blanc")
  grille[-2][3]=pion("blanc")
  grille[-6][2]=pion("blanc")
  grille[-3][6]=pion("blanc")
  grille[-3][5]=pion("blanc")
  grille[-3][4]=pion("blanc")
  return grille

#test_est_dans_grille permet de tester si est_dans_grille est correct et fonctionne 
def test_est_dans_grille():
 assert not est_dans_grille(""), "coordonnees vides"
 assert not est_dans_grille("tygiTh"), "coordonnees trop longues"
 assert not est_dans_grille("w"), "coordonnees trop courtes"
 assert not est_dans_grille("6K"), "la lettre n'a pas été entrée en premier"
 assert not est_dans_grille("K5"), "lettre inconnue, la case n'est pas sur le plateau"
 assert not est_dans_grille("a0"), "chiffre inconnu, la case n'est pas sur le plateau"

#test_jeu_gagnant verifie si jeu_gagant fonctionne bien et est correct
def test_jeu_gagnant():
  assert jeu_gagnant(configuration_fin()), "Erreur, un des joueurs est sensé gagner "
  assert not jeu_gagnant(configuration_milieu()), "Erreur, il n'y a pas victoire de l'un des joueurs"

#test_case_vide verifie si case_vide fonctionne bien et est correct
def test_case_vide():
  assert case_vide([3,0],configuration_depart()), "La case est en fait vide"
  assert not case_vide([0,0],configuration_depart()), "La case est en fait pleine"

#test_generaux regroupe toutes les fonctions de tests
def tests_generaux():
  test_est_dans_grille() 
  #on teste la fonction est_dans_grille
  test_jeu_gagnant()
  #on teste la fonction jeu_gagnant
  test_case_vide()
  #on teste la fonction case_vide


tests_generaux()
#on effectue les differents tests

print("")
jeu()
#pour jouer au jeu 