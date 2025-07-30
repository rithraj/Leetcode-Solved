class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse=True)

        capacity = truckSize
        maxUnits = 0

        for box, units in boxTypes:
            if capacity >= box:
                capacity = capacity - box
                maxUnits = maxUnits + (box * units)
            elif 0 < capacity < box:
                maxUnits = maxUnits + (capacity * units)
                capacity = 0
            
            if capacity == 0:
                return maxUnits

        return maxUnits
        