class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Create a set to store the points for fast lookup
        point_set = set((x, y) for x, y in points)
        min_area = float('inf')
        
        # Iterate over all pairs of points
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Check if the opposite points of a rectangle exist
                if x1 != x2 and y1 != y2 and (x1, y2) in point_set and (x2, y1) in point_set:
                    # Calculate the area of the rectangle formed
                    area = abs(x1 - x2) * abs(y1 - y2)
                    # Update the minimum area found so far
                    min_area = min(min_area, area)
        
        # If no rectangle is found, return 0
        return min_area if min_area != float('inf') else 0
