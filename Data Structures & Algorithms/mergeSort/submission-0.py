# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
  def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
    self._mergeSort(pairs, 0, len(pairs) - 1)
    return pairs

  def _mergeSort(self, pairs, s, e):
    if (e - s) + 1 <= 1:
      return

    m = (s + e) // 2

    self._mergeSort(pairs, s, m)
    self._mergeSort(pairs, m + 1, e)

    self.merge(pairs, s, m, e)

  def merge(self, pairs, s, m, e):
    L = pairs[s : m + 1]
    R = pairs[m + 1 : e + 1]

    l = 0
    r = 0
    i = s

    while l < len(L) and r < len(R):
      if L[l].key <= R[r].key:
        pairs[i] = L[l]
        l += 1
      else:
        pairs[i] = R[r]
        r += 1
      i += 1
    
    while l < len(L):
      pairs[i] = L[l]
      l += 1
      i += 1
    
    while r < len(R):
      pairs[i] = R[r]
      r += 1
      i += 1



