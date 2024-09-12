def first_half(str):
  if len(str) % 2 == 0:
      return str[0:int(len(str)/2)]
  else:
      return str

print(first_half("woohoo"))