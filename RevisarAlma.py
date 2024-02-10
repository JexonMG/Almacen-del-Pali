def revisar_almacen(cursor, conn):
    cursor.execute('CREATE TABLE IF NOT EXISTS Almacen (codigo SERIAL PRIMARY KEY, nombre VARCHAR(350), precio DOUBLE PRECISION, cantidad INTEGER, tipo VARCHAR(50))')
    cursor.execute('SELECT * FROM Almacen')
    resultados = cursor.fetchall()
    if resultados == []:
        print('No hay productos en el almacen')
    else:
        print('Codigo | Nombre | Precio | Cantidad | Tipo')
        for resultado in resultados:
            print(resultado)
    conn.commit()
