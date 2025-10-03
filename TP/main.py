import json
import random

def imprimir_opciones(lista_de_opciones: list):
    for x, evento in enumerate(lista_de_opciones):
        print(str(x + 1) + ". " + evento)

def validar_evento(lista_de_eventos: list):
    evento_valido = False

    while evento_valido == False:
        try:
            imprimir_opciones(lista_de_eventos)
            evento_elegido = int(input("Elija un evento al que asistir: "))

            while evento_elegido < 1 or evento_elegido > 3:
                print("Numero de evento invalido. Intente nuevamente")
                imprimir_opciones(lista_de_eventos)
                evento_elegido = int(input("Elija un evento al que asistir: "))

            evento_valido = True
            return lista_de_eventos[evento_elegido - 1]

        except ValueError:
            print("Valor ingresado no valido")


def validar_nombre():
    nombre = input("Ingrese su nombre: ") 
    
    while nombre.isdigit()  or len(nombre) == 0:
        print("Nombre invalido")
        nombre = input("Ingrese su nombre: ")

    return nombre


def validar_edad():
    edad_valida = False

    while edad_valida == False:
        try:
            edad = int(input("Ingrese su edad: "))

            while edad < 13 or edad > 100:
                print("Edad invalida. Intente nuevamente")
                edad = int(input("Ingrese su edad: "))
            
            edad_valida = True
            return edad
            
        except ValueError:
            print("Valor no valido")


def generar_id():
    id_valido = False
    id = random.randint(1, 9999)

    id_ya_registrado = False
    
    while id_valido == False:
        archivo_de_guardado_json = open("log.json", "r", encoding="utf-8", newline='')

        data = json.load(archivo_de_guardado_json)
        for item in data:
            if str(id) == item:
                id_ya_registrado = True
                    
        while id_ya_registrado == True:
            id_ya_registrado = False
            id = random.randint(1, 9999)

            for item in data:
                if str(id) == item:
                    id_ya_registrado = True

        id_valido = True
        archivo_de_guardado_json.close()

    return id


def main_usuario():
    lista_de_eventos = ["Copa algorítmica", "Partido de Fútbol", "UADE Esports"]
    diccionario_de_usuarios = {}

    evento_elegido = validar_evento(lista_de_eventos)
    nombre = validar_nombre()
    edad = validar_edad()
    id = generar_id()

    print("Tu numero de identificación es " + str(id))

    diccionario_de_usuarios[id] = {}
    diccionario_de_usuarios.update({id: [nombre, edad, evento_elegido]})

    archivo_de_guardado_json = open("log.json", "r+", encoding="utf-8", newline='')
    data = json.load(archivo_de_guardado_json)
    data[str(id)] = diccionario_de_usuarios[id]
    archivo_de_guardado_json.close()
    
    archivo_de_guardado_json_nuevo = open("log.json", "r+", encoding="utf-8", newline='')
    json.dump(data, archivo_de_guardado_json_nuevo, indent=4, ensure_ascii=False)
    archivo_de_guardado_json_nuevo.close()


def validar_contraseña_de_admin():
    contraseña_admin: int = 1234

    contraseña = int(input("Ingrese la contraseña de administrador (Si ingreso al modo administrador por error, ingrese '0' para volver atras): "))

    while contraseña != contraseña_admin:
        if contraseña == 0:
            return False
        
        print("Contraseña incorrecta. Por favor, intente nuevamente.")
        contraseña = int(input("Ingrese la contraseña de administrador (Si ingreso al modo administrador por error, ingrese '0' para volver atras): "))

    return True

def main_admin():
    if validar_contraseña_de_admin():
        print("Contraseña valida")
    else:
        elegir_modo_para_entrar()


def elegir_modo_para_entrar():
    print("----------------------------")
    print("1. Ingresar como Usuario")
    print("2. Ingresar como Administrador")
    modo_elegido = int(input("Elija un modo para ingresar: "))

    while modo_elegido < 1 or modo_elegido > 2:
        print("El modo elegido es inválido. Por favor, intente nuevamente.")
        print("1. Ingresar como Usuario")
        print("2. Ingresar como Administrador")
        modo_elegido = int(input("Elija un modo para ingresar: "))
    
    if modo_elegido == 1:
        main_usuario()
    else:
        main_admin()


elegir_modo_para_entrar()