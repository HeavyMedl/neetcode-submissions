class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr
        

    def decode(self, s: str) -> List[str]:

        #  4#neet4#code4#love3#you -> ["neet","code","love","you"]
        #       i^
        #   j^
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # now j is #. We need parse the length
            # from i up to j
            strLength = int(s[i:j])
            j += 1
            decoded.append(s[j:j+strLength])
            i = j + strLength

        return decoded
