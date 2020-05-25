'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

Hint #1  
Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as a recursion?
'''
from typing import List
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        A = [ -1 ] + A
        B = [ -1 ] + B
        
        dp_table = {}
        
        def helper( idx_a, idx_b ):
            
            if (idx_a, idx_b) in dp_table:
                return dp_table[(idx_a, idx_b)]
            
            
            if idx_a == 0 or idx_b == 0:
                return 0
            
            elif A[idx_a] == B[idx_b]:
                
                dp_table[(idx_a, idx_b)] = helper(idx_a-1, idx_b-1) + 1
                return dp_table[(idx_a, idx_b)]
            else:
                dp_table[(idx_a, idx_b)] = max( helper(idx_a-1, idx_b), helper(idx_a, idx_b-1))
                return dp_table[(idx_a, idx_b)]
        
        return helper( len(A)-1, len(B)-1 )


A1 = [1,3,7,1,7,5]
B1 = [1,9,2,5,1]


A2 = [2,5,1,2,5]
B2 = [10,5,2,1,5,2]

print(Solution().maxUncrossedLines(A1, B1))
print(Solution().maxUncrossedLines(A2, B2))