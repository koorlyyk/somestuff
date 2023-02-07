# 1
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.sort()
my_list_plus = my_list[1::2]
my_list_minus = my_list[2::-1]
my_list.append('cheburek')
print(len(my_list))
print(my_list.index('cheburek'))
2
def return_count_from_list(list_where_search):
    total_count = {}
    for i in list_where_search:
        if i not in total_count:
            total_count[i] = list_where_search.count(i)
    print(total_count)


#3
class Product :
    def __init__(self, name, rating, count):
        self.name = name
        self.rating = rating
        self.count = count

    def get_amount(self):
        if self.count == 0:
            return ('Нет в наличиии')
        elif 1 <= self.count <= 10:
            return ('В наличии мало')
        elif 11 <= self.count <= 50:
            return ('В наличии немного')
        elif self.count >= 51:
            return ('В наличии')
        else:
            return ('Инвалид вэлью')




monocular = Product('Монокуляр Veber 7-21x21W ZOOM', 4, 51)
apple = Product('Супер яблоко', 4, 0)
google_car = Product('Google car', 3, 10)
lenovo_yoga = Product('Lenovo yoga', 3, 50)

print(monocular.get_amount())
print(apple.get_amount())
print(google_car.get_amount())
print(lenovo_yoga.get_amount())