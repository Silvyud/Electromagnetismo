import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. ELECCIÓN DE PARÁMETROS
# ==========================================
mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío (T*m/A)
I_mag = 10.0 # Magnitud de la corriente en Amperios
a = 1.0 # Distancia horizontal 'a' en metros
b = 1.0 # Distancia vertical 'b' en metros

# Configuración a) Tres alambres
alambres_3 = [
    {'I': -I_mag, 'x': -a, 'y': 0, 'color': '#E74C3C', 'simbolo': 'x', 'label': f'-{I_mag}A (entra)'},
    {'I': I_mag,  'x': 0,  'y': 0, 'color': '#3498DB', 'simbolo': '•', 'label': f'+{I_mag}A (sale)'},
    {'I': -I_mag, 'x': a,  'y': 0, 'color': '#E74C3C', 'simbolo': 'x', 'label': f'-{I_mag}A (entra)'}
]

# Configuración b) Cinco alambres
alambres_5 = [
    {'I': -I_mag, 'x': -a, 'y': 0,  'color': '#E74C3C', 'simbolo': 'x', 'label': f'-{I_mag}A (entra)'},
    {'I': I_mag,  'x': 0,  'y': 0,  'color': '#3498DB', 'simbolo': '•', 'label': f'+{I_mag}A (sale)'},
    {'I': -I_mag, 'x': a,  'y': 0,  'color': '#E74C3C', 'simbolo': 'x', 'label': f'-{I_mag}A (entra)'},
    {'I': I_mag,  'x': 0,  'y': b,  'color': '#3498DB', 'simbolo': '•', 'label': f'+{I_mag}A (sale)'},
    {'I': I_mag,  'x': 0,  'y': -b, 'color': '#3498DB', 'simbolo': '•', 'label': f'+{I_mag}A (sale)'}
]

# ==========================================
# 2. FUNCIÓN PARA CÁLCULO DEL CAMPO B
# ==========================================
def calcular_campo_B(X, Y, alambres):
    Bx = np.zeros(X.shape)
    By = np.zeros(Y.shape)
    
    for alambre in alambres:
        dx = X - alambre['x']
        dy = Y - alambre['y']
        r_squared = dx**2 + dy**2
        
        # Evitar división por cero en el centro exacto del alambre
        r_squared[r_squared == 0] = 1e-10
        
        # Aplicación de las fórmulas de coordenadas cartesianas
        factor = (mu_0 * alambre['I']) / (2 * np.pi * r_squared)
        Bx += factor * (-dy)
        By += factor * (dx)
        
    B_mag = np.sqrt(Bx**2 + By**2)
    return Bx, By, B_mag

# ==========================================
# 3. GENERACIÓN DE LA GRILLA
# ==========================================
limite = 2.0
x_vals = np.linspace(-limite, limite, 30)
y_vals = np.linspace(-limite, limite, 30)
X, Y = np.meshgrid(x_vals, y_vals)

# Calculamos los campos para ambas configuraciones
Bx3, By3, Bmag3 = calcular_campo_B(X, Y, alambres_3)
Bx5, By5, Bmag5 = calcular_campo_B(X, Y, alambres_5)

# Normalizamos para que quiver muestre direcciones claras
Bx3_norm = Bx3 / Bmag3
By3_norm = By3 / Bmag3
Bx5_norm = Bx5 / Bmag5
By5_norm = By5 / Bmag5

# ==========================================
# 4. GRÁFICAS Y VISUALIZACIÓN
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.canvas.manager.set_window_title('Campo magnético de alambres con corriente')

def configurar_grafico(ax, X, Y, Bx_norm, By_norm, Bmag, alambres, titulo):
    # Utilizamos el mapa de colores 'turbo' para mayor contraste
    q = ax.quiver(X, Y, Bx_norm, By_norm, np.log10(Bmag), 
                  cmap='turbo', pivot='mid', scale=25, alpha=0.9)
    
    # Dibujar alambres
    for alambre in alambres:
        # Círculo base
        ax.scatter(alambre['x'], alambre['y'], color=alambre['color'], s=350, 
                   edgecolor='black', zorder=5)
                   
        # Símbolo (x o •). Ahora ambos se alinean al 'center'.
        tamano_fuente = 16 if alambre['simbolo'] == 'x' else 22
        ax.text(alambre['x'], alambre['y'], alambre['simbolo'], color='white', 
                fontsize=tamano_fuente, ha='center', va='center', 
                fontweight='bold', zorder=6)
                
        # Etiqueta de valor
        ax.text(alambre['x'], alambre['y'] + 0.18, alambre['label'], 
                fontsize=9, ha='center', fontweight='bold', zorder=6)

    ax.set_title(titulo, fontsize=13, pad=15)
    ax.set_xlabel("Eje X (m)", fontsize=11)
    ax.set_ylabel("Eje Y (m)", fontsize=11)
    ax.set_xlim([-limite, limite])
    ax.set_ylim([-limite, limite])
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.set_aspect('equal')
    return q

q1 = configurar_grafico(ax1, X, Y, Bx3_norm, By3_norm, Bmag3, alambres_3, "a) Configuración de 3 alambres")
q2 = configurar_grafico(ax2, X, Y, Bx5_norm, By5_norm, Bmag5, alambres_5, "b) Configuración de 5 alambres")

# Barra de color compartida
cbar = fig.colorbar(q2, ax=[ax1, ax2], fraction=0.02, pad=0.04)
cbar.set_label('Magnitud del campo log10(|B|) [Teslas]')

plt.show()