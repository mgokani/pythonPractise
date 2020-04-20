a = [10,20,30,40,10,20,30,40,30,30,40,40,50]

d = {x:a.count(x) for x in a}

print(d)

# to get key with max value
m = max(d.values())
print(m)
num = [key for key, value in d.items() if value == m]
print(num)

# to get keys with max to lowest values
a = sorted(d.values())
print(a)

l = []
for i in a:
  for key, value in d.items():
    if i == value and key not in l:
      l.append(key)

print(l)
