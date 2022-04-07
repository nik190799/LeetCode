class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        i,j=n-1,0
        
        while i>=0:
            while j<n:
                temp = matrix[i].pop(0)
                matrix[j].append(temp)
                j += 1
            i -= 1
            j = 0
        return