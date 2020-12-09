class File_Input_Reader:
	def __init__(self, file_name):
		self.file_name = file_name

	def get_input(self):
		with open(self.file_name) as f:
			line = f.readline()
			while line != '':
				yield line
				line = f.readline()
class Module:
	def __init__(self, input_file):
		self.input_reader = File_Input_Reader(input_file)

	def execute(self):
		print('Part One: {}'.format(self.part_one()))
		print('Part Two: {}'.format(self.part_two()))

	__execute = execute

	def part_one(self):
		return ''

	def part_two(self):
		return ''
