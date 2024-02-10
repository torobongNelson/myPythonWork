
 def char_ character (string):
 counts = {}
  for char in string:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts
