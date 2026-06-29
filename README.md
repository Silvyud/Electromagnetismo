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

## Correcciones realizadas

- Se corrigió el uso de `annot.xy` para que use las coordenadas reales del punto más cercano en la grilla.
- Se ajustó la leyenda para que no se superponga al gráfico principal.
- Se agregaron etiquetas identificadoras junto a cada carga para que sea más fácil distinguir `q1`, `q2`, `q3` y `q4`.

## Buenas prácticas para corregir el proyecto

1. Revisa el bloque donde se dibujan las cargas y asegúrate de que cada carga tenga un identificador claro.
2. Verifica la posición de la leyenda con `ax.legend(...)` y ajusta `bbox_to_anchor` si se solapa.
3. Comprueba la interacción del hover con `annot.xy` y `textcoords="offset points"`.
4. Si añades más datos o cargas, mantén un espacio suficiente entre las etiquetas y los puntos para mejorar la legibilidad.

## Cómo crear el repositorio en GitHub

1. Crea un repositorio nuevo en GitHub desde tu cuenta.
2. Copia la URL del repositorio.
3. En tu carpeta local del proyecto, ejecuta:

```powershell
git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git
git branch -M main
git push -u origin main
```

Reemplaza `TU_USUARIO` y `NOMBRE_REPO` por tus datos reales.
