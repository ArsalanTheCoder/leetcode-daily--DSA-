class Solution:
    def canConstruct(self, ransomNote, magazine):
        countMagazine = {}

        for mag in magazine:
            if mag in countMagazine:
                countMagazine[mag] += 1
            else:
                countMagazine[mag] = 1
        print(countMagazine)

        for ran in ransomNote:
            if ran in countMagazine and countMagazine[ran]>0:
                countMagazine[ran]-=1
            else:
                return False

        return True
            

obj = Solution()
result = obj.canConstruct(ransomNote = "aab", magazine = "baa")
print(result)