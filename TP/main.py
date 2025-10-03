import json

lista_de_eventos = ["Copa algorítmica", "Partido de Fútbol", "UADE Esports"]
diccionario_de_usuarios = {}


def main():

    print(diccionario_de_usuarios)
    evento_valido = False
    id_valido = False
    edad_valida = False

    while evento_valido == False:
        try:
            print("1. Copa algorítmica")
            print("2. Partido de fútbol")
            print("3. UADE Esports")
            evento_elegido = int(input("Elija un evento al que asistir: "))

            while evento_elegido < 1 or evento_elegido > 3:
                print("Numero de evento invalido. Intente nuevamente")
                print("1. Copa algorítmica")
                print("2. Partido de fútbol")
                print("3. UADE Esports")
                evento_elegido = int(input("Elija un evento al que asistir: "))

            match evento_elegido: 
                case 1:
                    evento_valido = True
                    print("Evento de 'Copa algorítmica' elegido")
                case 2:
                    evento_valido = True
                    print("Evento 'Partido de fútbol' elegido")
                case 3:
                    evento_valido = True
                    print("Evento de 'UADE Esports' elegido")

        except ValueError:
            print("Valor ingresado no valido")


    while id_valido == False:
        try:
            id = int(input("Ingrese su ID (numero del 1 al 9999): "))

            while id < 1 or id > 9999:
                print("Numero de id no valido. Intente nuevamente.")
                id = int(input("Ingrese su id (numero del 1 al 9999): "))

            id_ya_registrado = False

            with open("log.json", "r", encoding="utf-8", newline='') as archivo_de_guardado_json:

                data = json.load(archivo_de_guardado_json)
                
                for item in data:
                    if str(id) == item:
                       id_ya_registrado = True
                
                while id_ya_registrado == True or id < 1 or id > 9999:
                    print("Numero de id ya registrado o inválido. Intente nuevamente.")
                    id_ya_registrado = False
                    id = int(input("Ingrese su id (numero del 1 al 9999): "))

                    for item in data:
                        if str(id) == item:
                            id_ya_registrado = True

            id_valido = True

        except ValueError:
            print("Valor ingresado no valido. Intente nuevamente.")   
    

    nombre = input("Ingrese su nombre: ")
    
    while nombre.isdigit() or len(nombre) == 0:
        print("Nombre invalido")
        nombre = input("Ingrese su nombre: ")


    while edad_valida == False:
        try:
            edad = int(input("Ingrese su edad: "))

            while edad < 13 or edad > 100:
                print("Edad invalida. Intente nuevamente")
                edad = int(input("Ingrese su edad: "))
            
            edad_valida = True
            
        except ValueError:
            print("Valor no valido")

    diccionario_de_usuarios[id] = {}
    diccionario_de_usuarios.update({id: [nombre, edad, lista_de_eventos[evento_elegido - 1]]})


    with open("log.json", "r", encoding="utf-8", newline='') as archivo_de_guardado_json:
        data = json.load(archivo_de_guardado_json)

        data[str(id)] = diccionario_de_usuarios[id]
        
        with open("log.json", "w", encoding="utf-8") as archivo_de_guardado_json:
            json.dump(data, archivo_de_guardado_json)

            
main()


