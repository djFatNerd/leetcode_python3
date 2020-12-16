class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        # max area
        ma = 0
        
        while i<j:
            ma = max(ma, min(height[i], height[j]) * (j - i))
            # ****************MAIN IDEA HERE*******************
            # use the longer spike, increment/decrement shorter
            # becuz the area of the tank is limited by the shorter spike
            # therefore: if we move the longer spike, we'll never get an increase in area,
            # our maxA = (height[n] <= shorter) * (width(n-i)<j-i)
            
            # but if we move the shorter spike inside, we might get an increase in height
            # while we are decreasing width, which may result in a larger area
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return ma