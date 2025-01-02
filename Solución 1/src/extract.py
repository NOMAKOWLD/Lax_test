import pandas as pd
import os

def extract_data(folder_path):
    data_frames = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            try:
                data = pd.read_excel(file_path)
                data_frames[file_name] = data
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
    return data_frames



