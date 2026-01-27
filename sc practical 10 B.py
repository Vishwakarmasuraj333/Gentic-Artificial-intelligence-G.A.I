#Aim: Create two classes: City and Fitness using Genetic algorithm.
import numpy as np
import random

class City:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other_city: 'City') -> float:
        return np.sqrt((self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2)

    def __repr__(self):
        return f"City(x={self.x}, y={self.y})"

class Fitness:
    def __init__(self, route: list):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def calculate_distance(self) -> float:
        if self.distance == 0:
            total_distance = 0
            for i in range(len(self.route)):
                from_city = self.route[i]
                to_city = self.route[(i + 1) % len(self.route)]
                total_distance += from_city.distance_to(to_city)
            self.distance = total_distance
        return self.distance

    def calculate_fitness(self) -> float:
        if self.fitness == 0:
            self.fitness = 1 / float(self.calculate_distance())
        return self.fitness

    def __repr__(self):
        return f"Fitness(distance={self.distance}, fitness={self.fitness})"

if __name__ == "__main__":
    city1 = City(0, 0)
    city2 = City(3, 4)
    city3 = City(6, 0)

    route = [city1, city2, city3]
    fitness = Fitness(route)

    print("Route:", route)
    print("Total Distance:", fitness.calculate_distance())
    print("Fitness Score:", fitness.calculate_fitness())
