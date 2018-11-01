def parse(inputs):
	index = 0
	location = 0
	pri = ''
	data = [0 for i in range(40000)]
	while(index < len(inputs)):
		# Print character at location
		if inputs[index]['album'] == 'Your Name.':
			pri += chr(data[location])
		# Input characters
		elif inputs[index]['artist'] == 'Coldplay':
			inp = input()
			max = len(inputs[index]['name'].split()[0])
			for i in range(0, max):
				data[location] = ord(inp[i])
				location += 1
				if location >= 40000:
					location = 0
			location -= max
		# Move pointer forward
		elif inputs[index]['artist'] == 'Radiohead':
			location += 1
			if location >= 40000:
				location = 0
		# Move pointer backward
		elif inputs[index]['artist'] == 'Green Day':
			location -= 1
			if location <= 0:
				location = 39999
		# Increment
		elif inputs[index]['album'] == 'Origin of Symmetry' and inputs[index]['artist'] == 'Muse':
			data[location] += 1
			if data[location] > 255:
				data[location] -= 256
		# Decrement
		elif inputs[index]['album'] == 'Drones' and inputs[index]['artist'] == 'Muse':
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
		elif len(inputs[index]['album'].split()[0]) < 7:
			index += 1
			data[location] = ord(inputs[index]['name'][0])
		# Move to next index
		index += 1

	print(pri)
