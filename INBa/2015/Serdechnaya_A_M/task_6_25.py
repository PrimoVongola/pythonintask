﻿# Задача 6. Вариант 25.
# Создайте игру, в которой компьютер загадывает название одного из четырех океанов Земли, а игрок должен его угадать.
   
# Serdechnaya A.M.
# 29.04.2016
 
import random
x=random.randint(1,4)
if x==1:
	name="Тихий океан"
elif x==2:
	name = "Атлантический океан"
elif x==3:
	name = "Индийский океан"
elif x==4:
	name = "Северно-Ледовитый океан"
	
print("Давайте поиграем в игру. Я загадываю один из четырех океанов Земли, а вы должны угадать, какой именно.")	
ans=input()

while(name!=ans ):
 	print("\n Не этот океан. Попробуешь еще угадать?")
 	print ("Введите название океана")
 	ans=input()
if name==ans:
	print("Верно! я загадал "+name+" океан.")
input("Нажмите Enter для выхода") 