import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from src.extract import extract_data
from src.transform import transform_clientes
from src.load import load_data_to_sql

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuraciones
RAW_DATA_PATH = "data/raw"
PROCESSED_TABLE_CLIENTES = "clientes_contactados"
TABLES_WITHOUT_TRANSFORMATION = ["Campañas", "Movimientos", "Referencias"]

# Leer las credenciales desde el archivo .env
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "3306")  # Valor predeterminado si no está en el .env
DB_NAME = os.getenv("DB_NAME")

# Construir la cadena de conexión
CONNECTION_STRING = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def main():
    # Crear el motor de conexión a la base de datos
    engine = create_engine(CONNECTION_STRING)
    
    # Extracción
    raw_data = extract_data(RAW_DATA_PATH)
    
    # Procesar clientes contactados (requieren transformación)
    clientes_data = transform_clientes(raw_data)
    load_data_to_sql(clientes_data, PROCESSED_TABLE_CLIENTES, engine)

    # Procesar y cargar tablas sin transformación
    for table_name in TABLES_WITHOUT_TRANSFORMATION:
        if f"{table_name}.xlsx" in raw_data:  # Verificar si el archivo existe
            table_data = raw_data[f"{table_name}.xlsx"]
            load_data_to_sql(table_data, table_name.lower(), engine)
            print(f"Tabla '{table_name}' cargada exitosamente.")

if __name__ == "__main__":
    main()
