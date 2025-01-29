import os
import time

def add_execute_permission():
    # Obtener todos los archivos en el directorio actual
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # Filtrar archivos con la extensión .py
    py_files = [f for f in files if f.endswith('.py')]
    
    for file in py_files:
        # Cambiar permisos para agregar ejecución al usuario
        os.chmod(file, os.stat(file).st_mode | 0o100)

while True:
    add_execute_permission()
    print("Permisos de ejecución agregados a los archivos .py.")
    # Esperar 1 minuto antes de volver a ejecutar
    time.sleep(60)
