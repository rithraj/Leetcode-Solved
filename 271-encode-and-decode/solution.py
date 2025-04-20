def encode(self, strs: List[str]) -> str:
  res = ""
  for s in strs:
      res = res + str(len(s)) + "#" + s
  return res

def decode(self, s: str) -> List[str]:
  res = []
  i = 0
  while i < len(s):
      j = i
      while s[j] != "#":
          j += 1
      i, j = j + 1, i + int(s[i:j])
      res.append(s[i:j])
      i = j
  return res
      
