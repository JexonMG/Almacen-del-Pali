def registrar_ventas(cursor, conn):
    cursor.execute('SELECT nombre, precio, cantidad FROM Almacen')
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    venta = input('Ingrese el nombre del producto a vendido: ')
    venta = venta.lower().replace(" ", "")
    cursor.execute('SELECT precio FROM Almacen WHERE nombre = %s', (venta,))
    resultados = cursor.fetchall()
    if resultados == []:
        print('No existe el producto')
    else:
        cantidad = int(input('Ingrese la cantidad vendida del producto: '))
        cursor.execute('SELECT cantidad FROM Almacen WHERE nombre = %s', (venta,))
        TotalCant = cursor.fetchall()
        if cantidad > TotalCant[0][0]:
            print('No hay suficiente cantidad de producto')
        else:
            cursor.execute('SELECT precio FROM Almacen WHERE nombre = %s', (venta,))
            resultados = cursor.fetchall()
            precio = resultados[0][0] * cantidad
            cursor.execute('INSERT INTO Ventas VALUES (%s, %s, %s)', (venta, precio, cantidad))
            Cantidades = TotalCant[0][0] - cantidad
            cursor.execute('UPDATE Almacen SET cantidad = %s WHERE nombre = %s', (Cantidades, venta))
            conn.commit()
            print('---- Producto registrado en la venta -----')
    
    
def analisisProducto(cursor):
    # Most sold product
    cursor.execute('SELECT nombre, SUM(cantidad), precio FROM Ventas GROUP BY nombre, precio ORDER BY SUM(cantidad) DESC LIMIT 1')
    resultados = cursor.fetchall()
    print('Producto mas vendido: ', resultados[0][0])
    print('Cantidad vendida: ', resultados[0][1])
    print('Ganancias: ', resultados[0][2])

    # Least sold product
    cursor.execute('SELECT nombre, SUM(cantidad), precio FROM Ventas GROUP BY nombre, precio ORDER BY SUM(cantidad) ASC LIMIT 1')
    resultados = cursor.fetchall()
    print('Producto menos vendido: ', resultados[0][0])
    print('Cantidad vendida: ', resultados[0][1])
    print('Ganancias: ', resultados[0][2])


def administrasVentas(cursor, conn):
    while True:
        print('''
        1. Analisis de productos
        2. Registrar ventas del dia
        3. Salir
        ''')
        option = int(input('Ingrese una opcion: '))
        if option == 1:
            analisisProducto(cursor)
        elif option == 2:
            registrar_ventas(cursor, conn)
        elif option == 3:
            print('Saliendo...')
            break
        else:
            print('Opcion invalida')