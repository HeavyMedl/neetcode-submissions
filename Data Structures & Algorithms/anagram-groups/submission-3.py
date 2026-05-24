class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we need a dict to store grouped anagrams
        anagrams = {}

        # iterate through strs
        for s in strs:
            # initialize a list of 26 representing the alphabet
            anagramKey = [0] * 26
            
            # iterate through each char in each string,
            # compute the unicode value which will correspond with the
            # index in the anagramKey and iterate
            for char in s:
                index = ord(char.lower()) - ord('a')
                anagramKey[index] += 1


            # with the computed anagram key list, push the
            # string to an existing list within anagrams matching
            # the anagramKey, or initialize a new one
            anagrams.setdefault(tuple(anagramKey), []).append(s)

        return list(anagrams.values())