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


def nearest_neighbor_algorithm(first_point, list_of_points):
    
    l = list(list_of_points.keys())
    chemin = list()
    chemin.append(first_point)
    
    #départ sup la valeur de la liste
    j = 0
    for j in range (len(l) - 1):
        if l[j] == first_point:
            del l[j]
            break
    
    dtest = calcul_distance(list_of_points[first_point], list_of_points[l[0]])
    z = 0
    i = 0
    for i in range (len(l) - 1):

        d2 = calcul_distance(list_of_points[first_point], list_of_points[l[i + 1]])
        if d2 < dtest:
                dtest = d2
                z = i + 1
    
    
    #print(dtest)
    d = 0 
    while len(l) != 0:
        
        #print(l[z])
        #print(d)
        pt = l[z]
        chemin.append(pt)
        
        del l[z]
        if len(l) < 1:
            break

        d = calcul_distance(list_of_points[pt], list_of_points[l[0]])
            
        t = 0
        z = 0
        
        for t in range (len(l) - 1):
            d2 = calcul_distance(list_of_points[pt], list_of_points[l[t + 1]])
                    
            if d2 < d:
                d = d2
                z = t + 1
    
    return chemin
    #return list(list_of_points.keys())


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
    
    d1 = calcul_distance(list_of_points[first_point], list_of_points[l[0]])
    z = 0
    i = 0
    for i in range (len(l) - 1):

        d2 = calcul_distance(list_of_points[first_point], list_of_points[l[i + 1]])
        if d2 < d1:
                d1 = d2
                z = i + 1

    d = 0 
    while len(l) != 0:
        
        #print(l[z])
        #print(d)
        pt = l[z]
        chemin.append(pt)
        
        del l[z]
        if len(l) < 1:
            break

        d = d1 + calcul_distance(list_of_points[pt], list_of_points[l[0]])
            
        t = 0
        z = 0
        
        for t in range (len(l) - 1):
            d2 = calcul_distance(list_of_points[pt], list_of_points[l[t + 1]])
                    
            if d2 < d:
                d = d2
                z = t + 1

    return list(list_of_points.keys())'''


def optimal_algorithm(first_point, list_of_points):
    """
        faire tout les chemins possibles et calculer son circuit.. à chaque fois que l'on parcourt un nouveau chemin comparer avec celui d'av
        faire une classe arbre, créer tout les arbres.. parcourir ensuite... et calculer puis comparer
    """

    return list(list_of_points.keys())


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


def test_calcul_distance():
    a = (-3, -2)
    b = (5, 2)

    #result = round(calcul_distance(a,b), 3)
    #return result
    assert round(calcul_distance(a, b), 3) == 8.944

#print(test_calcul_distance())

def test_calcul_min_circuit():
    a = (-3, -2)
    b = (5, 2)
    list_of_points = {'a': a, 'b': b}
    cycle = ['a', 'b']

    #result = round(calcul_circuit(list_of_points, cycle), 3)
    #return result
    assert round(calcul_circuit(list_of_points, cycle), 3) == 17.889


def test_calcul_circuit():
    list_of_points = get_small_list_of_points()

    cycle = list(list_of_points.keys())
    distance = calcul_circuit(list_of_points, cycle)
    
    #result = round(distance, 3)
    #return result
    
    assert round(distance, 3) == 38.483

def test_return_sized():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)

    print(result)

    #assert len(result) == 10
    #assert result[0] == first_point


def test_small_nearest_neighbor():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    
    #assert len(result) == 10
    #assert result[0] == first_point
    #assert round(calcul_circuit(list_of_points, result)) <= 27
    c = round(calcul_circuit(list_of_points, result))
    return c

print(test_small_nearest_neighbor())

'''def test_big_nearest_neighbor():
    """I will test with a lot of points"""
    pass


def test_small_better_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_better_algorithm():
    """I will test with a lot of points"""
    pass


def test_small_optimal_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass
'''