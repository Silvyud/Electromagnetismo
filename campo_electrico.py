import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. ELECCIÓN DE PARÁMETROS
# ==========================================
k = 9e9 # Constante de Coulomb (N·m^2/C^2)
q_magnitude = 1e-6 # Magnitud de la carga: 1 microCoulomb. A contiinuación es multiplicada para el caso de cada carga.
a = 1.0 # Distancia 'a' entre las cargas en metros (cuadrado de lado 'a')

# Se define el arreglo de 4 cargas según el esquema del parcial
# q1 (+), q4 (-), q2 (-), q3 (+)
charges = [
    {'q': q_magnitude,  'x': -a/2, 'y': a/2,  'color': '#E74C3C', 'label': '+q1 (1 µC)',  'name': 'q1'},
    {'q': -q_magnitude, 'x': -a/2, 'y': -a/2, 'color': '#3498DB', 'label': '-q2 (-1 µC)', 'name': 'q2'},
    {'q': q_magnitude,  'x': a/2,  'y': -a/2, 'color': '#E74C3C', 'label': '+q3 (1 µC)',  'name': 'q3'},
    {'q': -q_magnitude, 'x': a/2,  'y': a/2,  'color': '#3498DB', 'label': '-q4 (-1 µC)', 'name': 'q4'}
]

# ==========================================
# 2. GENERACIÓN DE LA GRILLA (Malla espacial)
# ==========================================
# Rango de visualización adecuado para los ejes x e y
x_vals = np.linspace(-1.5, 1.5, 40)
y_vals = np.linspace(-1.5, 1.5, 40)
X, Y = np.meshgrid(x_vals, y_vals)

# ==========================================
# 3. CÁLCULO DEL CAMPO ELÉCTRICO
# ==========================================
Ex = np.zeros(X.shape)
Ey = np.zeros(Y.shape)

for charge in charges:
    dx = X - charge['x']
    dy = Y - charge['y']
    r_squared = dx**2 + dy**2
    
    # Evitar la división por cero exactamente sobre las cargas
    r_squared = np.maximum(r_squared, 1e-6)
    r = np.sqrt(r_squared)
    
    # E = k*q / r^2. Luego se multiplica por el vector unitario (dx/r, dy/r)
    E_mag = k * charge['q'] / r_squared
    Ex += E_mag * (dx / r)
    Ey += E_mag * (dy / r)

# Magnitud total del campo para colorear el gráfico
E_total_mag = np.sqrt(Ex**2 + Ey**2)

# Se normalizan los vectores para que quiver dibuje todas las flechas del mismo tamaño, 
# dejando que el color represente la magnitud. Se evita dividir por cero en puntos donde
# el campo neto se cancela.
E_total_mag_safe = np.where(E_total_mag > 1e-12, E_total_mag, 1e-12)
Ex_norm = np.zeros_like(Ex)
Ey_norm = np.zeros_like(Ey)
mask = E_total_mag > 1e-12
Ex_norm[mask] = Ex[mask] / E_total_mag[mask]
Ey_norm[mask] = Ey[mask] / E_total_mag[mask]

# Para el color se usa una versión segura de la magnitud
percentil_98 = np.percentile(E_total_mag, 98)
E_clip = np.clip(E_total_mag, 0, percentil_98)
color_values = np.log1p(E_clip)

# --- Puntos ejemplo resultado del campo eléctrico ---

# Campo eléctrico en el punto (0, 0)
Ex0 = 0.0
Ey0 = 0.0
for charge in charges:
    dx = 0.0 - charge['x']
    dy = 0.0 - charge['y']
    r = np.sqrt(dx**2 + dy**2)
    E_mag = k * charge['q'] / (r**2)
    Ex0 += E_mag * (dx / r)
    Ey0 += E_mag * (dy / r)
E0_mag = np.sqrt(Ex0**2 + Ey0**2)

# --- (calculos desarrollados a mano también) ---

# Campo eléctrico en el punto (0, 0.5)
Ex1 = 0.0
Ey1 = 0.0
for charge in charges:
    px = 0.0 - charge['x']
    py = 0.5 - charge['y']
    r = np.sqrt(px**2 + py**2)
    E_mag = k * charge['q'] / (r**2)
    Ex1 += E_mag * (px / r)
    Ey1 += E_mag * (py / r)
E1_mag = np.sqrt(Ex1**2 + Ey1**2)

