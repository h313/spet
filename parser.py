index = 0
location = 0
data = [0 for i in range(40000)]

def parse(inputs):
	while(index < len(inputs)):
		# Print character at location
		if inputs[index]['name'] == 'Dream Lantern':
			print(chr(location))
		# Input characters
		elif inputs[index]['artist'] == 'Coldplay':
			inp = input()
			max = len(inputs[index]['artist'].split()[0]) + index
			for i in range(location, max):
				data[location] = ord(inputs[location]['artist'].split()[0][i])
				location += 1
		# Move pointer forward
		elif inputs[index]['artist'] == 'Radiohead' :
			location += 1
		# Move pointer backward
		elif inputs[index]['artist'] == 'Green Day':
			location -= 1
		# Increment
		elif inputs[index]['album'] == 'Origin of Symmetry':
			data[location] += 1
		# Decrement
		elif inputs[index]['album'] == 'Drones':
			data[location] -= 1
		# Move to next index
		index += 1
