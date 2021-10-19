# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def convert_damages(damages):
  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = []
  for damage in damages:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage)*conversion['M'])
    if damage[-1] == 'B':
      updated_damages.append(float(damage)*conversion['B'])
    return updated_damages
# test function by updating damages
updated_damages = convert_damages(damages)

# 2 
# Create a Table
def dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  num_hurricance = len(names)
  for i in range(num_hurricance):
    hurricanes[names[i]] = {
      'Name' : names[i],
      'Month' : months[i],
      'Year' : years[i],
      'Max sustained wind' : max_sustained_winds[i],
      'Areas Affected' : areas_affected[i],
      'Damages' : damages[i],
      'Deaths' : deaths[i]}
    return hurricanes

hurricanes = dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# 3
# Organizing by Year
def year_dictionary(hurricanes):
  hurricanes_by_year= dict()
  for cane in hurricanes:
      current_year = hurricanes[cane]['Year']
      current_cane = hurricanes[cane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year
  print(hurricanes_by_year[1932])
# 4
# Counting Damaged Areas
def damages_dict(hurricanes):
  num_affected_areas = {}
  for i in hurricanes:
    for area in hurricanes[i]['Areas Affected']:
      if area not in num_affected_areas:
        num_affected_areas[area] = 1
      else:
        num_affected_areas[area] += 1
      return num_affected_areas

num_affected_areas = damages_dict(hurricanes)

def most_affected_area(num_affected_areas):
  max_area = 'Central America'
  max_area_count = 0
  for area in num_affected_areas:
    if num_affected_areas[area] > max_area_count:
      max_area = area
      max_area_count = num_affected_areas[area]
    return max_area, max_area_count
max_area, max_area_count = most_affected_area(num_affected_areas)
print(max_area, max_area_count)
# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for i in hurricanes:
    if hurricanes[i]['Deaths'] > max_mortality:
      max_mortality_cane = i
      max_mortality = hurricanes[i]['Deaths']
  return max_mortality_cane, max_mortality

# find highest mortality hurricane and the number of deaths
max_damage_cane, max_damage = deadliest_hurricane(hurricanes)
print(max_damage_cane, max_damage)


# 9
# Rating Hurricanes by Damage
def cat_by_damage(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in hurricanes:
    total_damage = hurricanes[i]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage
# categorize hurricanes in new dictionary with damage severity as key
