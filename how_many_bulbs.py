'''
# We're in a room with a row of lightbulbs. Below each bulb is a switch that
# controls just the bulb above it.

# When we begin, all the lightbulbs are off. The first person flips the switch
# on every bulb, turning them all on. The second person then comes through
# and flips the switch on every 2nd bulb, turning half of them off. The
# third person then comes through, and flips the switch on every 3rd bulb,
# turning some of them off and some of them on (the ones which person #2
# turned off). The fourth person flips the switch on every 4th bulb, and so on
# down the line, up until the very last person, who flips the switch for just
# the last bulb.

# Write a function that, given a number of bulbs N, prints the number of bulbs
# that will be in the "ON" position once all N people have gone through and
# done their switch flipping.

# For example:
# how_many_bulbs_on(1) => 1
# how_many_bulbs_on(3) => 1
# how_many_bulbs_on(5) => 2
'''

def findFactors(d):
  factor = []
  for i in range(1, d + 1):
    if d % i == 0:
      factor.append(i)
  return len(factor)

def how_many_bulbs(n):
  bulbsON = 0
  for i in range(1, n+1):
    if findFactors(i) % 2 != 0:
      bulbsON += 1
  return bulbsON


if __name__ == "__main__":
  n = 1
  print(how_many_bulbs(7))
