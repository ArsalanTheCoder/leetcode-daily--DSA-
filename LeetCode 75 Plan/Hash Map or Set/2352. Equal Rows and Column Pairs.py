from collections import Counter

class Solution:
    def equalPairs(self, grid):
        count_rows = Counter()
        for row in grid:
            row_tuple = tuple(row)
            count_rows[row_tuple] += 1

        total_count = 0

        for col in zip(*grid):
            total_count += count_rows[col]
        
        return total_count 


obj = Solution()
print(obj.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


# from collections import Counter

# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
#         # Step 1: Ek khali Counter banaya taake hum rows ki ginti kar sakein
#         count_rows = Counter()
        
#         # Step 2: Grid ki har row ko ek-ek karke pakro
#         for row in grid:
#             # Row (list) ko 'tuple' mein badla taake dictionary isay accept kar le (The "Tappal" trick!)
#             row_tuple = tuple(row)
            
#             # Is tuple ko dictionary mein daala aur uski taadaad (count) mein 1 ka izafa kar diya
#             count_rows[row_tuple] += 1

#         # Step 3: Yeh hamara final score card hai
#         total_count = 0

#         # Step 4: zip(*grid) ka jadoo! Yeh grid ko ghumata hai aur humein seedhay columns nikal kar deta hai (as tuples)
#         for col in zip(*grid):
#             # Check karo ke kya yeh column hamari rows wali dictionary mein mojood hai?
#             # Agar hai, toh wo row jitni dafa aayi thi, utne points total_count mein add kar do
#             total_count += count_rows[col]
        
#         # Step 5: Final score wapas bhej do
#         return total_count 

# # Testing the code
# obj = Solution()
# print(obj.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))