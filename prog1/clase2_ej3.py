precio_del_boleto_normal = 1032
precio_del_boleto_con_20_de_descuento = precio_del_boleto_normal- (precio_del_boleto_normal * 0.2)
precio_del_boleto_con_30_de_descuento = precio_del_boleto_normal - (precio_del_boleto_normal * 0.3)
precio_del_boleto_con_40_de_descuento = precio_del_boleto_normal - (precio_del_boleto_normal * 0.4)

def calcular_costo_de_viaje(viajes):
    costo_del_viaje = 0

    for i in range(viajes):
        if i <= 20:
            costo_del_viaje += precio_del_boleto_normal
        elif i > 20 and i <= 30:
            costo_del_viaje += precio_del_boleto_con_20_de_descuento
        elif i > 30 and i <= 40:
            costo_del_viaje += precio_del_boleto_con_30_de_descuento
        else:
            costo_del_viaje += precio_del_boleto_con_40_de_descuento

    return costo_del_viaje

cantidad_de_viajes = int(input("Ingrese la cantidad de viajes a realizar en el mes: "))

costo_total = calcular_costo_de_viaje(cantidad_de_viajes)
print(costo_total)