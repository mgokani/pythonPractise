'''
# A group of centaurs (mythical half-human, half-horse creatures) all sign
# up for Facebook accounts at the same time. They immediately start
# sending each other friend requests, in accordance with the ancient rules
# that have governed centaur friendship since the dawn of time:
#
# 1) A centaur will only send a friend request to another centaur if the
# recipient is at least (X/2 + 7) of the sender's age. For example, a 200-year
# old centaur can only send friend requests to centaurs that are at least 107 years old.
# 2) A centaur will not send a friend request to another centaur that is older
# than it is.
# 3) A centaur over 100 years old will not send a friend request to a recipient
# under 100 years old. But centaurs under 100 years old can friend each other.
# 4) If any of the conditions for sending a friend request are not met, no friend
# request will be sent.
#
# Write a function that, given an array of centaur ages, returns an integer
# of the total number of friend requests that the group of centaurs will send
# to each other.
#
# Examples:
# count_all_friend_requests([120, 110])  => 1
# # Friend requests          1    0
# count_all_friend_requests([120, 110, 99]) => 1
# # Friend requests          1    0    0
# count_all_friend_requests([120, 45, 230, 400, 88, 300, 101]) => 4
# # Friend requests          1    0   0    2    0   1    0
# count_all_friend_requests([120, 45, 55, 230, 400, 88, 300, 101]) => 6
# # Friend requests          1    0   1   0    2    1   1    0
'''


def countfriendrequests(l):
  count = 0
  for i in range(0, len(l)):
    for j in range(1, len(l)):
      min_age = (l[i]/2 + 7)
      if l[i] > 100:
        if l[j] > min_age and l[j] < l[i] and l[j] > 100:
          count += 1
      else:
        if l[j] > min_age and l[j] < l[i]:
          count += 1
  return count


if __name__ == "__main__":
  l = [120, 45, 55, 230, 400, 88, 300, 101]
  print(countfriendrequests(l))


  






