def arreglo_numero(precio):
    numero = precio
    # Convertir el número a una cadena y obtener su longitud
    numero_str = str(numero)
    longitud = len(numero_str)

    # Inicializar variables para el bucle y el nuevo número formateado
    bucle = ''
    nuevo_numero = ''

    # Iterar sobre cada dígito del número original en sentido inverso
    for i in range(longitud - 1, -1, -1):
        bucle = numero_str[i] + bucle  # Agregar el dígito al principio del bucle

        # Si el bucle alcanza tres dígitos o es el primer dígito
        if len(bucle) == 3 or (i == 0 and len(bucle) > 0):
            nuevo_numero = ',' + bucle + nuevo_numero  # Agregar comas y el bucle al principio del nuevo número
            bucle = ''  # Reiniciar el bucle

    # Eliminar la coma inicial si existe
    nuevo_numero = nuevo_numero.lstrip(',')
    nuevo_numero = '₡' + nuevo_numero
    return nuevo_numero

def agregar_producto(cursor, conn):
    nombre = input('Ingrese el nombre del producto: ')
    nombre = nombre.lower().replace(" ", "")
    tipo = input('Ingrese el tipo del producto: ')
    tipo = tipo.lower().replace(" ", "")
    precio = int(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))
    if precio != 0 and cantidad != 0 and nombre != '' and tipo != '':
        iva = precio * 0.13
        precio = precio + iva
        #precio = arreglo_numero(precio)
        cursor.execute('INSERT INTO Almacen (nombre, precio, cantidad, tipo) VALUES (%s, %s, %s, %s)', (nombre, precio, cantidad, tipo))
        conn.commit()
        print('---- Producto registrado en el almacen -----')
    else:
        print('No se puede agregar un producto sin precio o cantidad')


def eliminar_producto(cursor, conn):
    cursor.execute('SELECT * FROM Almacen')
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    codigo = input('Ingrese el codigo del producto a eliminar: ')
    cursor.execute('DELETE FROM Almacen WHERE codigo = %s', (codigo,))
    conn.commit()
    print('---- Producto eliminado del almacen -----')
    
def modificar_producto(cursor, conn):
    cursor.execute('SELECT * FROM Almacen')
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    codigo = input('Ingrese el codigo del producto a modificar: ')
    nombre = input('Ingrese el nombre del producto: ')
    tipo = input('Ingrese el tipo del producto: ')
    precio = int(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))
    if precio != 0 and cantidad != 0 and nombre != '' and tipo != '':
        iva = precio * 0.13
        precio = precio + iva
        #precio = arreglo_numero(precio)
        cursor.execute('UPDATE Almacen SET nombre = %s, precio = %s, cantidad = %s, tipo = %s WHERE codigo = %s', (nombre, precio, cantidad, tipo, codigo))
        conn.commit()
        print('---- Producto modificado en el almacen -----')
    else:
        print('No se puede modificar un producto sin precio o cantidad')
    

def AdministrarAlma(cursor, conn):
    while True:
        print('''
        1. Agregar producto
        2. Eliminar producto
        3. Modificar producto
        4. Salir
        ''')
        option = int(input('Ingrese una opcion: '))

        if option == 1:
            agregar_producto(cursor, conn)
        elif option == 2:
            eliminar_producto(cursor, conn)
        elif option == 3:
            modificar_producto(cursor, conn)
        elif option == 4:
            print('Saliendo...')
            break  # Exit the loop
        else:
            print('Opcion no valida. Intente de nuevo.')