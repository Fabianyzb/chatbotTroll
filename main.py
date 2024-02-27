import time
import pyautogui as auto
import pywhatkit as kit
import keyboard  # Importa el módulo keyboard

# Función para verificar si se presionó la tecla de interrupción (en este caso, la tecla 'q')
def check_interrupt():
    if keyboard.is_pressed('q'):  # Verifica si se ha presionado la tecla 'q'
        return True
    return False

# Espera 3 segundos antes de iniciar
time.sleep(3)

# Abre el archivo text.txt en modo de lectura
with open('text.txt', 'r') as theFile:
    auto.FAILSAFE = False
    for line in theFile:
        # Verifica si se presionó la tecla de interrupción
        if check_interrupt():
            print("Proceso interrumpido por el usuario.")
            break  # Sale del bucle si se presiona la tecla 'q'
        
        # Escribe cada línea en el teclado
        auto.typewrite(line)
        auto.press('enter')

# Envía el mensaje
try:
    kit.sendmsg()
    print("Envío exitoso")
except:
    print("Ha ocurrido un error")
