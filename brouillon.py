# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math #https://docs.python.org/3/library/math.html

from math import*

def calcul_distance(first_point_value, second_point_value):

    cal1 = ((second_point_value[0]) - (first_point_value[0]))**2
    cal2 = ((second_point_value[1]) - (first_point_value[1]))**2
    result = cal1 + cal2
    
    d = sqrt(result)

    return d



def calcul_circuit(list_of_points, cycle):
    
    res = 0
    i = 0

    for i in range(len(cycle) - 1):
        
        v = cycle[i]
        v2 = cycle[i + 1]
        
        d = calcul_distance(list_of_points[v], list_of_points[v2])
        res = res + d 

    x = cycle[0]
    y = cycle[len(cycle) - 1]
    lastD = calcul_distance(list_of_points[y], list_of_points[x])
    result = res + lastD

    return result


'''def great_algorithm(first_point, list_of_points):
    
    l = list(list_of_points.keys())
    chemin = list()
    chemin.append(first_point)
    
    #départ sup la valeur de la liste
    j = 0
    for j in range (len(l) - 1):
        if l[j] == first_point:
            del l[j]
            break
    
    pt = first_point
    tour1 = True

    while len(l) != 0:
        
        if (tour1 == False): #au premier tour on ne peut pas écraser la valeur de d1 par la suite oui car d sera égal à la distance totale
            pt = kk #car on prend le 2e
            
            chemin.append(z)
            chemin.append(pt) #on rajoute les 2 dans la liste finale
            n = 0
            for n in range (len(l) - 1):
                if (l[n] == pt):
                    del l[n]
            n = 0
            for n in range (len(l) - 1):   
                if (l[n] == z):
                    del l[n]

            ctotal = round(calcul_circuit(list_of_points, chemin))
        
        if len(l) < 1:
            break
        
        i = 0
        z = 0
        k = 0
            
        if len(l) <= 1:
            break
            
        d1 = calcul_distance(list_of_points[pt], list_of_points[l[i]])
        
        j = 0
        dspec = d1 + calcul_distance(list_of_points[l[i]], list_of_points[l[j]])
            
        if l[i] == l[j]:
            dspec = d1 + calcul_distance(list_of_points[l[i]], list_of_points[l[j + 1]])
            k = l[j + 1]

        for j in range (len(l) - 1): #on cherche quelle 2e valeur crée le chemin le + court avec la 1ere valeur étudiée
                
            dnext = d1 + calcul_distance(list_of_points[l[i]], list_of_points[l[j + 1]])
            if(l[j] == l[i]) or (l[j + 1] == l[i]):
                continue
                
            if dnext < dspec:
                dspec = dnext #k z et kk sont les indices de la liste...
                k = l[j + 1]
                
        if i == 0:
            dOficiel = dspec
            z = l[i]
            kk = k

        if i != 0:
            if dspec < dOficiel:
                dOficiel = dspec
                z = l[i]
                kk = k
        
        i=i+1
        tour1 = False

    print('distance finale')
    print(dOficiel)
    print(z)
    print(kk) #à continuer en faisant comme avant mais avec la double boucle...
    
    #d = 0 
   

        #d = d1 + calcul_distance(list_of_points[pt], list_of_points[l[0]])
           
        



    #return chemin
    #return list(list_of_points.keys())'''

class Tree(object):

    def __init__(self, nom, children, list_of_points):
        
        self.nom = nom
        self.children = children
        self.list_of_points = list_of_points
        print(self.nom)
        print(self.children)

    def builtTree(self):

        if len(self.children) == 1:
            newTree = Tree(self.children[0], None, self.list_of_points)
            return 0 
        if len(self.children) > 1:
            i = 0
            for i in range (len(self.children)):
                l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                x=0
                while(l[x] != self.children[i]):
                    del l[0]
                    x+=1
                
                del l[x]

                newTree = Tree(self.children[i], l, self.list_of_points)
                newTree.builtTree()

    '''def betterRoad(self, cal):
        
        c.append(self.nom)
        x = 0
        for x in range (len(self.children)):
            c.append(self.children[x])
            self.nom = children[x]
            cal2 = betterRoad(self) '''
        
    
    def showTree(self):
        print(self.nom)
        print(self.children)

def createLittleTree(i, l, list_of_points):
    l2 = l.copy()
    x=0
    while(l2[x] != l[i]):
        x+=1
                
    del l2[x]

    newTree = Tree(l[i], l2, list_of_points)


