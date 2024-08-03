import math


def findBottomLeft(points):
    return min(points, key=lambda p: (p.y, p.x))


def sortCCW(points):
    bottom_left = findBottomLeft(points)

    def angle_to_bottom_left(p):
        if p.x == bottom_left.x and p.y == bottom_left.y:
            return -math.inf
        return math.atan2(p.y - bottom_left.y, p.x - bottom_left.x)

    points.sort(key=angle_to_bottom_left)


def isLeftTurn(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x) > 0


def grahamScan(points):
    if len(points) < 3:
        return points

    sortCCW(points)

    stack = [points[0], points[1]]

    for i in range(2, len(points)):
        while len(stack) > 1 and not isLeftTurn(stack[-2], stack[-1], points[i]):
            stack.pop()
        stack.append(points[i])

    # Add the starting point to the end to close the hull
    stack.append(points[0])

    return stack