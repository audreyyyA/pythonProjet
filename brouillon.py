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


def great_algorithm(first_point, list_of_points):
    
    l = list(list_of_points.keys())
    matrice = [0]*len(l)

    i = 0
    for i in range (len(l)): #génère une matrice

        matrice[i] = [0]*len(l)
        x = 0
        for x in range (len(l)):
            c = calcul_distance(list_of_points[l[i]], list_of_points[l[x]])
            matrice[i][x] = c
    
    return matrice
    
    

def great_algorithmdico(first_point, list_of_points):
    
    l = list(list_of_points.keys())
    matrice = dict()
    matmat = dict()

    i = 0
    for i in range (len(l)): #génère une matrice

        matrice[l[i]] = matmat.copy()
        x = 0
        for x in range (len(l)):
            c = calcul_distance(list_of_points[l[i]], list_of_points[l[x]])
            matrice[l[i]][l[x]] = c
    
    return matrice



class Matrice (object):
    def __init__(self,first_point,list_of_points,matrice):
        self.first_point = first_point
        self.list_of_points=list(list_of_points.keys())
        self.matrice=matrice
    
    def dijkstra(self):
        
        chemin = list()
        tableau = dict()
        #initialisation
        chemin.append(self.first_point)
        self.list_of_points.remove(self.first_point)
        tableau = dict(self.matrice[self.first_point])
        del tableau[self.first_point]
        
        chemin.append(min(tableau, key=tableau.get))
        ptmarque = min(tableau, key=tableau.get)
        
        valeurmarque = tableau[ptmarque]
        self.list_of_points.remove(ptmarque)
        del tableau[ptmarque]

        while(len(self.list_of_points) > 1): 
            i = 0
            for i in range (len(self.list_of_points)):
                
                c = self.matrice[ptmarque][self.list_of_points[i]] + valeurmarque
                
                if ( c < tableau[self.list_of_points[i]]):
                    tableau[self.list_of_points[i]] = (self.matrice[ptmarque][self.list_of_points[i]] + valeurmarque)

            ptmarque = min(tableau, key=tableau.get)
            valeurmarque = tableau[ptmarque]
            chemin.append(ptmarque)
            del tableau[ptmarque]
            self.list_of_points.remove(ptmarque)
        
        chemin.append(self.list_of_points[0])
        return chemin









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
r = great_algorithmdico(0, l)
mat = Matrice(0, l, r)
chemin = mat.dijkstra()
print(chemin)
print(round(calcul_circuit(l, chemin)))

