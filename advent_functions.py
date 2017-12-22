#!/usr/bin/pythona3

def day_one_part_one(puzzle_input):
	result = 0
	for i in range(0, len(puzzle_input)):
		if puzzle_input[i] == puzzle_input[i-1]:
			result += int(puzzle_input[i])
	print(result)

def day_one_part_two(puzzle_input):
	result = 0
	input_len = len(puzzle_input)
	for i in range(0, input_len):
		if puzzle_input[i] == puzzle_input[i-int(input_len/2)]:
			result += int(puzzle_input[i])
	print(result)

def day_two_part_one(puzzle_input):
	result = 0
	for row in puzzle_input.split('\n'):
		row_min = None
		row_max = None
		for entry in row.split():
			entry_int = int(entry)
			if row_min is None or row_min > entry_int:
				row_min = entry_int
			if row_max is None or row_max < entry_int:
				row_max = entry_int
		result += (row_max - row_min)
	print(result)

def day_two_part_two(puzzle_input):
	result = 0
	for row in puzzle_input.split('\n'):
		row_entries = row.split()
		row_result = None
		for i in range(0, len(row_entries)):
			for j in range(0, len(row_entries)):
				if i != j and int(row_entries[i]) % int(row_entries[j]) == 0:
					row_result = int(int(row_entries[i])/int(row_entries[j]))
					break
			if row_result:
				break
		result += row_result
	print(result)

def day_three_part_one_math(puzzle_input):
	import math
	result = 0
	ring_level = 0
	ring_position = 0
	ring_level = math.sqrt(puzzle_input)
	ring_level = math.ceil(ring_level) // 2
	if ring_level:
		ring_position = puzzle_input - ((((ring_level - 1) * 2) + 1) ** 2)
		ring_position = ring_position % (2 * ring_level)
		ring_position = abs(ring_position - ring_level)
	result = ring_level + ring_position
	print(result)

def day_three_part_one(puzzle_input):
	result = 0
	x = 0
	y = 0
	value = 1
	matrix = {(x, y): value}
	direction = 'right'
	while(value < puzzle_input):
		if direction == 'right':
			x += 1
		elif direction == 'up':
			y += 1
		elif direction == 'left':
			x -= 1
		else:
			y -= 1
		value += 1
		matrix[(x, y)] = value
		if direction == 'right' and (x + y) == 1:
			direction = 'up'
		elif direction == 'up' and x == y:
			direction = 'left'
		elif direction == 'left' and (x + y) == 0:
			direction = 'down'
		elif direction == 'down' and x == y:
			direction = 'right'
	result = abs(x) + abs(y)
	print(result)

def day_three_part_two(puzzle_input):
	result = 0
	x = 0
	y = 0
	value = 1
	matrix = {(x, y): value}
	direction = 'right'
	while(value <= puzzle_input):
		if direction == 'right':
			x += 1
		elif direction == 'up':
			y += 1
		elif direction == 'left':
			x -= 1
		else:
			y -= 1
		value = 0
		if (x+1, y) in matrix:
			value += matrix[(x+1, y)]
		if (x+1, y+1) in matrix:
		  value += matrix[(x+1, y+1)]
		if (x, y+1) in matrix:
		  value += matrix[(x, y+1)]
		if (x-1, y+1) in matrix:
		  value += matrix[(x-1, y+1)]
		if (x-1, y) in matrix:
		  value += matrix[(x-1, y)]
		if (x-1, y-1) in matrix:
		  value += matrix[(x-1, y-1)]
		if (x, y-1) in matrix:
		  value += matrix[(x, y-1)]
		if (x+1, y-1) in matrix:
			value += matrix[(x+1, y-1)]
		matrix[(x, y)] = value
		if direction == 'right' and (x + y) == 1:
			direction = 'up'
		elif direction == 'up' and x == y:
			direction = 'left'
		elif direction == 'left' and (x + y) == 0:
			direction = 'down'
		elif direction == 'down' and x == y:
			direction = 'right'
	result = value
	print(result)

def day_four_part_one(puzzle_input):
	result = 0
	for line in puzzle_input.splitlines():
		line_list = line.split()
		line_set = frozenset(line_list)
		if len(line_list) == len(line_set):
			result += 1
	print(result)
	
def day_four_part_two(puzzle_input):
	result = 0
	for line in puzzle_input.splitlines():
		line_list = line.split()
		line_set = set()
		for word in line_list:
			line_set.add(''.join(sorted(word)))
		if len(line_list) == len(line_set):
			result += 1
	print(result)

