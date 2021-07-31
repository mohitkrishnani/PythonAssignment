arr = []
class Person:
  def __init__(self,name,age,email,phone):
    self.name = name
    self.age = age
    self.email = email
    self.phone = phone

class InvalidNameExc(Exception):
  def __init__(self,msg,name):
    self.msg = msg
    self.name = name
  def checkName(person):
    if type(person.name) != type(""):
      raise InvalidNameExc("Invalid name ,",person.name)

class InvalidPhoneExc(Exception):
  def __init__(self,msg,name):
    self.msg = msg
    self.name = name
  def checkPhone(person):
    if len(str(person.phone)) != 10:
      raise InvalidPhoneExc("Invalid phone ,",person.phone)
  
class InvalidEmailExc(Exception):
  def __init__(self,msg,name):
    self.msg = msg
    self.name = name
  def checkEmail(person):
    if type(person.email) != type(""):
      raise InvalidEmailExc("Invalid email ,",person.email)

class InvalidAgeExc(Exception):
  def __init__(self,msg,name):
    self.msg = msg
    self.name = name
  def checkAge(person):
    if person.age< 0 or person.age>100:
      raise InvalidAgeExc("Invalid age ,",person.age)

name = input("Name ")
age =int(input("Age "))
email = input("Email ")
phone = int(input("Phone "))

try:
  p = Person(name,age,email,phone)
  InvalidNameExc.checkName(p)
  InvalidAgeExc.checkAge(p)
  InvalidPhoneExc.checkPhone(p)
  InvalidEmailExc.checkEmail(p)
except InvalidNameExc as e:
  print(e.msg,e.name)
except InvalidAgeExc as e:
  print(e.msg,e.name)
except InvalidEmailExc as e:
  print(e.msg,e.name)
except InvalidPhoneExc as e:
  print(e.msg,e.name)

else:
  arr.append(p)

print(len(arr))


'''Output
Name Binod
Age 103
Email msdj
Phone 282718
Invalid age , 103
0'''