import psycopg2
from RevisarAlma import revisar_almacen
from RevisarVen import revisar_ventas
from AdminAlma import AdministrarAlma
def menu():
    print('''
_________    _____   .____     .___ 
\______   \  /  _  \  |    |    |   |
 |     ___/ /  /_\  \ |    |    |   |
 |    |    /    |    \|    |___ |   |
 |____|    \____|__  /|_______ \|___|
    Opciones:
    1. Revisar Almacen
    2. Revisar Ventas
    3. Administar Almacen
    4. Administar Ventas
    5. Salir ''')

def main():
    conn = psycopg2.connect(database='postgres', user='postgres', password='posgres', host='localhost', port='5432')
    cursor = conn.cursor()
    user = 'Admin'
    password = '1234'
    while True:
        input_user = input('Ingrese su usuario: ')
        input_password = input('Ingrese su contraseña: ')
        
        if input_user == user and input_password == password:
            menu() 
            option = int(input('Ingrese una opcion: '))
            if option == 1:
                revisar_almacen(cursor, conn)
                print('Accion realizada')
            elif option == 2:
                revisar_ventas(cursor, conn)
                print('Accion realizada')
            elif option == 3:
                AdministrarAlma(cursor, conn)
                print('Accion realizada')
            elif option == 4:
                print('Administar Ventas')
            elif option == 5:
                print('Saliendo del programa...')
                break
        else:
            print('Usuario o contraseña incorrectos')

if __name__ == "__main__":
    main()