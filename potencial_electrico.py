import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PASO 1: ELECCIÓN DE PARÁMETROS
# ==========================================
k = 9e9 # Constante de Coulomb (N*m^2/C^2) 
q_magnitude = 5e-6 # Magnitud de la carga: 5 microCoulombs (5e-6 C)
a = 1.5 # Lado del cuadrado en metros

# Arreglo de cargas con sus posiciones y propiedades visuales
# Posiciones en x, y correspondientes a las esquinas de un cuadrado de lado 'a'
# Formato: {'q': carga, 'x': posicion_x, 'y': posision_y, 'color': color_esfera, 'label': etiqueta}
cargas = [
    {'q': q_magnitude,  'x': -a/2, 'y': a/2,  'color': '#E74C3C', 'label': '+5 µC'}, # q1
    {'q': -q_magnitude, 'x': -a/2, 'y': -a/2, 'color': '#3498DB', 'label': '-5 µC'}, # q2
    {'q': q_magnitude,  'x': a/2,  'y': -a/2, 'color': '#E74C3C', 'label': '+5 µC'}, # q3
    {'q': -q_magnitude, 'x': a/2,  'y': a/2,  'color': '#3498DB', 'label': '-5 µC'}  # q4
]

# ==========================================
# PASO 2 y 3: GRILLA Y CÁLCULO DEL POTENCIAL
# ==========================================
# Creamos una malla (grilla) de puntos en el plano x,y. 
# Ajustamos el límite a 2.0 para darle respiro visual a las cargas separadas por 1.5m
limit = 2.0
x = np.linspace(-limit, limit, 300)
y = np.linspace(-limit, limit, 300)
X, Y = np.meshgrid(x, y)

# Inicializamos el potencial total en cero
V_total = np.zeros(X.shape)

# Sumamos escalarmente la contribución de cada carga
for carga in cargas:
    # Distancia euclidiana r = sqrt(dx^2 + dy^2)
    R = np.sqrt((X - carga['x'])**2 + (Y - carga['y'])**2)
    # Evitamos la división por cero asignando un valor mínimo a R en las singularidades
    R[R == 0] = 1e-10
    
    # Cálculo del potencial V = k*q / r
    V_total += k * carga['q'] / R

# Limitamos los valores extremos para que la gráfica de contorno no se sature.
V_limite = 150000 
V_total = np.clip(V_total, -V_limite, V_limite)

# ==========================================
# PASO 4: GENERACIÓN DE LA GRÁFICA DE CONTORNO
# ==========================================
fig, ax = plt.subplots(figsize=(10, 8))

# Generamos curvas de nivel rellenas (contourf) con un mapa de color divergente
niveles = np.linspace(-V_limite, V_limite, 60)
contorno_relleno = ax.contourf(X, Y, V_total, levels=niveles, cmap='RdBu_r', alpha=0.85)

# Agregamos las líneas de contorno sólidas superpuestas (contour)
lineas_contorno = ax.contour(X, Y, V_total, levels=20, colors='black', linewidths=0.5, alpha=0.6)

# Barra de color para indicar la magnitud del potencial
cbar = fig.colorbar(contorno_relleno, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Potencial eléctrico $V$ (voltios)', fontsize=12)

# Dibujamos las cargas como esferas y añadimos su valor
for i, carga in enumerate(cargas, start=1):
    # Dibuja la carga como un círculo grande
    ax.scatter(carga['x'], carga['y'], color=carga['color'], s=900, 
               edgecolor='black', linewidth=2, zorder=5)
    
    # Etiqueta con el nombre de la carga (q1, q2...)
    ax.text(carga['x'], carga['y'] + 0.20, f"q{i}", fontsize=12, 
            ha='center', va='center', fontweight='bold', zorder=6)
            
    # Etiqueta con el valor interno (ej. +5 µC)
    ax.text(carga['x'], carga['y'], carga['label'], color='white', 
            fontsize=10, ha='center', va='center', fontweight='bold', zorder=6)

# Configuraciones finales de la gráfica
ax.set_title("Curvas de nivel del potencial eléctrico (distribución de 4 cargas)", fontsize=14, pad=15)
ax.set_xlabel("Eje X (metros)", fontsize=12)
ax.set_ylabel("Eje Y (metros)", fontsize=12)
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])

# Ejes centrales de referencia
ax.axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
ax.set_aspect('equal') # Mantiene la proporción geométrica
ax.grid(False)

plt.tight_layout()
plt.show()