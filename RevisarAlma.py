def revisar_almacen(cursor, conn):
    cursor.execute('CREATE TABLE IF NOT EXISTS Almacen (codigo SERIAL PRIMARY KEY, nombre VARCHAR(350), precio DOUBLE PRECISION, cantidad INTEGER, tipo VARCHAR(50))')
    cursor.execute('SELECT * FROM Almacen')
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    conn.commit()
