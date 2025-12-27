s = set()

s.add("goat")
s.add("ME")
print(s)
print(type(s))


d = {1, 3, 5, 6}
print(len(d))

d.remove(5)
print(d)

print(d.union({5,11}))

print(d.intersection({5,6}))      


print(d.pop())

print(d.clear())

print(d)
