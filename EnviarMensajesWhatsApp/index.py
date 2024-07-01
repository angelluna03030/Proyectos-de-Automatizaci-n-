import pywhatkit

# Definir contactos
contacto1 = "+57 3213754980"

# Enviar mensaje de WhatsApp usando pywhatkit.sendwhatmsg
# Parámetros:
# 1. Número de teléfono con el código del país (str)
# 2. Mensaje a enviar (str)
# 3. Hora en formato 24 horas (int) - horas
# 4. Minuto (int)
# 5. Tiempo de espera antes de enviar el mensaje (int, opcional, predeterminado=20 segundos)
# 6. Cerrar la pestaña del navegador después de enviar el mensaje (bool, opcional, predeterminado=False)
# 7. Espera adicional después de enviar el mensaje en segundos (int, opcional, predeterminado=3 segundos)

# Ejemplo de uso de pywhatkit.sendwhatmsg con parámetros detallados

#recomendacion se se envia los mensaje por si solo pero hay que dejar tiempo para que lo hago esto es un
# tiempo recomendado en el tiempo de espera 10 segundos y el tiempo de ciere 15 segundos esta bien 
pywhatkit.sendwhatmsg(contacto1, "Test", 0, 59, 10, True, 15)

# Nota:
# - En este ejemplo, el mensaje "Test" se enviará al número +57 3213754980 a las 00:54 horas.
# - La función esperará 2 segundos antes de enviar el mensaje.
# - La pestaña del navegador se cerrará automáticamente después de enviar el mensaje.
# - Habrá una espera adicional de 2 segundos después de enviar el mensaje.
grupo1 = ""



pywhatkit.sendwhatmsg_to_group(grupo1, "Test", 0, 59, 10, True, 15)
