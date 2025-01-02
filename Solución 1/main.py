from src.extract import extract_data
from src.transform import transform_clientes
from src.load import load_data_to_sql

# Configuraciones
RAW_DATA_PATH = "data/raw"
PROCESSED_TABLE_CLIENTES = "clientes_contactados"
CONNECTION_STRING = "sqlite:///data/processed/Lax_test.db"
TABLES_WITHOUT_TRANSFORMATION = ["Campañas", "Movimientos", "Referencias"]

def main():
    # Extracción
    raw_data = extract_data(RAW_DATA_PATH)
    
    # Procesar clientes contactados (requieren transformación)
    clientes_data = transform_clientes(raw_data)
    load_data_to_sql(clientes_data, PROCESSED_TABLE_CLIENTES, CONNECTION_STRING)

    # Procesar y cargar tablas sin transformación
    for table_name in TABLES_WITHOUT_TRANSFORMATION:
        if f"{table_name}.xlsx" in raw_data:  # Verificar si el archivo existe
            table_data = raw_data[f"{table_name}.xlsx"]
            load_data_to_sql(table_data, table_name.lower(), CONNECTION_STRING)
            print(f"Tabla '{table_name}' cargada exitosamente.")

if __name__ == "__main__":
    main()
