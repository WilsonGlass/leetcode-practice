from heapq import heappop, heappush

"""
Given an array of points where points[i] = [xi, yi] represents a point
on the xy plane, return the k closest points to the origin (0,0). The distance
between two points is calculated using the Euclidean distance formula
"""

def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, list[int]]] = []

    for pt in points:
        heappush(heap, (pt[0] ** 2 + pt[1] ** 2, pt))

    res = []
    for _ in range(k):
        _, pt = heappop(heap)
        res.append(pt)
    return res