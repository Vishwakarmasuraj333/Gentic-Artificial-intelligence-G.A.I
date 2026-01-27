#Aim: Kohonen Self organizing map. install(pip install minisom)
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom

colors = np.array([
    [0., 0., 0.],
    [0., 0., 1.],
    [0., 0., 0.5],
    [0.125, 0.529, 1.0],
    [0.33, 0.4, 0.67],
    [0.6, 0.5, 1.0],
    [0., 1., 0.],
    [1., 0., 0.],
    [0., 1., 1.],
    [1., 0., 1.],
    [1., 1., 0.],
    [1., 1., 1.],
    [0.33, 0.33, 0.33],
    [0.5, 0.5, 0.5],
    [0.66, 0.66, 0.66]
])

color_names = [
    'black', 'blue', 'darkblue', 'skyblue',
    'greyblue', 'lilac', 'green', 'red',
    'cyan', 'violet', 'yellow', 'white',
    'darkgrey', 'mediumgrey', 'lightgrey'
]

som = MiniSom(20, 30, 3, sigma=1.0, learning_rate=0.5)
som.random_weights_init(colors)
som.train(colors, 100)

plt.imshow(som.distance_map().T, cmap='bone', origin='lower')

for i, color in enumerate(colors):
    x, y = som.winner(color)
    plt.text(y, x, color_names[i],
             ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5, lw=0))

plt.title('Color SOM')
plt.show()
