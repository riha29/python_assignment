# task-01
class Customer:
  def __init__(self,name):
    self.name= name
  def greet(self, name= None):
    if name== None:
      print('Hello!')
    else:
      print('Hello', name, '!')
  def purchase(self, *item):
    print(self.name, ', you purchased', len(item), 'item(s):')
    for idx in list(item):
      print(idx)
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")



# task-02
class Panda:
  def __init__(self, name, gender, age):
    self.name= name
    self.gender= gender
    self.age= age    
  def sleep(self, sleep=None):
    if sleep!= None:
      if sleep>=3 and sleep<=5:
        return(f"{self.name} sleeps {sleep} hours daily and should have Mixed Veggies")
      elif sleep>=6 and sleep<=8:
        return(f"{self.name} sleeps {sleep} hours daily and should have Eggplant & Tofu")
      elif sleep>=9 and sleep<=11:
        return(f"{self.name} sleeps {sleep} hours daily and should have Broccoli Chicken")
    else:
      return(f"{self.name} 's duration is unknown thus should have only bamboo leaves")
panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())



# task-03
class Cat:
  def __init__(self, color='White', doing='sitting'):
    self.color= color
    self.doing= doing
  def printCat(self):
    print(f"{self.color} cat is {self.doing}")
  def changeColor(self, color):
    self.color= color
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat() 
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()



# task-04
class Student:
  def __init__(self, name='Default student'):
    self.name= name
  def quizcalc(self, mark1, mark2=0, mark3=0):
     self.avg = (mark1+mark2+mark3)/3
  def printdetail(self):
    print(f"Hello {self.name} \nYour average quiz score is {self.avg}")
s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()


# task-05
class Student:
  def __init__(self, name, id, dept='CSE'):
    self.name= name
    self.id= id
    self.dept= dept
  def dailyEffort(self, effort):
    self.effort= effort
    if self.effort<=2:
      self.suggestion= 'Should give more effort!'
    elif self.effort<=4:
      self.suggestion= 'Keep up the good work!'
    else:
      self.suggestion= 'Excellent! Now motivate others.'
  def printDetails(self):
    print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.dept}\nDaily Effort: {self.effort} hour(s)\nSuggestion: {self.suggestion}")

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()



# task-06
class Patient:
  def __init__(self, name, age):
    self.name= name
    self.age= age
  def add_Symptom(self, symp1, symp2='', symp3=''):
    self.symp1= symp1
    self.symp2= symp2
    self.symp3= symp3
  def printPatientDetail(self):
    print(f"Name: {self.name}\nAge: {self.age}\nSymptoms: {self.symp1} {self.symp2} {self.symp3}")

p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()


# task-07
class Match:
  def __init__(self, game):
    self.game= game
    self.wicket=0
    self.run=0
    print('5..4..3..2..1.. Play !!!')
  def add_run(self, run):
    self.run= self.run+ run
  def add_over(self,over):
    if over>4:
      print(f"Warning! Cannot add {over} over/s (5 over match)")
    else:
      self.over= over
  def add_wicket(self, wicket):
    self.wicket= wicket
  def print_scoreboard(self):
    return (f"Batting Team: Rangpur Riders\nBowling Team: Cumilla Victorians\nTotal Runs: {self.run}  Wickets: {self.wicket}   Overs: {self.over}")

match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())



# task-08-----------------not done
class ParcelKoro:
  def __init__(self, *args):
    self.name= 'No name set'
    self.product_weight=0
    self.location_charge= 0
    if len(args)==1:
      self.name= args[0]
    elif len(args)==2:
      self.name= args[0]
      self.product_weight= args[1]  
  def calculateFee(self, location=''):
    if location!='':
      self.location_charge+=100
    else:
      self.location_charge+=50
  def printDetails(self):
    if self.product_weight==0:
      self.total_fee=0
    else:
      self.total_fee= (self.product_weight * 20) + self.location_charge
    print(f"Customer Name: {self.name}\nProduct Weight: {self.product_weight}\nTotal fee: {self.total_fee}")
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()



# task-09
class Batsman:
  def __init__(self, *args):
    self.name= 'New Batsman'
    self.run= 6101
    self.ball= 7380 
    if len(args)==2:
      self.run= args[0]
      self.ball= args[1]
    elif len(args)==3:
      self.name= args[0] 
      self.run= args[1]
      self.ball= args[2]
  def printCareerStatistics(self):
    print(f"Name: {self.name}\nRuns Scored: {self.run} , Balls Faced: {self.ball}")
  def battingStrikeRate(self):
    return (self.run/ self.ball)* 100
  def setName(self, name2):
    self.name= name2
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())




# task-10
class EPL_Team:
  def __init__(self, *args):
    self.title= 0
    self.name= ''
    self.song= 'No Slogan'
    if len(args)==2:
      self.name= args[0]
      self.song= args[1]
    if len(args)==1:
      self.name= args[0]
  def showClubInfo(self):
    return (f"Name: {self.name}\nSong: {self.song}\nTotal No of title: {self.title}")
  def increaseTitle(self):
    self.title+=1
  def changeSong(self, songChange):
    self.song= songChange

manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())


# task-11
class Author:
  def __init__(self, *args):
    self.name= 'Default'
    self.books1= ''
    self.books2= ''
    self.books3= ''
    if len(args)==1:
      self.name= args[0]
    elif len(args)==3:
      self.name= args[0]
      self.books1= args[1]
      self.books2= args[2]
  def addBooks(self, *books):
    if len(books)==2:
      self.books1= books[0]
      self.books2= books[1]
    elif len(books)==3:
      self.books1= books[0]
      self.books2= books[1]
      self.books3= books[2]
  def printDetails(self):
    print(f"Author Name: {self.name}\n--------\nList of Books:\n{self.books1}\n{self.books2}\n{self.books3} ")
  def changeName(self, newName):
    self.name= newName

auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()



