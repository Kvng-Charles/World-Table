import pandas


countries = {}
name_list = []
continent_list = []
area_list = []
population_list = []
sel_index = []

#------------------------COLLECTING COUNTRIES INFO---------------------------#

for n in range(3):
    name = input("Name of country?")
    continent = input("Continent your country belongs to?")
    area = int(input("What is its area?"))
    population = int(input("What is the population of the country?"))

    name_list.append(name)
    continent_list.append(continent)
    area_list.append(area)
    population_list.append(population)

#----------------------------------------------------------------------------#
#--------------------------CREATING PANDA TABLE------------------------------#

countries["name"] = name_list
countries["continent"] = continent_list
countries["area"] = area_list
countries["population"] = population_list

country_table = pandas.DataFrame(countries)
print(country_table)

#----------------------------------------------------------------------------#
#--------------------CREATE NEW TABLE OF BIG COUNTRIES-----------------------#

for index, row in country_table.iterrows():
    if row["area"] > 3000000 or row["population"] > 25000000:
        sel_index.append(index)
        
new_table = country_table.iloc[sel_index].reset_index(drop = True)
print(new_table)

#----------------------------------------------------------------------------#

