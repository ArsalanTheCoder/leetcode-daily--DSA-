# from collections import Counter
# class Solution:
#     def uniqueOccurrences(self, arr: list[int]) -> bool:
#         occurrences = Counter(arr)
        
#         Occurrence_count = []
        
#         # Extract the counts into a list
#         for value in occurrences.values():
#             Occurrence_count.append(value)

#         # Compare the length of the list with the length of a set of that list
#         return len(set(Occurrence_count)) == len(Occurrence_count)
    

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Get all the occurrence counts (e.g., [3, 2, 1])
        counts = Counter(arr).values()
        
        # Check if the length changes when converted to a set
        return len(counts) == len(set(counts))

obj = Solution()
print(obj.uniqueOccurrences(arr=[1,2]))