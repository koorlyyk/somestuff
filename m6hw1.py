#1
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
#2
my_dict = {'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20}
my_dict = sorted(my_dict.values())
print(my_dict[3:6])

#3
rand = random.randint(1, 10000)
summ = 0
print (rand)
for i in (str(rand)):
    summ += int(i)
    print(summ)