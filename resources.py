default_icon_path = '<some_path>'

class Resourse:
	"""
	A class for representing game resources such as wood, iron ore, crystalls, etc.
	They can be seen on global map. Also on local level it also can be seen, e. g. in a sector there are 10k wood, for one chair local master needs 0.1 wood. There must be icon.
	@ tags --> list of tags of this Resource. E. g. iron ore is an ore and it's metal ore. Also iron ore agregate trasformation temperatures are T1, T2, T3. At first all characteristics are hidden from player. Then he can discover it via experiments. 
	@ icon_path --> path of an icon.
	@ description --> a short description explaining what's look like, for what can be used
	@ name --> name of the resource.
	"""
	name = 'resource'
	tags = []
	icon_path = []
	decription = "This is a resource. It can be used in production."
	def __init__(self, name, **kwarg):
		self.name = name
		self.tags = kwarg['tags'] if 'tags' in kwarg else []
		self.icon_path = default_icon_path if 'icon' not in kwarg else kwarg['icon']
		self.description = kwarg['description']
		assert len(self.description