import pyshorteners

link = input("Introduce un enlace:")

shortener = pyshorteners.Shortener().tinyurl
short_link = shortener.short(link)


print("\t Enlace Nuevo: " , short_link)