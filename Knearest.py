class KNearestNeighbor:
	def __init__(self, dataset):
		self.dataset = dataset 
		self.__test_row = 0
		self.__num_neighbors = 0
		
		
	# Scroll through each value in each row, and find the minimum and maximum
	# values for each column in the dataset. Append it to minmax list. 
	# not include last column of dataset, as it should be classification 0/1 column, no need for min/max	
	def Min_Max(self, dataset):
		MinMax = list()
		for i in range(len(dataset[0])-1):
			#the above represents # of columns in dataset
			col_values = [row[i] for row in dataset]
			#the above represents individual values for given columns in each row of dataset
			# basically an index for the column, along with all values
			Min = min(col_values)
			# this takes the minimum value in specific column
			Max = max(col_values)
			# takes maximum value in specific column
			MinMax.append([Min, Max])
			#appends this to a tuple, returns tuple
		return MinMax
	# using MinMaxx, which is the list of min and max values from the min_max function,
	# we can iterate over each value in each row, 
	# normalize the data, and return normalized dataset
	#not normalizing last column in Dataset, as it should be classification row of 0/1 already
	def Normalize(self, dataset):
		MinMaxx = self.Min_Max(dataset)
		for row in dataset:
			for i in range(len(row)-1):
				row[i] = (row[i]-MinMaxx[i][0]) / (MinMaxx[i][1]-MinMaxx[i][0])
		return dataset		
	
	#vector distance takes in a specific row, and finds the distance
	# between that row and other rows, or in the case of a dataset, 
	# all other rows in that dataset
	# it scrolls through each column in the test_row aside from the last one, 
	# which should be the classification column,  and compares it to 
	# values in the other specified rows
	# it squares their distances, adds it to the distance value, and takes
	# the square root of this value, to find the distance
	#not including last column of dataset, as it should be the classification row
	def vector_distance(self, test_row, dataset):
		
		distance = 0.0
		for i in range(len(test_row)-1):
			distance += (test_row[i] - dataset[i])**2
		return distance**2
	#fit takes in a normalized dataset,
	# and then taking the vector distance between specific rows and target row in that dataset,
	# adds them to a tuple, sorts the tuple by distances, smallest at top of list, 
	# creates a new list called neighbors, and for specified number of neighbors,
	# scrolls through the distances list, and appends the rows in order 
	# to the neighbors list, hence giving the nearest neighbors
	# returns the neighbors list

	def fit(self, dataset, test_row, num_neighbors):
		#dataset = self.Normalize(dataset)
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
	def predict(self, dataset, test_row, num_neighbors, neighbors):
		output = [row[-1] for row in neighbors]
		prediction = max(set(output), key=output.count)
		return prediction
	#we take the nearest neighbors from the fit method,
	# take the final column in their specific rows, which must always be the classifying column in dataset,
	# take the predicted classifier, 0, or 1, of the majority nearest neighbors from the predict method,
	# and just compare each classifier value in each nearest neighbor equal to this prediction/ the length of 
	# nearest neighbors, then *100 to make into a percent
	# Of all the neighbors, what percent are the classification of the prediction
	def conclusiveness(self, dataset, test_row, num_neighbors, neighbors, prediction):
		
		output = [row[-1] for row in neighbors]
		correct = 0
		for i in range(len(output)):
			if output[i] == prediction:
				correct += 1
		return correct / float(len(output)) * 100.0    


#Helper Functions to help read in the data, and change string columns into numerical
# Classification columns



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
# convert class column to integers for specific column
string_to_int(dataset, len(dataset[0])-1)
#print(dataset)

prediction = KNearestNeighbor(dataset)
# This will give the majority classification prediction based on number of nearest neighbors

#prediction.Min_Max(dataset)
#x2 = prediction.Normalize(dataset)

#print(x2)
print ("   ")
# create a new record
row = [1,.3,1.5,1.5]
#find nearest neighbors to new data point
x3 = prediction.fit(dataset, row, 9)
print(x3)

#use nearest neighbors to predict new data points classification
x4 = prediction.predict(dataset, row, 9, x3)
#print(x4)
#use conclusiveness to predict potential accuracy of new classification
x5 = prediction.conclusiveness(dataset, row, 9, x3, x4)
print(x4)
print(x5)









#dataset1 = [[2.7810836,2.550537003,0],
#	[1.465489372,2.362125076,1],
#	[1.38807019,1.850220317,1],
#	[3.06407232,3.005305973,0],
#	[7.627531214,2.759262235,1],
#	[5.332441248,2.088626775,1],
#	[6.922596716,1.77106367,1],
#	[8.675418651,-0.242068655,1],
#	[7.673756466,3.508563011,1]]
