import csv

def print_first_rows(file_path, file_delimiter):
    """
    Abre el archivo principal del dataset e imprime las primeras 
    10 filas para verificar que fue abierto correctamente.
    
    Args:
        file_path (str): La ruta del archivo a trabajar.
        file_delimiter (str): El caracter que separa las columnas.
    """
    #Abrimos el archivo en modo lectura
    with open(file_path, mode='r', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=file_delimiter)
          
        #Usamos enumerate para llevar la cuenta de las filas y frenar en 10
        for index, row in enumerate(reader):
            if index >= 10:
                break
            print(f"Fila {index + 1}: {row}\n")



def get_column_names(file_path, file_delimiter):
    """
    Lee el archivo principal del dataset y retorna una lista 
    con los nombres de todas sus columnas.
    
    Args:
        file_path (Path/str): La ruta del archivo a trabajar.
        file_delimiter (str): El caracter que separa las columnas.
    """
    with open(file_path, mode='r', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=file_delimiter)
        
        #Avanzamos a la primera posición, en donde se encuentran los headers
        headers = next(reader)
        
        return headers
    


def get_column_indices(file_path, file_delimiter):
    """
    Retorna un diccionario con el nombre de cada columna como clave
    y su posición como valor.

    Args:
        file_path (Path/str): La ruta del archivo a trabajar.
        file_delimiter (str): El caracter que separa las columnas.
    """

    #Traemos la lista de columnas y creamos el diccionario vacío column_indices
    headers = get_column_names(file_path, file_delimiter)
    column_indices = {}

    #Recorremos la lista, guardando el índice como valor y el nombre como clave
    for index, column_name in enumerate(headers):
        column_indices[column_name] = index
    
    return column_indices