# ==========================================
# 4. GRÁFICA Y VISUALIZACIÓN
# ==========================================
fig, ax = plt.subplots(figsize=(10, 8))
fig.canvas.manager.set_window_title('Visualización de campo eléctrico')

# Se usa quiver para el campo vectorial (pivot='mid' centra la flecha en la coordenada)
# Se aplica escala logarítmica al color para notar mejor los contrastes
graf_quiver = ax.quiver(X, Y, Ex_norm, Ey_norm, color_values,
                        cmap='Spectral_r', pivot='mid', scale=30, alpha=0.8)
cbar = fig.colorbar(graf_quiver, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Magnitud del campo eléctrico ln(|E|) [N/C]')

# Para darle buena estética, se dibujan las cargas eléctricas como circulos
for charge in charges:
    ax.scatter(charge['x'], charge['y'], color=charge['color'], s=400, 
               edgecolor='black', zorder=5, label=charge['label'])
    # Símbolo de la carga en el centro
    sign = "+" if charge['q'] > 0 else "-"
    ax.text(charge['x'], charge['y'], sign, color='white', 
            fontsize=16, ha='center', va='center', fontweight='bold', zorder=6)
    # Etiqueta corta de identificación de la carga
    dx = 0.12 if charge['x'] <= 0 else -0.12
    dy = 0.15 if charge['y'] >= 0 else -0.18
    ax.text(charge['x'] + dx, charge['y'] + dy, charge['name'], color='black',
            fontsize=10, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='black', alpha=0.8), zorder=7)

# Marcar el punto (0, 0) y mostrar el valor del vector del campo en ese punto
ax.scatter(0, 0, color='black', marker='x', s=120, zorder=8, label='Punto (0,0)')
ax.annotate(
    f"E(0,0)\nEx = {Ex0:.2e} N/C\nEy = {Ey0:.2e} N/C\n|E| = {E0_mag:.2e} N/C",
    xy=(0, 0),
    xytext=(0.18, 0.18),
    textcoords='data',
    fontsize=9,
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.9),
    arrowprops=dict(arrowstyle='->', color='gray'),
    zorder=9
)
# Marcar el punto (0, 0.5) y mostrar el valor del vector del campo en ese punto
ax.scatter(0, 0.5, color='black', marker='x', s=120, zorder=8)
ax.annotate(
    f"E(0, 0.5)\nEx = {Ex1:.2e} N/C\nEy = {Ey1:.2e} N/C\n|E| = {E1_mag:.2e} N/C",
    xy=(0, 0.5),
    xytext=(0.18, 0.75),
    textcoords='data',
    fontsize=9,
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.9),
    arrowprops=dict(arrowstyle='->', color='gray'),
    zorder=9
)

ax.set_title("Campo eléctrico vectorial de un arreglo de 4 cargas (cuadrupolo)", fontsize=14, pad=15)
ax.set_xlabel("Distancia en x (m)", fontsize=12)
ax.set_ylabel("Distancia en y (m)", fontsize=12)
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.axhline(0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax.axvline(0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', bbox_to_anchor=(1.15, 0.95), borderaxespad=0.5)

# ==========================================
# 5. INTERACTIVIDAD (Hover)
# ==========================================
# Caja de texto oculta que se mostrará al pasar el cursor
annot = ax.annotate("", xy=(0,0), xytext=(15, 15), textcoords="offset points",
                    bbox=dict(boxstyle="round,pad=0.4", fc="#FAFAFA", ec="gray", alpha=0.9),
                    arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
annot.set_visible(False)

def hover(event):
    if event.inaxes == ax:
        # Encontrar el punto de la grilla más cercano a la posición del cursor
        dist = np.sqrt((X - event.xdata)**2 + (Y - event.ydata)**2)
        idx = np.unravel_index(np.argmin(dist, axis=None), dist.shape)
        
        # Recuperar valores en ese índice
        ex_val = Ex[idx]
        ey_val = Ey[idx]
        mag_val = E_total_mag[idx]
        
        # Actualizar la anotación
        annot.xy = (X[idx], Y[idx])
        text = f"Vector E\nEx: {ex_val:.2e} N/C\nEy: {ey_val:.2e} N/C\nMagnitud: {mag_val:.2e} N/C"
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw_idle()
    else:
        if annot.get_visible():
            annot.set_visible(False)
            fig.canvas.draw_idle()

# Conectar el evento de movimiento del ratón con la función
fig.canvas.mpl_connect("motion_notify_event", hover)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.show()