import random #выбирает рандом 
pl = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))#показываешь какие тут действия и даешь им названия 
if pl == 1:
    print("Вы выбради камеь.")
if pl == 2:
    print("Вы выбради ножницы.")
if pl == 3:
    print("Вы выбради бумага.") 
comp = random.randint(1, 3)#То что выбирает комп 
if comp == 1:
   print("Компьбтер выюрал камень.")
if comp == 2:
   print("Компьбтер выюрал бумага.")
if comp == 3:
   print("Компьбтер выюрал ножницы.")
if pl == comp:#Сравнивает действия игрока и компьютера
    win = 0
if pl == 1 and comp == 2:
    win = 1
if pl == 1 and comp == 3:
    win = 2
if pl == 2 and comp == 1:
    win = 2
if pl == 2 and comp == 3:
    win = 1
if pl == 3 and comp == 1:
    win = 2
if win == 0:#Условия сути игы 
    print("Ничья!")
if win == 1:
    print("Победил игрок!")
if win == 2:
    print("Победил компьютер!")
