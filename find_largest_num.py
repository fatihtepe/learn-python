listem = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('enter a number: '))
    listem.append(numbers)
print('maximum number in the listem is:', max(listem), '\nMinumum element in the listem is: ', min(listem))


# 2

count = 0
listem = []
num = int(input('How many numbers will you enter?: '))
while count < num:
    numbers = int(input('enter a number'))
    listem.append(numbers)
    count += 1
largest = listem[0]
for i in listem:
    if i > largest:
        largest = i
print('largest number is: ', largest)