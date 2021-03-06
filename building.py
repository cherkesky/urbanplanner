'''
In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

Properties
designer - It will hold your name.
date_constructed - This will hold the exact time the building was created.
owner - This will store the same of the person who owns the building.
address
stories

Methods
Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

Constructor
Define your __init__ method to accept two arguments
address
stories
Once defined this way, you can send those values as parameters when you create each instance

 eight_hundred_eighth = Building("800 8th Street", 12)
Creating Your Buildings
Create 5 building instances
Have each one get purchased by a real estate magnate
After purchased, construct each one
Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
Example
800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.
'''
import datetime

class Building:
  def __init__(self, address, stories):
    self.designer = "Guy Cherkesky"
    self.address = address
    self.stories = stories

  def construct(self):
    self.date_constructed = datetime.datetime.now()

  def purchase(self, owner):
    self.owner = owner

  def print_building(self):
    print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories')

# dwell1 = Building("1234 2nd Ave S #4", "2")
# dwell1.construct()
# dwell1.purchase("Bill Gates")
# # dwell1.print_building()

# dwell2 = Building("1234 2nd Ave S #7", "2")
# dwell2.construct()
# dwell2.purchase("Bill Gates")
# # dwell2.print_building()

# dwell3 = Building("1234 2nd Ave S #13", "2")
# dwell3.construct()
# dwell3.purchase("Bill Gates")
# # dwell3.print_building()

# dwell2 = Building("1234 2nd Ave S #7", "2")
# dwell2.construct()
# dwell2.purchase("Bill Gates")
# # dwell2.print_building()

# clifton1 = Building("620 27th Ave N", "3")
# clifton1.construct()
# clifton1.purchase("Bill Gates")
# # clifton1.print_building()

# clifton2 = Building("622 27th Ave N", "3")
# clifton2.construct()
# clifton2.purchase("Bill Gates")
# # clifton2.print_building()