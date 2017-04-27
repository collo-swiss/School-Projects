"""Gathumbi Collins Githiari
A program to show to implement K Nearest Neighbour Algorithm in Machine Learning"""
def squared(term):
    return term*term

key = int(input("Please enter the parameter of the nearest neighbour: "))
data = []
counterA=0
counterB=0
#sample to be learned from
fdata = input("Enter lists containing your learning data: ")
#data = [[7, 7, "Bad"], [7, 4, "Bad"], [3, 4, "Good"], [1, 4, "Good"]]
data = eval(fdata)

#data to be queried against
query = input("Enter the list containing the new data to be queried: ")
query = eval(query)

#Find the distance between the query and all instances
for sample in data:
    sample.append(squared(sample[0]-query[0]) + squared(sample[1]-query[1]))
    
#Save the different types of classifications
termA = (data[1][2])
for data_sample in data:
    if data_sample[2] is not termA:
        termB = data_sample[2]
    
#Sort the lists based on the distance
data.sort(key=lambda each: each[3])

#Get the attributes of the neighbouring samples only.
for x in range(key):
    print(data[x])
    if(data[x][2] is termA):
        counterA = counterA +1
    elif(data[x][2] is termB):
        counterB = counterB +1

#Get the predominant feature in the neighbours and assign it to the query       
if(counterA>counterB):
    query.append(termA)
else:
    query.append(termB)
    
print("The attribute of the query is: "+str(query))
