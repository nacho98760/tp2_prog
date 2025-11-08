import json
import random

def devolver_lista_de_datos(dato_a_buscar):
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)

    lista_de_datos = []

    for i in data:
        for j in data[i]:
            lista_de_datos.append(j[dato_a_buscar])
    
    archivo_de_eventos_y_entradas_json.close()
    return lista_de_datos


def imprimir_opciones(lista_de_opciones):
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)

    lista_de_precios = devolver_lista_de_datos(3)

    print('---------------------------------------')
    for x, evento in enumerate(lista_de_opciones):
        print(str(x + 1) + ". " + evento + " (precio: " + str(lista_de_precios[x]) + ") " + buscar_si_quedan_entradas(data, evento))

def buscar_si_quedan_entradas(data, evento):
    tiene_entradas = ""

    for i in data:
        for j in data[i]:
            if j[0] == evento:
                if j[1] <= 0:
                    tiene_entradas = " (No tiene entradas disponibles)"
                    break
    
    return tiene_entradas
    

def validar_evento(lista_de_eventos):
    evento_valido = False

    entradas_restantes_de_evento_elegido = 0

    while evento_valido == False:
        try:
            imprimir_opciones(lista_de_eventos)
            evento_elegido = int(input("Elija un evento al que asistir: "))

            if evento_elegido < 0 or evento_elegido > len(lista_de_eventos):
                print("Evento elegido no valido.")
                return

            lista_de_entradas = devolver_lista_de_datos(1)
            entradas_restantes_de_evento_elegido = lista_de_entradas[evento_elegido - 1]
            
            while evento_elegido < 1 or evento_elegido > len(lista_de_eventos) or entradas_restantes_de_evento_elegido <= 0:
                print(evento_elegido)
                print(len(lista_de_eventos))
                print(entradas_restantes_de_evento_elegido)
                print('---------------------------------------')
                print("El numero de evento es invalido o no quedan entradas disponibles. Intente nuevamente")
                imprimir_opciones(lista_de_eventos)
                evento_elegido = int(input("Elija un evento al que asistir: "))
                
                if evento_elegido < 0 or evento_elegido > len(lista_de_eventos):
                    print("Evento elegido no valido.")
                    return
                
                lista_de_entradas = devolver_lista_de_datos(1)
                entradas_restantes_de_evento_elegido = lista_de_entradas[evento_elegido - 1]
            
            cantidad_de_entradas_elegida = verificar_cantidad_de_entradas()

            ingresar_cantidad_de_entradas(entradas_restantes_de_evento_elegido, evento_elegido, cantidad_de_entradas_elegida)
            evento_valido = True

        except ValueError:
            print("Valor ingresado no valido")
    
    lista_de_precios = devolver_lista_de_datos(3)
    precio_final = lista_de_precios[evento_elegido - 1] * cantidad_de_entradas_elegida

    return lista_de_eventos[evento_elegido - 1], cantidad_de_entradas_elegida, precio_final


def ingresar_cantidad_de_entradas(entradas_restantes_de_evento_elegido, evento_elegido, cantidad_de_entradas_elegida):
    while cantidad_de_entradas_elegida > entradas_restantes_de_evento_elegido:
        print("La cantidad de entradas elegida excede la cantidad disponible para el evento elegido. Por favor ingrese una cantidad valida.")
        cantidad_de_entradas_elegida = verificar_cantidad_de_entradas()
            
    nueva_cantidad_de_entradas = entradas_restantes_de_evento_elegido - cantidad_de_entradas_elegida

    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)
                
    for i in data:
        data[i][evento_elegido - 1][1] = nueva_cantidad_de_entradas
    
    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)

    archivo_de_eventos_y_entradas_json_actualizado.close()

