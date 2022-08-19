# 01
class Student:
 def __init__(self, name='Just a student', dept='nothing'):
   self.__name = name
   self.__department = dept
 def set_department(self, dept):
   self.__department = dept
 def get_name(self):
   return self.__name
 def set_name(self,name):
   self.__name = name
 def __str__(self):
   return 'Name: '+self.__name+' Department: '+self.__department

class BBA_Student(Student):
  def __init__(self, name= 'Default'):
    super().__init__(name, 'BBA')      

# class BBA_Student(Student):
#   def __init__(self, ):
#     super().set_department('BBA')

print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))


# 02
class Vehicle:
  def __init__(self):
    self.x = 0
    self.y = 0
  def moveUp(self):
    self.y+=1
  def moveDown(self):
    self.y-=1
  def moveRight(self):
    self.x+=1
  def moveLeft(self):
    self.x-=1
  def __str__(self):
    return '('+str(self.x)+' , '+str(self.y)+')'

#write your code here
class Vehicle2010(Vehicle):
  def __init__(self):
    self.x= 0
    self.y= 0
  def moveLowerLeft(self):
    self.y-= 1
    self.x-= 1
  def equals(self, car2):
    if car1.x== car2.x and car1.y== car2.y:
      return True
    else:
      return False

print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))


# 03
class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
#write your code here
class Cricket_Tournament(Tournament):
  def __init__(self, name= 'Default', team= 0, Type= 'No type'):
    self.name= name
    self.team= team
    self.Type= Type
    super().__init__(name)    
  def detail(self):
    return (f"Cricket Tournament Name: {self.name}\nNumber of Teams: {self.team}\nType: {self.Type}")
class Tennis_Tournament(Tournament):
  def __init__(self, name, pl_num):
    self.name= name
    self.pl_num= pl_num
  def detail(self):
    return (f"Tennis Tournament Name:{self.name}\nNumber of Players: {self.pl_num}")

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())



# 04
class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+"Price: "+str(self.__price)
#write your code here
class Book(Product):
  def __init__(self,id, title, price, isbn, publisher):
    self.id, self.title, self.price, self.isbn, self.publisher= id, title, price, isbn, publisher    
    super().__init__(id, title, price)
  def printDetail(self):
    return (f"ID: {self.id} Title: {self.title} Price: {self.price}\nISBN: {self.isbn} Publisher: {self.publisher}")
class CD(Product):
  def __init__(self, id, title, price, band, duration, genre):
    self.id, self.title, self.price,self.band, self.duration, self.genre= id, title, price, band, duration, genre
  def printDetail(self):
    return (f"ID: {self.id} Title: {self.title} Price: {self.price}\nBand: {self.band} Duration: {self.duration} minutes\nGenre: {self.genre}")
    

book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())



# 05
class Animal:
  def __init__(self,sound):
    self.__sound = sound
  def makeSound(self):
    return self.__sound 
class Printer:   
  def printSound(self, a):
    print(a.makeSound())
#write your code here
class Dog(Animal):
  def __init__(self, ty_sound):
    super().__init__(ty_sound)
class Cat(Animal):
  def __init__(self, ty_sound):
    super().__init__(ty_sound)

d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)


# 06
class Shape:
  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base
  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

#write your code here
class triangle(Shape):
  def __init__(self, name='Default', height=0, base=0):
    self.name, self.height, self.base= name, height, base
  def calcArea(self):
    self.area= .5* self.height* self.base
  def printDetail(self):
    return f"Shape name: {self.name}\nHeight: {self.height}, Base: {self.base}\nArea: {self.area}"

class trapezoid(Shape):
  def __init__(self, name, height, base, side):
    self.name, self.height, self.base, self.side= name, height, base, side
  def calcArea(self):
    self.area= .5* self.height* (self.base+self.side)
  def printDetail(self):
    return f"Shape name: {self.name}\nHeight: {self.height}, Base: {self.base}, Side_A: {self.side}\nArea: {self.area}"

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())


# 07
class Football:
  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0
  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here
class Player(Football):
  def __init__(self, team, name, role, goal, total):
    self.team, self.name, self.role, self.goal, self.total= team, name, role, goal, total
  def calculate_ratio(self):
    self.earning= (self.goal * 1000) + (self.total * 10)
    self.ratio= self.goal/self.total
  def print_details(self):
    print(f'Name: {self.name}, Team Name: {self.team}\nTeam Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.total}\nGoal Ratio: {self.ratio}\nMatch Earning: {self.earning}')

class Manager(Football):
  def __init__(self, team, name, role, win):
    self.team, self.name, self.role, self.win= team, name, role, win
    self.earning= self.win*1000
  def print_details(self):
    print(f'Name: {self.name}, Team Name: {self.team}\nTeam Role: {self.role}\nTotal Win: {self.win}\nMatch Earning: {self.earning}')


player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

