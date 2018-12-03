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
		self.input_list = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

	def get_inputs(self):
		for _input in self.input_list:
			yield _input

def part_one():
#	input_reader = list_input_reader()
	input_reader = file_input_reader('puzzle_3_input.txt')
	fabric = [[[] for _ in range(1000)] for _ in range(1000)]
	for _input in input_reader.get_inputs():
		id, _, edges, dimentions = _input.split(' ')
		id = id.strip('#')
		left_edge, top_edge = edges.strip(':').split(',')
		width, height = dimentions.split('x')
		for i in range(int(left_edge), int(left_edge) + int(width)):
			for j in range(int(top_edge), int(top_edge) + int(height)):
				fabric[i][j].append(id)

	overlap = 0
	for col in fabric:
		for cell in col:
			if len(cell) > 1:
				overlap += 1
	
	print(overlap)


def part_two():
#	input_reader = list_input_reader()
	input_reader = file_input_reader('puzzle_3_input.txt')
	fabric = [[[] for _ in range(1000)] for _ in range(1000)]
	id_set = set()
	for _input in input_reader.get_inputs():
		id, _, edges, dimentions = _input.split(' ')
		id = id.strip('#')
		id_set.add(id)
		left_edge, top_edge = edges.strip(':').split(',')
		width, height = dimentions.split('x')
		for i in range(int(left_edge), int(left_edge) + int(width)):
			for j in range(int(top_edge), int(top_edge) + int(height)):
				fabric[i][j].append(id)

	overlap = 0
	for col in fabric:
		for cell in col:
			if len(cell) > 1:
				id_set = id_set - set(cell)
	
	print(id_set)

part_one()
part_two()
