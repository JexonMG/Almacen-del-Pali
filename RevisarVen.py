def revisar_ventas(cursor, conn):
    cursor.execute('CREATE TABLE IF NOT EXISTS Ventas (nombre VARCHAR(50), precio INTEGER, cantidad INTEGER)')
    cursor.execute('SELECT * FROM Ventas')
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    conn.commit()
    