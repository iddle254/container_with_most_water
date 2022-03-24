class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        p1 = 0
        p2 = len(height) -1
        while p1 < p2:
            height_cont = min(height[p1], height[p2])
            width = p2 - p1
            calculated_area = height_cont * width
            max_area = max(max_area, calculated_area)
            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1
        print(max_area)
        return max_area

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
max_amount_of_water = solution.maxArea(height)