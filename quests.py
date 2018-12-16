class Action:
	"""
	an action is a simple block for building quests. It must be both human&machine readable.
	
	An action must be written in this way:

	%actor% %action% [none/action_object] [none/location][none/time]
	Actor can be omitted if it's a person that have took the quest.
	Only Present Simple is allowed.
	"""
	def __init__(self, name, human_descr):
		self.name = name
		self.descr = human_descr
		self.state = False

	def __str__(self):
		return self.name + ': ' + self.descr + ' [{}]'.format('Done' if self.state else 'Uncompleated')

	def compleate():
		self.state = True

class Quest:
	"""
	A quest is a simple task that can be taken and given by any character. 
	"""

	def __init__(self, name, descr, actions):
		self.actions = actions
		self.name = name
		self.descr = descr
		self.state = len(actions)

	def get_curr_action(self):
		if self.state:
			return None
		for el in self.actions:
			if not el.state:
				return el
		return None

	def compleate_action(self):
		if self.state == 0:
			return
		self.state -= 1
		for el in self.actions:
			if not el.state:
				el.state = True
				break

	def __str__(self):
		s = "Quest: " + self.name + " [{}]\n".format('Done' if self.state == 0 else 'Uncompleated')
		for i in range(len(self.actions)):
			s += '  {}. '.format(i + 1) + str(self.actions[i]) + '\n'
		return s

if __name__ == '__main__':
	from copy import deepcopy, copy
	kill = Action('Kill the king', 'Kill the king in 3 days')
	relocate = Action('Come back', 'Bring his head to me')
	reward = Action('Get the reward', 'I give you a reward')
	q = Quest('Assasin of the king', 'Kill the king. Then come back to get the reward', [kill, relocate, reward])
	print(q)
	for i in range(3):
		q.compleate_action()
		print(q)
