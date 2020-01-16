from building import Building
from city import City

# Birth of a City
# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

megalopolis = City("CherkeskyLand", "Guy Cherkesky", "1980")

# Awesome code here

megalopolis.addBuildings(dwell1)
megalopolis.addBuildings(dwell2)
megalopolis.addBuildings(dwell3)
megalopolis.addBuildings(clifton1)
megalopolis.addBuildings(clifton2)



for building in megalopolis.buildings:
    print(building)