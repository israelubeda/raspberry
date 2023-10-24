import RPi.GPIO as GPIO
import time

# Configura los pines
PIN_DO = 17  # Asume que la salida digital está conectada al pin GPIO 17

# Configura la biblioteca GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_DO, GPIO.IN)

try:
    while True:
        # Lee la salida digital
        digital_value = GPIO.input(PIN_DO)
        print(f'Valor Digital: {"Alto" if digital_value else "Bajo"}')
        time.sleep(1)

except KeyboardInterrupt:
    pass  # Se detiene el bucle cuando se presiona Ctrl+C

# Limpia los pines GPIO antes de salir
GPIO.cleanup()
