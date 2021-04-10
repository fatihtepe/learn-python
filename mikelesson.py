# mix_dic = dict(animal = 'dog', planet = 'nepton', number = 40, pi = 3.14159, is_good =True )

# mix_dic.update({'name5' : 'Burhan', 'name6' : 'Fatih'})

# del mix_dic['animal']
# print(mix_dic.items())

# Function to check object
# is iterable or not 
# def iterable(obj):
#     try:
#         iter(obj)
#         return True
          
#     except TypeError:
#         return False

# for element in [34, [4, 5], (4, 5),
#              {"a":4}, "dfsdf", 4.5]:
                   
#     print(element, " is iterable : ", iterable(element))

school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },               
        },
        
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },               
        },        
}

# print(school_records['personal_info']['teen']['marry']['age'])
# pprint.pprint(school_records['personal_info']['teen'])

# print(list(school_records['grades_info']['teen']['joseph'].items()))
# print(school_records['grades_info']['teen']['joseph'])
# print(school_records)
print(school_records['grades_info']['teen']['joseph'].values())