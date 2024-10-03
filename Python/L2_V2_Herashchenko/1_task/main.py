import numpy as np

def point2angle(point):
    sign = np.sign(point[:,1])*np.sign(point[:,0])
    return sign * np.arccos(point[:,0])

points = np.array([[0, 0],
                    [-0.5, 0],
                    [0.5, 1],
                    [-1, 0],
                    [0, -1]])
angles = point2angle(points)

sorted_indices = np.argsort(angles)
sorted_points = points[sorted_indices]
sorted_angles = angles[sorted_indices]

#------------------------------------------
print(sorted_points[0])
#------------------------------------------

filtered_indices = np.where((sorted_angles >= 0) & (sorted_angles <= np.pi / 2))[0]

filtered_points = sorted_points[filtered_indices]
filtered_angles = sorted_angles[filtered_indices]

#------------------------------------------
print("Filtered angles:")
print(filtered_points)
print(filtered_angles)
#------------------------------------------