def day_five_part_one(puzzle_input):
	result = 0
	jump = 0
	jump_list = puzzle_input.splitlines()
	jump_list_len = len(jump_list)
	for i in range(0, jump_list_len):
		jump_list[i] = int(jump_list[i])
	i = 0
	while(0 <= i < jump_list_len):
		result += 1
		jump = jump_list[i]
		jump_list[i] += 1
		i += jump
	print(result)

def day_five_part_two(puzzle_input):
	result = 0
	jump = 0
	jump_list = puzzle_input.splitlines()
	jump_list_len = len(jump_list)
	for i in range(0, jump_list_len):
		jump_list[i] = int(jump_list[i])
	i = 0
	while(0 <= i < jump_list_len):
		result += 1
		jump = jump_list[i]
		if jump >= 3:
			jump_list[i] -= 1
		else:
			jump_list[i] += 1
		i += jump
	print(result)

def day_six_part_one(puzzle_input):
	result = 0
	memory_banks = [int(i) for i in puzzle_input.split()]
	memory_banks_history = []
	while memory_banks[:] not in memory_banks_history:
		memory_banks_history.append(memory_banks[:])
		largest_bank = 0
		largest_bank_index = 0
		for i in range(0, len(memory_banks)):
			if memory_banks[i] > largest_bank:
				largest_bank = memory_banks[i]
				largest_bank_index = i
		memory_banks[largest_bank_index] = 0
		while largest_bank > 0:
			largest_bank_index = (largest_bank_index + 1) % len(memory_banks)
			memory_banks[largest_bank_index] += 1
			largest_bank -= 1
	result = len(memory_banks_history)
	print(result)

def day_six_part_two(puzzle_input):
	result = 0
	memory_banks = [int(i) for i in puzzle_input.split()]
	memory_banks_history = []
	while memory_banks[:] not in memory_banks_history:
		memory_banks_history.append(memory_banks[:])
		largest_bank = 0
		largest_bank_index = 0
		for i in range(0, len(memory_banks)):
			if memory_banks[i] > largest_bank:
				largest_bank = memory_banks[i]
				largest_bank_index = i
		memory_banks[largest_bank_index] = 0
		while largest_bank > 0:
			largest_bank_index = (largest_bank_index + 1) % len(memory_banks)
			memory_banks[largest_bank_index] += 1
			largest_bank -= 1
	result = len(memory_banks_history) - memory_banks_history.index(memory_banks[:])
	print(result)

class day_event_tree_node():
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.total_weight = None
		self.children_string = children
		self.children = []
	def add_child(self, node):
		self.children.append(node)
	def calculate_weight(self):
		self.total_weight = self.weight
		for child in self.children:
			self.total_weight += child.get_weight()
		return self.total_weight
	def check_balance(self):
		balanced = True
		if len(self.children) > 0:
			base_child_weight = self.children[0].total_weight
			for child in self.children[1:]:
				balanced = base_child_weight == child.total_weight
				if not balanced:
					break
		return balanced
	def find_unbalanced_node(self):
		unbalanced_node = None
		for child in self.children:
			if not child.check_balance():
				unbalanced_node = child.find_unbalanced_node()
		if unbalanced_node is None:
			child_weights = [child.total_weight for child in self.children]
			for weight in child_weights:
				if child_weights.count(weight) == 1:
					for child in self.children:
						if child.total_weight == weight:
							unbalanced_weight = child.name
		return unbalanced_node

def day_seven_part_one(puzzle_input):
	result = None
	disc_list = puzzle_input.splitlines()
	unassigned_tree_node_pool = {}
	for disc in disc_list[:]:
		children = None
		if '->' in disc:
			disc, children = disc.split(' -> ')
		name, weight = disc.split()
		unassigned_tree_node_pool[name] = day_event_tree_node(name, int(weight[1:-1]), children)
	for node in list(unassigned_tree_node_pool.values())[:]:
		if node.children_string:
			for child_name in node.children_string.split(', '):
				node.add_child(unassigned_tree_node_pool.pop(child_name))
	result = list(unassigned_tree_node_pool.keys())
	print(result)

def day_seven_part_two(puzzle_input):
	result = None
	disc_list = puzzle_input.splitlines()
	unassigned_tree_node_pool = {}
	for disc in disc_list[:]:
		children = None
		if '->' in disc:
			disc, children = disc.split(' -> ')
		name, weight = disc.split()
		unassigned_tree_node_pool[name] = day_event_tree_node(name, int(weight[1:-1]), children)
	for node in list(unassigned_tree_node_pool.values())[:]:
		if node.children_string:
			for child_name in node.children_string.split(', '):
				node.add_child(unassigned_tree_node_pool.pop(child_name))
	result = list(unassigned_tree_node_pool.values())[0].find_unbalanced_node()
	print(result)

