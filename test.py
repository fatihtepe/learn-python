from collections import Counter
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
fre = Counter(numbers)

print(f'the most frequent number is {fre.most_common(1)[0][0]} and it was {fre.most_common(1)[0][1]} times repeated')
