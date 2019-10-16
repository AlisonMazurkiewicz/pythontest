def first_not_repeating(str):
  ctr = {}
  x = "_"

  for c in str:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1

  for c in str:
    if ctr[c] == 1:
      return c

  return x
