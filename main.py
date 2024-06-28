#! /usr/bin/env python
import os
import time
import pygame
import pygame.mixer
import RPi.GPIO as GPIO
from threading import Timer

# Configuración del GPIO
vibration_pin = 4  # Cambia este pin según tu configuración
GPIO.setmode(GPIO.BCM)
GPIO.setup(vibration_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Inicializamos Pygame y el mezclador de audio
pygame.mixer.init()

# Función para cargar los archivos de audio de una carpeta específica
def load_tracks(folder):
    tracks = []
    for file_name in sorted(os.listdir(folder)):
        if file_name.endswith('.mp3') or file_name.endswith('.wav'):
            tracks.append(pygame.mixer.Sound(os.path.join(folder, file_name)))
    return tracks

# Selecciona la carpeta de tracks a usar
# Aquí puedes cambiar la carpeta según el grupo que quieras probar
folder1 = "/home/nuna/SoundLayersPi/Tracks/chamiza grupos"
folder2 = "/home/nuna/SoundLayersPi/Tracks/GRUPO AGUA"
folder3 = "/home/nuna/SoundLayersPi/Tracks/GRUPO FESTEJO"
folder4 = "/home/nuna/SoundLayersPi/Tracks/GRUPO INTRO"
folder5 = "/home/nuna/SoundLayersPi/Tracks/GRUPO MONTAÑA"
folder6 = "/home/nuna/SoundLayersPi/Tracks/GRUPO PELILEO"
folder7 = "/home/nuna/SoundLayersPi/Tracks/GRUPO RITUAL"

# Cargamos los archivos de audio de la carpeta seleccionada
tracks = load_tracks(folder7)

# Variables para el control de las capas de sonido
current_layers = 0
max_layers = len(tracks)  # Ajusta el número máximo de capas según los archivos cargados
adding_layers = True

# Duración del fade-in y fade-out en milisegundos
fade_duration = 1000

auto_stop_timer=None
auto_stop_delay=60

def play_next_layer():
    global current_layers
    if current_layers < max_layers:
        tracks[current_layers].play(loops=-1, fade_ms=fade_duration)  # Reproduce en bucle con fade-in
        current_layers += 1
        print(f"Reproduciendo capa {current_layers}")

def stop_last_layer():
    global current_layers
    if current_layers > 0:
        current_layers -= 1
        tracks[current_layers].fadeout(fade_duration)  # Fade-out del sonido
        print(f"Eliminando capa {current_layers + 1}")

def process_input():
    global adding_layers, auto_stop_timer
    if adding_layers:
        play_next_layer()
        if current_layers == max_layers:
            adding_layers = False
    else:
        stop_last_layer()
        if current_layers == 0:
            adding_layers = True
            
    if auto_stop_timer is not None:
        auto_stop_timer.cancel()
    auto_stop_timer= Timer(auto_stop_delay,auto_stop_layers)
    auto_stop_timer.start()
    
def auto_stop_layers():
    global current_layers, auto_stop_timer
    if current_layers>0:
        stop_last_layer()
        auto_stop_timer=Timer(fade_duration/1000,auto_stop_layers)
        auto_stop_timer.start()


# Bucle principal
try:
    running = True
    while running:

        # Lectura desde el sensor de vibración
        if GPIO.input(vibration_pin) == GPIO.HIGH:
            print("Sensor de vibración activado!")
            process_input()
            time.sleep(1)  # Pequeña espera para evitar múltiples detecciones rápidas

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa terminado.")
finally:
    pygame.mixer.quit()
    GPIO.cleanup()
