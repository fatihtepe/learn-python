# ourfirsttuple = ('google', 'facebook', 'youtube')
# print(ourfirsttuple)
# ourfirsttuple = ('google', 'facebook', 'youtube', 'google', 'facebook', 'youtube')
# print(len(ourfirsttuple))

ourfirsttuple = tuple(('Google', 'Apple', 'Microsoft'))
# print(ourfirsttuple)

tuple1 = ('google', 'facebook', 'youtube')
tuple2 = (1, 2, 3, 4, 5, 6,)
tuple3 = (True, False, False)
# print(tuple1, tuple2, tuple3) 

# Access Tuples

mytuple = ('google', 'youtube', 'faceboo')
print(mytuple[1])

mytuple = ('google', 'youtube', 'faceboo')
print(mytuple[-1])

if 'google' in mytuple:
    print('yes')


# Update Tuples

x = ('google', 'facebook', 'youtube')
y = list(x) 
y.insert(0, 'Twitter')
y.append('instagram')
y.remove('youtube')
print(y)
x = tuple(y)
print(x) 

mytuple = ('google', 'facebook', 'youtube')
(green, yellow, red) = mytuple
print(green)
print(yellow)
print(red)