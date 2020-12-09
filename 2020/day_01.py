#!/usr/bin/python3

from module_base import Module

class Day_One_Module(Module):
	def part_one(self):
		input_list = [int(i) for i in self.input_reader.get_input()]
		input_indexes = self.find_indexes(input_list)
		return input_list[input_indexes[0]] * input_list[input_indexes[1]]

	def part_two(self):
		input_list = [int(i) for i in self.input_reader.get_input()]
		input_indexes = self.find_three_indexes(input_list)
		return input_list[input_indexes[0]] * input_list[input_indexes[1]] * input_list[input_indexes[2]]

	def find_indexes(self, input_list):
		for i in range(len(input_list)):
			for j in range(i+1, len(input_list)):
				if input_list[i] + input_list[j] == 2020:
					return (i, j)
		return None

	def find_three_indexes(self, input_list):
		for i in range(len(input_list)):
			for j in range(i+1, len(input_list)):
				for k in range(j+1, len(input_list)):
					if input_list[i] + input_list[j] + input_list[k] == 2020:
						return (i, j, k)
		return None


day_one = Day_One_Module('day_one_input.txt')
day_one.execute()
