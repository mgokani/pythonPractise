'''
Amazon interview question -

# Given a log file containing two days of web server logs,
# find the percentage of users who visited the site on
# both days. The log file contains the following
# columns, separated by spaces.

# Date, Operation, Path, User, Status Code
# 2019-02-02T18:83:03 GET /some/webpage.html ted 200
# 2019-02-02T18:83:03 GET /some/otherpage.html ted 200
# 2019-02-02T18:83:03 GET /some/otherwebpage.html sue 200
# 2019-02-02T18:83:03 GET /some/third.html josh 404
# 2019-02-03T18:83:03 GET /some/webpage.html ted 200

>>> percentage_users(log_file) = 33.33
'''

import csv


def percentage_users(log_file):
  ''':input type file
  :rtype float
  '''
  
  d = {}
  with open(log_file, 'r') as f:
    csvData = csv.reader(f, delimiter = ' ')
    next(csvData) # ignore the first line in the file
    for line in csvData:
      date = line[0].split('T')[0]
      user = line[3]
      print(date, user)
      try:
        d[date].add(user)
      except KeyError:
        d[date] = {user}
  
  print(d) # for debugging
  day1, day2 = d.values()
  both_days = len(day1.intersection(day2))
  total_users = len(day1.union(day2))
  return both_days/total_users * 100




if __name__ == "__main__":
  log_file = 'log.txt'
  print('percentage of users visited both days = {} %'.format(percentage_users(log_file)))

