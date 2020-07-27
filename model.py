from math import sqrt

#calculate the Euclidean distance between two vectors
def vector_distance(row_x, row2):
	distance = 0.0
	for i in range(len(row_x)-1):
		distance += (row_x[i] - row2[i])**2
	return sqrt(distance)

    # you are scrolling through each value in each row, specified by 
    # i in range(len(row_x)-1)
    # and taking the squared difference between the specified row, row_x
    # and all other rows in the dataset, specified by row2
      
    # you are then adding up all of these squared differences, and taking the sqrt
    # of them, to find the overall distances between given rows, as vectors


dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
row0 = dataset[0]
#row0 is the specified row you are looking to take difference in distance of
for row in dataset:
	distance = vector_distance(row0, row)
# row represents scrolling through all other rows in the dataset
# to compare to row0

	print(distance)  


def get_neighbors(dataset, test_row, num_neighbors):
    
	distances = list()
	for row in dataset:

		dist = vector_distance(test_row, row)
		distances.append((row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

    # so basically, create a tuple of rows and their distances, based on
    # difference in distance from euclidean formula. Specify which row to 
    # test from using test_row attribute.
    #sort the distances by the distance, which is index 1 in the tuple

    #create a new list called neighbors, which takes in the num_neighbors
    # attribute, scrolls through, and returns the closest rows, as specified
    # by index 0 in the distances tuple, prints entire rows and their values

close_neighbors = get_neighbors(dataset, dataset[0], 3)

for neighbor in close_neighbors:
	print(neighbor)
#So this function is first finding the closest neighbors to the specific row being
# tested...then it is finding the classification column, which in this case,
# is the last column , represented by row[-1] for each closely related row in neighbors
# then it is finding the most common value through this max(set) function, 
# and the majority value in this column will be returned as a prediction
def predict(dataset, test_row, num_neighbors):
	neighbors = get_neighbors(dataset, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
#the function below is using the above prediction with the same dataset, 
# and for the given prediction, using dataset, column 0, last row, which is the 
# test row's classification number as expected, and "got" represents the 
# prediction from predict
prediction = predict(dataset, dataset[0], 3)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))

class KNearestNeighbor:
    def __init__(self, dataset):
		self.dataset = dataset 
		

	def vector_distance(row_x, row2):
		distance = 0.0
	for i in range(len(row_x)-1):
		distance += (row_x[i] - row2[i])**2
	return sqrt(distance)


	def fit(dataset, test_row, num_neighbors):
    
	distances = list()
	for row in dataset:

		dist = vector_distance(test_row, row)
		distances.append((row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors


	def predict(dataset, test_row, num_neighbors):
	neighbors = fit(dataset, test_row, num_neighbors)
	output = [row[-1] for row in neighbors]
	prediction = max(set(output), key=output.count)
	return prediction


