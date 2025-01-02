from sqlalchemy import create_engine


def load_data_to_sql(data, table_name, connection_string):
    engine = create_engine(connection_string)
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded to {table_name}")
