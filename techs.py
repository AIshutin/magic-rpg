class DescriptionException(Exception):
	def __init__(self, text):
		self.text = text

	def __str__(self):
		return "Something wrong with description:" + self.text

	__repr__ = __str__

class Technologie:
	"""
	A class for descripting technologies(technos).
	At first character observe something. Then it type the idea. 
	If the idea is mutch with description and the character knowledge of situation and skills are ok, technologies will 
	be discovered. It means that character can view it's description and quests to 
	complete for unlocking. After unlocking tech can be used.
	
	Attributes:

		@ name <-- the name of tech. Must be unique. 
		Underscores will be replaced with spaces later. This name will be displayed later.
		
		@ description <-- a long description (definetly more than 200 words). It must contain 
		information about the general idea of tech, realization of the tech and where it can be used.
		
		@ level <-- integet in range [0, INF] that describes the advance of tech. The bigger level is
		the more advance tech is.

		@ depencencies <-- a list of depencencies that must be __unlocked__ for discovering this tech. 
		E. g. you can't invent a computer without electricity and math knowledge.

		@ requirements <-- a list of requirements that are required for discovering tech. E. g.
		if you don't have a mech facilities you can't discover the tech connected to mech production optimization. 

		@ quests <-- a list of quest names to compleate for unlocking this tech.

		@ skills <-- a list of skill names and levels to have for discovering this tech.
	
	The idea is that all techs are meaningfull. They contain an idea of real optimization that
	can be implemented in real life. It's not just "Mech production optimization", but for example
	it contains an idea of pipeline that can speed up all processes.
	
	Player must understand processes behind the world to unlock them.
	Not only player can unlock techs. Characters too. 
	"""

	name = "name-of-technologie"
	description = "long-long descritpion"
	level = 0
	
	def __init__(self, **kwargs):
		self.name = kwargs['name']
		self.description = kwargs['description']
		if len(self.description) <= 600:
			raise DescriptionException('Name: {}. Cause: the length is too short.'.format(self.name))
		if 'level' in kwargs:
			self.level = kwargs['level']
		if int(self.level) != self.level or self.level < 0:
			raise DescriptionException('Name: {}. Cause: the level is not integer of in range'.format(self.name))
		if 'skills' in kwargs:
			self.skills = kwargs[skills]
		else:
			self.skills= []
		self.depencencies = []
		if 'dep' in kwargs:
			self.depencencies = kwargs['dep']
		if self.name in self.depencencies:
			raise DescriptionException('Name: {}. Cause: tech depends on itself'.format(self.name))
		self.quests = []
		if 'quests' in kwargs:
			self.quests = kwargs['quests']
		if 'req' in kwargs:
			self.requirements = kwargs['quests'] 

	def __repr__(self):
		return 'Tech({})'.format(self.name)

	def __str__(self):
		s = 'Tech Name: {} \n'.format(self.name)
		s += 'Level: {}\n'.format(self.level)
		s += 'Quest: {}\n\n'.format('none' if len(self.quests) == 0 else ','.join(self.quests))
		s += self.description
		s += '\n'
		return s

if __name__ == "__main__":
	print(Technologie(name='Magick', description='Magick, you know?)' + '.' * 600))