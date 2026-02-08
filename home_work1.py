#region Задача 1
rate = 1.68 #стоимость
value = 100 #обьем
payment = value * rate #перемножили
print("Задача 1:",payment)
print()
#endregion 1

#region Задача 2
rate = 1.68
value_day = 100
value_night = 200 #ночной тариф делим на 2 по условиям задачм
payment = value_day * rate + value_night * (rate/2)
print ("Задача 2:",payment)
print()
#endregion 2

#region Задача 3 конкатенация рядов
first_name = "Oleksii"
last_name = "Rodionov"
full_name = first_name + " " + last_name # не забываем пробел " "
print("Задача 3:",full_name)
print ()
#endregion 3

#region Задача 4, довжина, ширина, площа кімнати
length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print("Задча 4:",show)
print()
#endregion 4

#region Задача 5 Створити 4 типи змінних
name = "Oleksii" #str
age = 43 #int
is_active = True #bool
subscription = None #non type
print ("Задача 5 без принта, просто переменные")
print ()
#endregion 5

#region Задача 6 Площа кімнати але рядкові значення первести в числові
length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print("Задача 6:",show)
print ()
#endregion 6

#region Задача 7, запитує дані та зберігає в змінні
# name = input ("Enter your name: ") #input всегда возвращает ряд
# email = input("Enter your email: ")
# age = int(input("Enter your age: ")) # int возраст в целое число
# height = float(input("Enter your height: ")) #float рост в действ число
# is_active = bool(input("Do you want to receive info&")) #если без ввода то фолс, если ввел то тру
# print ("Задача 7 без принта, просто переменные")
# print ()
#endregion 7

#region Задача 8 яка ініціалізує порожній список і заповнює його певними значеннями за вказаними індексами
my_list = []
my_list.insert(0, 2024)
my_list.insert(1, 'Python')
my_list.insert(2, 3.12)
print("Задача 8:",my_list)
print()
#endregion 8

#region Задача 9, яка виконує серію операцій з двома списками, змінюючи їхній вміст і порядок елементів.
my_list = [1, 2, 3]
some_data = ['a', 'b', 'c']
my_list.extend(some_data) #extend → [1, 2, 3, 'a', 'b', 'c']
my_list.insert(1, 'Python') #insert(1, 'Python') → [1, 'Python', 2, 3, 'a', 'b', 'c']
my_list.reverse() #reverse() → ['c', 'b', 'a', 3, 2, 'Python', 1]
print("Задача 9:",my_list)
print()
#endregion 9

#region Задача 10, ініціалізує порожній словник і заповнює його певними ключами та відповідними значеннями.
data = {}
data["year"] = 2026
data["lang"] = "Python"
data["version"] = 3.13
print("Задача 10:",data)
print()
#endregion 10

#region Задача 11 модифікує порожній словник cat, додаючи до нього різні ключі та значення, а також використовує значення з іншого словника info
cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["лагідний", "кусається"]
age = cat.get("age")
cat.update(info)
print("Задача 11:",info)
print()