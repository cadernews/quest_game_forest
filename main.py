print('''
   ad88                                                     
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888  
''')
print("Добро пожаловать в ЛЕС.")
print("Твоя миссия - выбраться!") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print()
print("                                                        🠕 ")
print("Ты заблудился в лесу, перед тобой три пути: 🠔 left |straight| right 🠖")
way = input("Какой путь выберешь?\n")
lower_way = way.lower()
if lower_way == "left":
  print("Ты пошел налево, через густую чащу и сорвался с обрыва...")
  print("Ты летишь и в панике замечаешь 2 веревки, brown и blue")
  rope = input("За какую схватишься?\n")
  lower_rope = rope.lower()
  if lower_rope == "brown":
    print("Ты хватаешь коричневую веревку и понимаешь, что это старые корни дерева, которое с трудом пыталось вырасти в этом ущелье")
    print("Они не выдерживают такую неожиданную нагрузку и ты потеряв последнию надежду, разбиваешься")
    print("You dead. Game over.")
  else:
    print("Ты хватаешь синию веревку...")
    print("Тебе повезло, эта веревка оказалась крепкой, видимо её оставили другие путешествиники...")
    print("Ты с трудом, но поднимаешься из ущелья.")
    print("Замечая обходной путь, минуешь зловещее ущелье, и выходишь из леса.")
    print("You win. Game over.")
elif lower_way == "straight":
  print("Ты пошел прямо. И набрел на избушку...")
  print("В избушке оказалась старая рация, но чтобы ее включить есть 2 кнопки - red или black")
  button = input("Какую нажмешь?\n")
  lower_button = button.lower()
  if lower_button == "red":
    print("Нажал красную кнопку.")
    print("Все заискрилось, вспыхнул огонь.")
    print("Дом вспыхнул как спичка. Ты сгорел заживо")
    print("You dead. Game over.")
  else:
    print("Нажав черную кнопку. Ты услышал голос в динамиках рации.")
    print("Тебе удалось вызвать спасателей...")
    print("You win. Game over.")
elif lower_way == "right":
  print("Ты пошел направо.")
  print("Вышел к бурной реке..")
  print("Заметив 2 лодки у берега, ты поспешил к ним...")
  print("Перед тобой выбор, rubber лодка или wooden")
  boat = input("В какую лодку сядишь?\n")
  lower_boat = boat.lower()
  if lower_boat == "rubber":
    print("Сев в резиновую лодку ты отчалил от берега.")
    print("Но лодка оказалась с ненадежным дном")
    print("И первый же каменный порог потопил твою лодку.")
    print("Ты пошел ко дну, потеряв последнию надежду.")
    print("You dead. Game over.")
  else:
    print("Сев в деревянную лодку ты отчалил от берега.")
    print("Лодка оказалась крепкой и паневренной")
    print("В ней ты обнаружил сигнальную ракету")
    print("Выпустил её.")
    print("Течение привело тебя к выходу из леса")
    print("Ты спасься")
    print("You win. Game over.")
else:
  print("Что то не так попробуй снова!!")



