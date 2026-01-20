# ---------------------------------------------------------
# PROBLEM STATEMENT (LeetCode 1071)
# ---------------------------------------------------------
# Goal: Hamein 2 strings (str1, str2) di gayi hain. 
# Hamein wo "Sabse Bari String X" dhundni hai jo dono ko repeat ho kar bana sake.
# (Jaise Tiles floor ko cover karti hain bina gap ke).
# Agar aisi koi string nahi milti, to empty "" return karna hai.
# ---------------------------------------------------------

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # ---------------------------------------------------
        # Step 1: Pattern Check (DNA Test)
        # ---------------------------------------------------
        # Sabse pehle check karo: Kya inka pattern same hai?
        # Agar hum str1+str2 karein aur wo str2+str1 ke barabar NA ho,
        # to iska matlab ye kabhi ek dusre ko nahi bana sakte.
        # Example: "ABC" + "DEF" != "DEF" + "ABC" (Alag hain -> Return "")
        if str1 + str2 != str2 + str1:
            return ""

        # ---------------------------------------------------
        # Step 2: Calculate Size (Math ka Jadu)
        # ---------------------------------------------------
        # Agar pattern same hai, to ab bas ye pata karna hai ke
        # wo common block kitna lamba (long) hai.
        # Answer ki length dono strings ki lengths ka GCD hogi.
        # Example: Length 6 aur 4 ka GCD = 2 hota hai.
        max_length = math.gcd(len(str1), len(str2))

        # ---------------------------------------------------
        # Step 3: Extract and Return
        # ---------------------------------------------------
        # Ab bas pehli string me se shuru ke 'max_length' letters utha lo.
        # Wahi apka final answer hai.
        return str1[:max_length]

obj = Solution()
print(obj.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))