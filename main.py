import json
import random

def devolver_lista_de_datos(evento_o_entrada):
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)

    lista_de_datos = []

    for i in data:
        for j in data[i]:
            lista_de_datos.append(j[evento_o_entrada])
    
    archivo_de_eventos_y_entradas_json.close()
    return lista_de_datos


def imprimir_opciones(lista_de_opciones: list):
    for x, evento in enumerate(lista_de_opciones):
        print(str(x + 1) + ". " + evento)


def validar_evento(lista_de_eventos: list):
    evento_valido = False

    while evento_valido == False:
        try:
            imprimir_opciones(lista_de_eventos)
            evento_elegido = int(input("Elija un evento al que asistir: "))
            lista_de_entradas = devolver_lista_de_datos(1)
            entradas_restantes_de_evento_elegido = lista_de_entradas[evento_elegido - 1]

            while evento_elegido < 1 or evento_elegido > len(lista_de_eventos) or entradas_restantes_de_evento_elegido < 0:
                print("Numero de evento invalido. Intente nuevamente")
                imprimir_opciones(lista_de_eventos)
                evento_elegido = int(input("Elija un evento al que asistir: "))
                lista_de_entradas = devolver_lista_de_datos(1)
                entradas_restantes_de_evento_elegido = lista_de_entradas[evento_elegido - 1]
            
            cantidad_de_entradas_elegida = verificar_cantidad_de_entradas()
            while cantidad_de_entradas_elegida > entradas_restantes_de_evento_elegido:
                print("La cantidad de entradas elegida excede la cantidad disponible para el evento elegido. Por favor ingrese una cantidad valida.")
                cantidad_de_entradas_elegida = verificar_cantidad_de_entradas()
            
            entradas_restantes_de_evento_elegido -= cantidad_de_entradas_elegida
            evento_valido = True

        except ValueError:
            print("Valor ingresado no valido")
    
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)
                
    for i in data:
        data[i][evento_elegido - 1][1] = entradas_restantes_de_evento_elegido
    
    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)

    archivo_de_eventos_y_entradas_json_actualizado.close()

    return lista_de_eventos[evento_elegido - 1], cantidad_de_entradas_elegida


def verificar_cantidad_de_entradas():
    cantidad_maxima_de_entradas = 9

    entrada_valida = False

    while entrada_valida == False:
        try: 
            cantidad_de_entradas = int(input("Ingrese la cantidad de entradas que desea comprar (maximo: " + str(cantidad_maxima_de_entradas) + "): "))
            
            while cantidad_de_entradas < 1 or cantidad_de_entradas > cantidad_maxima_de_entradas:
                print("La cantidad de entradas elegida no es valida.")
                cantidad_de_entradas = int(input("Ingrese la cantidad de entradas que desea comprar (maximo: " + str(cantidad_maxima_de_entradas) + "): "))
            
            entrada_valida = True
            return cantidad_de_entradas

        except ValueError:
            print("El valor ingresado no es valido.")


def validar_nombre():
    nombre = input("Ingrese su nombre: ") 
    
    while nombre.isdigit() or len(nombre) == 0:
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
    lista_de_eventos = devolver_lista_de_datos(0)
    diccionario_de_usuarios = {}

    evento_elegido, cantidad_de_entradas_elegida = validar_evento(lista_de_eventos)
    nombre = validar_nombre()
    edad = validar_edad()
    id = generar_id()

    print("Tu numero de identificación es " + str(id))

    diccionario_de_usuarios[id] = {}
    diccionario_de_usuarios.update({id: [nombre, "Edad: " + str(edad), evento_elegido, "Entradas: " + str(cantidad_de_entradas_elegida)]})

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


