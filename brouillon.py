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
    
    print(matrice)
    
    
    #Dijkstra(matrice, first_point, None)

    
    #return list(list_of_points.keys())

def great_algorithmdico(first_point, list_of_points):
    
    l = list(list_of_points.keys())
    matrice = dict()
    matmat = dict()

    i = 0
    for i in range (len(l)): #génère une matrice

        matrice[l[i]] = matmat
        x = 0
        for x in range (len(l)):
            c = calcul_distance(list_of_points[l[i]], list_of_points[l[x]])
            matrice[l[i]][l[x]] = c
    
    return matrice



def dijkstra(graph,position,dest,visited=[],distances={},predecessors={}):
    
    # On verifie si les 2 points sont dans notre réseau
    if position not in graph:
        print('Le point de départ n\'existe pas.')
    if dest not in graph:
        print('Le point d\'arrivé n\'existe pas.')    
    
    if position != dest:
        # On commence en mettant le point de départ à 0
        if not visited: 
            distances[position]=0
        # Puis nous visitons les points voisins pour calculer leurs distances 
        for neighbor in graph[position] :
            if neighbor not in visited:
                new_distance = distances[position] + graph[position][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = position
        # On marque les points voisins comme étant visités
        visited.append(position)
        # Maintenant que les points voisins sont visités, on choisit le prochain point avec le poids le plus bas.

        unvisited={}   
        for p in graph:
            if p not in visited:
                unvisited[p] = distances.get(p,float('inf'))        
        dijkstra(graph,min(unvisited, key=unvisited.get),dest,visited,distances,predecessors)
    else :
        # Maintenant que tous les points dans le réseau sont visités, on obtient le chemin 
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('Le chemin le plus court (reste a mettre a l\'envers) : '+str(path)+" avec une distance de "+str(distances[dest]))


    


# Le réseau est donné sous la forme de "graph"




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
print(dijkstra(r, 0, 0))

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



