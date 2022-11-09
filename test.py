# DEBUT

# # print("hello world")
# r = 12000 
# s = 1250
# e = 10
# rh = 230 
# assertUn = (( (365 * 3) / (24 - (16 - 8))) * (rh) > r ) == (e * s < r)# false
# assertPrunUn = (( (365 * 3) / (24 - (16 - 8))) * (rh) > r )# true
# assertPrunDeux = (e * s < r)# false
# #assertionUn = assertDeux == assertTrois # false 
# print(assertDeux == assertTrois)



# assertDeux = (( 365 * 3) / (4 - (12 - 8)) * (rh) > r ) == (e * s < r)# true
# assertPrdeuxUn = (( 365 * 3) / (4 - (12 - 8)) * (rh) > r )# false
# assertPrdeuxDeux = (e * s < r)# false

# x = 3

# def retournerSixPlusTrois():
#     return 6 + 3
# def retournerSixPlusX(x){
#     return 6 + x 
# }

# print("Qui vole un " + retournerSixPlusTrois() + " vole un boeuf ")
# print(retournerSixPlusX(3))

# def add(x,y)
#     return x,y

# def sub(x,y)
#     return x,y 

# def multiply(x,y)
#     return x,y

# def divide(x,y)
#     return x,y

# def modulo(x,y)
#     return x,y

# def calculsalaireparseconde(
# salairehoraire,
# heureparjoursouvrable
# nbjoursouvrable)



# def calculsalairenet(
#     salairebrut, coeff )



# def calculSalaireParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
#     #Assigner a salaireAnnuel, le nombre d'heure travaillées en un an
#     salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable
#     #Calculer, puis assigner a nombreDeSecondeParAn , le nombre de seconde dans une année nom-bisextille 
#     nombreDeSecondeParAn = 60 * 60 * 24 * 365 
#     #Retourner le salaire Annuel divisé par le nombre de seconde par an 
#     return salaireAnnuel / nombreDeSecondeParAn 

# def calculSalaireNet(salaireBrut, coeff):
#     #Assigner SalaireNet, SalaireBrut * coeff 
#     SalaireNet = salaireBrut * (1-coeff)
#     #Return SalaireNet 
#     return SalaireNet 


# def withdrawfees(total, percent):
#     #Calcul du montant des taxes a retirer : 
#     fees = total * (percent / 100)
#     #Retourner la valeur totale moins les taxes 
#     return total - fees

# def calculSalaireNet(salaireBrut, public):
#     #Calculer et retourner le Salaire Net a partir du salaire brut
#     #Return withdrawfees(salaireBrut, coeff)

#     #Si j'occupe un poste de la fonction publique 
#     if public: 
#         #alors je retourne le salaire brut - 15% de taxes 
#         return withdrawfees(salaireBrut, 15)
#     #Sinon ? C'est que je suis travaileur dans le secteur privé, alors je retourne le salaire brut - 23% de douille a l'ancienne 
#     else:
#         return withdrawfees(salaireBrut, 23)

# def divide(x,y)
#     #Si Y est egal a 0, alors la divition est impossible 
#     if y == 0: 
#     #Alors renvoyer un message d'erreur
#         print("bah alors ?")
#         return None 
#     #Sinon 
#     else: 
#     #Retourner le calcul x / y
#         return x/y


# def input():
#Renvoie un caractere de type string au hasard 

#Exercice:
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere 
    #Le caractere doit etre parametrable 

                                                    # def game(yo):
                                                    # # Assigner game a un caractere de input
                                                    #     yo = input()
                                                    #     # Input est egal a la variable yo 
                                                    #     while yo != t:
                                                    #     yo = input()
                                                    #     # Si le caractere est autre que t continué
                                                    #         if yo == t
                                                    #         # Si le caractere est égal a t
                                                    #         print ('bien jouer!')
                                                    #         # Alors ecrir bien jouer 










                                                    # def miniGame(lettreSouhaite)
                                                    #     # Je defini une  variable cararctereAleatoire qui permet dce contenir le caractere généré avec input 
                                                    #     caractereAleatoire = input()
                                                    #     # Tant que cartactereAleatoire est different de la lettre souhaitee 
                                                    #     while caractereAleatoire != lettreSouhaite
                                                    #         # Alors j'attribue a caractereAleatoire, une nouvelle lettre 
                                                    #         caractereAleatoire = input()
                                                        
                                                    #     # Si la lettre souhaitee est egal au carectere 
                                                    #     if caractereAleatoire == lettreSouhaite
                                                    #     # Alors afficher une message de victoire 
                                                    #     print ('vous avez gagné')















                                                    # def input():
                                                    #     char = input()
                                                    #     while (char != t):
                                                    #         if (char == t):








tableau = [0,8,985,54,3,2914,15,194,7]

# Pour Recuperer 15 je prends dans tableau l'index 6
print(tableau[6]) # Afficher 15

len(tableau) # renvoie la longueur de tableau 

prenom = "Lukas"
nom = "Saint-Omer"
idendite = nom + prenom # retourne "LukasSaint-Omer"
idendite = nom + ' ' + prenom # retourne "Lukas Saint-Omer"
*
integerValue = 342 # renvoie 342
stringIntegerValue = str(342) # renvoie "342"


# exercice1 
# faire une fonction qui concatene 2 chaines de caractere, les séparant par une virgule 


def concatWithComma(strA, strB):
# Definir la fonction concatWithComma qui prend comme parametre strA et strB
    stringifiedStrA = str(strA)
    # Assigner a stringifiedStrA le retour de l'execution de la fonction str with comme parametre strA 
    stringifiedStrB = str(strB)
    # Assigner a stringifiedStrB le retour de l'execution de la fonction str with comme parametre strB
    chaineResultat = stringifiedStrA + ", " + stringifiedStrB 
    # Assigner a chaineResultat la concatenation de stringifiedStrA, de la chaine ", " et de stringifiedStrB
    return chaineResultat 
    # Retourne chaineResultat





# exercice2 
# faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaîne de carectere 
# avec l'ensembles des accurence d'un chiffre e.g.: 
# pour tableau = [0,1,1,1,0,1,1,0,1]
# la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hesitez pas a implementer la premiere fonction 



tableau = [0,1,1,1,0,1,1,0,1]
# Definir la fonction findIndexes with comme parametre une liste de tableau et x quelconque
def findIndexes(tableau, x):
    # Definir i egal a 0 
    i = 0 
    # Assigner un caractere vide a chaineRetour
    chaineRetour = ""
    # Tant que i est inferieur a la len du tableau 
    while i < len(tableau):
        # Alors assigner selected a la valeur du tableau 
        selected = tableau[i]
        # Si selected est egal a x 
        if selected == x:
            # Alors 
            # Si isfirst est vrai
            
                # Alors on assigne a chaineRetour la valeur de i
                # Changer isfirst a faux
            # Sinon
                # On assigne a chaineRetour le retour de l'execution de la fonction concatWithComma
                # with comme parametre chaineRetour et i
                chaineRetour = concatWithComma(chaineRetour, i)
           # Assigner i a l'adition de i plus 1
         i = i + 1
      # Retourne chaineRetour 
      return chaineRetour









# FIN