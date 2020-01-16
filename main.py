from building import Building
from city import City

# Birth of a City
# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

megalopolis = City("CherkeskyLand", "Guy Cherkesky", "1980")

# Awesome code here
dwell1 = Building("1234 2nd Ave S #4", "2")
dwell1.construct()
dwell1.purchase("Bill Gates")
# dwell1.print_building()

dwell2 = Building("1234 2nd Ave S #7", "2")
dwell2.construct()
dwell2.purchase("Bill Gates")
# dwell2.print_building()

dwell3 = Building("1234 2nd Ave S #13", "2")
dwell3.construct()
dwell3.purchase("Bill Gates")
# dwell3.print_building()

dwell2 = Building("1234 2nd Ave S #7", "2")
dwell2.construct()
dwell2.purchase("Bill Gates")
# dwell2.print_building()

clifton1 = Building("620 27th Ave N", "3")
clifton1.construct()
clifton1.purchase("Bill Gates")
# clifton1.print_building()

clifton2 = Building("622 27th Ave N", "3")
clifton2.construct()
clifton2.purchase("Bill Gates")
# clifton2.print_building()


megalopolis.addBuildings(dwell1)
megalopolis.addBuildings(dwell2)
megalopolis.addBuildings(dwell3)
megalopolis.addBuildings(clifton1)
megalopolis.addBuildings(clifton2)



for building in megalopolis.city_buildings:
    print(building.address)