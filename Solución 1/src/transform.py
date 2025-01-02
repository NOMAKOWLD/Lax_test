import numpy as np
import pandas as pd

def transform_clientes(data_frames):
    # Extraer los DataFrames de ClientesContactados_PDV_*
    pdv_frames = [df for name, df in data_frames.items() if 'ClientesContactados_PDV' in name]
    
    # Convertir cada DataFrame a un arreglo numpy
    numpy_arrays = [df.to_numpy() for df in pdv_frames]
    
    # Concatenar todos los arreglos numpy
    combined_array = np.vstack(numpy_arrays)
    
    # Reconstruir un DataFrame desde el arreglo numpy
    combined_df = pd.DataFrame(combined_array, columns=pdv_frames[0].columns)
    
    return combined_df