def ver_registros_completos():
    archivo_json = open("log.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_json)

    for x, item in enumerate(data):
        print("Usuario " + str(x + 1) + ":")
        print("ID: " + item)
        print("Nombre: " + data[item][0])
        print("Edad: " + str(data[item][1]))
        print("Evento al que asistío: " + data[item][2])
        print("-----------------------------------")

    archivo_json.close()


def ver_registro_especifico():
    archivo_json = open("log.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_json)

    id_valido = False

    while id_valido == False:
        try:
            id_elegido = int(input("Ingrese el id del usuario que desea encontrar: "))
            for item in data:
                if str(id_elegido) == item:
                    id_valido = True
                    break   
            
            if id_valido == False:
                print("El id no se ha encontrado.")

        except ValueError:
            print("El valor ingresado no es valido.")
 
    print("Usuario encontrado")
    print("Nombre: " + data[str(id_elegido)][0])
    print("Edad: " + str(data[str(id_elegido)][1]))
    print("Evento al que asistio: " + data[str(id_elegido)][2])
    print("---------------------")

    datos_del_usuario = ["nombre", "edad", "evento", "entradas"]

    mostrar_opciones_de_modificacion(datos_del_usuario)
    
    opcion_valida = False

    while opcion_valida == False:
        try:
            opcion_elegida = int(input("Elija una opcion de las anteriores: "))

            while opcion_elegida < 1 or opcion_elegida > len(datos_del_usuario):
                print("Opcion no valida. Por favor, intente nuevamente.")
                mostrar_opciones_de_modificacion(datos_del_usuario)
                opcion_elegida = int(input("Elija una opcion de las anteriores: "))
            
            opcion_valida = True

        except ValueError:
            print("El valor ingresado no es valido. Por favor, intente nuevamente.")
        
    buscar_dato_a_modificar(opcion_elegida, id_elegido)
    

    archivo_json.close()


def buscar_dato_a_modificar(opcion_elegida, id_elegido):
    archivo_json = open("log.json", "r+", encoding="utf-8", newline='')
    data = json.load(archivo_json)

    match opcion_elegida:
        case 1:
            modificar_nombre(id_elegido, data)
        case 2:
            modificar_edad(id_elegido, data)
        case 3:
            modificar_evento(id_elegido, data)
        case 4:
            modificar_entradas(id_elegido, data)
    
    archivo_json.close()

    archivo_json_actualizado = open("log.json", "w", encoding="utf-8", newline='')
    json.dump(data, archivo_json_actualizado, indent=4, ensure_ascii=False)
    archivo_json_actualizado.close()


def modificar_nombre(id_elegido, data):
    nuevo_nombre = input("Ingrese un nuevo nombre para reemplazar al existente: ")
    
    if (nuevo_nombre.isdigit() or nuevo_nombre == ""): return

    data[str(id_elegido)][0] = nuevo_nombre


def modificar_edad(id_elegido, data):
    edad_valida = False
    while edad_valida == False:
        try:
            nueva_edad = int(input("Ingrese un nuevo valor para reemplazar al existente: "))

            while nueva_edad < 13 or nueva_edad > 100:
                print("Edad ingresada no válida.")
                nueva_edad = int(input("Ingrese un nuevo valor para reemplazar al existente: "))

            edad_valida = True

        except ValueError:
            print("El valor ingresado no es válido. Por favor, intente nuevamente.")

    data[str(id_elegido)][1] = "Edad: " + str(nueva_edad)


def modificar_evento(id_elegido, data):
    lista_de_eventos_actual = devolver_lista_de_datos(0)

    evento_valido = False
    while evento_valido == False:
        try:
            print("--------------------------------------------")
            for x, i in enumerate(lista_de_eventos_actual):
                print(str(x + 1) + ". " + i)
            nuevo_evento = int(input("Elija un nuevo evento de las opciones anteriores para reemplazar al existente: "))

            while nuevo_evento < 1 or nuevo_evento > len(lista_de_eventos_actual):
                print("Opcion elegida no válida. Por favor, intente nuevamente.")
                print("--------------------------------------------")
                for x, i in enumerate(lista_de_eventos_actual):
                    print(str(x + 1) + ". " + i)
                nuevo_evento = int(input("Elija un nuevo evento de las opciones anteriores para reemplazar al existente: "))

            evento_valido = True

        except ValueError:
            print("El valor ingresado no es válido. Por favor, intente nuevamente.")

    data[str(id_elegido)][2] = lista_de_eventos_actual[nuevo_evento - 1]


def modificar_entradas(id_elegido, data):
    cantidad_de_entradas_valida = False
    while cantidad_de_entradas_valida == False:
        try:
            nueva_cantidad_de_entradas = int(input("Ingrese una nueva cantidad de entradas para reemplazar a la existente: "))

            while nueva_cantidad_de_entradas < 1 or nueva_cantidad_de_entradas > 9:
                print("Cantidad de entradas ingresada no válida.")
                nueva_cantidad_de_entradas = int(input("Ingrese una nueva cantidad de entradas para reemplazar a la existente: "))

            cantidad_de_entradas_valida = True

        except ValueError:
            print("El valor ingresado no es válido. Por favor, intente nuevamente.")

    numero_de_entradas_encontrado = None

    for i in data[str(id_elegido)][3]:
        if i.isdigit():
           numero_de_entradas_encontrado = i
           break

    data[str(id_elegido)][3] = "Entradas: " + str(nueva_cantidad_de_entradas)

    cantidad_de_entradas_restantes_actualizada = int(numero_de_entradas_encontrado) - nueva_cantidad_de_entradas

    lista_de_eventos = devolver_lista_de_datos(0)

    index_de_evento_elegido = lista_de_eventos.index(data[str(id_elegido)][2])

    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data_eventos_entradas = json.load(archivo_de_eventos_y_entradas_json)

    for i in data_eventos_entradas:
        data_eventos_entradas[i][index_de_evento_elegido][1] += cantidad_de_entradas_restantes_actualizada
    

    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "w", encoding="utf-8", newline='')
    
    json.dump(data_eventos_entradas, archivo_de_eventos_y_entradas_json, indent=4, ensure_ascii=False)
    archivo_de_eventos_y_entradas_json.close()

        
def mostrar_opciones_de_modificacion(datos_del_usuario):
    for x in range(len(datos_del_usuario)):
        print(str(x + 1) + ". " + "Modificar " + datos_del_usuario[x] + " del usuario")

    print(str(len(datos_del_usuario) + 1) + ". Salir") 


def imprimir_opciones_para_administrador(lista_de_opciones_de_administrador):
    for x, item in enumerate(lista_de_opciones_de_administrador):
        print(str(x + 1) + ". " + item)


def elegir_opcion_para_administador(opcion_elegida):
    funciones_para_ejecutar = {1: ver_registros_completos, 2: ver_registro_especifico, 3: agregar_evento, 4: remover_evento}

    funciones_para_ejecutar[opcion_elegida]()


def agregar_evento():
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)

    evento = input("Ingrese un nombre para el evento a agregar: ")

    while evento.isdigit() or evento == "":
        print("Nombre no válido.")
        evento = input("Ingrese un nombre para el evento a agregar: ")

    for i in data:
        data[i].append([evento, 250])
    
    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)
    archivo_de_eventos_y_entradas_json_actualizado.close()


