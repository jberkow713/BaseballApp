class KNearestNeighbor:
	def __init__(self, dataset):
		self.dataset = dataset 
		self.__test_row = 0
		self.__num_neighbors = 0
			
	def Min_Max(self, dataset):
		MinMax = list()
		for i in range(len(dataset[0])-1):
			col_values = [row[i] for row in dataset]
			Min = min(col_values)
			Max = max(col_values)
			MinMax.append([Min, Max])
		return MinMax
	
	def Normalize(self, dataset):
		MinMaxx = self.Min_Max(dataset)
		for row in dataset:
			for i in range(len(row)-1):
				row[i] = (row[i]-MinMaxx[i][0]) / (MinMaxx[i][1]-MinMaxx[i][0])
		return dataset		
		
	def vector_distance(self, test_row, dataset):
		distance = 0.0
		for i in range(len(test_row)-1):
			distance += (test_row[i] - dataset[i])**2
		return distance**(.5)
	
	def fit(self, dataset, test_row, num_neighbors):
		distances = list()
		for row in dataset:
			dist = self.vector_distance(test_row, row)
			distances.append((row, dist))
		distances.sort(key=lambda tup: tup[1])
		neighbors = list()
		for i in range(num_neighbors):
			neighbors.append(distances[i][0])
		return neighbors
    	
	def predict(self, dataset, test_row, num_neighbors, neighbors):
		output = [row[-1] for row in neighbors]
		prediction = max(set(output), key=output.count)
		return prediction
	
	def conclusiveness(self, dataset, test_row, num_neighbors, neighbors, prediction):
		output = [row[-1] for row in neighbors]
		correct = 0
		for i in range(len(output)):
			if output[i] == prediction:
				correct += 1
		return correct / float(len(output)) * 100.0  


from csv import reader
# reading in a csv file, into necessary dataset

def load_dataset(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
# this is turning a string into a float
# so that it can be evaluated in the str_column_to_int method


def string_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())


#youre scrolling through a dataset, row by row, and finding a specific column, 
# in the case of the iris dataset, it is the last column, specified by (len(dataset[0])-1)
# youre taking all specific values in that column, throughout the dataset, and you are storing them in an array,
# Distinct represents the different values in values array
# taking the set values from Distinct, adding them to Dictionary
# you are then making the value in the specific row, equal to the new enumerated Dictionary value
# Hence manually encoding the classification variable



def string_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
dataset = load_dataset('iris.csv')	
for i in range(len(dataset[0])-1):
	string_to_float(dataset, i)
string_to_int(dataset, len(dataset[0])-1)
prediction = KNearestNeighbor(dataset)



row = [8,1,0.2,3.4]

x1 = prediction.fit(dataset, row, 9)
print(x1)

x2 = prediction.predict(dataset, row, 9, x1)

x3 = prediction.conclusiveness(dataset, row, 9, x1, x2)
print(x2)
print(x3)        