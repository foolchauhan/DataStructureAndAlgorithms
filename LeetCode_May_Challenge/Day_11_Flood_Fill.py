from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def floodIt(roww, coll):
            if image[roww][coll] == color:
                image[roww][coll] = newColor
                if roww >= 1:
                    floodIt(roww-1, coll)
                if roww+1 < row:
                    floodIt(roww+1, coll)
                if coll >= 1:
                    floodIt(roww, coll-1)
                if coll+1 < col:
                    floodIt(roww, coll+1)
        
        floodIt(sr, sc)
        return image