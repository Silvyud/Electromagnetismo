# Campo Eléctrico - Proyecto de Visualización

Este proyecto calcula y visualiza el campo eléctrico de un arreglo de 4 cargas eléctricas en Python usando `numpy` y `matplotlib`.

## Archivos

- `campo_electrico.py` - Script principal que genera la grilla, calcula el campo eléctrico y muestra la visualización interactiva.
- `potencial_electrico.py` - Script que calcula y grafica el potencial eléctrico de un arreglo de 4 cargas eléctricas.
- `README.md` - Documentación del proyecto.
- `.gitignore` - Ignora archivos generados y entornos virtuales.

## Requisitos

- Python 3.8+ (recomendado)
- `numpy`
- `matplotlib`

Instala dependencias con:

```powershell
pip install numpy matplotlib
```

## Cómo ejecutar

Desde la carpeta del proyecto, ejecuta el script que quieres usar:

```powershell
python campo_electrico.py
python potencial_electrico.py
```

Si deseas ejecutar solo uno de ellos, usa el comando correspondiente:

```powershell
python campo_electrico.py
```

```powershell
python potencial_electrico.py
```

## Qué hace cada script

- `campo_electrico.py`
  1. Define cuatro cargas con posiciones y signos distintos.
  2. Genera una malla 2D de puntos en el plano XY.
  3. Calcula el vector del campo eléctrico en cada punto.
  4. Dibuja el campo con `quiver` y colorea según la magnitud.
  5. Muestra las cargas con símbolos y etiquetas.
  6. Agrega interactividad para ver el valor del campo cuando mueves el cursor.

- `potencial_electrico.py`
  1. Define cuatro cargas en las esquinas de un cuadrado.
  2. Genera una malla 2D de puntos en el plano XY.
  3. Calcula el potencial eléctrico en cada punto sumando las contribuciones de todas las cargas.
  4. Grafica curvas de nivel del potencial y coloca las cargas en el plano.