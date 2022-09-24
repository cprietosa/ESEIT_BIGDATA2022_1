# pseudo codigo
# main()
#   datos = get_data(filename)
#   reporte = generate_reporte(datos)
#    save_data(reporte)
import os
from pathlib import Path
import pandas as pd
root_dir = Path(".").resolve()

def get_data(filename):
    data_dir = "raw"
    file_path = os.path.join(root_dir,"data",data_dir,filename)  # Ruta del archivo que necesito 

    datos = pd.read_csv(file_path,sep=";",encoding="latin-1")
    print('get_data')
    print('La tabla contiene', datos.shape[0], 'filas', datos.shape[1], 'columnnas')
    return datos

def generate_reporte(datos):
    # Crear un diccionario vacio
    dict_reporte = dict()

    # look para llenar el diccionario de columnas con valores unicas
    for col in datos.columns:
        valores_unicos=datos[col].unique()
        n_valores=len(valores_unicos)
        dict_reporte[col] = n_valores
    # print('columna',col,n_unicos)}

    reporte = pd.DataFrame.from_dict(dict_reporte, orient='index')
    reporte.rename({0: 'conteo'}, inplace=True,axis=1)   # 1 buscar en la columna, 0 en las filas

    print('generate_report')
    print(reporte.head())
    return reporte


def save_date(reporte,filename):
    # Guardar tabla
    out_name = 'resumen_' + filename # Renombrar ya el archivo de salida
    out_path =  os. path.join(root_dir,"data", "processed", out_name)
    reporte.to_csv(out_path)

def main():

    filename = 'llamadas123_julio_2022.csv'
    datos = get_data(filename)
    reporte = generate_reporte(datos)
    save_date(reporte, filename)

if __name__ == '__main__':
    main()