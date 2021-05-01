'''filter()'''

# first task
mylist = [5, 12, 17, 18, 24, 32, 999, 101]
def less_than_100(number):
    return number < 100

newlist = filter(less_than_100, mylist)
final_list = list(newlist)
print(final_list)


# second task
def filterWovels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if letter.lower() in vowels:
        return True
    else:
        return False
    
sentence = 'I want to eat cake before dinner'
filtered_sentence = filter(filterWovels, sentence)
print(set(filtered_sentence))


# third task
mix_list = [5, 12, 17,'a', 'e', 'i', 24, 32,101] 

def less_than_ten(num):
    if num <= 10:
        return True
    else:
        return False
    
filt_list = filter(less_than_ten, mix_list)

newlist = list(filt_list)
print(newlist)
# TypeError: '<=' not supported between instances of 'str' and 'int'


# third task (edited)
mix_list = [5, 12, 17,'a', 'e', 'i', 24, 32,101] 

def less_than_ten(num):
    if type(num) == int and num <= 10:
        return True
    else:
        return False
    
filt_list = filter(less_than_ten, mix_list)

newlist = list(filt_list)
print(newlist)