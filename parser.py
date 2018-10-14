def parse(inputs):
	index = 0
	location = 0
	data = [0 for i in range(40000)]
	while(index < len(inputs)):
		# Print character at location
		if inputs[index]['album'] == 'Your Name.':
			print(chr(data[location]))
		# Input characters
		elif inputs[index]['artist'] == 'Coldplay':
			inp = input()
			max = len(inputs[index]['name'].split()[0])
			for i in range(0, max):
				data[location] = ord(inp[i])
				location += 1
			location -= max
		# Move pointer forward
		elif inputs[index]['artist'] == 'Radiohead':
			location += 1
		# Move pointer backward
		elif inputs[index]['artist'] == 'Green Day':
			location -= 1
		# Increment
		elif inputs[index]['album'] == 'Origin of Symmetry':
			data[location] += 1
			if data[location] > 255:
				data[location] -= 256
		# Decrement
		elif inputs[index]['album'] == 'Drones':
			data[location] -= 1
			if data[location] < 0:
				data[location] += 256
		# Analogue of the `[` brainfuck command
		elif 'Run' in inputs[index]['name']:
			if data[location] == 0:
				while 'Talk' not in inputs[index]['name']:
					index += 1
		# Analogue of the `]` brainfuck command
		elif 'Talk' in inputs[index]['name']:
			if data[location] != 0:
				while 'Run' not in inputs[index]['name']:
					index -= 1
		# Take the next song and set the data location to the first letter of it
		elif len(inputs[index]['album'].split()[0]) < 5:
			index += 1
			data[location] = inputs[index]['name'][0]
		# Move to next index
		index += 1
