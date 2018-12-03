 #!/usr/bin/pythona3

class file_input_reader:
	def __init__(self, file_name):
		self.file_name = file_name

	def get_inputs(self):
		with open(self.file_name) as f:
			line = f.readline()
			while line != '':
				yield line
				line = f.readline()

class list_input_reader:
	def __init__(self):
		self.input_list = []

	def get_inputs(self):
		for _input in self.input_list:
			yield _input

def part_one():
	input_reader = file_input_reader('puzzle_1_input.txt')
	frequency = 0
	for _input in input_reader.get_inputs():
		operation = _input[0:1]
		amplitute = int(_input[1:])
		if operation == '+':
			frequency += amplitute
		elif operation == '-':
			frequency -= amplitute	
	print(frequency)

def part_two():
	input_reader = file_input_reader('puzzle_1_input.txt')
	frequency = 0
	frequency_set = set([0])
	frequency_found = False
	while not frequency_found:
		for _input in input_reader.get_inputs():
			operation = _input[0:1]
			amplitute = int(_input[1:])
			if operation == '+':
				frequency += amplitute
			elif operation == '-':
				frequency -= amplitute

			if frequency not in frequency_set:
				frequency_set.add(frequency)
			else:
				frequency_found = True
				break
	print(frequency)

part_two()
