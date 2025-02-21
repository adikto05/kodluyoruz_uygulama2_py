def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# 2D uzaydaki noktalar
points = [(1, 2), (4, 6), (7, 8), (2, 3)]

distances = []

distances.append(euclideanDistance(points[0], points[1]))
distances.append(euclideanDistance(points[2], points[3]))

# Minimum mesafenin bulunması
min_distance = min(distances)
print(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")