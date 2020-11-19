#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# Try and except
def double_index(lst, index):
  try:
    lst[index] = 2 * lst[index]
    return lst
  except:
    return lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
