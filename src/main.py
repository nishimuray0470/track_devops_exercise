def add(a, b, c=0):
  try:
    return int(a + b) + int(c)
  except:
    return "error"

print(add(7, 2))
print(add(5, "2", 3))
print(add("2", "8.2"))
print(add("8", "1", 3.6))
print(add("1", "2"))
print(add("3", "4", "5"))
print(add(2.6, "4", None))
print(add(2.5, 3, "5.1"))
print(add(5.4, 9.8))
print(add("1.4", "2", 3))
print(add(2.5, 3, "x"))
print(add(2.1, 9.3, 3.7))
print(add(1, 6, 3))
print(add(1.6, 2.1))
print(add(1.6, 2.1))
print(add(1.9, 4.3, "2.6"))
print(add("1", "2", 9))
print(add("4", "2.4", 1))
print(add(None, 3, "5.1"))
print(add("b", 4, 5))
