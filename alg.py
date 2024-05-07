import math
import random


def get_data():
    with open('tsp.txt', 'r') as f:
        n = int(f.readline())
        points = []
        for i in range(n):
            line = f.readline().split()
            point = [int(line[1]), int(line[2])]
            points.append(point)

    matrix = [[-1] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                matrix[i][j] = distance

    return matrix


def calculate_distance(path, matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += matrix[path[i]][path[i + 1]]
    distance += matrix[path[-1]][path[0]]
    return distance


def get_neighborhood(path, tabu_list, matrix):
    neighbors = []
    for i in range(1, len(path) - 1):
        for j in range(i + 1, len(path)):
            neighbor = path.copy()
            neighbor[i:j] = reversed(neighbor[i:j])
            if neighbor not in tabu_list:
                neighbors.append((neighbor, calculate_distance(neighbor, matrix)))
    return neighbors


def tabu_search(matrix, tabu_size, max_iterations):
    n = len(matrix)
    best_path = list(range(n))
    random.shuffle(best_path)

    best_distance = calculate_distance(best_path, matrix)
    tabu_list = []
    for i in range(max_iterations):
        neighborhood = get_neighborhood(best_path, tabu_list, matrix)
        if not neighborhood:
            break
        neighborhood.sort(key=lambda x: x[1])
        next_path = neighborhood[0][0]
        next_distance = neighborhood[0][1]
        tabu_list.append(next_path)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        if next_distance < best_distance:
            best_path = next_path
            best_distance = next_distance

    return best_distance


matrix = get_data()
tabu_size = len(matrix) * 0.15
max_iterations = len(matrix) + 50

result = tabu_search(matrix, tabu_size, max_iterations)
print(f"Długość trasy: {result}")
