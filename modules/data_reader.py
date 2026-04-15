import csv

def print_first_rows(file_path, file_delimiter):
    """
    Abre el archivo principal del dataset con la librería csv 
    e imprime las primeras 10 filas para verificar que
    fue abierto correctamente.
    
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
