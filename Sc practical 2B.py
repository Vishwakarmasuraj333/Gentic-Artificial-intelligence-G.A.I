# Generate XOR function using McCulloch-Pitts neural net

import math
import random

INPUT_NODES = 2
HIDDEN_NODES = 2
OUTPUT_NODES = 1
LEARNING_RATE = 0.2
MAX_ITERATIONS = 10000


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


class Network:
    def __init__(self):
        self.w_ih = [[random.random(), random.random()],
                     [random.random(), random.random()]]
        self.w_ho = [random.random(), random.random()]
        self.b_h = [random.random(), random.random()]
        self.b_o = random.random()

    def forward(self, x):
        self.h = []
        for i in range(HIDDEN_NODES):
            net = x[0] * self.w_ih[0][i] + x[1] * self.w_ih[1][i] - self.b_h[i]
            self.h.append(sigmoid(net))

        net_o = self.h[0] * self.w_ho[0] + self.h[1] * self.w_ho[1] - self.b_o
        self.o = sigmoid(net_o)
        return self.o

    def train(self, x, target):
        output = self.forward(x)
        error = target - output

        delta_o = output * (1 - output) * error

        for i in range(HIDDEN_NODES):
            self.w_ho[i] += LEARNING_RATE * delta_o * self.h[i]

        self.b_o -= LEARNING_RATE * delta_o

        for i in range(HIDDEN_NODES):
            delta_h = self.h[i] * (1 - self.h[i]) * delta_o * self.w_ho[i]
            self.w_ih[0][i] += LEARNING_RATE * delta_h * x[0]
            self.w_ih[1][i] += LEARNING_RATE * delta_h * x[1]
            self.b_h[i] -= LEARNING_RATE * delta_h


net = Network()

training_data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

for _ in range(MAX_ITERATIONS):
    x, y = random.choice(training_data)
    net.train(x, y)

print("XOR Outputs:")
for x, y in training_data:
    print(x, "->", round(net.forward(x), 3))
