#Задача 4
#num = int(input("Enter the integer (0 to 100): ")) #int перевод в целое число и ввод input и сохраняем в num
#sum = 0 #Спочатку сума дорівнює 0, бо ми ще нічого не додавали.
#while num > 0: #Цикл буде повторюватися, поки num більше 0.Якщо num = 0, цикл не запуститься, сума залишиться 0 (це правильно).
    #sum += num #Це те саме, що sum = sum + num Додаємо поточне num до sum.
    #num -= 1 #Це те саме, що num = num - 1.Щоб перейти до наступного числа (наприклад 20 → 19 → 18 → ... → 1)
#print(sum)

#Задача 5
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r" #Це символ, який ми хочемо порахувати в рядку message.
result = 0 #Тут будемо зберігати кількість знайдених символів.Починаємо з 0.

for char in message: #Цикл по черзі бере кожен символ із рядка message char — це поточний символ
    if char == search: #Порівнюємо поточний символ char Якщо він дорівнює символу search ("r")
        result += 1 #Знайшли потрібний символ → збільшуємо результат на 1

print(result)
print(0)
# endregion 5

#Задача 6
#pool = 1000 #Це загальна кількість SMS, які можна розподілити між розсилками.
#quantity = int(input("Enter the number of mailings: ")) #Користувач вводить число int() перетворює введений текст у ціле число Значення зберігається в quantity

#try: #У try ми пишемо код, який може зламатися.Тут може виникнути помилка, якщо:quantity == 0 бо ділити на нуль не можна
    #chunk = pool / quantity 
    #print(chunk)
#except ZeroDivisionError: #Якщо сталася помилка поділу на нуль Програма не падає Замість цього виводиться повідомлення
    #print("Divide by zero completed!")
#print()
#endregion 6

#Задача 7
def greeting(): #def — ключове слово для створення функції greeting — ім’я функції () — означає, що функція не приймає аргументів
    print("Hello world!") #Код всередині функції виконується тільки тоді, коли функцію викликають

greeting() #Саме тут функція запускається На екран виводиться Hello world!
print()
#endregion 7

#Задача 8
def invite_to_event(username): #invite_to_event — назва функції username — параметр (ім’я користувача)
    return f"Dear {username}, we have the honour to invite you to our event" #invite_to_event — назва функції username — параметр (ім’я користувача)
#endregion 8

#Задача 9
def discount_price(price, discount): #price — початкова ціна discount — знижка (наприклад 0.2 = 20%)
    def apply_discount():#Це функція всередині іншої функції Вона буде змінювати price
        nonlocal price #price оголошена у зовнішній функції nonlocal дозволяє змінювати саме її, а не створювати нову змінну Без nonlocal код працювати не буде
        price = price * (1 - discount) #Приклад: price = 100 discount = 0.2 100 * (1 - 0.2) = 80

    apply_discount()#Вкладені функції не виконуються автоматично — їх потрібно викликати.
    return price#Функція повертає кінцеву ціну після знижки
#endregion 9

#Задача 10
def get_fullname(first_name, last_name, middle_name=""): #first_name — імʼя last_name — прізвище middle_name — необовʼязковий аргумент
#якщо його не передати, він дорівнює "" (порожній рядок)

    if middle_name:#Якщо middle_name не порожній → умова істинна Якщо "" → умова хибна
        return f"{first_name} {middle_name} {last_name}" #Якщо є друге імʼя
    else:
        return f"{first_name} {last_name}" #Якщо другого імені немає
# endregion 10

#Задача 11

