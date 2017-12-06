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