def devolver_entradas_a_evento_anterior(cantidad_de_entradas_elegida, evento_anterior):
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)
                
    lista_de_eventos = devolver_lista_de_datos(0)
    index_del_evento_anterior = lista_de_eventos.index(evento_anterior)

    for i in data:
        data[i][index_del_evento_anterior][1] += cantidad_de_entradas_elegida
    
    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)

    archivo_de_eventos_y_entradas_json_actualizado.close()

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
    
    while nombre.isdigit() or len(nombre) == 0 or nombre.strip() == "":
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

    evento_elegido, cantidad_de_entradas_elegida, precio_final = validar_evento(lista_de_eventos)
    nombre = validar_nombre()
    edad = validar_edad()
    id = generar_id()

    print("Tu numero de identificación es " + str(id))

    diccionario_de_usuarios[id] = {}
    diccionario_de_usuarios.update({id: [nombre, "Edad: " + str(edad), evento_elegido, "Entradas: " + str(cantidad_de_entradas_elegida), "Precio final: " + str(precio_final)]})

    archivo_de_guardado_json = open("log.json", "r+", encoding="utf-8", newline='')
    data = json.load(archivo_de_guardado_json)
    data[str(id)] = diccionario_de_usuarios[id]
    archivo_de_guardado_json.close()
    
    archivo_de_guardado_json_nuevo = open("log.json", "r+", encoding="utf-8", newline='')
    json.dump(data, archivo_de_guardado_json_nuevo, indent=4, ensure_ascii=False)
    archivo_de_guardado_json_nuevo.close()

    continuar_programa_o_salir()


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
        print(str(data[item][1]))
        print("Evento al que asiste: " + data[item][2])
        print("Cantidad de entradas: " + data[item][3])
        print("Precio final: " + data[item][4])
        print("-----------------------------------")

    archivo_json.close()
    verificar_opcion_elegida()


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
            print("El valor ingresado no es válido.")
 
    print("Usuario encontrado")
    print("Nombre: " + data[str(id_elegido)][0])
    print(str(data[str(id_elegido)][1]))
    print("Evento al que asiste: " + data[str(id_elegido)][2])
    print("Cantidad de entradas: " + str(data[str(id_elegido)][3]))
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
            print("El valor ingresado no es válido. Por favor, intente nuevamente.")
        
    buscar_dato_a_modificar(opcion_elegida, id_elegido)
    
    archivo_json.close()

    verificar_opcion_elegida()


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
    
    while nuevo_nombre.isdigit() or nuevo_nombre.strip() == "": 
        print("El nombre no es válido. Por favor, intente nuevamente.")
        nuevo_nombre = input("Ingrese un nuevo nombre para reemplazar al existente: ")

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
    evento_actual = data[str(id_elegido)][2]

    lista_de_eventos_actual = devolver_lista_de_datos(0)
    
    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data_eventos = json.load(archivo_de_eventos_y_entradas_json)

    evento_valido = False
    while evento_valido == False:
        try:
            print('---------------------------------------')
            for x, evento in enumerate(lista_de_eventos_actual):
                print(str(x + 1) + ". " + evento + buscar_si_quedan_entradas(data_eventos, evento))

            nuevo_evento = int(input("Elija un nuevo evento de las opciones anteriores para reemplazar al existente: "))

            if nuevo_evento < 0 or nuevo_evento > len(lista_de_eventos_actual):
                print("Evento elegido no valido.")
                return
            
            lista_de_entradas = devolver_lista_de_datos(1)
            entradas_restantes_de_evento_elegido = lista_de_entradas[nuevo_evento - 1]

            while nuevo_evento < 1 or nuevo_evento > len(lista_de_eventos_actual) or entradas_restantes_de_evento_elegido <= 0:
                print("El número de evento es invalido o no quedan entradas disponibles. Intente nuevamente.")
                print("--------------------------------------------")
                for x, i in enumerate(lista_de_eventos_actual):
                    print(str(x + 1) + ". " + i + buscar_si_quedan_entradas(data_eventos, i))
                nuevo_evento = int(input("Elija un nuevo evento de las opciones anteriores para reemplazar al existente: "))

                if nuevo_evento < 0 or nuevo_evento > len(lista_de_eventos_actual):
                    print("Evento elegido no valido.")
                    return
            
                lista_de_entradas = devolver_lista_de_datos(1)
                entradas_restantes_de_evento_elegido = lista_de_entradas[nuevo_evento - 1]

            evento_valido = True

        except ValueError:
            print("El valor ingresado no es válido. Por favor, intente nuevamente.")
    

    cantidad_de_entradas_elegida = verificar_cantidad_de_entradas()
    ingresar_cantidad_de_entradas(entradas_restantes_de_evento_elegido, nuevo_evento, cantidad_de_entradas_elegida)
    devolver_entradas_a_evento_anterior(cantidad_de_entradas_elegida, evento_actual)
    data[str(id_elegido)][2] = lista_de_eventos_actual[nuevo_evento - 1]
    data[str(id_elegido)][3] = "Entradas: " + str(cantidad_de_entradas_elegida)


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
    print("--------------------------------------------")
    for x, item in enumerate(lista_de_opciones_de_administrador):
        print(str(x + 1) + ". " + item)


def elegir_opcion_para_administador(opcion_elegida):
    funciones_para_ejecutar = {1: ver_registros_completos, 2: ver_registro_especifico, 3: agregar_evento, 4: remover_evento, 5: continuar_programa_o_salir}

    funciones_para_ejecutar[opcion_elegida]()

def calcular_dias_del_mes(mes):
    meses_con_30_dias = [4, 6, 9, 11]
    meses_con_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses_con_28_dias = [2]

    if mes in meses_con_30_dias:
        return 30
    elif mes in meses_con_31_dias:
        return 31
    elif mes in meses_con_28_dias:
        return 28
    

