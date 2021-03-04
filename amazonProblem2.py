with open('log.csv', 'r') as f:
  next(f)
  d = {}
  for line in f:
    date = line.split('T')[0]
    user = line.split(' ')[3]
    try:
      d[date].append(user)
    except KeyError:
      d[date] = [user]

print(d)
d1, d2 = d.values()
day1 = set(d1)
day2 = set(d2)

common = day1.intersection(day2)
total = day1.union(day2)
print(len(common)/len(total)*100)
