import numpy as np

def point2angle(points):
    points = np.array(points)
    
    x = points[:, 0]
    y = points[:, 1]
    
    angles = np.arctan2(y, x)
    angles = np.where(angles < 0, angles + 2 * np.pi, angles)
    
    return angles

random_angles = np.random.uniform(0, 2 * np.pi, 10)

points = np.column_stack((np.cos(random_angles), np.sin(random_angles)))

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
print("Filtered points:")
print(filtered_points)
print("Filtered angles:")
print(filtered_angles)
#------------------------------------------