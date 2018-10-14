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
			for i in range(index, max):
				data[index] = ord(inputs[index]['artist'].split()[0][i])
				index += 1
		# Move forward
		elif inputs[index]['artist'] == 'Radiohead' :
			index += 1
		# Move backward
		elif inputs[index]['artist'] == "Green Day":
			index -= 1
		index++;
