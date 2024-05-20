import numpy as np  # Importa a biblioteca numpy
import math  # Importa o módulo math para funções matemáticas
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib.pyplot para visualizações
from mpl_toolkits.mplot3d import Axes3D  # Importa a classe Axes3D para gráficos 3D

def euler_to_quaternion(roll, pitch, yaw):
    # Função para converter ângulos de Euler em quaternions
    # Escreve toda a lógica para a transformação de euler para quaternions, isso faz parte da avaliação



    #Para converter angulos de euler em quaternions usamos as seguintes formulas
    #qx = s1c2c3 - c1s2s3
    #qy = c1s2c3 + s1c2c3
    #qz = c1c2s3 - s1s2c3
    #qw = c1c2c3 + s1s2s3
    #onde ci = cos(angulo/2) e si = sen(angulo/2)

    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)



    

    return qw, qx, qy, qz  # Retorna os componentes do quaternion

def plot_axes(ax, color, label):
    # Função para plotar os eixos de coordenadas em um gráfico 3D
    ax.quiver(0, 0, 0, 1, 0, 0, color=color, label=label)  # Eixo x
    ax.quiver(0, 0, 0, 0, 1, 0, color=color)  # Eixo y
    ax.quiver(0, 0, 0, 0, 0, 1, color=color)  # Eixo z

# Define os ângulos de Euler em graus
roll = 45  
pitch = 30  
yaw = 60  

# Converte os ângulos de Euler de graus para radianos
roll_rad = math.radians(roll)
pitch_rad = math.radians(pitch)
yaw_rad = math.radians(yaw)

# Converte de Euler para Quaternion
qw, qx, qy, qz = euler_to_quaternion(roll_rad, pitch_rad, yaw_rad)

print("Quaternions resultantes:")
print("qw:", qw)
print("qx:", qx)
print("qy:", qy)
print("qz:", qz)

# Cria uma nova figura com dois subplots 3D
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Plota os eixos de coordenadas nos subplots
plot_axes(ax1, 'r', 'Euler Angles Frame')
plot_axes(ax2, 'b', 'Quaternion Frame')

# Define os limites dos eixos para ambos os subplots
ax1.set_xlim([-1, 1])
ax1.set_ylim([-1, 1])
ax1.set_zlim([-1, 1])

ax2.set_xlim([-1, 1])
ax2.set_ylim([-1, 1])
ax2.set_zlim([-1, 1])

# Exibe o gráfico
plt.show()
