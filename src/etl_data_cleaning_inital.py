# PSEUCODIGO
# main()
#   datos = leer_datos(nombre del archivo : str) -> pd.dataframe
#   datos_no_dup = remover_duplicados_y_nulos(datos: pd.dataframe) ->pd.dat
#   datos = convertir_str_a_num(datos, col='EDAD') -> pd.dataframe
#   datos = coggerir_fechas(datos, col='FECHA1') -> pd.dataframe
#   datos = coggerir_fechas(datos, col='FECHA2') -> pd.dataframe
#   save_data()

import numpy as np
import pandas as pd 
import os
from pathlib import Path
from dateutil.parser import parse

root_dir = Path(".").resolve()
filename = "llamadas123_julio_2022.csv"

def leer_datos(filename):
    data_dir = 'raw'
    file_path = os.path.join(root_dir, "data", data_dir, filename) #Ruta del archivo, encuentro la base que necesito
    datos = pd.read_csv(file_path, encoding='latin-1', sep=';')
    print('get_data')
    print('La tabla contiene', datos.shape[0], 'filas', datos.shape[1], 'columnas')
    return datos

def renovar_duplicados_y_nulos(datos):
    data = datos.drop_duplicates()
    data.reset_index(inplace=True, drop=True)
    col = "UNIDAD"
    data[col].fillna("SIN_DATO", inplace=True)
    data[col].value_counts(dropna=False, normalize=True)
    col = "EDAD"
    data[col].fillna("SIN_DATO", inplace=True)
    data[col].value_counts(dropna=False, normalize=True)
    data[col].replace({"SIN_DATO": np.nan}, inplace=True)
    data[col]

    return data

def convetir_str_a_num(data, col="EDAD"):
    f = lambda x: x if pd.isna(x) else int(x) 
    data[col] = data[col].apply(f)
    data.info()

    return data

def corregir_fecha(data, col = "FECHA1"):
    col = "FECHA_INICIO_DESPLAZAMIENTO_MOVIL"
    data[col] = pd.to_datetime(data[col], errors = "coerce")
    data.info()
    fecha = "1985-02-30 00:00:00"
    pd.to_datetime(fecha, errors = "coerce", format = "%Y/%m/%d")
    col = "RECEPCION"
    data[col]
    list_fechas = list()
    for fecha in data[col]:
        try:
            new_fecha = parse(fecha)
        except Exception as e:        
            new_fecha = pd.to_datetime(fecha, errors="coerce") # el error es este el print muestra pero se reemplaza con new_fecha
            list_fechas.append(new_fecha)
            list_fechas
            data["RECEPCION_Carr"] = list_fechas
            data.head()

def generate_report(data):
    dict_resumen = dict()  # Crear un diccionario vacio
    for col in data.columns:
        valores_unicos = data[col].unique()
        n_valores = len(valores_unicos)
        dict_resumen[col] = n_valores

    reporte = pd.DataFrame.from_dict(dict_resumen, orient='index') 
    reporte.rename({0: 'Count'}, axis=1, inplace=True) # axis 1 buscar en la columna, 0 en las filas

    print('generate_report')
    print(reporte.head())
    return reporte

def save_data(reporte, filename): # Guardar tabla
    out_name = 'Limpieza1_' + filename # Indicar nombre al archivo de salida
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    reporte.to_csv(out_path, sep=';')
    
def main():

    filename = "llamadas123_julio_2022.csv"
    datos = leer_datos(filename)
    save_data(datos, filename)
    print('LISTO')

if __name__ == "__main__":
    main()
