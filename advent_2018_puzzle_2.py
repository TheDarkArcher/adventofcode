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
		self.input_list = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

	def get_inputs(self):
		for _input in self.input_list:
			yield _input

def part_one():
#	input_reader = list_input_reader()
	input_reader = file_input_reader('puzzle_2_input.txt')
	two_letter_codes = 0
	three_letter_codes = 0
	for _input in input_reader.get_inputs():
		letter_dict = {}
		for letter in _input:
			if letter not in letter_dict:
				letter_dict[letter] = 1
			else:
				letter_dict[letter] += 1
		if 2 in letter_dict.values():
			two_letter_codes += 1
		if 3 in letter_dict.values():
			three_letter_codes += 1
	print(two_letter_codes * three_letter_codes)

def part_two():
#	input_reader = list_input_reader()
	input_reader = file_input_reader('puzzle_2_input.txt')
	input_list = []
	for _input in input_reader.get_inputs():
		input_list.append(_input)
	
	for i in range(0, len(input_list)):
		current_code = input_list[i]
		for future_code in input_list[i+1:]:
			code_comparison = [x == y for x, y in zip(current_code, future_code)]
			if code_comparison.count(False) == 1:
				false_index = code_comparison.index(False)
				current_code = current_code[:false_index] + current_code[false_index+1:]
				print(current_code)
				return

part_two()
