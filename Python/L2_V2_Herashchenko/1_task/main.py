import numpy as np

points = np.random.uniform(0, 20, (10, 2))

def manhattan_distance_matrix(points):
    num_points = points.shape[0]
    distance_matrix = np.zeros((num_points, num_points))
    
    for i in range(num_points):
        for j in range(num_points):
            distance_matrix[i, j] = np.abs(points[i, 0] - points[j, 0]) + np.abs(points[i, 1] - points[j, 1])
    
    return distance_matrix

distance_matrix = manhattan_distance_matrix(points)

max_distance_index = np.unravel_index(np.argmax(distance_matrix, axis=None), distance_matrix.shape)
point1 = points[max_distance_index[0]]
point2 = points[max_distance_index[1]]

print("Generated points:")
for point in points:
    print(f"({point[0]:.2f}, {point[1]:.2f})")

print("\nDistances:")
print(np.round(distance_matrix, 2))

print(f"\nMost remote points: ({point1[0]:.2f}, {point1[1]:.2f}) and ({point2[0]:.2f}, {point2[1]:.2f})")