def remover_evento():
    lista_de_eventos = devolver_lista_de_datos(0) # ["Copa algoritimica", "Partido de futbol", "UADE Esports"]

    evento_valido = False

    while evento_valido == False:
        try:
            print("---------------------------------------")
            imprimir_opciones(lista_de_eventos)
            evento_a_remover = int(input("Elija el evento que desea remover: "))

            while evento_a_remover < 1 or evento_a_remover > len(lista_de_eventos):
                print("El evento elegido no existe. Por favor, intente de nuevo.")
                print("---------------------------------------")
                imprimir_opciones(lista_de_eventos)
                evento_a_remover = int(input("Elija el evento que desea remover: "))
                
            evento_valido = True

        except ValueError:
            print("El valor ingresado no es válido. Por favor, intente nuevamente.")
    
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)
    
    lista_de_datos = data["eventos_y_entradas_restantes"]
    lista_de_datos.remove(lista_de_datos[evento_a_remover - 1])
    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)



def main_admin():
    lista_de_opciones_de_administrador = ["Ver registros completos de usuarios", "Modificar un registro de usuario", "Agregar evento", "Remover evento"]

    if validar_contraseña_de_admin():
        
        imprimir_opciones_para_administrador(lista_de_opciones_de_administrador)
        opcion_elegida = int(input("Elija una opcion para continuar: "))

        opcion_valida = False

        while opcion_valida == False:
            try:
                while opcion_elegida < 1 or opcion_elegida > len(lista_de_opciones_de_administrador):
                    print("Opción no válida. Por favor, intente nuevamente.")
                    imprimir_opciones_para_administrador(lista_de_opciones_de_administrador)
                    opcion_elegida = int(input("Elija una opcion para continuar: "))
                
                opcion_valida = True

            except ValueError:
                print("El valor ingresado no es válido. Por favor, intente nuevamente.")
        
        elegir_opcion_para_administador(opcion_elegida)

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