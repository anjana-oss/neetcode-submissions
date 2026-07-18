class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)#row
        n=len(matrix[0])#colum
        l=0
        r=m*n-1

        while l<=r:
            mid=(l+r)//2
            row=mid//n
            col=mid%n
            val=matrix[row][col]

            if val==target:
                return True
            elif val>target:
                r=mid-1
            else:
                l=mid+1
        return False
