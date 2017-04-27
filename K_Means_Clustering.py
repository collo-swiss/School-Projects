"""Gathumbi Collins Githiari
A program to show to implementation of K Means Clustering Algorithm in Machine Learning"""
from math import sqrt
from pprint import pprint
main_cluster = []
class DataList(list):
    def __init__(self, a_name = '', a_values={}):
        list.__init__([])
        self.name = a_name
        self.values = a_values

    #function to find distance between data points and centroids    
    def distance(self, centroid):
        a = float((self.values['weight']))-(float(centroid.x))
        temp = (squared(float(self.values['weight'])-float(centroid.x))) + squared(float(self.values['pH'])-float(centroid.y))
        temp1 = round(sqrt(temp),2)
        return temp1

class Centroid():
    def __init__(self, first, second):
        self.x = first
        self.y = second

def squared(term):
    return term*term

def start(self):
    global main_cluster
    iteration = 0
    c1 = Centroid(self[0].values['weight'], self[0].values['pH'])
    c2 = Centroid(self[1].values['weight'], self[1].values['pH'])

    d_matrix = [[(self[0].distance(c1)), (self[1].distance(c1)), (self[2].distance(c1)), (self[3].distance(c1))],
                [(self[0].distance(c2)), (self[1].distance(c2)), (self[2].distance(c2)), (self[3].distance(c2))]]
    pprint(d_matrix)
    cluster = clustered(d_matrix)		    #local groups in a list
    main_cluster = cluster
    iteration = iteration + 1
    pprint(cluster)

    final = loop(iteration, cluster, self)
    return final

def loop(counter, cluster, self):
    global main_cluster
    if(counter > 1):
        print("I shouldn't be here")
        print(str(cluster) + " against "+ str(main_cluster))
        if(cluster is main_cluster):
            for index, elem in enumerate(cluster):
                print("Members in cluster " + str(index) + " are: ")
                for b in range(len(elem)):
                    if(elem[b] is 1):
                        print("Name: " + data[b].name + " weight: " + str(data[b].values['weight']) + "  pH: " + str(data[b].values['pH']))
            break
        else:
            new(cluster, self, counter)
    else:
        print(str(cluster) + " against "+ str(main_cluster))
        new(cluster, self, counter)


def new(cluster, self, counter):
    global main_cluster
    main_cluster = cluster 
    centroid1 = calc_centroid(cluster[0], self)     #group 1
    centroid2 = calc_centroid(cluster[1], self)     #group 2

    print("Centroid 1 is x:"+str(centroid1.x) + " y:" + str(centroid1.y))
    print("Centroid 2 is x:" +str(centroid2.x) + " y:" + str(centroid2.y)) 

    d_matrix = [[(self[0].distance(centroid1)), (self[1].distance(centroid1)), (self[2].distance(centroid1)), (self[3].distance(centroid1))],
                [(self[0].distance(centroid2)), (self[1].distance(centroid2)), (self[2].distance(centroid2)), (self[3].distance(centroid2))]]
    pprint(d_matrix)

    counter = counter + 1
    loop(counter, cluster, self)

#function to group data into centroids  
def clustered(d_matrix):
    group1 = [0,0,0,0]
    group2 = [0,0,0,0]
    cluster = []

    for each1 in range(len(d_matrix[0])):
        if(d_matrix[0][int(each1)]) < (d_matrix[1][int(each1)]):
            group1[int(each1)] = 1
        else:
            group2[int(each1)] = 1
        cluster = [group1, group2]
    pprint(cluster)
    return(cluster)

#function to calculate value of centroids       
def calc_centroid(group, data):
    counter = 0
    pos = []
    new_cent = []   

    for a in range(len(group)):
        if group[a] is 1:
            counter = counter + 1
            pos.append(a)
    print(counter)
    if (counter < 2):
        position = pos[0]
        cent = Centroid(data[position].values['weight'], data[position].values['pH'])
    else:
        new_cent = Average(data, counter, pos)
        cent = Centroid(new_cent[0], new_cent[1])
    return (cent)

#function to help in calculating value of centroid by finding the average of points       
def Average(data, counter, pos):
    total_weight = 0
    total_ph = 0
    for x in range(counter):
        a = pos.pop(0)
        total_weight = total_weight + int(data[a].values['weight'])
        total_ph = total_ph +int( data[a].values['pH'])
    print(total_weight)
    print(total_ph)
    return([round(total_weight/counter, 2), round(total_ph/counter, 2)])

#key = int(input("Please enter the parameter for the number of clusters: "))
key = 2
#counter = int(input("How many samples of data are you working with: "))
#data = DataList()
"""for x in range(counter):
    name = input("Please Enter Name of Medicine: ")
    value = input("Please enter a dictionary containing attributes of the medicine: ")
    value = eval(value)
    attr = DataList(name, value)
    data.append(attr)"""
name1 = "A"
value1 = {"weight":"1", "pH":"1"}
A = DataList(name1, value1)
name2 = "B"
value2 = {"weight":"2","pH":"1"}
B = DataList(name2, value2)
data = [A, B]
name1 = "C"
value1 = {"weight":"4", "pH":"3"}
C = DataList(name1, value1)
name2 = "D"
value2 = {"weight":"5","pH":"4"}
D = DataList(name2, value2)
data = [A, B, C, D]

for each in data:
    print("Name: " + each.name + " weight: " + str(each.values['weight']) + "  pH: " + str(each.values['pH']))


cluster = []    
iteration = 0

start(data)

