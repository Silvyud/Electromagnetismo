# Campo Eléctrico - Proyecto de Visualización

Este proyecto calcula y visualiza el campo eléctrico de un arreglo de 4 cargas eléctricas en Python usando `numpy` y `matplotlib`.

## Archivos

- `campo_electrico.py` - Script principal que genera la grilla, calcula el campo eléctrico y muestra la visualización interactiva.
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

Desde la carpeta del proyecto:

```powershell
python campo_electrico.py
```

## Qué hace el script

1. Define cuatro cargas con posiciones y signos distintos.
2. Genera una malla 2D de puntos en el plano XY.
3. Calcula el vector del campo eléctrico en cada punto.
4. Dibuja el campo con `quiver` y colorea según la magnitud.
5. Muestra las cargas con símbolos y etiquetas.
6. Agrega interactividad para ver el valor del campo cuando mueves el cursor.