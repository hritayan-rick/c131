import csv
import plotly.express as px

rows = []

with open('main.csv' , 'r') as f:
    a = csv.reader(f)
    for i in a:
        rows.append(i)


headers = rows[0]
planet_data_rows = rows[1:]

# print("----------------------------------------------------")
# print(headers)

# print("----------------------------------------------------")
# print(planet_data_rows[0])


headers[0] = "row_num"

solar_system_planet_count={}

for data in planet_data_rows:
    if solar_system_planet_count.get(data[11]):
        solar_system_planet_count[data[11]] += 1

    else:
        solar_system_planet_count[data[11]] = 1


max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("----------------------------------------------------")
print("Solar system {} has maximum planets {} out of all the solar systems we have discovered so far!".format(max_solar_system, solar_system_planet_count[max_solar_system]))


hd_10180_planets= []

for data in planet_data_rows:
    if max_solar_system == data[11]:
        hd_10180_planets.append(data)

print("----------------------------------------------------")
print(len(hd_10180_planets))

print("----------------------------------------------------")
# print(hd_10180_planets)      

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
 planet_mass = planet_data[3]
 if planet_mass.lower() == "unknown":
   planet_data_rows.remove(planet_data)
   continue
 else:
   planet_mass_value = planet_mass.split(" ")[0]
   planet_mass_ref = planet_mass.split(" ")[1]
   if planet_mass_ref == "Jupiters":
     planet_mass_value = float(planet_mass_value) * 317.8
   planet_data[3] = planet_mass_value


 planet_radius = planet_data[7]
 if planet_radius.lower() == "unknown":
   planet_data_rows.remove(planet_data)
   continue
 else:
   planet_radius_value = planet_radius.split(" ")[0]
   planet_radius_ref = planet_radius.split(" ")[2]
   if planet_radius_ref == "Jupiter":
     planet_radius_value = float(planet_radius_value) * 11.2
   planet_data[7] = planet_radius_value
   
print("----------------------------------------------------")

print(len(planet_data_rows))

# ----------------------------------- c 132 ----------------------------------------------------

temp_planet_data_rows = list(planet_data_rows) 

for data in planet_data_rows :
   if planet_data[1].lower() == "hd 100546 b":
      planet_data_rows.remove(planet_data)


planet_masses = []
planet_radiuses = []
planet_names = []

for data in planet_data_rows:
   planet_masses.append(data[3])
   planet_radiuses.append(data[7])
   planet_names.append(data[1])

planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

graph = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
# graph.show()


low_gravity_planets = []
for index , gravity in enumerate(planet_gravity):
   if gravity < 100:
      low_gravity_planets.append(planet_data_rows[index])


print("----------------------------------------------------")

print(len(low_gravity_planets))


planet_type_values = []

for data in planet_data_rows:
   planet_type_values.append(data[6])
   

print("----------------------------------------------------")

print(list(set(planet_type_values)))

# Neptune-like => These planets are like neptune! They are big in size and have rings around them. They are also made of Ice.

# Super-Earth => These are the planets that have mass greater than earth but smaller than that of Neptune! (Neptune is 17 times Earth)

# Terrestrial => It is a planet that is composed primarily of silicate rocks or metals (Like Earth, Mars)

# Gas Giant => There are the planets that are composed of Gas (Hydrogen and Helium)


planet_masses = []
planet_radiuses = []

for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])

fig = px.scatter(x=planet_radiuses, y=planet_masses)
fig.show()















