
# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math  # https://docs.python.org/3/library/math.html

class Node(object):

    def __init__(self, listOfPoints, origin, visited=None):
        assert origin in listOfPoints.keys()
        if visited is None:
            self.visitedPoints = list()
        else:
            self.visitedPoints = list(visited)
        self.listOfNodes = list()
        self.listOfPoints = listOfPoints
        self.visitedPoints.append(origin)
        

        for point in listOfPoints.keys():
            if not point in self.visitedPoints:
                self.listOfNodes.append(Node(self.listOfPoints, point, self.visitedPoints))
    

    def getPathLength(self):
        assert not self.listOfNodes
        i = calcul_circuit(self.listOfPoints, self.visitedPoints)
        return i
            

    def getBestPath(self):
        if not self.listOfNodes :
            return self.visitedPoints, self.getPathLength()
        else :
            min = math.inf
            l = list()
            for Node in self.listOfNodes:
                (tmpList, tmpLen) = Node.getBestPath()
                if (tmpLen < min):
                    min = tmpLen
                    l = tmpList
            return l, min




def calcul_distance(first_point_value, second_point_value):
    """
        Distance between two points calculation
        first_point_value : tuple (x, y) of a point
        second_point_value : tuple (x, y) of a point
        return a float, the distance between those two point
    """
    return math.sqrt(pow(second_point_value[0]-first_point_value[0],2)+pow(second_point_value[1]-first_point_value[1],2))


def calcul_circuit(list_of_points, cycle):
    """
        Circuit length calculation
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a float, a circuit length
    """
    res=0
    for i in range (len(cycle)-1) :
        first_point_value = list_of_points.get(cycle[i])
        second_point_value =  list_of_points.get(cycle[i+1])
        res+=calcul_distance(first_point_value,second_point_value)

    index_lastpoint=len(cycle)-1
    res += calcul_distance(list_of_points.get(cycle[0]),list_of_points.get(cycle[index_lastpoint]))

    return res


def nearest_neighbor_algorithm(first_point, list_of_points):
    """
    Implement the nearest_neighbor algorithm.
    first_point: label of the first point
    list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
    return a list of point to visit, starting from first_point.
    """
    unvisited = list(list_of_points.keys())
    visitedPoints=list()
    visitedPoints.append(first_point)
    unvisited.remove(first_point)
    a = first_point
    min=calcul_distance(list_of_points.get(a),list_of_points.get(a))

    
    while unvisited :
        for b in range (len(unvisited)):
            distance = calcul_distance(list_of_points.get(a),list_of_points.get(unvisited[b]))
            if(min>distance or min==0):
                min = distance
                tmp = unvisited[b]
        visitedPoints.append(tmp)
        unvisited.remove(tmp)
        min=math.inf
        a=tmp 
    return visitedPoints

     


def great_algorithm(first_point, list_of_points):
    """
        Implement a good algorithm to resolve the case.
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a list of point to visit, starting from first_point.
    """
    unvisited = list(list_of_points.keys())
    visited = list()

    visited.append(first_point)
    unvisited.remove(first_point)

    #for i in range (len(list_of_points)-1):

    return list(list_of_points.keys())


def optimal_algorithm(first_point, list_of_points):
    """
        Implement an optimal algorithm. This solution is the best, but it is slow
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a list of point to visit, starting from first_point.
    """

    n = Node(list_of_points, first_point)
    (l, len) = n.getBestPath()
    l = list(l)
    return l


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


def get_tricky_points():
    list_of_points = {
        0: (0, 0),
        1: (0, 1),
        2: (0, 3),
        3: (0, 11),
        4: (0, -21),
        5: (0, -5),
        6: (0, -1),
    }
    return list_of_points


def test_calcul_distance():
    a = (-3, -2)
    b = (5, 2)

    assert round(calcul_distance(a, b), 3) == 8.944

test_calcul_distance()
def test_calcul_min_circuit():
    a = (-3, -2)
    b = (5, 2)
    list_of_points = {'a': a, 'b': b}
    cycle = ['a', 'b']

    assert round(calcul_circuit(list_of_points, cycle), 3) == 17.889
test_calcul_distance()

def test_calcul_circuit():
    list_of_points = get_small_list_of_points()

    cycle = list(list_of_points.keys())
    distance = calcul_circuit(list_of_points, cycle)
    assert round(distance, 3) == 38.483
test_calcul_circuit()

def test_return_sized():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point
test_return_sized()

def test_small_nearest_neighbor():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) <= 27
test_small_nearest_neighbor()

def test_big_nearest_neighbor():
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
    circuit_cost = calcul_circuit(list_of_points, result)
    assert round(circuit_cost) <= 27
    assert round(circuit_cost, 2) == 24.75
    assert result == [0, 2, 3, 1, 7, 5, 9, 6, 8, 4]
test_small_optimal_algorithm

def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass


def test_tricky_nearest_neighbor():
    list_of_points = get_tricky_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) <= 80

test_tricky_nearest_neighbor()
def test_tricky_better_algorithm():
    list_of_points = get_tricky_points()

    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) < 80


def test_tricky_optimal_algorithm():
    list_of_points = get_tricky_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    print(result)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) == 64
test_tricky_optimal_algorithm()