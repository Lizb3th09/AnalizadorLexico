import re

# Rosa Lizbeth Barcenas Mancilla  C21930200

try:
    with open("read.prog", "r") as archivo:
        contenido = archivo.read()  # Lee el contenido del archivo
except FileNotFoundError:
    exit(1)
s_puntuacion = {':': 'dos puntos', ';': 'punto y coma', '.': 'punto', ',': 'coma'}

reservadas = {'if':'Palabra reservada', 'False': 'Palabra reservada', 'None': 'Palabra reservada', 'True': 'Palabra reservada', 'and': 'Palabra reservada', 'else': 'Palabra reservada', 'assert': 'Palabra reservada', 'async': 'Palabra reservada', 'await': 'Palabra reservada', 'break': 'Palabra reservada','class': 'Palabra reservada', 'def': 'Palabra reservada', 'elif': 'Palabra reservada', 'for': 'Palabra reservada', 'from': 'Palabra reservada', 'except': 'Palabra reservada', 'del': 'Palabra reservada' , 'while': 'Palabra reservada', 'return': 'Palabra reservada', 'import': 'Palabra reservada', 'try': 'Palabra reservada', 'not': 'Palabra reservada'}

operadores_aritmeticos = {'+': 'Operador de suma', '-': 'Operador de resta', '/': 'Operador de división',
                          '*': 'Operador de multiplicación', 'cos': 'Operador coseno', 'sen': 'Operador seno',
                          'log': 'Operador log'}
operadores_logicos = {'=': 'Operador de asignación', '==': 'Operador igual que', '>': 'mayor que',
                      '<': 'Operador menor que', '>=': 'Operador mayor igual que', '<=': 'Operador menor igual que'}
tipos_dato = {'int': 'Tipo entero', 'float': 'Punto flotante', 'char': 'Tipo carácter', 'long': 'Entero largo'}

# Expresiones regulares para identificar letras y números.

identificador = '^[A-Za-z]*$'
numero_entero = '^[-+]?[0-9]+$'
numero_real = r'^[-+]?[0-9]+\.[0-9]{1,5}$'

id = set()

contador = 0
programa = contenido.split("\n")

print("| Token | Lexema | Descripción | P_Reservada |")
print("|-------|--------|-------------|-----------|")

for linea in programa:
    contador += 1

    tokens = linea.split(' ')

    for token in tokens:
        if not token.strip():
            print(f"Error léxico en línea {contador}:'Dato nulo.")
            exit(1)
        if token in operadores_aritmeticos:
            lexema = token
            descripcion = operadores_aritmeticos[token]
            tipo_token = "Operador Arit"
            P_reservada = "No"
        elif token in s_puntuacion:
            lexema = token
            descripcion = s_puntuacion[token]
            tipo_token = "signos"
            P_reservada = "No"
        elif token in reservadas:
            lexema = token
            descripcion = reservadas[token]
            tipo_token = "Palabra Res"
            P_reservada = "si"
        elif token in operadores_logicos:
            lexema = token
            descripcion = operadores_logicos[token]
            tipo_token = "Operador Log"
            P_reservada = "No"
        elif token in tipos_dato:
            lexema = token
            descripcion = tipos_dato[token]
            tipo_token = "Tipo de dato"
            P_reservada = "No"
        elif re.match(identificador, token):
            if token[0].isdigit():
                print(f"Error léxico en línea {contador}: {token}' error.")
                exit(1)
            if len(token) > 20:
                print(f"Error léxico en línea {contador}: {token} 'Máximo de longitud")
                exit(1)
            if token in id:
                print(
                    f"Error léxico en línea {contador}: {token} Identificador definido previamente con un tipo antes de usarse.")
                exit(1)
            lexema = token
            descripcion = "Identificador"
            tipo_token = "ID"
            P_reservada = "No"
            id.add(token)
        elif re.match(numero_entero, token):
            if int(token) > 2147483647 or int(token) < -2147483648:
                print(f"Error léxico en línea {contador}: {token} Desbordamiento de datos")
                exit(1)
            lexema = token
            descripcion = "Número entero"
            tipo_token = "Número Ent"
            P_reservada = "no"
        elif re.match(numero_real, token):
            if len(token.split('.')[1]) > 4:
                print(f"Error léxico en línea {contador}:{token}  Desbordamiento")
                exit(1)
            lexema = token
            descripcion = "Número real"
            tipo_token = "Número Rl"
            P_reservada = "no"
        else:
            print(f"Error léxico en línea {contador}: {token} error")
            exit(1)

        print(f"| {tipo_token} | {lexema} | {descripcion} | {P_reservada} |")
