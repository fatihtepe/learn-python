empty_seat = 14
if empty_seat > 3:
    print('there is still seat to seat')


course = 'clarusway'
if course == 'clarusway':
    print('you guranteed the job')
else:
    print('think about it again')

number = 5 
if number <= 3:
    print('number is smaller than or equeal to 3')
else:
    print('number is bigger than 3')


weight = 70
if weight > 100:
    print('That is too heavy')
elif weight > 75:
    print('I can lift that')
else:
    print('That is too light!')


audience = 'baby'
if audience == 'kid':
    print('it is free to go to cinema')
elif audience == 'teen':
    print('discounted price!')
elif audience == 'adult':
    print('normal price')
elif audience == 'baby':
    print('everything is free for you!')
else:
    print('No such audience, stay at you home')


score = int(input('Enter your exam score: '))

if score >= 90:
    if score >= 95:
        Score_letter = 'A+'
    else:
        Score_letter = 'A'
elif score >= 80:
    if score >= 85:
        Score_letter = 'B+'
    else:
        Score_letter = 'B'
else:
    Score_letter = 'Below B'
print('Your degree: %s' % Score_letter)



price = input('how much did you pay?')

price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax)) 


price = input('how much did you pay?')

price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is: ' + str(tax)) 

country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('so you must like hockey!')
else:
    print('You are not from Canada')


province = input('What province do you live in? ')
tax = 0

if province in ('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
# print(tax)


country = input('What country do you live in?')

if country == 'Canada':
    province = input('What province do you live in? ')
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0
print(tax)


empty = set()

a = set('philadelphia')
b = set('dolphin')
c = set('fatih')
# print(a-b)
print(a.difference(b))
print(b.difference(a))

print(a | b )
print(a.union(b))
print(b.union(a))

print(a & b)
print(a.intersection(b))



day1 = set('04/14/2021')
day2 = {'04/14/2021'}

print (day1)
print(day2)



givent_list = [1, 2, 3, 3, 3, 4, 4, 5, 5]
unique = set(givent_list)
print(unique)




usa_capital = set('Washington')
new_zealand_capital = set('Wellington')

print(usa_capital)
print(new_zealand_capital)

# print(usa_capital.intersection(new_zealand_capital))

usa_capital = set('Washington')
new_zealand_capital = set('Wellington')

# print(usa_capital)
# print(new_zealand_capital)

print(usa_capital.intersection(new_zealand_capital))
print(new_zealand_capital.intersection(usa_capital))
# print(usa_capital.difference(new_zealand_capital))
# print(usa_capital.union(new_zealand_capital))
# print(usa_capital.difference(new_zealand_capital))

if True:
    print('it is true')

if False:
    print('it is true')
else:
    print('aaa')



if 1:
    print('ben')  # Truthy and Falsey 


if True:
    print('it is true')


if 0:
    print('ben') 
else:
    print('false')
if None:
    print('armut')

if {} or 1 and :
    print('elma')


ingredients = ['grocery store', 'lettuce', 'minced meat', 'pepper', 
'hamburger bread']  

if 'grocery store' in ingredients and 'hamburger bread' in ingredients\
    
    print('Bon Appetit')

a = set('TWELVE PLUS ONE')
b = set('ELEVEN PLUS TWO')
c = (a-b)

print(c)
if a == b:
    print(True)

convert = input('Enter Yes or No: ').title().strip() == 'Yes'
print('You entered: ', convert)

print('You entered: ', input('Enter Yes or No: ').title().strip() == 'Yes')



if rainy == 'evet':
    print('take umbrella')
else:
    print('gerek yok')

print("Merhaba, \n"
      "Şimdi seninle bir tahmin oyunu oynayacağız. \n"
      "İpucu: ..., Avrat, Silah")
gizli_kelime = "At"
tahmin = ""
tahmin_sayısı = 0
tahmin_sınırı = 3
tahmin_bitti = False
while tahmin != gizli_kelime and not (tahmin_bitti):
    if tahmin_sayısı < tahmin_sınırı:
        tahmin = input("Tahmin nedir?: ")
        tahmin_sayısı += 1
    else:
        tahmin_bitti = True
if tahmin_bitti:
    print("NE yazık ki bilemedin! :( ")
else:
    print("Aferin, bildin :) ")


xyz = int(input('Plese enter a number: '))

if xyz // 2 != 0:
    print('{} is even'.format(xyz))
else:
    print('{} is odd'.format(xyz))


xyz = float(input('Plese enter a number: '))

if xyz > 0:
    print('{} is positive'.format(xyz))
else:
    print('{} is negative'.format(xyz))


a = int(input('Plese enter a number: '))
b = int(input('Plese enter another number: '))

if a > b:
    print(f'the larger number is {a}')
else:
    print(f'the larger number is {b}')

bool_value = True
if bool_value:
    print('yes')
else:
    print('no')

province = input('What province do you live in? ')
tax = 0

if province in ('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
# print(tax)


a = int(input('Please enter a number: '))
b = int(input('Please enter another number: '))
c = int(input('Please enter last number: '))

if a > b and a > c:
    print(f'the largest number is {a}')
elif b > c and b > a:
    print(f'the largest number is {b}') 
else:
    print(f'the largest number is {c}')

minced = True
bread = True
#greens
lettuce = False
pepper = False
grocery_store = True
hamburger = (minced and grocery_store and bread) and (lettuce or pepper)
if hamburger:
    print("Bon Appetit")
else :
    print("There is no hamburger")


print(1 == 1)
print("henry" == "Henry")
print(12 < 12.1)
print("hard" != "easy")

set1 = set('TWELVE PLUS ONE')
set2 = set('ELEVEN PLUS TWO')

if set1 == set2:
    print('sets are equal...')

convert = input('Enter Yes or No: ').title().strip() == 'Yes'
print('you entered: ', convert)

xyz = int(input('Plese enter a number: '))

if xyz % 2 == 0:
    print('{} is even'.format(xyz))
else:
    print('{} is odd'.format(xyz))
