import math

dist_two_points = lambda p, q: math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def dist(p, q, r):
    d1 = dist_two_points(p, q)
    d2 = dist_two_points(p, r)
    d3 = dist_two_points(q, r)
    return (d1 + d2 + d3) / 3


print(dist((1, 3), (1 / 2, 2), (-3, -5)))