def optimal_algorithm(first_point, list_of_points):
    
    l = list(list_of_points.keys())

    x = 0
    for x in range (len(l) - 1):
        if l[x] == first_point:
            del l[x]
            break
    
    '''for i in range (len(l)):
        createLittleTree(i, l, list_of_points)'''
    
    
    newTree = Tree(first_point, l, list_of_points)
    newTree.builtTree()
    #return result
    #return list(list_of_points.keys())


def autreFonction(listlist, nb, l, chemin, liste, c): #enlever nb

    taille = len(l) 
    #l2 = l.copy() ptt plus besoins... au lieu d eprendre l2, utiliser listlist son index = etape + 1 et on enlève les éléments comme ça
    
    etape = nb + 1#ptt inutile pour etape...
    
    while((listlist[nb] != None)):   #avant c'était l2
        #condition qui vérifie si le pt existe dans le chemin 
        i = 0
        for i in range (taille):
            if ((l[i] in chemin) and len(chemin) != (taille + 1)):
                #nb = nb+1
                continue 
            
            elif (len(chemin) != (taille + 1)):
                chemin.append(l[i])
                #del l2[i]
                del listlist[etape - 1][i] #pb de del...
                nb = nb+1

            elif (l[i] in chemin):
                if (chemin.index(l[i]) < etape):
                    continue
                else:    
                    chemin[etape] = l[i] #puis del de l2 grâce à une boucle
                    x = 0
                    del listlist[etape - 1][x]
                       
            else:  
                chemin[etape] = l[i] #puis del de l2 grâce à une boucle
                x = 0
                del listlist[etape - 1][x]
                '''for x in range (len(listlist[nb]) - 1): #on enlève le -1
                    if listlist[nb - 1][x] == l[i]:#av l2[x]
                        #del l2[x]
                        del listlist[nb - 1][x]
                        break  '''     
            
            if (etape != (len(l))):
                c1 = autreFonction(listlist, nb, l, chemin, liste, c) #trouver un moyen de garder l2
                #ou créer autant de listes diff dès le départ que l'on numérote selon l'étape..
            
            if (nb >= (len(l))): #car nb dépassera 
                c1 = calcul_circuit(liste, chemin)
                nextRoad = True
                if c1<c:
                    c=c1
                break
        
        if (nextRoad == True):
            nextRoad = False
            break 
    return c


def get_small_list_of_points():
    list_of_points = {
        0: (1, 3),
        1: (2, 5),
        2: (0, 6),
        3: (1, 7),
        4: (5, 1),
        5: (5, 5),
        6: (6, 3),
        7: (4, 4),
        8: (7, 0),
        9: (6, 6)
    }
    return list_of_points

l = get_small_list_of_points()

def test_small_better_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    #result = great_algorithm(first_point, list_of_points)
    print(great_algorithm(first_point, list_of_points))
    #c = round(calcul_circuit(list_of_points, result))
    #return c
    #assert len(result) == 10
    #assert result[0] == first_point

#print(test_small_better_algorithm())
print(optimal_algorithm(0, l))

'''print(calcul_distance(l[0], l[1]))
print(calcul_distance(l[0], l[2]))
print(calcul_distance(l[0], l[3]))
print(calcul_distance(l[0], l[4]))
print(calcul_distance(l[0], l[5]))
print(calcul_distance(l[0], l[6]))
print(calcul_distance(l[0], l[7]))
print(calcul_distance(l[0], l[8]))
print(calcul_distance(l[0], l[9]))'''
#print(calcul_distance(l[0], l[0]))

#2.23606797749979 (1) - 2.23606797749979 (2) - 1.4142135623730951 (3) - 4.242640687119285 (7) - 1.4142135623730951 (5) - 1.4142135623730951 (9) - 
#3.0 (6) - 2.23606797749979 (4) - 2.23606797749979 (8) - 6.708203932499369 (0)
'''t = 0
        z = 0
        
        for t in range (len(l) - 1):
            d2 = d1 + calcul_distance(list_of_points[pt], list_of_points[l[t + 1]])
            
            if d2 < d:
                d = d2
                z = t + 1'''

'''class Tree:

    def __init__(first_point, points):
        self.first = first_point
        self.points = points 
    
    def createAllTree(self):

        l = self.points
    
        #départ sup la valeur de la liste
        j = 0
        for j in range (len(l) - 1):
            if l[j] == self.first_point:
                del l[j]
                break
        
        i = 0
        for i in range (len(l) - 1):
            t = self.points
            tInterm = t
            j = i
            for j in range (len(l) - 2):
                del tInterm[j]

                if (len(tInterm) > 0):
                    t[j] = Tree(0,tInterm)
                    t = t[j]

        return self.dico
    
    def showAllTree():

        return 0


dico = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
t = Tree(0, dico)
print(t.createAllTree())'''



