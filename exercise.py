#Save the direction of train 111 into a variable.
#Save the frequency of train 80B into a variable.
#Save the direction of train 610 into a variable.
#Create an empty list. Iterate through each train and add the name of the train into the list if it travels north.
#Do the same thing for trains that travel east.
#You probably just ended up rewriting some of the same code. 
#Move this repeated code into a function that accepts a direction and a list of trains as arguments, and returns a list of just the trains that go in that direction.
#Call this function once for north and once for east in order to DRY up your code.
#Pick one train and add another key/value pair for the first_departure_time. 
#For simplicity, assume the first train always leave on the hour. You can represent this hour as an integer: 6 for 6:00am, 12 for noon, 13 for 1:00pm, etc.
#Now we want to (programmatically) make a new dictionary where the train frequencies are the keys and the values are a list of train names, like so: python { 15: ['72C', '72D', '110', '111'], 5: ['610', '611'], 30: ['80A', '80B'] } 





trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

trains_list = []
trains_list_east = []

train_111 = trains [7]['direction']
train_80B = trains [5]['frequency_in_minutes']
train_610 = trains [2]['direction']
 
print(train_111)
print(train_80B)
print(train_610)


for x in range(0,len(trains)):
	if trains[x]['direction'] == "north":
		trains_list.append((trains[x]['train']))

print(trains_list)


for x in range(0,len(trains)):
	if trains[x]['direction'] == "east":
		trains_list_east.append((trains[x]['train']))

print(trains)

def direction_train(trains, direction):
	list_of_trains = []
	for x in range(0,len(trains)):
		if list_of_trains[x]['direction'] == direction:
			list_of_trains.append(trains[x]['train'])
			return list_of_trains

