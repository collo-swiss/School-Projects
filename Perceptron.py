"""Gathumbi Collins Githiari
A program that implements Perceptron Learning in Machine Learning."""
import os
from pprint import pprint
os.chdir('D:\\SCI\\Year 3\\Sem 2\\CSC 323 Machine Learning\\Codes')
fdata = open('heart.data.txt')
data = []
weights = []
curr_weights = []
length = 0
def sanitize(sample):
    ab = []
    for val in sample:
        ab.append(float(val))
    return ab
def product(values, weights):
    #vals = ((values * weights for values, weights in zip(values, weights)))
    #print (vals)
    return sum((values * weights for values, weights in zip(values, weights)))

def load_data():
    #key = int(input("Enter index of the output column: "))
    key = 13
    for each in fdata:
        global length
        each = each.strip('\r\n')
        sample = []
        sample.append(each.split(' ',key))
        sample = sample[0]
        output = sample[key]
        sample = sample[:key]
        sample = sanitize(sample)
        length = len(sample)
        #print(sample)
        a = {'values': sample, 'class': output}
        data.append(a)
    return data


load_data()
threshold = 1.5
learning_rate = 0.5
counter = 0
final_weights = []
for a in range(length):
    weights.append(0.0)
    final_weights.append(0.0)

while True:
    print('\n\n' + '*' * 200 + '\n\n')
    error_count = 0
    for each_item in data:
        print(weights)
        result = product(each_item['values'], weights)
        if result > threshold:
            output = 2
        else:
            output = 1
        error = int(each_item['class']) - output
        if error != 0:
            error_count +=1
            for index, elem in enumerate(each_item['values']):
                weights[index] += learning_rate * error * elem
        counter +=1
    if error_count == 0:
        print("Weights learned are:\n" + str(weights) +" and the loop is at: " + str(counter))
        break
