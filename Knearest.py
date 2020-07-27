class KNearestNeighbor:
	def __init__(self, dataset, test_row, num_neighbors, row_others):
		self.dataset = dataset 
		self.test_row = test_row
		self.num_neighbors = num_neighbors
		self.row_others = row_others 
		
	#vector distance takes in a specific row, and finds the distance
	# between that row and other rows, or in the case of a dataset, 
	# all other rows in that dataset
	# it scrolls through each column in the test_row aside from the last one, 
	# which should be the classification column,  and compares it to 
	# values in the other specified rows
	# it squares their distances, adds it to the distance value, and takes
	# the square root of this value, to find the distance
	# row_others represents rest of dataset
	def vector_distance(self, dataset, test_row):
		distance = 0.0
		for i in range(len(test_row)-2):
			distance += (test_row[i] - dataset[i])**2
		return distance**2
	#fit takes in vector distance between specific rows and target row,
	# adds them to a tuple, sorts the tuple by distances
	# creates a new list called neighbors, and for specified number of neighbors,
	# scrolls through the distances list, and appends the rows with the lowest
	# vector_distance to the neighbors list, hence giving the nearest neighbors
	# returns the neighbors list

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

	# based on the neighbors list from the fit method,
	# the predict method takes the last column in the neighbors rows, 
	# which should most likely be the classification 0/1 value,
	# takes the highest count of the nearest neighbors to the test row,
	# and returns a prediction value, so if there are 10 1s, and 9 0s, it will
	# predict a value of 1
	def predict(self, dataset, test_row, num_neighbors):
		neighbors = self.fit(dataset, test_row, num_neighbors)
		output = [row[-1] for row in neighbors]
		prediction = max(set(output), key=output.count)
		return prediction
	#we take the majority prediction and compare it to actual predictions,
	# return percentage of correct predictions
	def accuracy(self, dataset, test_row, num_neighbors):
		neighbors = self.fit(dataset, test_row, num_neighbors)
		output = [row[-1] for row in neighbors]
		prediction = max(set(output), key=output.count)
		correct = 0
		for i in range(len(output)):
			if output[i] == prediction:
				correct += 1
		return correct / float(len(output)) * 100.0    
	#in order for this to be most accurate, classification comparison column needs to be on far right, so that 
	# it is not included in the vector distances, and therefore the column does not interfere with the other columns
	# and their interaction with each other

dataset1 = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,1],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,1],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

prediction = KNearestNeighbor(dataset1, dataset1[0], 3, dataset1)
# This will give the majority classification prediction based on number of nearest neighbors

print(prediction.predict(dataset1, dataset1[0], 3))
print(prediction.accuracy(dataset1, dataset1[0], 3))
