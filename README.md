# SoundLayers Pi

SoundLayers Pi es un proyecto de Raspberry Pi que utiliza un sensor capacitivo para detectar toques y superponer capas de sonido de forma dinámica. Este proyecto permite la creación de composiciones musicales en tiempo real, donde cada toque activa o desactiva pistas de audio con transiciones suaves para una experiencia auditiva fluida.

## Características

- Detección de toques usando un sensor capacitivo I2C (MPR121).
- Reproducción de hasta 5 pistas de audio diferentes.
- Superposición de capas de sonido con transiciones suaves (fade-in y fade-out).
- Control dinámico para añadir y eliminar capas de sonido.

## Requisitos

- Raspberry Pi con Raspbian instalado.
- Sensor capacitivo MPR121.
- Altavoces o auriculares conectados a la Raspberry Pi.
- Python 3.
- Biblioteca `adafruit-circuitpython-mpr121`.
- Biblioteca `pygame`.

## Instalación

1. Clona este repositorio en tu Raspberry Pi:

    ```bash
    git clone https://github.com/tu-usuario/soundlayers-pi.git
    cd soundlayers-pi
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install adafruit-circuitpython-mpr121 pygame
    ```

3. Asegúrate de que los archivos de audio (`base.mp3`, `armonía.mp3`, `ritmo.mp3`, `arreglos.mp3`, `voces.mp3`) estén en el mismo directorio que el script de Python.

## Uso

1. Conecta el sensor capacitivo MPR121 a la Raspberry Pi usando los pines I2C (SCL y SDA).

2. Ejecuta el script de Python:

    ```bash
    python soundlayers_pi.py
    ```

3. Toca la malla conectada al sensor MPR121 para añadir o eliminar capas de sonido. El primer toque reproducirá `base.mp3`, el segundo toque superpondrá `armonía.mp3`, y así sucesivamente hasta alcanzar un máximo de 5 capas de sonido. Tocando nuevamente se eliminarán las capas en orden inverso.
