
# empty_set = set()
# print(type(empty_set))

# stRing_sample = "elmaarmutportakalordakal"
# yset = set(stRing_sample)
# print(yset) 
 
# list_sampel = city = ['New York', 'London', 'Seoul', 'Sydney', 111, 222]
# xset = set(list_sampel)
# print(xset)

# tuple_sample = (True, False, 1, 0, "a", "b", None)
# zset = set(tuple_sample)
# print(zset) #  True = 1 False = 0 REMEMBER!! 

state_capitals = {'Ontario': 'Toronto',
                   'Alberta': 'Edmonton',
                   'British Columbia': 'Victoria',
                   'Saskatchewan': 'Regina',
                   'Newfoundland and Labrador': 'St.John\'s',
                   'New Brunswick': 'Frederiction',
                   'Prince Edward Island': 'Chharlottetown',
                   'Quebec': 'Quebec',
                   'Manitoba': 'Winnipeg',
                   'Nunavut': 'Iqaluit',
                   'Northwest Territories': 'Yellowknife',
                   'Yukon': 'Whitehorse',
                   }

# set_from_dict = set(state_capitals)
# print(set_from_dict)

# set_from_values = set(state_capitals.values())
# print(set_from_values)

set_from_items = set(state_capitals.items())
print(set_from_items)
