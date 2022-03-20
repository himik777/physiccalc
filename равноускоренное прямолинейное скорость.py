print("Эта программа поможет вам вычислить данные по формуле v=V+a*t. В строку с неизвестной величиной введите ?.")
a = input("Введите ускорение(м/сек2):")
v = input("Введите кон. скорость(м/сек):")
t = input("Введите время(cек):")
V = input("Введите нач. скорость(м/сек):")
if v == "?":
    print("Кон. скорость равна")
    print(int(V) + int(a)*int(t))
if a == "?":
    print("Ускорение равно")
    print(int(v)//int(t)-int(V)//int(t)) 
if V == "?":
    print("Нач. скорость равна")
    print(int(V)-int(a)*int(t))
if t == "?":
    if V != 0:
        print("Время равно")
        print(int(v)//int(a)-int(V)//int(a))
    else:
        print("Время равно")
        print(int(v)//int(a))
