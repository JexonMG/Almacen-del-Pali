def registrar_ventas(cursor, conn):
    cursor.execute('SELECT nombre, precio FROM Almacen')
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    venta = input('Ingrese el nombre del producto a vendido: ')
    venta = venta.lower().replace(" ", "")
    cursor.execute('SELECT precio FROM Almacen WHERE nombre = %s')
    resultados = cursor.fetchall()
    if resultados == []:
        print('No existe el producto')
    else:
        cantidad = int(input('Ingrese la cantidad del producto: '))
        cursor.execute('SELECT cantidad FROM Almacen WHERE nombre = %s', (venta,))
        TotalCant = cursor.fetchall()
        if cantidad > TotalCant:
            print('No hay suficiente cantidad de producto')
        else:
            cursor.execute('SELECT precio FROM Almacen WHERE nombre = %s', (venta,))
            resultados = cursor.fetchall()
            precio = resultados * cantidad
            cursor.execute('INSERT INTO Ventas VALUES (%s, %s, %s)', (venta, precio, cantidad))
            Cantidades = TotalCant - cantidad
            cursor.execute('UPDATE Almacen SET cantidad = %s WHERE nombre = %s', (Cantidades, venta))
            conn.commit()
            print('---- Producto registrado en la venta -----')
    
    
    

def main(cursor, conn):
    while True:
        print('''
        1. Producto mas vendido
        2. Producto menos vendido
        3. Registrar ventas del dia
        4. Salir
        ''')
        option = int(input('Ingrese una opcion: '))
        if option == 1:
            producto_mas_vendido(cursor)
        elif option == 2:
            producto_menos_vendido(cursor)
        elif option == 3:
            registrar_ventas(cursor, conn)
        elif option == 4:
            print('Saliendo...')
            break
        else:
            print('Opcion invalida')