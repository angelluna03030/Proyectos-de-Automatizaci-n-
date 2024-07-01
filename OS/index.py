import os
from pathlib import Path, PurePath

#1.para seber en la nombre de la ruta en donde me encuetro
ruta =os.getcwd()
#nos devuelve una cade de String
print(ruta)
#nos devuelve un Path
print(Path.cwd())


#2. para seber lo archivos y carpetas que tenemos
print(os.listdir())
#como saber el contenido de un carpeta especial
print(os.listdir('nombrecarpeta'))
print(list(Path('nombrecarpeta').iterdir()))


#3.unir dos rutas

print(os.path.join(os.getcwd(), 'nombrecarpeta'))
print(PurePath.joinpath(Path.cwd(), "nombrecarpeta"))


#4.crear carpetas
os.mkdir('nombrecarpeta')
Path.mkdir('nombrecarpeta2')
Path('nombrecarpeta3').mkdir()
#si ya exite para no rompa el codigo
Path('nombrecarpeta3').mkdir(exist_ok=True)

#5. agregar carpetas dentro de carpetas 

os.makedirs(os.path.join('nombrecarpeta2', 'nombrecarpeta'))
PurePath.joinpath(Path.cwd(), "nombrecarpeta", "nombrecarpeta2").mkdir()
#si no sean creado las carpetas con esto las crea 
PurePath.joinpath(Path.cwd(), "nombrecarpeta", "nombrecarpeta2").mkdir(parents=True)


#6. renombre Archivos
os.rename('nombrecarpeta' ,'nombrecarpeta1')
path_actual= Path('nombrecarpeta1')
path_objetivo =Path('nombrecarpeta')
Path.rename(path_actual, path_objetivo)
#6.2 renombrar varios archivos
for file in os.listdir():
    if file.endswith('.pdf'):
        os.rename(file, f'2024_{file}')


#7. si existes el archivo 
print(os.path.exists('nombrecarpeta'))
archivo = Path('2024_2021_index2.pdf')
print(archivo.exists())


#8. saber los metadatos 
print(os.path.abspath('2024_2021_index.pdf'))
script = Path('2024_2021_index2.pdf')
print(script.resolve())
print(script.stem)
print(script.suffix)
print(script.stat().st_size)
