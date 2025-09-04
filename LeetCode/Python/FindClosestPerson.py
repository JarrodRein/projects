class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dif = z - y 
        dif2 = z -x
        if abs(dif) < abs(dif2):
            return 2
        if abs(dif) > abs(dif2):
            return 1
        else:
            return 0