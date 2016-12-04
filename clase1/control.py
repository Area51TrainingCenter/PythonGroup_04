edad_str = input('cual es tu edad?: ')
edad = int(edad_str)

if edad > 18 and edad < 99:
    # 4 espacios / tab / X espacios
    print('eres mayor de edad')
    if edad > 40:
        print('ya estas viejo')
elif edad <= 3:
    print('edad incorrecta')
elif edad < 18:
    print('eres menor de edad')
else:
    print('no estas vivo')

# Operador ternario
edad = 13
mayor = True if edad > 18 else False