def agregar_evento(): 
    evento = input("Ingrese un nombre para el evento a agregar: ")

    while evento.isdigit() or evento.strip() == "":
        print("Nombre no válido.")
        evento = input("Ingrese un nombre para el evento a agregar: ")

    cantidad_valida = False
    while cantidad_valida == False:
        try:
            cantidad_de_entradas_maxima = int(input("Ingrese la cantidad de entradas maximas para este evento (Mínimo 50): "))

            while cantidad_de_entradas_maxima < 50:
                print("La cantidad de entradas máximas es muy baja. Por favor, intente nuevamente.")
                cantidad_de_entradas_maxima = int(input("Ingrese la cantidad de entradas maximas para este evento (Mínimo 50): ")) 
            
            cantidad_valida = True

        except ValueError:
            print("La cantidad ingresada no es válida. Por favor, intente nuevamente")

    
    mes_valido = False

    while mes_valido == False:
        try:
            mes = int(input("Ingrese el numero del mes en el que se realizara el evento: "))
            while mes < 1 or mes > 12:
                print("El mes ingresado es invalido. Por favor, intente nuevamente")
                mes = int(input("Ingrese el numero del mes en el que se realizara el evento: "))

            mes_valido = True
        except ValueError:
            print("Valor ingresado no valido")

    dia_valido = False
    
    while dia_valido == False:
        try:
            dia = int(input("Ingrese el numero del dia en el que se realizara el evento: "))
            while dia < 1 or dia > calcular_dias_del_mes(mes):
                print("El dia ingresado es invalido. Por favor, intente nuevamente")
                dia = int(input("Ingrese el numero del dia en el que se realizara el evento: "))

            dia_valido = True
        except ValueError:
            print("Valor ingresado no valido")

    fecha = str(mes).zfill(2) + "/" + str(dia).zfill(2)

    precio_valido = False
    while precio_valido == False:
        try:
            precio_del_evento = int(input("Ingrese un precio para este evento (Mínimo $1000): "))

            while precio_del_evento < 1000:
                print("La cantidad de entradas máximas es muy baja. Por favor, intente nuevamente.")
                precio_del_evento = int(input("Ingrese un precio para este evento (Mínimo $1000): "))
            
            precio_valido = True

        except ValueError:
            print("El precio ingresado no es valido. Por favor, intente nuevamente")

    archivo_de_eventos_y_entradas_json = open("eventos_y_entradas.json", "r", encoding="utf-8", newline='')
    data = json.load(archivo_de_eventos_y_entradas_json)

    for i in data:
        data[i].append([evento, cantidad_de_entradas_maxima, fecha, precio_del_evento])
            
    archivo_de_eventos_y_entradas_json.close()

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w+", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)
    archivo_de_eventos_y_entradas_json_actualizado.close()

    verificar_opcion_elegida()


def remover_evento():
    lista_de_eventos = devolver_lista_de_datos(0) # "0" devuelve eventos, "1" devuelve entradas

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

    archivo_de_eventos_y_entradas_json_actualizado = open("eventos_y_entradas.json", "w+", encoding="utf-8", newline='')
    json.dump(data, archivo_de_eventos_y_entradas_json_actualizado, indent=4, ensure_ascii=False)


def verificar_opcion_elegida():
    lista_de_opciones_de_administrador = ["Ver registros completos de usuarios", "Modificar un registro de usuario", "Agregar evento", "Remover evento", "Volver atrás"]

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


def main_admin():
    if validar_contraseña_de_admin():
        verificar_opcion_elegida()

    else:
        elegir_modo_para_entrar()


def continuar_programa_o_salir():
    opcion_valida = False

    while opcion_valida == False:
        try:
            print("----------------------------")
            print('1. Volver a correr el programa')
            print('2. Salir')
            opcion_elegida = int(input('Elige una de las siguientes opciones: '))

            while opcion_elegida < 1 or opcion_elegida > 2:
                print('La opcion elegida no es valida. Por favor, intente nuevamente.')
                print("----------------------------")
                print('1. Volver a correr el programa')
                print('2. Salir')
                opcion_elegida = int(input('Elige una de las siguientes opciones: '))
            
            opcion_valida = True
        except ValueError:
            print('Valor ingresado no valido. Intente nuevamente.')
    
    if opcion_elegida == 1:
        elegir_modo_para_entrar()
    else:
        quit()


def elegir_modo_para_entrar():
    opcion_valida = False

    while opcion_valida == False:
        try:
            print("----------------------------")
            print("1. Ingresar como Usuario")
            print("2. Ingresar como Administrador")
            modo_elegido = int(input("Elija un modo para ingresar: "))

            while modo_elegido < 1 or modo_elegido > 2:
                print("El modo elegido es inválido. Por favor, intente nuevamente.")
                print("1. Ingresar como Usuario")
                print("2. Ingresar como Administrador")
                modo_elegido = int(input("Elija un modo para ingresar: "))
            
            opcion_valida = True

        except ValueError:
            print('Valor ingresado no valido. Intente nuevamente.')

    if modo_elegido == 1:
        main_usuario()
    else:
        main_admin()

elegir_modo_para_entrar()