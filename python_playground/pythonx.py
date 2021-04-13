fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']

fruit_list = []
fruit_list.insert(0, fruits)

# print(fruit_list[0][2][7])

# print(len([[12, 34, 56]][0]))

names = ['john', 'mariam', 'ali', 'jordan']

names.insert(1, 'anna')
# print(names)
names.append('fatih')
names.remove('john')
names.pop(3)
# names.clear()
names.count('j')
# print(names.count('fatih'))
names.sort()
names.reverse()
names.copy()


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))
# print(fruits.index('banana'))
# print(fruits.index('banana', 4)) # find banana after index 4
# print(fruits.pop())

stack = [3, 4, 5,]
stack.append(6)
stack.append(7)
# print(stack)
stack.pop()
stack.pop()
stack.pop()
# print(stack)

squares = []
for x in range(10):
    squares.append(x**2)
# print(squares)
# print([x ** 2 for x in range(10) if x > 5])

my_list = []
for x in range(11):
    if x % 2 != 0:
        my_list.append(x ** 2)
# print(my_list)
# print([x ** 2 for x in range(33) if x % 2 != 0])

my_list = []
for x in range(80):
    if x % 2 == 0:
        my_list.append(x + 1000)
# print(my_list)
# print([x + 100 for x in range(80) if x % 2 == 0])



my_list = [1, 3 ,3, 4, 5, 6, 7, 8, 9]
new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x ** 2)
# print(new_list)

# print([x ** 2 for x in my_list if x % 2 == 0])

tepe = [23, 45, 55, 6, 77, 8 ,99, 33, 2]
tepe_liste = []
for x in tepe:
    if x % 2 == 0:
        tepe_liste.append(x ** 2)

# print([x ** 2 for x in tepe if x % 2 ==0])

# print(tepe_liste)

# ***Tuples***
my_tuple = (1, 4, 3, 4, 5, 6, 7, 4)

my_list = list(my_tuple)
# print(my_list)

my_tuple = tuple(my_list)
# print(my_tuple)

last_name = 'tepe'
# print(tuple(last_name))


last_name = ('tepe',) # single tuple use ,
# print(last_name)

mix_value_tuple = (0, 'bird', 3.14, True)
# print(len(mix_value_tuple))

my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = my_list.count(8)
# print(x)

# python Tuple index() and count() methods

mysweet_tuple = ('a', 5, 'can', 'a', 'armut', 3.14)
output = mysweet_tuple.count('a') # 2 number of 'a'
output = mysweet_tuple.index(5) # 1 is index number of 5
# print(output)

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
# print(state_capitals['Alberta']) 
state_capitals['Nova Scotia'] = 'Halifax' # adding a new item
# print(state_capitals)
# print(state_capitals['Ontario'])

# print(state_capitals.items(), '\n')
# print(state_capitals.keys(), '\n')
# print(state_capitals.values())
# print('Nunavut' in state_capitals)
# print('Chicago' not in state_capitals)

mixed_dictionary = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)
mixed_dictionary.update({'is bad': False})
mixed_dictionary['not bad'] = 'None'
del mixed_dictionary['animal']
mixed_dictionary.pop('planet')
# print(mixed_dictionary)

