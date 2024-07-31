import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')

DROP_USERS_TABLE = 'DROP TABLE IF EXISTS users'

USERS_TABLE = '''CREATE TABLE users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)'''

# Comentario
# Son cambios necesarios

def system_clear(function):                             

    def wrapper(connect, cursor):                      

        os.system('clear')                              
        function(connect, cursor)                       
        
        input('')                                       
                                                        
        os.system('clear')                              
        
    wrapper.__doc__ = function.__doc__                  
                                                        
    return wrapper                                      


def user_exists(funtion):          
                                   
    def wrapper(connect, cursor):                     
                                                      
        id = input('Ingrese el id del usuario: ')     
        query = 'SELECT id FROM users WHERE id = %s' 
        cursor.execute(query, (id,))                  

        user = cursor.fetchone()                  
        if user:                                  
            funtion(id,connect,cursor)            
                                                  
        else:                                     
            print('Este usuario no existe')       
                                                  

    wrapper.__doc__ = funtion.__doc__             
                                                  
    return wrapper


@system_clear
def created_user(connect, cursor):
    '''a) crear un registro'''
    username = input('Ingresa un nombre de usuario: ').lower()
    email = input('Ingresa un email: ').lower()

    query = 'INSERT INTO users(username, email) VALUES(%s, %s)'
    values = (username, email)

    cursor.execute(query, values)
    connect.commit()

    print('>>>USUARIO CREADO')


@system_clear
def list_user(connect, cursor):
    '''b) listar registros'''

    query = 'SELECT id, username, email FROM users'
    cursor.execute(query)
    
    for id, username, email in cursor.fetchall(): 
        print(f'{id} - {username} - {email}')     


    print('>>>USUARIOS LISTA')

                                                                                 
@system_clear                                                 
@user_exists
def update_user(id, connect, cursor):             
    '''c) actulizar registro'''
                    
    username = input('Ingrese el nuevo username: ')
    email = input('Ingresa el nuevo email: ')

    query= 'UPDATE users SET username = %s, email = %s Where id = %s'
    values = (username, email, id)

    cursor.execute(query, values)
    connect.commit()

    print('>>>USUARIO ACTUALIZADO')

@system_clear
@user_exists                                      
def delete_user(id, connect, cursor):
    '''d) eliminar registro'''

    query = 'DELETE FROM users WHERE id = %s'
    cursor.execute(query, (id,))
    connect.commit()
    print('>>>USUARIO ELIMINADO')



def default(*args):                       
    print('OPCION NO VALIDA')


if __name__ == '__main__':
    
    
    options = {
        'a':created_user,
        'b':list_user,
        'c':update_user,
        'd':delete_user
    }

    try:
        connect = psycopg2.connect(f'dbname={db_name} user={db_user} password={db_password} host={db_host}')  

        with connect.cursor() as cursor:
            #$ cursor.execute(DROP_USERS_TABLE)  
            #$ cursor.execute(USERS_TABLE)       
            connect.commit()

            
            while True:
                for function in options.values(): 
                    print(function.__doc__)       
                print('q o quit para salir')      

                option = input('Selecciona una opcion valida: ').lower()


                if option =='quit' or option=='q':
                    break


                function = options.get(option, default) 
                function(connect, cursor)  


    except psycopg2.OperationalError as err:
        print('No fue posible realizar la conexion')
        print(err)

    finally:
        connect.close()
        print('Exito')

