import math #kütüphane kullandım
# Noktaların tanımladım
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  
# Öklid mesafesi için  fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
# Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
