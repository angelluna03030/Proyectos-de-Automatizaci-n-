import calendar
from pathlib import Path

# Lista de los nombres de los meses del año en español
meses_ano = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Lista de días específicos del mes
dias_mes = ["Día 1", "Día 10", "Día 20", "Día 30"]

# Crear una estructura de carpetas para cada combinación de mes y día
for i, mes in enumerate(meses_ano):
    for dia in dias_mes:
        # Crear la ruta de la carpeta para el año 2024, con subcarpetas para cada mes y día específico
        Path(f'2024/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)
