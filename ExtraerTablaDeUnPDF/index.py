import pandas as pd
import camelot

# Lee las tablas del PDF
tables = camelot.read_pdf("Remates.pdf", pages='2')


# Muestra las tablas encontradas
print(tables)

# Exporta la primera tabla a un archivo CSV
tables[0].to_csv('tabla.csv')
