class Shapes:
	def __init__(self,n_sides,extra_var):
		self.n_sides = n_sides
		self.extra_var = extra_var
		
	def function_a(self):
		print("This is shapes a")

	def function_b(self):
		print("This is shapes b")

class Triangle(Shapes):
	def __init__(self,n_sides,triangle_var,extra_var):
		Shapes.__init__(self,n_sides,extra_var)
		self.n_sides = n_sides
		self.triangle_var = triangle_var
		
	def function_a(self):
		print("This is triangle a")

	def function_tria(self):
		print("This is triangle b")
		
class Quadrilateral(Shapes):
	def __init__(self,n_sides,quad_var,extra_var):
		Shapes.__init__(self,n_sides,extra_var)
		self.n_sides = n_sides
		self.quad_var = quad_var
		
	def function_a(self):
		print("This is quadrilateral a")

	def function_quad(self):
		print("This is quad b")
	
class lowest_child1(Triangle):
	def __init__(self,low_11,low_12,n_sides,triangle_var,extra_var):
		Triangle.__init__(self,n_sides,triangle_var,extra_var)
		self.low_11 = low_11
		self.low_12 = low_12

	def function_tria(self):
		print("This is lowest child 1")
	
	def function_low1(self):
		print("This is extra function low 1")
	
	
	
	
class lowest_child2(Quadrilateral):
	def __init__(self,low_21,low_22,n_sides,quad_var,extra_var):
		Quadrilateral.__init__(self,n_sides,quad_var,extra_var)
		
		self.low_21 = low_21
		self.low_22 = low_22

	def function_quad(self):
		print("This is lowest child 2")
	
	def function_low2(self):
		print("This is extra function low 2")
		
		
A = lowest_child1("Hello","World",3,180,"Extra low1")
print("Lowest Child (Triangle) "+A.low_11,A.low_12)

print("Triangle ",A.n_sides,A.triangle_var)

print("Shapes ",A.n_sides,A.extra_var)

A.function_tria()
A.function_low1()
A.function_a()
A.function_b()

B = lowest_child2("Dummy","Dum",4,360,"Extra low2")

print("Lowest Child (Quadrilateral) "+B.low_21,B.low_22)

print("Quadrilateral ",B.n_sides,B.quad_var)

print("Shapes ",B.n_sides,B.extra_var)

B.function_quad()
B.function_low2()
B.function_a()
B.function_b()


'''Output
Lowest Child (Triangle) Hello World
Triangle  3 180
Shapes  3 Extra low1
This is lowest child 1
This is extra function low 1
This is triangle a
This is shapes b
Lowest Child (Quadrilateral) Dummy Dum
Quadrilateral  4 360
Shapes  4 Extra low2
This is lowest child 2
This is extra function low 2
This is quadrilateral a
This is shapes b
'''