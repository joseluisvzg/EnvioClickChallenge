class Data():
	def __init__(self, key, name, level, priority):
		self.key = key
		self.name = name
		self.level = level
		self.priority = priority
		self.childs = []

	@property
	def numeric_level(self):
		return self.levels[self.level]

	@property
	def numeric_priority(self):
		return self.priorities[self.priority]

	levels = {
		"one": 10,
		"two": 20,
		"three": 30,
		"four": 40,
		"five": 50
	}

	priorities = {
		"highest": 1,
		"high": 2,
		"medium": 3,
		"low": 4,
		"lowest": 5
	}