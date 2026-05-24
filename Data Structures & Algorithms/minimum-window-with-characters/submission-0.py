class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        result = [-1, -1]
        resultLen = float("infinity")
        windowMap = defaultdict(int)
        needMap = defaultdict(int)
        left = 0
        have = 0

        for c in t:
            needMap[c] += 1

        need = len(needMap)

        for right in range(len(s)):
            rightChar = s[right]

            windowMap[rightChar] += 1

            if rightChar in needMap and windowMap[rightChar] == needMap[rightChar]:
                have += 1
            
            while have == need: # I got what you neeeeeeeeed!
                # update result if the length is smaller
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                # Start closing the window (iterating the left boundary
                # to find a potentially smaller solution
                # First we need to actually decrement the count of whatever
                # is at the left pointer...
                leftChar = s[left]
                windowMap[leftChar] -= 1
                # Next we determine if we need to decrement "have" since the 
                # frequencies might be mismatched now

                if leftChar in needMap and windowMap[leftChar] < needMap[leftChar]:
                    have -= 1
                # finally, we increment left 
                left += 1 

        l, r = result
        return s[l : r + 1] if resultLen != float("infinity") else ""