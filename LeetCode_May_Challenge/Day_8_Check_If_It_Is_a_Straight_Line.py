from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(len(coordinates)-2):
            x1, y1 = coordinates[i][0], coordinates[i][1]
            x2, y2 = coordinates[i+1][0], coordinates[i+1][1]
            x3, y3 = coordinates[i+2][0], coordinates[i+2][1]
            if not ((x3-x2) == 0 or (x2-x1) == 0):
                m1 = (y2-y1)/(x2-x1)
                m2 = (y3-y2)/(x3-x2)
            if not ((x3-x2) == 0 or (x2-x1) == 0) and m1 != m2:
                return False
        return True

coordinates1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

coordinates2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coordinates3 = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]
print(Solution().checkStraightLine(coordinates1))
print(Solution().checkStraightLine(coordinates2))
print(Solution().checkStraightLine(coordinates3))