"""Manejo seguro de archivos JSON para persistencia"""

import json
import os
from pathlib import Path


def load_data(filepath):
    """
    Carga datos desde archivo JSON de forma segura.
    Retorna lista vacía si no existe o está dañado.
    """
    try:
        if not os.path.exists(filepath):
            print(f" Archivo {filepath} no existe. Creando nuevo...")
            return []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                print(f" Datos cargados: {len(data)} cliente(s)")
                return data
            else:
                print("  Archivo tiene formato incorrecto. Iniciando vacío.")
                return []
    
    except json.JSONDecodeError:
        print(" Error: Archivo JSON corrupto. Iniciando con datos vacíos.")
        return []
    except Exception as e:
        print(f" Error al cargar datos: {e}")
        return []


def save_data(filepath, data):
    """
    Guarda datos en archivo JSON de forma segura.
    Crea directorio si no existe.
    """
    try:
        # Crear directorio si no existe
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Guardar con indentación para legibilidad
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Datos guardados: {len(data)} cliente(s)")
        return True
    
    except Exception as e:
        print(f" Error al guardar datos: {e}")
        return False


def ensure_data_dir(dirpath):
    """Asegura que el directorio de datos existe"""
    if not os.path.exists(dirpath):
        Path(dirpath).mkdir(parents=True, exist_ok=True)
