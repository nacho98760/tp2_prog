lista_de_eventos = ["Evento 1", "Evento 2", "Evento 3"]
diccionario_de_usuarios = {}

def main():

    evento_valido = False
    id_valido = False
    edad_valida = False

    while evento_valido == False:
        try:
            print("1. Evento 1")
            print("2. Evento 2")
            print("3. Evento 3")
            evento_elegido = int(input("Elija un evento al que asistir: "))

            while evento_elegido < 0 or evento_elegido > 3:
                print("Numero de evento invalido. Intente nuevamente")
                evento_elegido = int(input("Elija un evento al que asistir: "))

            match evento_elegido: 
                case 1:
                    evento_valido = True
                    print("Evento 1 elegido")
                case 2:
                    evento_valido = True
                    print("Evento 2 elegido")
                case 3:
                    evento_valido = True
                    print("Evento 3 elegido")

        except ValueError:
            print("Valor ingresado no valido")


    while id_valido == False:
        try:
            id = int(input("Ingrese su id (numero del 1 al 9999)"))
            
            while id < 1 or id > 9999:
                print("Numero de id no valido. Intente nuevamente.")
                id = int(input("Ingrese su id (numero del 1 al 9999)"))
            
            id_valido = True

        except ValueError:
            print("Valor ingresado no valido. Intente nuevamente.")   
    

    nombre = input("Ingrese su nombre: ")
    
    while nombre.isdigit() or len(nombre) == 0:
        print("Nombre invalido")
        nombre = input("Ingrese su nombre: ")



    while edad_valida == False:
        try:
            edad = int(input("Ingrese su edad"))

            while edad < 13 or edad > 100:
                print("Edad invalida. Intente nuevamente")
                edad = int(input("Ingrese su edad"))
            
            edad_valida = True
            
        except ValueError:
            print("Valor no valido")


    diccionario_de_usuarios[id] = {nombre, edad}
    print(diccionario_de_usuarios)

main()


