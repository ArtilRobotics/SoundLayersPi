# SoundLayers Pi

SoundLayers Pi es un proyecto de Raspberry Pi que utiliza un sensor de vibracion para detectar toques y superponer capas de sonido de forma dinámica. Este proyecto permite la creación de composiciones musicales en tiempo real, donde cada toque activa o desactiva pistas de audio con transiciones suaves para una experiencia auditiva fluida.

## Características

- Detección de toques usando un sensor de vibracion 801s.
- Reproducción de múltiples pistas de audio diferentes.
- Superposición de capas de sonido con transiciones suaves (fade-in y fade-out).
- Control dinámico para añadir y eliminar capas de sonido.

## Requisitos

- Raspberry Pi con Raspbian instalado.
- Sensor vibracion 801s.
- Altavoces o auriculares conectados a la Raspberry Pi.
- Python 3.
- Biblioteca `pygame`.

## Instalación

1. Clona este repositorio en tu Raspberry Pi:

    ```bash
    git clone https://github.com/tu-usuario/soundlayers-pi.git
    cd soundlayers-pi
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Asegúrate de que los archivos de audio estén en las carpetas correctas y sean accesibles por el script.

## Uso

1. Conecta el Sensor vibracion a la Raspberry Pi usando uno de los GPIO 4.

2. Configura la carpeta de pistas de audio que deseas usar editando la variable `folder` en el script `soundlayers_pi.py`.

3. Ejecuta el script de Python:

    ```bash
    python soundlayers_pi.py
    ```

4. Toca Sensor vibracion o presiona la barra espaciadora en tu teclado para añadir o eliminar capas de sonido. El primer toque reproducirá la primera pista, el segundo toque superpondrá la segunda pista, y así sucesivamente hasta alcanzar el máximo número de capas. Tocando nuevamente se eliminarán las capas en orden inverso.

## Contribuciones
¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia Pública General de GNU, versión 3.

## Propiedad de las Pistas de Audio
Todas las pistas de audio en las carpeta Tracks son propiedad del Centro Cultural Nuna Humanista Ecuador y pueden tener otra licencia.