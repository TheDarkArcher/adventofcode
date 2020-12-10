#!/usr/bin/python3

from module_base import Module

class Day_Four_Module(Module):
	def __init__(self, input_file):
		super().__init__(input_file)
		self.passport_list = []
		passport = {}
		for line in self.input_reader.get_input():
			line = line.strip()
			if line == '':
				self.passport_list.append(passport)
				passport = {}
			else:
				for entry in line.split(' '):
					key, value = entry.split(':', 2)
					passport[key] = value
		self.passport_list.append(passport)

	def part_one(self):
		valid_count = 0
		required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) 
		for passport in self.passport_list:
			if passport.keys() >= required_keys:
				valid_count = valid_count + 1
		return valid_count


	def part_two(self):
		pass


day = Day_Four_Module('day_four_input.txt')
day.execute()
