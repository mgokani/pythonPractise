'''
# I want to monitor a value produced from a streaming app; say one of the swap columns from vmstat. If the value exceeds a given threshold X for more than Y consecutive samples I'd like a message printed out.
#
# The command should take standard input and be invoked as:
#
# yourscript <column_number> <repetitions> <threshold value>
#
# Example: vmstat 1 | yourscript 7 5 200
#
# That means that when the value of column 7 has gone over 200 for more than 5 times in a row, print something out. My plan is to leave this running over night and check back on it in the morning.

# Output -


# 5  4      0 556532 1698688 32809712  201    0     0  1304 3168 6853  31  1 58 11  0
# 5  4      0 556532 1698688 32809712  201    0     0  1304 3168 6853  31  1 58 11  0
# 5  4      0 556532 1698688 32809712  201    0     0  1304 3168 6853  31  1 58 11  0
# 5  4      0 556532 1698688 32809712  201    0     0  1304 3168 6853  31  1 58 11  0
# 5  4      0 556532 1698688 32809712  201    0     0  1304 3168 6853  31  1 58 11  0
# 5  4      0 556532 1698688 32809712  201    0     0  1304 3168 6853  31  1 58 11  0
# 5  4      0 517944 1698696 32809792    0    0     0  1360 3345 10589 31  1 53 15  0
# 6  4      0 477476 1698748 32836968  300    0     4  1459 3819 20150 39  2 42 17  0
'''

with open('vmstat.log', 'r') as f:
  count = 0
  for line in f:
    val = line.split()[6]
    if int(val) > 200:
      count += 1
    if count == 5:
      print("alert")
      count = 0

# input will be sys.stdin.read() 
