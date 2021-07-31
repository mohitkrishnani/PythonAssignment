class Country:
	AVG_POPULATION = 5000;
	def __init__(self,country_name, country_code):
		if (type(country_name) != type("") ) or (type(country_code) != type("") ):
			raise ValueError("Incorrect parameter type")
		elif len(country_code) != 3 :
			raise ValueError("Incorrect length of country code")
		else:
			self.country_name = country_name
			self.country_code = country_code
	
	def getCountryName(self):
		return self.country_name
		
	def getCountryCode(self):
		return self.country_code
		
	def setCountryName(self,country_name):
		self.country_name = country_name
		
	def setCountryCode(self,country_code):
		self.country_code = country_code
	

	def country_short_form(self):
		return self.country_name[:2].upper()
	
	@classmethod
	def is_densly_populated(cls,population):
		if population>cls.AVG_POPULATION:
			return True
	
	
	@staticmethod
	def world_avg_population(arr):
		return sum(arr)/len(arr)
	
	def formatted_country_name(function):
		def wrapper(*args,**kwargs):
			print(args[0].country_name+"("+args[0].country_code+")")
		return wrapper
	
	@formatted_country_name
	def print_function(self):
		print()
		
a = Country("India","IND")
print(a.country_short_form())
print(a.is_densly_populated(7000))
print(a.world_avg_population([2000,2323,2324,5600,7900]))
a.print_function()


'''Output
IN
True
4029.4
India(IND)
'''