class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Find the closest x-coordinate in the rectangle
        closestX = max(x1, min(xCenter, x2))

        # Find the closest y-coordinate in the rectangle
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Check whether the closest point is inside the circle
        return dx * dx + dy * dy <= radius * radius