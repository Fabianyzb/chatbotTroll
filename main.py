import time
import pyautogui as auto
import pywhatkit as kit

# Espera 3 segundos
time.sleep(3)

# Abre el archivo text.txt en modo de lectura
with open('text.txt', 'r') as theFile:
    auto.FAILSAFE = False
    for line in theFile:
        # Escribe cada línea en el teclado
        auto.typewrite(line)
        auto.press('enter')

# Envía un mensaje en WhatsApp a las 22:28
try:
    kit.sendmsg("+56956089820", "Hola desde Python", 16, 36)
    print("Envío exitoso")
except:
    print("Ha ocurrido un error")
